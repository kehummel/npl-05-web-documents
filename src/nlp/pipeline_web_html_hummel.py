"""src/nlp/pipeline_web_html.py - Module 5 Script.

NO EDITS REQUIRED IN THIS FILE (if paths have not changed.)

Purpose

  Orchestrate a standard EVTL pipeline for web document data.
  Illustrate how to fetch an HTML page, validate its structure,
  transform it into usable structured data, and load it into a sink.
  Illustrate how to parse HTML using BeautifulSoup to extract
  metadata from a web document.


Analytical Questions

- How can we fetch an HTML page from the web and save it to a file?
- How can we validate the structure and content of an HTML document?
- How can we transform HTML into clean, structured data?
- How can we load the transformed data into a sink (like a CSV file)?

Notes:
- This file should not require modification.
- This is the main pipeline script that orchestrates the entire EVTL process.
- It assumes a standard ETL pipeline enhanced with a VALIDATE stage,
  making it an EVTL pipeline.
- The stages are modularized into separate files for clarity and
  maintainability.
- Each stage has its own source and sink, which are clearly indicated
  in the stage files.
- The configuration values (like the page URL and file paths) are stored
  in a separate config file.

Run from root project folder with:

  uv run python -m nlp.pipeline_web_html_hummel
"""

# ============================================================
# Section 1. Setup and Imports
# ============================================================

import logging
import time

from datafun_toolkit.logger import get_logger, log_header, log_path
import pandas as pd

from nlp.config_hummel import (
    COMBINED_CSV_PATH,
    DATA_PATH,
    HTTP_REQUEST_HEADERS,
    PAGE_URLS,
    PROCESSED_CSV_PATHS,
    PROCESSED_PATH,
    RAW_HTML_PATHS,
    RAW_PATH,
    ROOT_PATH,
)
from nlp.stage01_extract import run_extract
from nlp.stage02_validate import run_validate
from nlp.stage03_transform_hummel import run_transform
from nlp.stage04_load import run_load

# ============================================================
# Section 2. Configure Logging
# ============================================================

LOG: logging.Logger = get_logger("CI", level="DEBUG")


# ============================================================
# Section 3. Define Main Pipeline Function
# ============================================================


def main() -> None:
    """Main function."""
    log_header(LOG, "Module 5: EVTL PIPELINE - WEB DOCUMENTS (HTML)")
    LOG.info("START PIPELINE")

    RAW_PATH.mkdir(parents=True, exist_ok=True)
    PROCESSED_PATH.mkdir(parents=True, exist_ok=True)

    log_path(LOG, "ROOT_PATH", ROOT_PATH)
    log_path(LOG, "DATA_PATH", DATA_PATH)
    log_path(LOG, "RAW_PATH", RAW_PATH)
    log_path(LOG, "PROCESSED_PATH", PROCESSED_PATH)

    all_dfs: list[pd.DataFrame] = []

    for i, (url, raw_path, csv_path) in enumerate(
        zip(PAGE_URLS, RAW_HTML_PATHS, PROCESSED_CSV_PATHS, strict=True), start=1
    ):
        LOG.info(f"===== ARTICLE {i} of {len(PAGE_URLS)}: {url} =====")

        try:
            # EXTRACT
            html_content = run_extract(
                source_url=url,
                http_request_headers=HTTP_REQUEST_HEADERS,
                raw_html_path=raw_path,
                LOG=LOG,
            )

            # VALIDATE
            validated_soup = run_validate(html_content=html_content, LOG=LOG)

            # TRANSFORM
            df = run_transform(soup=validated_soup, LOG=LOG)

            # LOAD
            run_load(df=df, processed_csv_path=csv_path, LOG=LOG)

            all_dfs.append(df)

        except Exception as e:  # noqa: BLE001
            LOG.error(f"Article {i} failed ({url}): {e}")
            continue  # keep going with the remaining articles

        time.sleep(1)  # be polite to arXiv between requests

    # Combine all successful articles into one CSV
    if all_dfs:
        combined = pd.concat(all_dfs, ignore_index=True)
        combined.to_csv(COMBINED_CSV_PATH, index=False)
        LOG.info(f"Wrote {len(combined)} rows to {COMBINED_CSV_PATH}")

    LOG.info("========================")
    LOG.info(
        f"Pipeline finished: {len(all_dfs)} of {len(PAGE_URLS)} articles succeeded."
    )
    LOG.info("========================")


# ============================================================
# Section 4. Run Main Function when This File is Executed
# ============================================================

if __name__ == "__main__":
    main()

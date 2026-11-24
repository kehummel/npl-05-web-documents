"""src/nlp/config_hummel.py - Module Configuration.

(MODIFY YOUR VERSION OF THIS FILE)

Stores configuration values for the web document EVTL pipeline.
Source: arXiv abstract page for "Agents of Chaos" (2602.20021)

Purpose

  Store configuration values.

Analytical Questions

- What web page URL should be used as the data source?
- Where should raw and processed data be stored?

Edit your Python file to change:
- PAGE_URL (source of the HTML web page document),
- customize your output file name.
"""

from pathlib import Path

# ============================================================
# API CONFIGURATION
# ============================================================

PAGE_URLS: list[str] = [
    "https://arxiv.org/abs/2602.20021",
    "https://arxiv.org/abs/2611.29009",
    "https://arxiv.org/abs/2611.30385",
    "https://arxiv.org/abs/2611.30779",
    "https://arxiv.org/abs/2611.30849",
]

# Let them know who we are (and that we're doing educational web mining).
HTTP_REQUEST_HEADERS: dict = {
    "User-Agent": "Mozilla/5.0 (educational-use; web-mining-course)"
}

# ============================================================
# PATH CONFIGURATION
# ============================================================

ROOT_PATH: Path = Path.cwd()
DATA_PATH: Path = ROOT_PATH / "data"
RAW_PATH: Path = DATA_PATH / "raw"
PROCESSED_PATH: Path = DATA_PATH / "processed"


# One raw HTML file and one processed CSV per URL, numbered from 1
RAW_HTML_PATHS: list[Path] = [
    RAW_PATH / f"hummel_raw_{i}.html" for i in range(1, len(PAGE_URLS) + 1)
]
PROCESSED_CSV_PATHS: list[Path] = [
    PROCESSED_PATH / f"hummel_processed_{i}.csv" for i in range(1, len(PAGE_URLS) + 1)
]

# Combined output across all articles
COMBINED_CSV_PATH: Path = PROCESSED_PATH / "hummel_processed_all.csv"

# Workflow D: Apply Skills

## Technical Modification

Run Using the command:
uv run python -m nlp.pipeline_web_html

For section D, we a apply a technical modification to the example project. For this project I added a sentence count for the abstract. It was a suggested modification but also made the most sense. This is because there is limited data on arxiv.org, but also there was not much else that provided meaningful analysis without acquiring more data. For instance, you could count the genders of the authors to see if there are more male or female contributors to this topic but the genders are not listed on that webpage so we'd have to go find additional information.

The only file I had to change was the stage03_transform file; every other file remained the same. So I made a copy of it and called it stage03_transform_phaseD.py. Then in the config file I changed the output file names to include phaseD and in the pipeline file I made sure it called the changed file.

[stage03_transform_phaseD.py](../src/nlp/stage03_transform_phase_d.py)

![sentence word count code](images/sentence_count_code.png)

The code counts the number of times there is an ending punctuation mark with a space after it, so that it would only count the end of sentences instead of any punctuation mark or decimal numbers in the abstract.

After that I added sentence_count to the records so that it would show up in the dataframe. I also created a log output with the other derived fields so that all of that information was altogether.

![sentence count output](images/sentence_count_dataframe.png)

## Custom Application

Run using the command:
uv run python -m nlp.pipeline_web_html_hummel

### Files Used for Custom Application:

- [config_hummel.py](../src/nlp/config_hummel.py)
- [pipeline_web_html_hummel.py](../src/nlp/pipeline_web_html_hummel.py)
- [stage01_extract.py](../src/nlp/stage01_extract.py)
- [stage02_validate.py](../src/nlp/stage02_validate.py)
- [stage03_transform_hummel.py](../src/nlp/stage03_transform_hummel.py)
- [stage04_load.py](../src/nlp/stage04_load.py)

For the custom application, I knew I was going to change the data source, but I felt like that wasn't enough of a change because it would just be copying and pasting a line or two, and then trouble shooting if needed. I wasn't expecting a lot of trouble shooting because the technical modification went well so I didn't think that there would need to be much during the custom application.

I decided to do multiple articles/websites from arxiv. My thought was that if this is functioning as a pipeline, I would want to be able to do these same steps multiple times over, with any number of links from arxiv. I decided on the first 5 (meaning the five most recent) articles in the databases subcategory of Computer Science articles. I initially created a separate PAGE_URL for each article as well as a separate raw and processed file name. That would mean that my next step would be to create a pipeline for each article/website. I felt that this defeated the purpose of making it easily replicable as I was doing extra steps for each new file.

I realized I should be creating a loop instead, meaning I'd have one set of pipeline code and it would cycle through the articles/websites and give me differentiated outputs without having to write a separate label for each dataset/csv. I used AI to help me with this because while I have a basic understanding of loops, I struggle in getting all of the formatting correct. I started by making my PAGE_URLs a list of the five websites I chose, and then added a looping function to the raw and processed data file paths so that I wouldn't have to come up with the names of each dataframe. Then in the pipeline file I moved the extract, validate, transform, and load functions into a loop so that the pipeline would cycle through all of those stages with each website.

I also decided to add a count of the words in the title, just to make it so that there was more information in the dataframe.

Because this project has a lot of logs, which do a great job explaining what is happening and how the pipeline process is going, it is hard to parse through the helpful information. Additionally, the processed data includes the title, and abstract which can contain a lot of words and make it hard to compare values that are not showing up on the same screen. I decided to make a table in this markdown file so it was easy to see and compare the values. I did this because I felt like this is what we would do in a real world situation. We'd run the pipeline of data to be able to compare data.

It was a good thing that I did this in that it helped me catch an error. When I was looking at the output, I would just look to see that there were values for the different dataframe details. But when I was actually typing them in, I realized that the abstract word count and the title word count were giving the same value. This mistake happened because I used the abstract word count as the base for my title word count meaning I copied and pasted the code to calculate the abstract word count and changed it as needed. I accidentally kept "if abstract != "unknown" else 0" and forgot to change "abstract" to "title" in that line of code. So when the code ran, it was pulling the words in the abstract and completing a word count instead of pulling the words from the title.

## Article Comparison

In the table are the calculated values for the five different webpages. This table makes it easier to read the calculated values as well as make comparisons between them.

| Arxiv ID   | Author Count  | Title Word Count  | Abstract Word Count | Abstract Sentence Count |
|--------------|----------|----------|----------|----------|
| 2602.20021 | 38 | 3 | 177 | 9 |
| 2611.29009 | 1 | 18 | 244 | 8 |
| 2611.30385 | 5 | 12 | 282 | 12 |
| 2611.30779 | 4 | 10 | 288 | 8 |
| 2611.30849 | 3 | 6 | 157 | 5 |

## Next Steps

Next steps would be to have the pipeline give this tabled results instead of having to type it in afterwards.

There are many possible next steps with this data and it would just depend on what your goals were in learning from the data. You could easily calculated the range or median of these values. You could compare them to articles in different categories. You could also sample recently published articles against articles published the previous year, or five years. There are many ways to continue and extend the process started here.

## Data Source

Top five Arxiv articles in Computer Science sub category Databases

https://arxiv.org/list/cs.DB/recent

Since the website is updated regularly, the articles used may no longer be the top five if accessed at a later date (after 11/24/26). Therefore the articles I used are listed below.

- https://arxiv.org/abs/2602.20021
- https://arxiv.org/abs/2611.29009
- https://arxiv.org/abs/2611.30385
- https://arxiv.org/abs/2611.30779
- https://arxiv.org/abs/2611.30849

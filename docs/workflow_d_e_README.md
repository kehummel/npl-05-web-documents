# Workflow D: Apply Skills

## Technical Modification

For section D, we a apply a technical modification to the example project. For this project I added a sentence count for the abstract. It was a suggested modification but also made the most sense. This is because there is limited data on arxiv.org, but also there was not much else that provided meaningful analysis without acquiring more data. For instance, you could count the genders of the authors to see if there are more male or female contributors to this topic but the genders are not listed on that webpage so we'd have to go find additional information.

I forgot to make a new file before adding in the sentence count, so I just left it in the example document

![sentence word count code](images/sentence_count_code.png)

The code counts the number of times there is an ending punctuation mark with a space after it, so that it would only count the end of sentences instead of any punctuation mark or decimal numbers in the abstract.

After that I added sentence_count to the records so that it would show up in the dataframe. I also created a log output with the other derived fields so that all of that information was altogether.

![sentence count output](images/sentence_count_dataframe.png)

## Custom Application

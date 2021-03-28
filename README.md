[![Build Status](https://travis-ci.com/dev-11/eigen-technical-task.svg?branch=master)](https://travis-ci.com/dev-11/eigen-technical-task)
[![codecov](https://codecov.io/gh/dev-11/eigen-technical-task/branch/master/graph/badge.svg)](https://codecov.io/gh/dev-11/eigen-technical-task)
<!--
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/5cfd5da40bc744beb49b5f1121bd8822)](https://www.codacy.com/manual/dev-11/eigen-technical-task?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=dev-11/eigen-technical-task&amp;utm_campaign=Badge_Grade)
-->

# Eigen Coding Task
Here at Eigen, we spend a lot of time getting useful stuff out of documents. Usually a word or two, perhaps a sentence or paragraph. For this task, we’d like you to show us how you would do something similar!

We’ve attached a few documents, each of which has lots of words and sentences. For this task, produce a list of the most frequent interesting words, along with a summary table showing where those words appear (sentences and documents). For example, like this table:

|Word (Total Occurrences) | Documents | Sentences containing the word  |
|---|---|---|
|Philosophy (42)| x, y, z | I don't have time for **philosophy** <br/><br/> Surely this was a touch of fine **philosophy**; though no doubt he had never heard there was such a thing as that. <br/><br/>  Still, her pay-as-you-go **philosophy** implies it. |
| ---      | ---      | -- |


You can be creative with the output, so feel free to format in whatever way you feel best fits your solution! 

This task can be tackled in any way you feel best solves the problem; feel free to show off your prowess! Our only “rule” is that you write your solution in Python, since that’s the main language we use at Eigen. Otherwise, please include instructions to help us get up and running with your code! 


## The approach

The solution scans the directory which is defined in the `config.py` and reads every txt file.
After we've read up the files the system will parse it, which is basically breaking down the whole text to sentences.
When we have the separate sentences of the actual file the `WordCounterService` will count the words in the actual sentence
and maintain the `word_counter` list. Because we want to list the most interesting words the user can define a threshold
and if the actual work is not interesting enough it will not be added to the list. The `InterestingService` will calculate the
interestingness of a word, which is at the moment calculated by the length of the word. There are two weights, service wide and word specific.
If a word contains a `-` character it will boost its interesting rate.

Command to run the app `python3 app.py` which will launch an API endpoint which can be tested at http://127.0.0.1:5006/ 

Sample output format
```
[
    {
        "word": "one-hundred-and-five-year-old",
        "interesting_rating": 58,
        "count": 1,
        "test_docs/doc3.txt": [
            "And ever since I met this frail, one-hundred-and-five-year-old African-American woman who had found the strength to leave her house and come to a rally because she believed that her voice mattered, I've thought about all she's seen in her life."
        ]
    }
]
``` 



### Improvements
Right now we load the whole file into the memory which can be a bottleneck in the future. I would also improve the `InterestingService` to use a word frequency service like https://www.wordsapi.com/ to find rare words in the text.

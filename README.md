# ACM Research Coding Challenge (Fall 2021)
For this coding challenge, I utilized Python programming language and NLTK Python packages to help me conquer and finish the problem.
## My Approach:
I spent quite a while to learn about the basic foundation of sentiment analysis and tried to grasp the idea of what I need for this coding challenge.
When googling for resources to help myself with the challenge, I came across a lot of articles, tutorials and documentations on different approaches and Python libraries that can be used. However, since we are not provided with trained data or model and have to analyse data from a text file from scratch, I decided to conquer the challenge with rule-based analysis, which means to approach using a set of human-crafted rules to help identify subjectivity, polarity, or the subject of an opinion. Rule-based analysis will count the number of negative words and positive words and compare their number of appearance to come up with the conclusion whether the text holds negative, positive or neutral sentiment.
First of all, the read-in input file containing the text needs to be "cleaned". To do that, I converted all the letters in the text to lowercase, then start removing punctuations and splitting the text into list of words.
After that, I installed NLTK packages. To finish off cleaning the text, I removed "stopwords" that are used so often in language that they have no use for sentiment analysis, such stopwords list come from nltk package. I used the emotions dictionary that I found online from [youtube](https://www.youtube.com/watch?v=dyN_WtjdfpA&t=1s) that show how different words can express similar emotions. 
From then, I utilized funtions from the nltk package and finalizing the output sentiment score of the text. 


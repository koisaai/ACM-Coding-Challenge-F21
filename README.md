# ACM Research Coding Challenge (Fall 2021)
For this coding challenge, I utilized Python programming language and NLTK Python packages to help me conquer and finish the problem.
## My Approach:
I spent quite a while to learn about the basic foundation of sentiment analysis and tried to grasp the idea of what I need for this coding challenge.
When googling for resources to help myself with the challenge, I came across a lot of articles, tutorials and documentations on different approaches and Python libraries that can be used. However, since we are not provided with trained data or model and have to analyse data from a text file from scratch, I decided to conquer the challenge with rule-based analysis, which means to approach using a set of human-crafted rules to help identify subjectivity, polarity, or the subject of an opinion. Rule-based analysis will count the number of negative words and positive words and compare their number of appearance to come up with the conclusion whether the text holds negative, positive or neutral sentiment.
First of all, the read-in input file containing the text needs to be "cleaned". To do that, I converted all the letters in the text to lowercase, then start removing punctuations and splitting the text into list of words.
After that, I installed NLTK packages. To finish off cleaning the text, I removed "stopwords" that are used so often in language that they have no use for sentiment analysis, such stopwords list come from nltk package. I used the emotions dictionary that I found online from [youtube](https://www.youtube.com/watch?v=dyN_WtjdfpA&t=1s) that show how different words can express similar emotions. 
From then, I utilized funtions from the nltk package and finalizing the output sentiment score of the text. 

## Result Comprehension:
The program output:
{'neg': 0.076, 'neu': 0.735, 'pos': 0.189, 'compound': 0.9979}
The text has positive sentiment with the score of 0.189

The text has a positive sentiment with a score of 0.189. The overall output says the text has a score of 0.076 for negative vibe which is less than 0.189 for positive vibe. The compound score is the sum of positive, negative and neutral scores which is then normalized between -1(most extreme negative) and +1 (most extreme positive). The more Compound score closer to +1, the higher the positivity of the text. In our case, the compound score is 0.9979 which is closer to +1, which means the text is very positive. 

This surprised me a little bit because on the first part of the text, it seems to give of a negative vibe. However, the latter part is flooded with positive words therefore makes the text has a high positive score. 


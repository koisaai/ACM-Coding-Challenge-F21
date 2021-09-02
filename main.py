import string
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer

text = open('input.txt', encoding = 'utf-8').read()
lower_case = text.lower()

cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))

tokenized_words = word_tokenize(cleaned_text, "english")


final_words = []
for word in tokenized_words:
    if word not in stopwords.words('english'):
        final_words.append(word)


#print(final_words)
emotion_list = []
with open('emotions.txt', 'r') as file:
    for line in file:
        clear_line = line.replace('\n','').replace(',','').replace("'",'').strip()
        word, emotion = clear_line.split(':')

        if word in final_words:
            emotion_list.append(emotion)

def sentiment_analyse(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    print(score)
    neg = score['neg']
    pos = score['pos']

    if neg > pos:
        print("The text has negative sentiment with the score of " + str(neg))
    elif pos > neg:
        print("The text has positive sentiment with the score of " + str(pos))
    else:
        print("The text has neutral sentiment.")
    
sentiment_analyse(cleaned_text)
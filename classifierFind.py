import random
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB


# Read csv files
def read_csv_file(path: str):
    return pd.read_csv(path, sep=',', encoding="utf8")


# Find and return category messages
def get_classification(messages: list):
    data = read_csv_file('questions.csv')

    vectorizer = CountVectorizer()
    counts = vectorizer.fit_transform(data['value'].values)
    targets = data['intent'].values

    classifier = MultinomialNB()
    classifier.fit(counts, targets)

    messages_count = vectorizer.transform(messages)
    predictions = classifier.predict(messages_count)

    return predictions


# Random selection of filtered categories
def random_choose_with_intent(intent: str):
    data = read_csv_file('answers.csv')
    data_filter = data[data['intent'].isin([intent])]
    result = random.choice(data_filter['value'].values)

    return result


# Get the answer with the specified intention
def get_answer_intent(intent: str):
    return random_choose_with_intent(intent)


# Only when this is the original executable file is the condition true
# To test this script
if __name__ == '__main__':
    result = random_choose_with_intent('hate')
    print(result)

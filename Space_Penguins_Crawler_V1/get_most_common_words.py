import operator
def is_stopword(word):
    with open('stopwords.txt') as file:
        contents = file.read()
        if word.upper() in contents.upper():
            return True
        else:
            return False


def get_most_common_words(tweets):
    most_common_words = {}
    for index, tweet in tweets.iterrows():
        tweet['Tweet'] = tweet['Tweet'].replace(".", "")
        tweet['Tweet'] = tweet['Tweet'].replace(",", "")
        tweet['Tweet'] = tweet['Tweet'].replace(":", "")
        tweet['Tweet'] = tweet['Tweet'].replace("\"", "")
        tweet['Tweet'] = tweet['Tweet'].replace("!", "")
        tweet['Tweet'] = tweet['Tweet'].replace("â€œ", "")
        tweet['Tweet'] = tweet['Tweet'].replace("â€˜", "")
        tweet['Tweet'] = tweet['Tweet'].replace("*", "")
        tweet['Tweet'] = tweet['Tweet'].replace("'", "")
        for word in tweet['Tweet'].split(' '):
            if not is_stopword(word):
                if word.upper() in most_common_words:
                    most_common_words[word.upper()] += 1
                else:
                    most_common_words[word.upper()] = 1

    # Sort Dict
    sorted_most_common_words = dict(sorted(most_common_words.items(), key=operator.itemgetter(1), reverse=True))
    return sorted_most_common_words

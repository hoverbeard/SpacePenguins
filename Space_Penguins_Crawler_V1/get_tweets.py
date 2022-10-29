import tweepy
import pandas as pd
import random

def get_tweet(news_sites, nr_per_site=10):
    # Useful link:
    client = tweepy.Client(
        "AAAAAAAAAAAAAAAAAAAAALnHigEAAAAARk3IxCWUYNojcexwlbwdQsAIjzc%3DSlg5ge1NQBveZusM31kxAIc25BD6bRMIfD1nkEA27q25rg6z8D")

    # Columns for Dataframe:
    # Person, Tweet, Link, Timestamp, Category, Bias-Classifier, ...?
    counter = 0
    tweets_frame = pd.DataFrame(columns=['Source', 'Tweet', 'Link', 'Timestamp', 'Reliability', 'Bias'])
    for e in news_sites:
        print(f'{e} analyzed')
        # Replace with your own search query
        query = 'from:' + e  # -is:retweet'

        tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at'],
                                             max_results=nr_per_site)

        for tweet in tweets.data:
            if 'http' not in tweet.text[-23:]:
                continue
            tweets_frame.loc[counter] = [e, tweet.text, tweet.text[-23:], tweet.created_at, random.randint(0, 10), random.randint(-10, 10)]
            counter += 1
    return tweets_frame

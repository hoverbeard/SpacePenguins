import numpy as np
import pandas as pd

import generate_html
import generate_js
from get_tweets import get_tweet
import get_most_common_words
import json

# Authenticate to Twitter:
# Using Twitter API V2 (important)
#news_sites = ['FoxNews', 'BBCWorld', 'CNN', 'bbcbreaking', 'time', 'mashable', 'theeconomist']
news_sites = ['foxnews', 'bbcbreaking', 'time', 'mashable', 'theeconomist']
#news_sites = ['mashable', 'cnnbrk', 'time', 'bbcbreaking', 'espn', 'gizmodo', 'wired', 'wsj', 'cnn', 'nytimes', 'foxnews', 'theeconomist', 'slate', 'reuters', 'usatoday', 'cbsnews', 'latimes', 'nzz', 'tagesanzeiger', '20min', 'bild']

tweets_frame = get_tweet(news_sites, nr_per_site=10)


how_comon_dict = get_most_common_words.get_most_common_words(tweets_frame)

# Take 40 most common keywords
how_comon_dict = first2pairs = {k: how_comon_dict[k] for k in list(how_comon_dict)[:30]}

html = generate_html.generate_html(how_comon_dict, tweets_frame)
with open('index.html', 'w') as f:
    f.write(html)

js = generate_js.generate_js(how_comon_dict, tweets_frame)
with open('script.js', 'w') as f:
    f.write(js)

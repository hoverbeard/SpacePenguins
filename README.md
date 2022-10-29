# Hackstairs 2022: A Visual News Text Classification Creator
# Space Penguin 

<h1 style="font-weight:normal">
  <a href="https://sourcerer.io">
    <img src=https://user-images.githubusercontent.com/20287615/34189346-d426d4c2-e4ef-11e7-9da4-cc76a1ed111d.png alt="Sourcerer" width=35>
  </a>
  &nbsp;sourcerer.io&nbsp;
  <a href="https://sourcerer.io/start"><img src=https://img.shields.io/badge/sourcerer-start%20now-brightgreen.svg?colorA=087c08></a>
  <a href="https://github.com/sourcerer-io/sourcerer-app/releases"><img src=https://img.shields.io/github/release/sourcerer-io/sourcerer-app.svg?colorB=58839b></a>
  <a href="https://github.com/sourcerer-io/sourcerer-app/blob/master/LICENSE.md"><img src=https://img.shields.io/github/license/sourcerer-io/sourcerer-app.svg?colorB=ff0000></a>
</h1>


[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/SpacePenguin/DECA/blob/master/Detailed_Expression_Capture_and_Animation.ipynb?authuser=1)


# Get Started 
Text can be an extremely rich source of information, but extracting insights from it can be hard and time-consuming, due to its unstructured nature.
 
 ![grafik](https://user-images.githubusercontent.com/78131082/198841347-648ebaa8-881e-4122-9a44-e1a67f3d38e2.png)


In natural language processing and machine learning, which both fall under the vast umbrella of artificial intelligence, sorting text data is getting easier.

## Idea: 

![grafik](https://user-images.githubusercontent.com/78131082/198841246-ec20b80a-f15f-4483-be67-1de52110f27a.png)

![grafik](https://user-images.githubusercontent.com/78131082/198841254-9620dbe1-de98-4df8-a3e6-6de1dfb06591.png)

![grafik](https://user-images.githubusercontent.com/78131082/198841205-f3c0a760-4967-4f44-a352-71e31170ef57.png)

![grafik](https://user-images.githubusercontent.com/78131082/198841214-57680ab5-881f-47b7-a8a9-d2fc3b7b47d0.png)

![grafik](https://user-images.githubusercontent.com/78131082/198841220-19248d6a-69ee-43c5-a74d-ef9c6551ee64.png)

<p align="center">
  <img alt="sergey" src="https://user-images.githubusercontent.com/20287615/47371068-c70f5a00-d6ef-11e8-8988-dcdca71bf83c.gif">
</p>


### **Why do we use activation functions in entry for ratings?**

**Crawling? How do we get text classification from the data we have?**

*"Wie komme ich an die News?"
Crawler: Informationen von irgendwo holen*

Input from news (ex. Twitter, Apple, Google etc) and using Binary Classifier Technical Machine Learning Algorithms to classify Text in different categories. 

Memes:
![alt text][image]
[image]: /idea/memes/Hack-idea-meme-interface.jpeg "alt_txt"


![grafik](https://user-images.githubusercontent.com/78131082/198840485-f3ae2d2c-2dc0-4774-b181-df8905c06a8e.png)

<img src="https://user-images.githubusercontent.com/78131082/198840485-f3ae2d2c-2dc0-4774-b181-df8905c06a8e.png)" alt="" width="200">


![grafik](https://user-images.githubusercontent.com/78131082/198841184-bcdeddce-62b0-45f2-9d9a-4219db0ddf1a.png)

# Current Problem 
Using [OpenAPI Natural language to Stripe API](https://beta.openai.com/examples/default-stripe-api), we can achieve 

`import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
  model="code-davinci-002",
  prompt="\"\"\"\nUtil exposes the following:\n\nutil.stripe() -> authenticates & returns the stripe module; usable as stripe.Charge.create etc\n\"\"\"\nimport util\n\"\"\"\nCreate a Stripe token using the users credit card: 5555-4444-3333-2222, expiration date 12 / 28, cvc 521\n\"\"\"",
  temperature=0,
  max_tokens=100,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0,
  stop=["\"\"\""]
)`

in the sample response: 

`token = util.stripe().Token.create(
card={
    "number": '5555-4444-3333-2222',
    "exp_month": 12,
    "exp_year": 28,
    "cvc": '521'
},
)

"""          `


# Implementation / How to Build

To build and run this application locally, you'll need latest versions of Git, Gradle and JDK installed on your computer. From your command line:

# Clone this repository
$ git clone https://github.com/hoverbeard/hackstairs2022

# Go into the repository
$ cd hackstairs2022

# Build
$ gradle build

# Run the app
$ python3 -jar build/libs/hackstairs2022.py



Usage
=====
To install hoverboard run the following command in bash:

```
curl -s https://hoverbeard/app/install | bash
```

To run wizard use `hoverbeard` command for macOS and Linux, `python3 -py sourcerer.py` in folder `Users\user\.hoverboard` for Windows.

Use parameter `--help` for additional info.



![grafik](https://user-images.githubusercontent.com/78131082/198842129-06b1b2ba-4f06-4cd4-b098-ade9e49f9847.png)


## Sourcecode from Kaggle 

### Simple Text Classification using Random Forest.

` import numpy as np from sklearn.feature_extraction.text 

import CountVectorizer from sklearn.ensemble 

import RandomForestClassifier from sklearn import datasets `

Following represents the corpus of text data used. The sample data we used from Twitter is meant to classify text topics including ITnews. This could be used for emails for classifying text topics for news. 

` corpus = [‘The apple is on sale’,’The oranges in on sale’,’The apple and is present’,’The orange and is present’] `

Case for Apple as group 1, and case for orange as group 2.

` Y = np.array([1,2,1,2]) `

Creating bag-of-words using CountVectorizer

` vectorizer = CountVectorizer(min_df=1)
X = vectorizer.fit_transform(corpus).toarray()`

Lastly, classify the text using random forest tree classifier.

`clf = RandomForestClassifier()
clf.fit(X, Y)
clf.predict(vectorizer.transform([‘apple is present’]).toarray())
`



# Conclusion (Demo)

[Youtube](https://youtu.be/YwtzSopqld0)

[<img src="![grafik](https://user-images.githubusercontent.com/78131082/198840975-366691c1-6b46-4da8-be70-f6cd14fa5c01.png)
" width="50%">](https://youtu.be/YwtzSopqld0 "Now in NLP")

# Results

![grafik](https://user-images.githubusercontent.com/78131082/198840913-e42d65cb-d9c5-4fb6-b75a-de6dc75fbb93.png)

PCA of resulting SCAN Embeddings provide visual representations of how the SCAN approach reshapes document vectors. Using the Google Snippets dataset, the left panel plots the first two principal components of the SBERT embeddings formed from those documents.
![grafik](https://user-images.githubusercontent.com/78131082/198841561-4bef8125-cc87-478f-94cb-b63dbead772f.png)

The right panel shows the principal components of the [CLS]-token of a fine-tuned RoBERTabase model using SCAN. Figure 3 and 4 provide the same exercise for the AG News data and the Abstracts Group data. 

![grafik](https://user-images.githubusercontent.com/78131082/198841509-c09facba-b679-483d-bd5f-4d697a12e13e.png)

In all cases, we find that the representation of the [CLS]-token neatly clusters datapoints into its corresponding classes after having been fine-tuned on the SCAN objective.

![grafik](https://user-images.githubusercontent.com/78131082/198841590-6f479f52-5c87-45ee-abd0-f222a372ad43.png)


# License

Sourcerer is under the MIT license. See the LICENSE for more information.

## Contributors

@[hoverbeard](https://github.com/hoverbeard)
@[GruneEnterTaste](https://github.com/GruneEnterTaste)
@[A5TEX](https://github.com/A5TEX)
@[esthicodes](https://github.com/esthicodes)


# Citations (Resources)

[Google Cloud API]
The Cloud Natural Language API supports a variety of languages. These languages are specified within a request using the optional language parameter. Language code parameters conform to ISO-639-1 or BCP-47 identifiers. If you do not specify a language parameter, then the language for the request is auto-detected by the Natural Language API.

[Text Classification](https://monkeylearn.com/text-classification/)
[Google Japan Keyboard](https://m.youtube.com/watch?v=9G3DWHf1xX0&feature=youtu.be)

[ETH Library DocSCAN: Unsupervised Text Classification via Learning from Neighbors](https://www.research-collection.ethz.ch/bitstream/handle/20.500.11850/48468/CLE_WP_2021_08.pdf?sequence=1&isAllowed=y)
![grafik](https://user-images.githubusercontent.com/78131082/198841472-c03d1c2d-bf4f-4301-bcdc-171823587b80.png)

[Twitter News API]

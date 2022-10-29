# Hackstairs2022 SpacePenguins Team

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YadiraF/DECA/blob/master/Detailed_Expression_Capture_and_Animation.ipynb?authuser=1)


# Introduction 
Text can be an extremely rich source of information, but extracting insights from it can be hard and time-consuming, due to its unstructured nature.
 
In natural language processing and machine learning, which both fall under the vast umbrella of artificial intelligence, sorting text data is getting easier.

## Idea: 

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


# Implementation 



## Sourcecode from Kaggle 

### Simple Text Classification using Random Forest.

` import numpy as np from sklearn.feature_extraction.text 
import CountVectorizer from sklearn.ensemble 
import RandomForestClassifier from sklearn import datasets `

Following represents the corpus of text data used. The sample data I used is meant to classify text about apple and oranges. This could be used for emails for classifying spam.

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

Youtube 


# Results



## Contributors

@[hoverbeard](https://github.com/hoverbeard)
@[GruneEnterTaste](https://github.com/GruneEnterTaste)
@[A5TEX](https://github.com/A5TEX)
@[esthicodes](https://github.com/esthicodes)


# Citations (Resources)

[Google Cloud API]
The Cloud Natural Language API supports a variety of languages. These languages are specified within a request using the optional language parameter. Language code parameters conform to ISO-639-1 or BCP-47 identifiers. If you do not specify a language parameter, then the language for the request is auto-detected by the Natural Language API.

[Text Classification]
[Google Japan Keyboard]()

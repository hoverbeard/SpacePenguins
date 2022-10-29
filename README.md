# Hackstairs2022 SpacePenguins Team

# Introduction 

Idea: **Why do we use activation functions in neural networks?**

**What is the “vanishing gradient” problem? Which activation functions are subject to
this issue?**

Input from 

Memes:



# Implementation 

## Sourcecode from Kaggle 

Simple Text Classification using Random Forest.

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

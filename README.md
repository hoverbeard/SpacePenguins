# Hackstairs2022 
# SpacePenguins Team

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YadiraF/DECA/blob/master/Detailed_Expression_Capture_and_Animation.ipynb?authuser=1)


# Introduction 
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


# Implementation 



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

PCA of resulting SCAN Embeddings provide visual representations of how the SCAN approach reshapes document vectors. Using the Google Snippets dataset, the left panel plots the first two principal components of the SBERT embeddings formed from those
documents. The right panel shows the principal components of the [CLS]-token of a fine-tuned RoBERTabase model using SCAN. Figure 3 and 4 provide the same exercise for the AG News data and the Abstracts Group data. In all cases, we find that the representation of the [CLS]-token neatly clusters datapoints into its corresponding classes after having been fine-tuned on the SCAN objective.

![grafik](https://user-images.githubusercontent.com/78131082/198841509-c09facba-b679-483d-bd5f-4d697a12e13e.png)


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
[ETH Library DocSCAN: Unsupervised Text Classification via Learning from Neighbors](https://www.research-collection.ethz.ch/bitstream/handle/20.500.11850/48468/CLE_WP_2021_08.pdf?sequence=1&isAllowed=y)

![grafik](https://user-images.githubusercontent.com/78131082/198841472-c03d1c2d-bf4f-4301-bcdc-171823587b80.png)

[Twitter News API]

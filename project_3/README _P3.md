
# Executive Summary



# 1. Problem Statement


The television shows 'Elementary' and 'Sherlock' are about the detective Sherlock Holmes from the studios CBS and BBC respectively. The CBS executives want to use a model to classify the subreddit threads r/elementary and r/sherlock to determine whether in viewers' minds there are differences between 'Elementary' and the other show.

This project will develop a model to distinguish between the 2 subreddits. The positive class will be the posts from the elementary subreddit and the negative class will be sherlock subreddit posts. Logisitic Regression and Naive Bayes models will be used to classify the 2 subreddits. The accuracy scores will be used to evaluate and find the best model for classification.

The project will also analyse which words were used by the model for successful classification to help CBS executives find out which terms/topics resonate in viewers' minds to ensure the popularity of the show.

---

# 2.  Overview

The summary of the process is to first scrape the reddit subthreads 'r/sherlock' and 'r/elementary. The subredits data were then cleaned by converting the null values to space so as to not lose information in the rows and to drop duplicate rows and columns that do not contain any text relevant for classification, the remaining text was lemmatized, cleaned of urls, removal of common words and changed to lower case. The text was analysed for top common words and words different between the threads as well as any words that may stand out. Pipeline and gridsearch was then used to determine that the highest scoring model is Logistic Regression. The model was able to do much better than the baseline with a score of 0.83. The model is slightly better in classifying the negative class i.e posts from 'r/sherlock'. The model also has a ROCAUC score of 88 which means it can distinguish between the 2 subreddits fairly well.


---

# 3. Contents

1. [Data Aquisition](01_Data_Aquisition.ipynb)


2. [Data Cleaning](02_Data_Cleaning.ipynb)   


3. [EDA](03_EDA.ipynb)


4. [Modeling and Evaluation](04_Modeling_and_Evaluation.ipynb)

---

# 4. Conclusion

The Logisitic Regression was selected and fine tuned as it had the highest accuracy score 0.89 (rounded) as compared the Naive Bayes model on the test data. The model has a slight bias towards the negative class i.e r/sherlock posts.

There were misclassified posts that had words not relevant to either subreddits and hence understandably misclassified.

Hence CBS executives should be reassured that the high model accuracy demonstrates that viewers are able to distinguish between both the shows.

---

# 5. Recommendations

CBS executves should consider developing plots based on the the topics/themes found in the top 25 impactful words.

The model can be improved by getting more data, changing the hyperparameters, reducing the no.of features, using different classifiers and transformers.

---

# 6. References

Presentation
 https://www.tvguide.com/
https://en.wikipedia.org/wiki/Sherlock_(TV_series)
https://en.wikipedia.org/wiki/Elementary_(TV_series)

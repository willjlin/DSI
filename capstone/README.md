# Capstone: Bank Marketing Prediction
####  Will Lin



## Problem Statement

Using data on social economic indicators, bank client data, telemarketing campaign data, contact to find the best machine learning model that can predict whether a customer will purchase a term deposit i.e fixed deposit at different economic levels.

This is to help the bank sales people target customers during different economic levels and time periods of the year and determine who have a higher probability to purchase the bank's product and hence increase bank's sales revenue

The accuracy and recall score from different machine-learning models will be compared and used to evaluate to find the best model for production and prediction.



## Executive Summary

**Exploratory Data Analysis**

There is no trend from economic indicators.

Bank client data show a positive trend relating to disposable income i.e clients with higher paying jobs indicating more disposable income would purchase the bank's product.

Contact before current campaign data shows that clients would be more likely to purchase if they had been contacted previously and if they had bought a product in the previous campaign

Current campaign data shows a negative trend of less number of contacts, the higher likelihood the clients would purchase. This makes sense as if they had liked the product they would have purchased in the earlier contacts.

Time related data such as month and day did not show any trend due to inconsistent calling rates.


**Modelling**

Logistic Regression, Naive Bayes, RandomForest and XGboost models were used to model the data. There is a heavy class-imbalance in the data. The Synthetic Minority Over-sampling Technique (SMOTE) was used to adjust for the imbalance.

Logistic Regression has shown to be the best performing model at an accuracy score of 0.838, with recall score of 0.77.


## Conclusions

Economic factors have the strongest negative and positive impact on whether a client would purchase a product. Time related data have the next largest impact but any trend derived may not be accurate due to inconsistent calling rates. Clients with higher disposable income would be more likely to purchase a product. Psychological factors seem to have weakest purchase impact.

However, the model may not be able to generalise at other economic levels and other countries e.g Singapore as data used is from a Portuguese bank

### Recommendations

More data on disposable income, risk acceptance level, different financial products bought, product yield, interest rate vs product yield, product risk level would help the bank to target products to suitable customers

More data on telemarketer's selling ability to help determine the influence of this factor.

More years of data from different countries at different economic levels to help generalise to other countries



### References

 Data dictionary


|Feature|Type|Description|
| --- | --- | --- |
 |age  <br/>            |int      | the age of client
 |job <br/>          |str      |type of job
 |marital <br/>     |str  | marital status
 |education  <br/>      |str      | educational level
 |default<br/>        |str      |whether client has credit default
 |housing <br/>       |str      |whether client has housing loan
 |loan <br/>        |str    |whether client has personal loan
 |contact <br/>|str| communication device contacted
 |month <br/>           |str|last month contacted
 |day_of_week <br/>           |str| last day of the week contacted
 |duration <br/>    |int| last call duration
 |campaign <br/>       |int      | number of contacts performed during this campaign for this client
 |pdays  <br/>         |int      | number of days that passed by after the client was last contacted from a previous campaign (999 means client was not previously contacted)
 |previous <br/>|int | number of contacts performed before this campaign and for this client
 |poutcome <br/>        |str     | outcome of the previous marketing campaign
 |emp.var.rate <br/>|float| employment variation rate
 |cons.price.idx <br/>      |float| consumer price index - monthly indicator
 |cons.conf.idx <br/> |float|  consumer confidence index - monthly indicator
 |euribor3m  <br/>   |float| euribor 3 month rate - daily indicator
 |nr.employed:  <br/>  |int| number of employees - quarterly indicator
 |y <br/>    |str| whether the client subscribed a term deposit


Journal references

Moro et al., 2014] S. Moro, P. Cortez and P. Rita. A Data-Driven Approach to Predict the Success of Bank Telemarketing. Decision Support Systems, Elsevier, 62:22-31, June 2014.

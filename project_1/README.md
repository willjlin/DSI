# Analysis of SAT and ACT tests

---
# Problem Statement
The SAT and ACT are standardised tests used for admission requirements by US universities. The tests assess the student's proficiency in various academic skills necessary for college success.

ACT had been the most popular test for college applications till 2018, when SAT had higher participation rates.

The continued popularity of SAT should be in the interest of College Board which owns that test. Hence the factors that increase the participation rate need to be identified and a suitable state selected to implement these factors.

---
# Overview

The summary of the process to clean the data, exploratory data analyze, visualize , analysis via descriptive and inferential statistics, the conduct of outside research and the conclusions and recommendations are provided below.

---
### 1. 2017 Data Import & Cleaning

The 2017 SAT and ACT data were imported from the csv files provided.

The SAT 2017 data consisted of the all 51 states' participation rates, the average student's scores for Evidence Based reading and writing, Math and average student's Total score.

The ACT 2017 data consisted of the all 51 states' participation rates, the average student's scores for English, Math, Reading, Science and Composite score.
An analysis of the data showed the following:
-	There were no missing values.
-	Minimum value of the SAT math score was 52 which is lower than the minimum possible value of 200.
-	Minimum value of the ACT Science score was 2.30 which was 8 times lower than mean value.
-	There is an extra row containing National statistics for ACT 2017 data
-	The state and participation rates for SAT and ACT 2017 and the ACT 2017 Composite score were object data types. The rest of the numerical values were integer or float data types
-	ACT 2017 Composite score for Wyoming was incorrect at “20.2x”
Data cleaning process:
-	The errors were corrected after comparison with the source data in the provided links
-	The columns were renamed to be informative, lower case and with no spaces
-	The columns with numerical values were changed to float data types
-	Row containing National Statistics for ACT 2017 data was dropped
A data dictionary was created.
Both data sets were merged and saved into “combined_2017.csv”

---
### 2. 2018 Data Import and Cleaning

The 2017 SAT and ACT data were imported from the csv files provided.
The SAT and ACT 2018 data consisted of the all 51 states' participation rates, the average student's scores for Evidence Based reading and writing, Math and average student's Total score.
The ACT 2018 data consisted of the all 51 states' participation rates, the average student's scores for English, Math, Reading, Science and Composite score.
An analysis of the data showed the following:
-	There were no missing values.
-	The participation rates for SAT were object data types.
-	Delaware’s ACT Composite score differs from the source data by 0.6
-	The rest of the numerical values were integer or float data types
Data cleaning process:
-	The errors were corrected after comparison with the source data in the provided links
-	The columns were renamed to be informative, lower case and with no spaces
-	The columns with numerical values were changed to float data types
A data dictionary was created.
Both data sets were merged and saved into “combined_2018.csv” . Both 2018 and 2017 data were then merged into a dataframe named “final.csv”
---
### 3. Exploratory Data Analysis

The standard deviation was manually calculated. Standard deviations from the manual calculations and numpy's std method are slightly different from using panda's describe function as panda uses the corrected sample standard deviation formula while numpy and the the manual calculations uses the uncorrected sample standard deviation formula

North Dakota, Mississippi and Iowa have the lowest participation at 2 percent% for SAT 2017 while Michigan, District of Columbia, Delaware and Connecticut have the highest participation at 100 % for SAT 2017

North Dakota has the lowest participation at 2 percent% for SAT 2018 while Michigan, Idaho, Colorado, Delaware and Connecticut have the highest participation at 100 % for SAT 2018.

Maine has the lowest participation at 8 percent% for ACT 2017 while South Carolina, Utah, Tennessee, Alabama, Missouri, North Carolina, Nevada, Montana, Wisconsin ,Mississippi, Minnesota, Louisiana, Kentucky, Colorado, Arkansas, Oklahoma and Wyoming have the highest participation at 100 % for ACT 2017
Maine has the lowest participation at 2 percent% for ACT 2018 while Utah, Tennessee, South Carolina, Alabama, Missouri, Ohio, North Carolina, Nevada, Nebraska, Montana, Wisconsin, Mississippi, Louisiana, Kentucky, Arkansas, Oklahoma and Wyoming have the highest participation at 100 % for ACT 2018

District of Columbia has the lowest total score at 950 for SAT 2017 while Minnesota has the highest total score at 1295 for SAT 2017.

District of Columbia has the lowest total score at 977 for SAT 2018 while Minnesota has the highest total score at 1298 for SAT 2018.

Nevada has the lowest composite score at 17.8 for ACT 2017  while New Hampshire has the highest composite score at 25.5 for ACT 2017.

Nevada has the lowest composite score at 17.7 for ACT 2018 while Connecticut has the highest composite score at 25.6 for ACT 2018.
The District of Columbia's SAT participation rate decreased from 100% to 92%  in 2018 while Minnesota and Colorado's ACT participation rate decreased from 100% to 99% and 30% respectively in 2018.
Florida, Georgia, Hawaii have more than 50% participation rate for both tests in 2017 while Florida, Georgia, Hawaii, North and South Carolina have more than 50% participation rate for both tests in 2018.

---

### 4. Data Visualization

According to the heat map visualization, SAT participation rates are negatively correlated to ACT participation rates. Test scores are also negatively correlated to participation rate for both tests.
According to the histogram visualization, there are more states that have 100% ACT participation rate than SAT for both 2017 and 2018. There are more states that have 0-20% SAT participation rate than ACT for both 2017 and 2018. Both SAT and ACT math scores have similar shapes for both years. ACT has a slight increase in math scores in 2018. SAT reading scores are higher than ACT scores. There is a slight increase in reading scores for SAT 2018.

According to the scatterplot visualizations, there is no trend between the 2017 SAT and ACT math, read and total/composite scores. There is a positive trend between the 2017-2018 SAT total scores and 2017 - 2018 ACT composite scores. There is a negative correlation between SAT and ACT participation for both years. This is also shown in the previous heat map.

According to the boxplot visualizations, there is a slight increase in the spread of SAT participation in 2018, however ACT participation spread seems to remain unchanged. The participation rate for ACTs are higher than SATs for both years. Students taking SAT score higher in reading and writing for both years than math. The spread for both subjects decreased slightly in 2018. The spread of SAT total score in 2018 decreased slightly. The ACT reading test is highest scoring subject, followed by english and then by both math and science. For most tests there is no change from 2017-2018 except for english which has a slight increase in scores in 2018. This is a similar trend to SAT where the non-technical subjects score higher than the technical subjects.The spread for most subjects remain unchanged except for english which increased in 2018. There is no change in the ACT composite score from 2017-2018.

---
### 5. Descriptive and Inferential Statistics

The histograms show that all variables are not normally distributed. The distributions have 2 peaks and hence bimodal. The standard deviation for all variables is smaller relative to the mean and shows that the data is not spread out which indicates it is not normally distributed.

The assumption that the distribution for the math and reading scores and participation rate will be normally distributed should hold if larger random samples are taken as according to the central limit theorem.

Statistical inference is not necessary as the conduct of SAT and ACT tests are based on education policy and hence probability does not explain the relationship.

It cannot be said that students with higher SAT math score are better than those with lower ACT math score, or vice versa as the scale i.e scores range for both tests and content are different.

---
### 6. Outside Research

3 states, Missouri, Tennesse and South Carolina were selected due to their 100% ACT participation rates even though the tests are not mandated. Research shows their high participation rate is mostly due to funding by the state to take the test or retake the test.

---
### 7. Conclusions and Recommendations

There is negative correlation in the participation rates for both tests. The participation rates seem to depend on whether the state mandates the test or provides funding. In addition, SAT Day has also increased participation rates.

Oregon was selected to focus on increasing their low participation rate as the state does not mandate taking either SAT or ACT tests and there is no state funding provided to take the tests.

College Board can discuss with the state on mandating or providing state funding for taking SAT. College Board can also offer reduced fees for students retaking the tests.


---
### 8. References

Data Dictionaries

|Feature|Type|Dataset|Description|
|---|---|---|---|
|state|object|SAT|This is the name of the state|
|participationpct_sat_2017|float|SAT|This is the precentage of students who took the SAT tests in 2017 in the corresponding state|
|reading & writing_sat_2017|float|SAT|This is the average score of the students who have taken the SAT evidence-based reading and writing test in 2017 in the corresponding state|
|math_sat_2017|float|SAT|This is the average score of the students who have taken the SAT math test in 2017 the corresponding state|
|total_sat_2017|float|SAT|This is the average total score of the students who have taken both the SAT tests in 2017 in the corresponding state|
|state|object|ACT|This is the name of the state|
|participationpct_act_2017|float|ACT|This is the precentage of students who took the ACT tests in 2017 in the corresponding state|
|english_act_2017|float|ACT|This is the average score of the students who have taken the ACT english test in 2017 in the corresponding state|
|math_act_2017|float|ACT|This is the average score of the students who have taken the ACT math test in 2017 in the corresponding state|
|reading_act_2017|float|ACT|This is the average score of the students who have taken the ACT reading test in 2017 in the corresponding state|
|science_act_2017|float|ACT|This is the average score of the students who have taken the ACT science test in 2017 in the corresponding state|
|composite_act_2017|float|ACT|This is the average total score of the students who have taken the ACT tests in 2017 in the corresponding state|
|participationpct_sat_2018|float|SAT|This is the precentage of students who took the SAT tests in 2018 in the corresponding state|
|reading & writing_sat_2018|float|SAT|This is the average score of the students who have taken the SAT evidence-based reading and writing test in 2018 in the corresponding state|
|math_sat_2018|float|SAT|This is the average score of the students who have taken the SAT math test in 2018 the corresponding state|
|total_sat_2018|float|SAT|This is the average total score of the students who have taken both the SAT tests in 2018 in the corresponding state|
|state|object|ACT|This is the name of the state|
|participationpct_act_2018|float|ACT|This is the precentage of students who took the ACT tests in 2018 in the corresponding state|
|english_act_2018|float|ACT|This is the average score of the students who have taken the ACT english test in 2018 in the corresponding state|
|math_act_2018|float|ACT|This is the average score of the students who have taken the ACT math test in 2018 in the corresponding state|
|reading_act_2018|float|ACT|This is the average score of the students who have taken the ACT reading test in 2018 in the corresponding state|
|science_act_2018|float|ACT|This is the average score of the students who have taken the ACT science test in 2018 in the corresponding state|
|composite_act_2018|float|ACT|This is the average total score of the students who have taken the ACT tests in 2018 in the corresponding state|



Problem statement

https://blog.prepscholar.com/act-vs-sat

Descriptive and inferential statistics

https://bolt.mph.ufl.edu/6050-6052/unit-1/one-quantitative-variable-introduction/describing-distributions/

https://www.robertniles.com/stats/stdev.shtml)
(http://sphweb.bumc.bu.edu/otlt/MPH-Modules/BS/BS704_Probability/BS704_Probability12.html)

Outside Research

https://blog.prepscholar.com/which-states-require-the-act-full-list-and-advice

https://blog.prepscholar.com/which-states-require-the-sat

https://www.tn.gov/education/news/2018/10/31/tn-students-break-records-with-highest-ever-act-score-and-participation-rate.html

https://dese.mo.gov/communications/news-releases/missouri-act-scores-released-class-2018

https://www.thestate.com/news/politics-government/article236809728.html

https://www.greenvilleonline.com/story/news/education/2019/09/24/sat-scores-drop-more-sc-students-take-sat-standardized-test/2427143001/

https://www.washingtonpost.com/local/education/sat-scores-drop-for-2019-class-but-participation-rises-through-testing-in-schools/2019/09/23/332fc4d0-de11-11e9-8dc8-498eabc129a0_story.html

Conclusions and Recommendations

https://www.edweek.org/ew/articles/2018/10/31/sat-scores-rise-as-number-of-test-takers.html

https://www.hanoverresearch.com/media/Best-Practices-to-Increase-SAT-Participation-1.pdf

https://www.opb.org/news/article/oregon-high-school-state-tests/

https://www.oregonlive.com/education/2020/03/oregons-public-universities-wont-ask-for-sat-scores-in-college-applications-anymore.html

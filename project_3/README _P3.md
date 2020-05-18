
# Executive Summary



# 1. Problem Statement

To identify indicators/ features from the Ames Housing dataset which predict the sale price of housing in Ames Iowa. This information will help buyers and investors to find the best houses based on their preferences and needs.  It will also help sellers to identify ways to increase their house's selling price. Linear regression models with and without regularization such as Lasso, Ridge and ElasticNet will be used to model the data and R squared and Root Mean Square Error will be used to evaluate and find the best model for production and prediction.

The predicted sale price based on the data from Kaggle will be submitted to the DSI Kaggle competition to evaluate the effectiveness of the model on unseen data.

---

# 2.  Overview

The summary of the process is to clean the data, perform EDA, data visualization , analysis via descriptive and inferential statistics, using pipeline and gridsearch to model and fine tune the model, evaluate and select the best model for production and to use on the Kaggle data set for prediction and submission. Outside research will be conducted and the conclusions and recommendations are provided below.

---

# 3. Contents

1. [EDA and Cleaning](01_EDA_and_Cleaning.ipynb)


2. [Preprocessing and Feature Engineering](02_Preprocessing_and_Feature_Engineering.ipynb)   


3. [Model Bechmarks](03_Model_Benchmarks.ipynb)


4. [Model Tuning](04_Model_Tuning.ipynb)


5. [Production Model and Insights](05_Production_Model_and_Insights.ipynb)


6. [Kaggle Submission](05_Kaggle_Submission.ipynb)

---

# 4. Conclusion

The ElasticNet model was selected and fine tuned as it had the highest R squared (R2) and lowest Root Mean Squared errors (RMSE) as compared the Linear Regression, Lasso and Ridge models, with a R2 of 0.89 and RMSE of 26003.6 on the test data.

The RMSE on the Kaggle test data was about 31 175.5. This indicates that the ElasticNet might have overfitted on the training data.

Analysis of the coefficients of the final selected features shows that age related, condition related, exterior related, interior related, size and location related features have an impact on the sale price. Size and condition related features have the highest coefficients positively corresponding to sale price, while age-related features are negatively corresponding to sale prince.

---

# 5. Recommendations

Ames Iowa is a university town. Research has shown that housing at university towns are higher priced due to staff, faculty members and students wanting to stay near the university. Investors want to buy property near universities as well to rent out to abovementioned group of people.

To generalise the model to other cities, more information on the house distance from the university should be obtained to determine the effect the distance from university or facilities has on sale price. In addition, information on demographics, inflation, weather, economic activity is needed to determine their impact on sale price.

---

# 6. References

 Data dictionary


| Feature| dtype | Description
| --- | --- | --- |
| 1st Flr SF| int64 | First Floor square feet
| 2nd Flr SF| int64 | Second Floor square feet
| 3Ssn Porch| int64 | Three season porch area in square feet
| Alley| object | Type of alley access to property
| Bedroom AbvGr| int64 | Number of bedrooms above basement level
| BedroomA bvGr| int64 | Number of bedrooms above basement level
| Bldg Type| object | Type of dwelling
| Bsmt Cond| object | General condition of the basement
| Bsmt Exposure| object | Walkout or garden level basement walls
| Bsmt Full Bath| float64 | Basement full bathrooms
| Bsmt Half Bath| float64 | Basement half bathrooms
| Bsmt Qual| object | Height of the basement
| Bsmt Unf SF| float64 | Unfinished square feet of basement area
| BsmtFin SF 1| float64 | Basement Type 1 finished square feet
| BsmtFin SF 2| float64 | Basement Type 2 finished square feet
| BsmtFin Type 1| object | Quality of basement finished area
| BsmtFin Type 2| object | Quality of second finished area (if present)
| Central Air| object | Central air conditioning
| Condition 1| object | Proximity to main road or railroad
| Condition 2| object | Proximity to main road or railroad (if a second is present)
| Electrical| object | Electrical system
| Enclosed Porch| int64 | Enclosed porch area in square feet
| Exter Cond| object | Present condition of the material on the exterior
| Exter Qual| object | Exterior material quality
| Exterior 1st| object | Exterior covering on house
| Exterior 2nd| object | Exterior covering on house (if more than one material)
| Fence| object | Fence quality
| Fireplace Qu| object | Fireplace quality
| Fireplaces| int64 | Number of fireplaces
| Foundation| object | Type of foundation
| Full Bath| int64 | Full bathrooms above grade
| Functional| object | Home functionality rating
| Garage Area| float64 | Size of garage in square feet
| Garage Cars| float64 | Size of garage in car capacity
| Garage Cond| object | Garage condition
| Garage Finish| object | Interior finish of the garage Fin Finished
| Garage Qual| object | Garage quality
| Garage Type| object | Garage location
| Garage Yr Blt| float64 | Year garage was built
| Gr Liv Area| int64 | Above grade (ground) living area square feet
| Half Bath| int64 | Half baths above grade
| Heating| object | Type of heating
| Heating QC| object | Heating quality and condition
| house age| int64 | Age of house
| House Style| object | Style of dwelling
| Kitchen AbvGr| int64 | Number of kitchens
| Kitchen Qual| object | Kitchen quality
| Land Contour| object | Flatness of the property
| Land Slope| object | Slope of property
| Lot Area| int64 | Lot size in square feet
| Lot Config| object | Lot configuration
| Lot Frontage| float64 | Linear feet of street connected to property
| Lot Shape| object | General shape of property
| Low Qual Fin SF| float64 | Low quality finished square feet (all floors)
| Mas Vnr Area| float64 | Masonry veneer area in square feet
| Mas Vnr Type| object | Masonry veneer type
| Misc Feature| object | Miscellaneous feature not covered in other categories
| Misc Val| int64 | Value of miscellaneous feature in dollars
| Mo Sold| int64 | Month Sold
| MS SubClass| int64 | The building class
| MS Zoning| object | Identifies the general zoning classification of the sale.
| Neighborhood| object | Physical locations within Ames city limits
| Open Porch SF| int64 | Open porch area in square feet
| Overall Cond| int64 | Overall condition rating
| Overall Qual| int64 | Overall material and finish quality
| Paved Drive| object | Paved driveway
| Pool Area| int64 | Pool area in square feet
| Pool QC| object | Pool Quality
| reno newness| int64 | The age of latest renovation
| Roof Matl| object | Roof material
| Roof Style| object | Type of roof
| Sale Type| object | Type of sale
| SalePrice| int64 | the property's sale price in dollars
| Screen Porch| int64 | Screen porch area in square feet
| Street| object | Type of road access to property
| Total Bsmt SF| float64 | Total square feet of basement area
| TotRms AbvGrd| int64 | Total rooms above grade (does not include bathrooms)
| Wood Deck SF| int64 | Wood deck area in square feet
| Year Built| int64 | Original construction date
| Year Remod/Add| int64 | Remodel date (same as construction date if no remodeling or additions)
| Yr Sold| int64 | Year Sold


Presentation

https://sites.duke.edu/urbaneconomics/?p=1102
https://www.weather.gov/images/dmx/Climate/Annual_AvgT.png
https://en.wikipedia.org/wiki/Ames,_Iowa
http://jse.amstat.org/v19n3/decock.pdf
https://www.census.gov/quickfacts/amescityiowa

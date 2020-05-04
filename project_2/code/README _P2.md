
# Executive Summary

#### by Jane Liang 12/06/2018


## 1. Problem Statement

The main purpose of this data science project is to use simple regression models to accurately predict the home prices in Ames, Iowa. By doing regression analysis, we can confirm the theoretical relationship and identify the features which are potentially have relationship with taraget variable. Most likely, there is specific interest in the magnitudes and signs of the coefficients in the linear regression model. Throughout the iterative modeling and feature selection processes, we can gain a deeper insight of 80 features relate to the home price and understand better the mechanism behind various models.


## 2. Data Description
In this data science project, I'll explore the Ames, Iowa Housing Dataset, prepared by Dean De Cock, and described in the paper [Ames, Iowa: Alternative to the Boston Housing Data as an End of Semester Regression Project](http://jse.amstat.org/v19n3/decock.pdf) 
. The Ames Housing training dataset provides 2051 homes in Ames and 80 features. For each `Id` in the test set, we must predict the value of the `SalePrice` variable for 879 houses. 

| feature | dype |Description 
| --- | --- | --- | 
| MS SubClass | int64 |
| MS Zoning | object |Identifies the general zoning classification of the sale.
| Lot Frontage | float64 |Linear feet of street connected to property
| Lot Area | int64 |Lot size in square feet
| Street | object |Type of road access to property
| Lot Shape | object |General shape of property
| Land Contour | object |Flatness of the property
| Neighborhood | object |Physical locations within Ames city limits
| Condition 1 | object |Proximity to main road or railroad
| Condition 2 | object |Proximity to main road or railroad (if a second is present)
| Bldg Type | object |Type of dwelling
| House Style | object |Style of dwelling
| Overall Qual | int64 |Overall material and finish quality
| Overall Cond | int64 |Overall condition rating
10 Very Excellent
| Year Built | int64 |Original construction date
| Year Remod/Add | int64 |Remodel date (same as construction date if no remodeling or additions)
| Roof Style | object |Type of roof
Flat Flat
| Roof Matl | object |Roof material
| Exterior 1st | object |Exterior covering on house
| Exterior 2nd | object |Exterior covering on house (if more than one material)
| Mas Vnr Type | object |Masonry veneer type
| Mas Vnr Area | float64 |Masonry veneer area in square feet
| Exter Qual | object |Exterior material quality
| Exter Cond | object |Present condition of the material on the exterior
| Foundation | object |Type of foundation
| Bsmt Qual | object |Height of the basement
| Bsmt Cond | object |General condition of the basement
| Bsmt Exposure | object |Walkout or garden level basement walls
| BsmtFin Type 1 | object | Quality of basement finished area
| BsmtFin Type 2 | object |Quality of second finished area (if present)
| Total Bsmt SF | float64 |Total square feet of basement area
| Heating | object |Type of heating
| Heating QC | object |Heating quality and condition
| Central Air | object |Central air conditioning
| Electrical | object |Electrical system
| Gr Liv Area | int64 |Above grade (ground) living area square feet
| Bsmt Full Bath | float64 |Basement full bathrooms
| Bsmt Half Bath | float64 |Basement half bathrooms
| Full Bath | int64 |Full bathrooms above grade
| Half Bath | int64 |Half baths above grade
| Bedroom AbvGr | int64 |Number of bedrooms above basement level
| Kitchen AbvGr | int64 |Number of kitchens
| Kitchen Qual | object |Kitchen quality
| TotRms AbvGrd | int64 |Total rooms above grade (does not include bathrooms)
| Functional | object |Home functionality rating
| Fireplaces | int64 |Number of fireplaces
| Fireplace Qu | object |Fireplace quality
| Garage Type | object |Garage location
| Garage Yr Blt | float64 |Year garage was built
| Garage Finish | object |Interior finish of the garage Fin Finished
| Garage Cars | float64 |Size of garage in car capacity
| Garage Area | float64 |Size of garage in square feet
| Garage Qual | object |Garage quality
| Garage Cond | object |Garage condition
| Paved Drive | object |Paved driveway
| Wood Deck SF | int64 |Wood deck area in square feet
| Open Porch SF | int64 |Open porch area in square feet
| Enclosed Porch | int64 |Enclosed porch area in square feet
| 3Ssn Porch | int64 |Three season porch area in square feet
| Screen Porch | int64 |Screen porch area in square feet
| Pool Area | int64 |Pool area in square feet
| Mo Sold | int64 |Month Sold
| Yr Sold | int64 |Year Sold
| Sale Type | object |Type of sale
| SalePrice | int64 | the property's sale price in dollars



## 3. Contents of Jupyter Notebook

1. [EDA and Cleaning](01_EDA_and_Cleaning.ipynb)
    - 1.1 [Problem Statement](#1.-Problem-Statement)
    - 1.2 [Data Description](#2.-Data-Description)
    - 1.3 [Missing Values](#5.-Missing-Values) 
    - 1.4 [EDA and cleaning](#6.-Exploratory-Data-Analysis-and-Cleaning)
    
    
2. [Preprocessing and Feature Engineering](02_Preprocessing_and_Feature_Engineering.ipynb)   
    - 2.1 [Feature Engineering](02_Preprocessing_and_Feature_Engineering.ipynb/#3.-Feature-Engineering)
    - 2.2 [Polynomial Features](02_Preprocessing_and_Feature_Engineering.ipynb/#4.-Polynomial-Feature-of-Top-4-Important-Features)
    - 2.3 [One-hot encoding](02_Preprocessing_and_Feature_Engineering.ipynb/#5.-One-hot-encoding)
    - 2.4 [Split training and validation dataset](02_Preprocessing_and_Feature_Engineering.ipynb/#7.-Create-training-and-validation-sets)
 
 
3. [Model Bechmarks](03_Model_Benchmarks.ipynb)
    - 3.1 [Linear regression model](03_Model_Benchmarks.ipynb/#4.-Baseline-Model-Setup)
    - 3.2 [Results](03_Model_Benchmarks.ipynb/#5.-Baseline-model-test-result)
    
    
4. [Model Tuning and Selection](04_Model_Tuning_and_Selection.ipynb)
    - 4.1 [Pipeline](04_Model_Tuning_and_Selection.ipynb/#3._Pipeline)
    - 4.2 [GridSearch](04_Model_Tuning_and_Selection.ipynb/#4._GridSearch)
    - 4.3 [Model Selection](04_Model_Tuning_and_Selection.ipynb/#5.-Comparing-model-performance )
    - 4.4 [Interpretation](04_Model_Tuning_and_Selection.ipynb/#6.-Model-Interpretation )
    
    
5. [Kaggle Submission](05_Kaggle_Submission.ipynb)


Start by conducting some exploratory data analysis followed by processing the data based on our findings. Set up the pipeline and gridsearch for best parameters and hyperparameters for programmatical feature selection feature selection and modeling. Test the various regression models including Multiple Linear Regression model, Lasso, Ridge, and ElasticNEt. Select the best model and interpret the model with the beta coefficients.


# 4. Figures and Finding from EDA

[Presentation Link](./Project2_Jane.pdf)



# 5. Conclusion

My Ridge model is done with a cross validated score of 90.5% on my train set and 90.5% on the test set which indicated that the model works good. I implemented polynomial features and log-tranformed the two variables (making the relationship with the target “more linear”). 

However, in regression with multiple independent variables, the coefficient tell us how much the dependent variable is expected to increase when that independent variable increases by one, holding all the other independent variables constant. However, if the variables are entered in the multiple regression and those variables are correlated with each other to high degree and correlated to our target variable, then the beta weights for these correlated independent variables are arbitrarily allocated predictive credit among the correlated independent variables.

For example, when the interaction term between `Overall Qual` and `Total_sqft` increase by one, the `SalePrice` increase about \$1500000. However, the `Total_Sqft^2` increase by one the SalePrice decreased in about $15000 in the same time. Hence, the model's interpretability decreased since main effects becoming insignificant when we add interactions. The recommendation for increasing interpretability of this model is to reduce correlated independent variables.

# MLmodellinear
ML model lienar

## Boston Housing Dataset
The Boston Housing Dataset contains information collected by the U.S Census Service concerning housing in the area of Boston, Massachusetts. It has 506 samples and 13 feature variables. The features include:
- CRIM: per capita crime rate by town
- ZN: proportion of residential land zoned for lots over 25,000 sq. ft.
- INDUS: proportion of non-retail business acres per town
- CHAS: Charles River dummy variable (1 if tract bounds river; 0 otherwise)
- NOX: nitric oxides concentration (parts per 10 million)
- RM: average number of rooms per dwelling
- AGE: proportion of owner-occupied units built prior to 1940
- DIS: weighted distances to five Boston employment centers
- RAD: index of accessibility to radial highways
- TAX: full-value property tax rate per $10,000
- PTRATIO: pupil-teacher ratio by town
- B: 1000(Bk - 0.63)^2 where Bk is the proportion of black people by town
- LSTAT: % lower status of the population

## Linear Regression Model
A linear regression model is used to predict the value of a target variable by fitting a linear relationship between the target variable and one or more predictor variables. In this case, we are using the Boston Housing Dataset to predict the median value of owner-occupied homes (in $1000s) using the 13 feature variables.

## Dependencies and Installation
To run the `boston_housing_linear_regression.py` script, you need the following dependencies:
- numpy
- pandas
- scikit-learn

You can install these dependencies using pip:
```
pip install numpy pandas scikit-learn
```

## Running the Script
To run the `boston_housing_linear_regression.py` script, use the following command:
```
python boston_housing_linear_regression.py
```

## Running the Streamlit App
To run the Streamlit app, you need to install Streamlit:
```
pip install streamlit
```

Then, use the following command to run the Streamlit app:
```
streamlit run app.py
```

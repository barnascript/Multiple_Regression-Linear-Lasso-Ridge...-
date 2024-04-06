In this machine learning regression project, I built NumPy Regression Models (Linear Regression, Ridge Regression, Lasso Regression) from Scratch.


I understood

Regression?
The applications of regression?
Different types of regression
Differentiation between regression and classification
loss function?
gradient descent?
Drawbacks of linear regression
bias and variance
ridge and lasso regression?
decision tree?
Understanding the different terminologies in the decision tree
Advantages and disadvantages of decision trees
Importing the dataset and required libraries.
Missing data handling using appropriate methods.
Finding a correlation between the features.
Building various regression models from scratch using the NumPy module
Gaining confidence in the model using metrics such as MSE, and R squared.


Regression is a supervised learning algorithm. Regression analysis is used to establish a relationship between one or more independent variables and a dependent variable. There are several variations in regression analysis like linear, multiple linear, and nonlinear. One can create regression models with the help of the ‘Scikit-learn’ library, the most valuable and robust library for machine learning in Python. But, in this project, we will be building our models from scratch using NumPy. Building your model allows for more flexibility during the training process, and one can tweak the model to make it more robust and responsive to real-world data as required in the future during re-training or in production.

This project explains how linear regression works and how to build various regression models such as linear regression, ridge regression, lasso regression, and decision tree from scratch using the NumPy module.

 

## Data Description 

The dataset provides information about the players of a particular sport, and the target is the predict the scores. The dataset consists of around 200 rows and 13 columns.

 

## Aim

To build multiple regression models from scratch using the NumPy module.

 

## Tech stack

Language - Python
Libraries - Pandas, NumPy
 

## Approach

Importing the required libraries and reading the dataset.
Data pre-processing
Removing the missing data points
Dropping categorical variables
Checking for multi-collinearity and removal of highly correlated features
Creating train and test data by randomly shuffling data
Performing train test split
Model building using NumPy
Linear Regression Model
Ridge Regression
Lasso Regressor
Decision Tree Regressor
Model Validation
Mean Absolute Error
R2 squared

# Regression Dataflow



## Datasets used

1. Auto-mpg data set



## Assumptions

I will assume we start with a datafile (ex. already have the .csv, .txt, .data, etc.) downloaded locally on our computer. From here our language will be able to perform machine learning tasks on these datasets.


## Considerations

We notice that there are some machine learning tasks that may deviate from the steps we may have generalized. These tasks may be implemented in the future as the ML-SQL develops.

- Missing data or NA's
- Hyperparameter tuning

## Steps to Process Data

1. Read in file
    - Different types of separators (',',' ', '\t', '\s', etc.)
    - Specify whether there is a header or not
    - Name different columns
    - Editting values to matchup with columns
    
1. Handle missing values (ex. ?, NA, etc.)
    - remove these examples?
    - set these values to an arbitrary value like 0 or NA
    - replace missing values with the mean

1. Select columns for the regression tasks
    - Select columns I want to use as predictors
    - Select which column am I using as a target (trying to predict)

1. Transform columns or variables
    - create new features from the features we already have (combinations, squaring, cubing, etc.)
    - PCA?
    - scaling?
    
1. Split data into training and testing sets
    - Set a percentage or value for a training or testing set sizes
    - Also create a validation set?
    - Crossvalidation instead?
    
1. Train model using the training data
    - include regularization? (hyperparameter tuning)
    - specify method/ algorithm (lasso, ridge, simple, SVM, etc.)

1. Perform diagnostics on the model
    - See coefficients
    - See metrics like mean squared error, residual sum of errors, r-squared, etc.

1. Test model on held out testing set
    - See metrics like mean squared error, residual sum of errors, etc.
    
1. Visualizations
    - Visualize dataset as a whole (scatter plot matrix)
    - See diagnostic plots (cooks distances, deviances, predicted vs. actual, etc.)
    - bias or variance issues? 
    
1. Repeat for a new model


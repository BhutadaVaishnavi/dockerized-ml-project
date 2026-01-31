Project Overview:

This project is a simple machine learning application built using the Titanic dataset from Kaggle.
The goal of the project is to predict whether a passenger survived or not based on basic details like age, gender, class, and fare.

The dataset is taken from the Kaggle Titanic: Machine Learning from Disaster competition.
I used the train.csv file for training the model.
The dataset contains passenger information such as class, gender, age, fare, and survival status.

I used Logistic Regression for this project because it is easy to understand and works well for binary classification problems.
The data was cleaned by removing missing values and converting text data into numeric form.
After training, the model is saved so it can be reused for predictions.

Docker is used to package the entire project including the Python code, required libraries, and the trained model.
This helps the project run the same way on any system without worrying about installation or version issues.
Anyone can run the project using Docker with a single command.

Project Workflow

Load the Titanic dataset
Clean and prepare the data
Train the machine learning model
Save the trained model
Run predictions using the saved model
Execute the complete workflow inside a Docker container

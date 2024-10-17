# Student Exam Performance Prediction

## Project Overview

The **Student Exam Performance Prediction** project is a machine learning application designed to predict a student's math score based on various input factors such as gender, race, parental education, lunch type, and scores in other subjects (writing and reading). The tool provides an estimate of the student's math score based on these factors.

## Features

- Predicts math score based on user input.
- Inputs include:
  - Gender
  - Race or Ethnicity
  - Parental Level of Education
  - Lunch Type
  - Test Preparation Course
  - Writing Score (out of 100)
  - Reading Score (out of 100)
- Displays the predicted math score on submission.

## How it Works

The model takes into account the demographic and academic factors to predict the math score. The trained model uses historical student performance data to provide a reasonable prediction based on the user's input.


To run this project locally, follow these steps:

### Prerequisites

- Python 3.12
- Flask (for serving the web app)
- Scikit-learn (for machine learning)
- Pandas and NumPy (for data manipulation)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/student-exam-performance-prediction.git

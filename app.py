# Importing necessary modules from Flask to create the web application
from flask import Flask, request, render_template

# Importing additional libraries
import numpy as np  # Used for handling numerical data (e.g., calculations)
import pandas as pd  # Used for managing and structuring data in tables

# Importing custom classes: CustomData and PredictPipeline from the custom module 'src.pipeline.predict_pipeline'
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

# Initializing a new Flask application instance
app = Flask(__name__)

# Defining the route for the homepage of the web application
@app.route('/')
def index():
    # This function loads and displays the 'home.html' file when users visit the homepage
    return render_template('home.html')

# Defining the route for the prediction page, allowing both GET and POST requests
@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    # If the user is just opening the page, show the home page
    if request.method == 'GET':
        return render_template('home.html')
    else:
        # When the user submits the form, we handle the input data here
        try:
            # Capture and organize the form data into a structure
            data = CustomData(
                gender=request.form.get('gender'),  # Fetches 'gender' data
                race_ethnicity=request.form.get('ethnicity'),  # Fetches 'ethnicity' data
                parental_level_of_education=request.form.get('parental_level_of_education'),  # Fetches parent's education level
                lunch=request.form.get('lunch'),  # Fetches 'lunch' data
                test_preparation_course=request.form.get('test_preparation_course'),  # Fetches 'test preparation' data
                reading_score=float(request.form.get('reading_score')),  # Ensures 'reading_score' is a number
                writing_score=float(request.form.get('writing_score'))  # Ensures 'writing_score' is a number
            )

            # Convert the collected form data into a pandas DataFrame, which the prediction pipeline can use
            pred_df = data.get_data_as_data_frame()
            print(f"Input DataFrame: \n{pred_df}")

            # Initialize the prediction pipeline (pre-trained model is loaded here)
            predict_pipeline = PredictPipeline()

            # Use the pipeline to predict based on the input data
            results = predict_pipeline.predict(pred_df)
            print(f"Prediction Result: {results}")

            # Display the prediction result on the same 'home.html' page
            return render_template('home.html', results=results[0])

        except Exception as e:
            # If there’s any error during prediction, print it for debugging
            print(f"Error during prediction: {e}")
            # Show an error message on the homepage if there's an issue
            return render_template('home.html', error="An error occurred during prediction. Please check your input.")

# Run the Flask web application
if __name__ == "__main__":
    # Run the app, accessible to any device in the network, and in 'debug' mode to assist in development
    app.run(host="0.0.0.0", debug=True)

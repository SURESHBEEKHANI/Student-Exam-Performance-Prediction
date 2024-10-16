# Importing necessary modules from Flask to create the web application
from flask import Flask, request, render_template

# Importing additional necessary libraries
import numpy as np  # For numerical operations
import pandas as pd  # For data manipulation and creating DataFrame objects

# Importing custom modules: CustomData and PredictPipeline from the 'src.pipeline.predict_pipeline' module
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

# Initializing the Flask application
app = Flask(__name__)

# Defining the route for the homepage of the web application
@app.route('/')
def index():
    # Rendering the 'index.html' template when the root URL is accessed
    return render_template('index.html')

# Defining the route for prediction, with both GET and POST methods allowed
@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    # If the request method is GET, render 'home.html'
    if request.method == 'GET':
        return render_template('home.html')
    else:
        try:
            # Capture the form data (ensure form field names match these keys)
            data = CustomData(
                gender=request.form.get('gender'),
                race_ethnicity=request.form.get('ethnicity'),
                parental_level_of_education=request.form.get('parental_level_of_education'),
                lunch=request.form.get('lunch'),
                test_preparation_course=request.form.get('test_preparation_course'),
                reading_score=float(request.form.get('reading_score')),  # Ensuring correct casting
                writing_score=float(request.form.get('writing_score'))   # Ensuring correct casting
            )

            # Convert the collected form data into a pandas DataFrame
            pred_df = data.get_data_as_data_frame()
            print(f"Input DataFrame: \n{pred_df}")

            # Initialize the prediction pipeline
            predict_pipeline = PredictPipeline()

            # Make the prediction
            results = predict_pipeline.predict(pred_df)
            print(f"Prediction Result: {results}")

            # Render 'home.html' and display the prediction result
            return render_template('home.html', results=results[0])

        except Exception as e:
            print(f"Error during prediction: {e}")
            # If any error occurs, render the home page with an error message
            return render_template('home.html', error="An error occurred during prediction. Please check your input.")

# Run the Flask app
if __name__ == "__main__":
    # Running the app on host 0.0.0.0 (accessible from any device in the network), debug mode ON for development
    app.run(host="0.0.0.0", debug=True)

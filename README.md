Tourism Data Analytics Report:

Submitted by: Manjula M
Batch: AI/ML
Date: 05-10-2025
GitHub Link: https://github.com/Manjula1989/Amazon-Delivery-Time-Prediction.git

Abstract
This project presents an Amazon Delivery Time Prediction System developed using Python and Streamlit to estimate delivery times for Amazon orders. The system integrates datasets containing agent details, order information, weather, traffic, and area characteristics to predict delivery durations. By applying data preprocessing, machine learning modeling, and interactive visualization through Streamlit, the project provides actionable insights for operational planning and customer satisfaction.

Introduction
Timely deliveries are crucial for customer satisfaction and logistics efficiency. Accurate prediction of delivery times helps companies optimize routes, manage resources, and improve service quality. This project uses historical Amazon order data to train a predictive model and provides an interactive Streamlit app to estimate delivery time based on order details.

Objectives
Preprocess and clean historical Amazon delivery data.
Train a machine learning model to predict delivery times.
Build an interactive Streamlit application for real-time predictions.
Summarize insights and provide a ready-to-use dashboard for operations.

Dataset Description
Order Data: Order ID, category, distance, and area details.
Agent Data: Agent age, rating, and experience.
External Factors: Weather conditions and traffic levels.
Delivery Data: Historical delivery times for supervised learning.

Methodology
Predictive Modeling: Used a regression model to predict delivery time based on order and agent features.
Data Cleaning: Removed duplicates and handled missing values; converted categorical features into numerical format.
Exploratory Data Analysis (EDA): Identified delivery time patterns across categories, areas, and traffic conditions using visualizations.
Visualization: Streamlit interface enables interactive user inputs and prediction visualization.

Streamlit Interface / Visuals
Input Form Example:
Parameter	Example Input
Agent Age	30
Agent Rating	4.5
Distance (km)	5.00
Weather	Sunny
Traffic	Low
Area	Semi-Urban
Category	Books

Predicted Output: Estimated Delivery Time: 102.55 minutes
Description: Users enter details such as agent age, rating, distance, weather, traffic, area, and category. The system predicts the estimated delivery time for each order.


Predicted Delivery Time: 


Instructions to Run
Install required libraries: pip install -r requirements.txt
Train the model (if needed) using training scripts.
Run batch predictions: python predict.py
Launch the Streamlit app: streamlit run main.py
Input order details to view estimated delivery time.

Personalized Insights / Sample Predictions
Parameter	Value
Agent Age	30
Rating	4.5
Distance	5 km
Weather	Sunny
Traffic	Low
Area	Semi-Urban
Category	Books

Predicted Delivery Time: 102.55 minutes

Key EDA Insights
Metric	Value
Average delivery time	120 minutes
Fastest delivery category	Books
Longest delivery category	Electronics
Total records analyzed	5000 rows

Conclusion
The Amazon Delivery Time Prediction Project demonstrates how Python and Streamlit can transform historical delivery data into actionable insights. Predictive modeling enables accurate estimation of delivery times, helping logistics teams enhance efficiency and customer satisfaction.

Future Work
Integrate real-time tracking and traffic data.
Add predictive analytics for route optimization.
Develop a recommendation system for scheduling and resource allocation.
Enhance the Streamlit interface for batch uploads and advanced visualization.

References:
Python Libraries:  https://pandas.pydata.org / https://matplotlib.org

Streamlit Documentation: https://docs.streamlit.io


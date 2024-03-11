

 
# Motor Vehicle Collisions in New York City Analysis Dashboard

![Title Image Placeholder](Crash.jpeg)

This dashboard application analyzes motor vehicle collisions data in New York City. It provides interactive visualizations and insights into various aspects of vehicle collisions, including geographical distribution, time trends, and street-level analysis of injuries. The application is built using Streamlit, a Python library for building interactive web applications for data science and machine learning projects.

## Project Overview

1. **Load the Motor Vehicle Collisions Data**: The application loads the Motor Vehicle Collisions dataset, which contains information about vehicle collisions in New York City.

2. **Visualize Data on a Map**: Users can visualize the geographical distribution of motor vehicle collisions on an interactive map.

3. **Filtering Data and Interactive Tables**: Users can filter the data based on criteria such as the number of injuries and view interactive tables of filtered data.

4. **Plot Filtered Data on a 3D Interactive Map**: The application plots filtered data on a 3D interactive map, allowing users to explore collisions in a spatial context.

5. **Charts and Histograms**: Users can view breakdowns of collisions by minute using charts and histograms, providing insights into time trends.

6. **Select Data Using Dropdowns**: Users can select specific types of people affected by collisions (e.g., pedestrians, cyclists, motorists) and view the top 5 dangerous streets for each category.

## Running the Application

To run the application locally, execute the following command:

```bash
streamlit run app.py
```

## Project Structure

- `app.py`: The main Python script containing the Streamlit application code.
- `Motor_Vehicle_Collisions_-_Crashes.csv`: The dataset used for analysis.
- `Crash.jpeg`: Image file used as the title image in the dashboard.

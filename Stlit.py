import streamlit as st
import plotly.express as px
import pandas as pd

# --- Title and Introduction ---
st.title("Interactive Visualizations with Plotly and Streamlit")

# --- Input for Author Information ---
st.sidebar.header("Visualization skill workshop - Plotly")
name = st.sidebar.text_input("Shreyas Kamath D")
usn = st.sidebar.text_input("38")
instructor_name = st.sidebar.text_input("Ashwini Kumar")

# Display author information if provided
if name and usn and instructor_name:
    st.markdown(
        f"<h5 style='color: teal;'>Created by:</h5>"
        f"<p style='color: white;'>{name} (USN: {usn})</p>"
        f"<p style='color: white;'>Instructor: {instructor_name}</p>",
        unsafe_allow_html=True
    )

# --- Load Dataset ---
# Instead of seaborn, we load the 'tips' dataset directly from Plotly
dataset = px.data.tips()  # Using Plotly's inbuilt dataset

# Display the first few rows of the dataset
st.write("## Dataset Overview")
st.write(dataset.head())  # Displaying the first 5 rows of the dataset

# --- Task 2: Interactive Bar Chart ---
st.subheader("Task 2: Bar Chart - Average Tip by Day")
# Bar Chart: Average Tip by Day with color for each day
fig2 = px.bar(
    dataset, x='day', y='tip', color='day',
    title='Average Tip by Day',
    labels={'tip': 'Average Tip ($)', 'day': 'Day of the Week'},
    template='plotly_white'
)
st.plotly_chart(fig2)  # Display the chart in Streamlit

# --- Task 3: Histogram - Tip Distribution (Colored by Gender) ---
st.subheader("Task 3: Tip Distribution (Colored by Gender)")
fig6 = px.histogram(
    dataset, x='tip', color='sex',
    title='Distribution of Tips (Colored by Gender)', 
    labels={'tip': 'Tip ($)', 'sex': 'Gender'},
    template='plotly_white',
)
st.plotly_chart(fig6)

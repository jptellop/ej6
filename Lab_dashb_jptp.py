#import streamlit as st
import pandas as pd
import numpy as np
#!pip install streamlit
import streamlit as st
# Sample Data
data = {
    'Order ID': range(1, 21),
    'Product': ['Laptop', 'Phone', 'Tablet', 'Monitor', 'Headphones'] * 4,
    'Category': ['Electronics', 'Electronics', 'Electronics', 'Accessories', 'Accessories'] * 4,
    'Price': np.random.randint(50, 1000, 20),
    'Quantity': np.random.randint(1, 5, 20)
}
df = pd.DataFrame(data)
df['Total'] = df['Price'] * df['Quantity']

# Sidebar Filter
st.sidebar.header("Filters")
category_filter = st.sidebar.selectbox("Select Category", ['All'] + list(df['Category'].unique()))
if category_filter != 'All':
    df = df[df['Category'] == category_filter]

# KPIs
st.title("E-commerce Sales Dashboard")
st.metric("Total Revenue", f"${df['Total'].sum():,.2f}")
st.metric("Total Orders", len(df))

# Data Table
st.subheader("Sales Data")
st.dataframe(df)

# Chart
st.subheader("Sales by Category")
category_sales = df.groupby('Category')['Total'].sum().reset_index()
st.bar_chart(category_sales.set_index('Category'))

####
data = {
    'Employee': [f'Employee {i}' for i in range(1, 21)],
    'Department': ['HR', 'IT', 'Marketing', 'Finance'] * 5,
    'Hours Worked': np.random.randint(30, 50, 20),
    'Tasks Completed': np.random.randint(5, 20, 20)
}
df = pd.DataFrame(data)

# Sidebar Filter
st.sidebar.header("Filters")
department_filter = st.sidebar.selectbox("Select Department", ['All'] + list(df['Department'].unique()))
if department_filter != 'All':
    df = df[df['Department'] == department_filter]

# KPIs
st.title("Employee Productivity Tracker")
st.metric("Average Hours Worked", f"{df['Hours Worked'].mean():.1f} hrs")
st.metric("Total Tasks Completed", df['Tasks Completed'].sum())

# Data Table
st.subheader("Employee Data")
st.dataframe(df)

# Chart
st.subheader("Hours Worked Distribution")
st.line_chart(df[['Employee', 'Hours Worked']].set_index('Employee'))


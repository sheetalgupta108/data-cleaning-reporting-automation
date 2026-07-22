import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Dashboard Title
st.title("Data Cleaning & Reporting Automation Dashboard")

# Upload CSV File
uploaded_file = st.file_uploader(
    "Upload Your CSV File",
    type=["csv"]
)

if uploaded_file is not None:

    # Read CSV File
    df = pd.read_csv(uploaded_file)

    # Show Original Dataset
    st.subheader("Original Dataset")
    st.dataframe(df)

    # Missing Values Count
    missing_values = df.isnull().sum().sum()

    # Duplicate Values Count
    duplicate_values = df.duplicated().sum()

    # Data Cleaning
    df = df.dropna()
    df = df.drop_duplicates()

    # Show Cleaned Dataset
    st.subheader("Cleaned Dataset")
    st.dataframe(df)

    # Report Section
    st.subheader("Automated Data Cleaning Report")

    st.write(
        f"Total Missing Values Removed: {missing_values}"
    )

    st.write(
        f"Total Duplicate Rows Removed: {duplicate_values}"
    )

    st.write(
        f"Total Rows After Cleaning: {len(df)}"
    )

    # Dataset Information
    st.subheader("Dataset Summary")

    st.write(df.describe())

    # Visualization Section
    st.subheader("Visual Summary")

    numeric_columns = df.select_dtypes(
        include=["int64", "float64"]
    ).columns

    if len(numeric_columns) > 0:

        selected_column = st.selectbox(
            "Select a Numeric Column",
            numeric_columns
        )

        fig, ax = plt.subplots()

        ax.hist(df[selected_column])

        ax.set_xlabel(selected_column)
        ax.set_ylabel("Frequency")
        ax.set_title(
            f"{selected_column} Distribution"
        )

        st.pyplot(fig)

    else:
        st.warning(
            "No numeric columns available for visualization."
        )
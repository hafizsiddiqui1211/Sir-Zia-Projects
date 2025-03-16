# Imports
import streamlit as st
import pandas as pd
import os
from io import BytesIO

# Setup our App
st.set_page_config(page_title="📀 Data Sweeper", layout="wide")
st.title("📀 Data Sweeper by Hafiz Siddiqui")
st.write("Transform your files between CSV and Excel formats with built-in data cleaning and visualization!")

uploaded_files = st.file_uploader("Upload your files (CSV or Excel):", type=[
                                  "csv", "xlsx"], accept_multiple_files=True)

if uploaded_files:
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[-1].lower()
        if file_ext == ".csv":
            df = pd.read_csv(file)
        elif file_ext == ".xlsx":
            df = pd.read_excel(file)
        else:
            st.error(f"Unsupported file format. Please upload :{file_ext}.")
            continue

        # Display info about the file
        st.write(f"File Name: {file.name}")
        st.write(f"File Size: {file.size/1024}")

        # Display the first 5 rows of the data frame
        st.write("🔎 Preview the Head of the Dataframe")
        st.dataframe(df.head())

        # Options for Data Cleaning
        st.subheader("🛠 Options for Data Cleaning")
        if st.checkbox(f"Clean Data for {file.name}"):
            col1, col2 = st.columns(2)

            with col1:
                if st.button(f"Remove Duplicates from {file.name}"):
                    df.drop_duplicates(inplace=True)
                    st.success("🎉 Duplicates removed successfully.")

            with col2:
                if st.button(f"Fill Missing Values in {file.name}"):
                    numeric_cols = df.select_dtypes(
                        include=["number"]).columns
                    df[numeric_cols] = df[numeric_cols].fillna(
                        df[numeric_cols].mean())
                    st.success("🎉 Missing values filled with successfully.")

        # Choose Specific Columns to Keep or Convert
        st.subheader("🎯 Select columns to convert")
        columns = st.multiselect(
            f"Choose columns for {file.name}", df.columns, default=df.columns)
        df = df[columns]

        # Options for Data Visualization
        st.subheader("📊 Data Visualization")
        if st.checkbox(f"Show Visualization for {file.name}"):
            st.bar_chart(df.select_dtypes(include="number").iloc[:, :2])

        # Convert the file -> CSV to EXCEL
        st.subheader("🔁 Conversion Options")
        conversion_type = st.radio(f"Convert {file.name} to:", [
                                   "CSV", "EXCEL"], key=file.name)
        if st.button(f"Convert {file.name}"):
            buffer = BytesIO()
            if conversion_type == "CSV":
                df.to_csv(buffer, index=False)
                file_name = file.name.replace(file_ext, ".csv")
                mime_type = "text/csv"
            elif conversion_type == "EXCEL":
                df.to_excel(buffer, index=False)
                file_name = file.name.replace(file_ext, ".xlsx")
                mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            buffer.seek(0)

            # Download Button
            st.download_button(
                label=f"⏬ Download {file_name} as {conversion_type}", data=buffer, file_name=file_name, mime=mime_type)
    st.success("🎉 All Files Processed!")

st.sidebar.header("Contact Us")
st.sidebar.info("Data Sweeper by Hafiz Siddiqui")
st.sidebar.info("Version: 1.0.0")
st.sidebar.info("Contact: 📞0302-9775253")
st.sidebar.info("Email: 📧wildansiddiqui8@gmail.com")
st.sidebar.info(
    "Linkedin: https://www.linkedin.com/in/hafiz-siddiqui-018587295/")

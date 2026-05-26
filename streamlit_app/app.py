import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Chunks Maker",
    layout="centered"
)

st.title("Chunks Maker")

st.write(
    "Upload CSV or Excel files and split them into chunks."
)

uploaded_file = st.file_uploader(
    "Upload CSV or Excel File",
    type=["csv", "xlsx", "xls"]
)

if uploaded_file is not None:

    st.success(
        f"Uploaded: {uploaded_file.name}"
    )

    file_extension = (
        uploaded_file.name
        .split(".")[-1]
        .lower()
    )

    if file_extension == "csv":

        df = pd.read_csv(uploaded_file)

    else:

        df = pd.read_excel(uploaded_file)

    total_rows = len(df)

    st.write(
        f"Total Rows Found: {total_rows}"
    )

    st.dataframe(df.head())
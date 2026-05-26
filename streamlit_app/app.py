import streamlit as st

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
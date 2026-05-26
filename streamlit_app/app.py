import streamlit as st
import pandas as pd
import math
import os
import zipfile

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

    chunk_size = st.number_input(
        "Enter number of rows per chunk",
        min_value=1,
        step=1
    )

    if chunk_size:

        total_chunks = math.ceil(
            total_rows / chunk_size
        )

        st.write(
            f"Total Chunks To Be Created: "
            f"{total_chunks}"
        )

        if st.button("Create Chunks"):

            base_name = os.path.splitext(
                uploaded_file.name
            )[0]

            output_folder = (
                f"{base_name}_chunks"
            )

            os.makedirs(
                output_folder,
                exist_ok=True
            )

            created_files = []

            for chunk_number in range(total_chunks):

                start_idx = (
                    chunk_number * chunk_size
                )

                end_idx = (
                    start_idx + chunk_size
                )

                chunk_df = df.iloc[
                    start_idx:end_idx
                ]

                output_file = os.path.join(
                    output_folder,
                    f"{base_name}_chunk"
                    f"{chunk_number + 1}.xlsx"
                )

                chunk_df.to_excel(
                    output_file,
                    index=False
                )

                created_files.append(
                    output_file
                )

            zip_file_name = (
                f"{base_name}_chunks.zip"
            )

            with zipfile.ZipFile(
                zip_file_name,
                "w"
            ) as zipf:

                for file in created_files:

                    zipf.write(file)

            st.success(
                "ZIP file created successfully!"
            )

            with open(
                zip_file_name,
                "rb"
            ) as file:

                st.download_button(
                    label="Download ZIP File",
                    data=file,
                    file_name=zip_file_name,
                    mime="application/zip"
                )
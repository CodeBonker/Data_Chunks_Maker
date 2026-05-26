import streamlit as st
import pandas as pd
import math
import os
import zipfile

st.set_page_config(
    page_title="Chunks Maker",
    layout="wide"
)

st.title("Chunks Maker")

st.write(
    "Upload your data files and split them into smaller chunks."
)

uploaded_file = st.file_uploader(
    "Upload CSV or Excel File",
    type=["csv", "xlsx", "xls"]
)

if uploaded_file is not None:

    file_extension = (
        uploaded_file.name
        .split(".")[-1]
        .lower()
    )

    with st.spinner("Reading file..."):

        if file_extension == "csv":

            df = pd.read_csv(uploaded_file)

        else:

            df = pd.read_excel(uploaded_file)

    st.success(
        f"Uploaded: {uploaded_file.name}"
    )

    total_rows = len(df)

    with st.sidebar:

        st.header("Chunk Settings")

        chunk_size = st.number_input(
            "Rows Per Chunk",
            min_value=1,
            step=1
        )

        naming_mode = st.radio(
            "Naming Mode",
            [
                "Automatic Name",
                "Custom Name"
            ]
        )

        download_mode = st.radio(
            "Download Type",
            [
                "ZIP File",
                "Excel Files",
                "CSV Files"
            ]
        )

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Total Rows",
            total_rows
        )

    if chunk_size:

        total_chunks = math.ceil(
            total_rows / chunk_size
        )

    else:

        total_chunks = 0

    with col2:

        st.metric(
            "Total Chunks",
            total_chunks
        )

    st.subheader("Data Preview")

    st.dataframe(
        df.head(),
        use_container_width=True
    )

    original_base_name = os.path.splitext(
        uploaded_file.name
    )[0]

    if naming_mode == "Automatic Name":

        base_name = original_base_name

    else:

        base_name = st.text_input(
            "Enter Custom Base Name"
        )

    if st.button(
        "Create Chunks",
        use_container_width=True
    ):

        if base_name == "":

            st.error(
                "Custom name cannot be empty"
            )

        else:

            output_folder = (
                f"{base_name}_chunks"
            )

            os.makedirs(
                output_folder,
                exist_ok=True
            )

            created_files = []

            progress_bar = st.progress(0)

            status_text = st.empty()

            for chunk_number in range(total_chunks):

                status_text.write(
                    f"Creating Chunk "
                    f"{chunk_number + 1} "
                    f"of {total_chunks}"
                )

                start_idx = (
                    chunk_number * chunk_size
                )

                end_idx = (
                    start_idx + chunk_size
                )

                chunk_df = df.iloc[
                    start_idx:end_idx
                ]

                if any(
                    char.isdigit()
                    for char in base_name
                ):

                    file_base = (
                        f"{base_name}_"
                        f"{chunk_number + 1}"
                    )

                else:

                    file_base = (
                        f"{base_name}_chunk"
                        f"{chunk_number + 1}"
                    )

                if download_mode == "CSV Files":

                    output_file = os.path.join(
                        output_folder,
                        f"{file_base}.csv"
                    )

                    chunk_df.to_csv(
                        output_file,
                        index=False
                    )

                else:

                    output_file = os.path.join(
                        output_folder,
                        f"{file_base}.xlsx"
                    )

                    chunk_df.to_excel(
                        output_file,
                        index=False
                    )

                created_files.append(output_file)

                progress_bar.progress(
                    (chunk_number + 1)
                    / total_chunks
                )

            status_text.empty()

            if download_mode == "ZIP File":

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
                        mime="application/zip",
                        use_container_width=True
                    )

            else:

                st.success(
                    "Chunk files created successfully!"
                )

                for file_path in created_files:

                    with open(file_path, "rb") as file:

                        st.download_button(
                            label=os.path.basename(file_path),
                            data=file,
                            file_name=os.path.basename(file_path),
                            use_container_width=True
                        )
# Data Chunks Maker

Data Chunks Maker is a Streamlit-based utility that helps users split large CSV and Excel datasets into smaller manageable chunks.

The project can be used in:
- Google Colab
- VS Code
- Streamlit Web UI

---

## Features

- CSV, XLSX and XLS support
- Split files into custom chunk sizes
- Download all chunks as ZIP
- Download chunks as Excel files
- Download chunks as CSV files
- Batch downloads for large outputs
- Automatic naming mode
- Custom naming mode
- Estimated output size preview
- Interactive Streamlit UI
- Google Colab compatible
- VS Code compatible

---

## Tech Stack

- Python
- Streamlit
- Pandas
- OpenPyXL

---

## Project Structure

```text
Data_Chunks_Maker/
│
├── Notebook/
│   └── Data_chunk_maker.ipynb
│
├── streamlit_app/
│   └── app.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/CodeBonker/Data_Chunks_Maker.git
```

Go to the project directory

```bash
cd Data_Chunks_Maker
```

Create virtual environment

```bash
python -m venv .venv
```

Activate virtual environment

Mac/Linux

```bash
source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit app

```bash
streamlit run streamlit_app/app.py
```

---

## Running In Google Colab

Open the notebook file:

```text
Notebook/Data_chunk_maker.ipynb
```

Upload CSV or Excel file and run all notebook cells.

---

## Running In VS Code

Open the project folder in VS Code.

Run:

```bash
streamlit run streamlit_app/app.py
```

Or run the notebook directly using the Jupyter extension.

---

## Usage

1. Upload CSV or Excel file
2. Select rows per chunk
3. Choose naming mode
4. Select download type
5. Click Create Chunks
6. Download generated files

---

## Download Modes

| Mode | Description |
|------|-------------|
| Download All (ZIP) | Downloads all chunk files together |
| Excel Files | Generates Excel chunk files |
| CSV Files | Generates CSV chunk files |

---

## Batch Download System

- Files are grouped into batches of 10
- Each batch can be downloaded together
- Individual file downloads are also available

---

## Current Capabilities

- Handles large datasets
- Maintains original data integrity
- Supports automatic chunk naming
- Supports custom naming
- Displays estimated output size
- Supports batch ZIP downloads

---

## Deployment

Recommended deployment platform:

- Streamlit Cloud

---

## Author

Shikhar Navdeep
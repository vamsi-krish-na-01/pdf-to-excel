import streamlit as st
import pdfplumber
import pandas as pd

st.title("vamsi pdf to excel converter")

pdf_file = st.file_uploader("Upload PDF", type="pdf")

if pdf_file is not None:
    data = []
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            table = page.extract_table()
            if table:
                data.extend(table)

    if data:
        df = pd.DataFrame(data)
        st.write(df)
        excel_file = "output.xlsx"
        df.to_excel(excel_file, index=False)
        with open(excel_file, "rb") as f:
            st.download_button("Download Excel", f, file_name="converted.xlsx")
    else:
        st.warning("No tables found in the PDF")

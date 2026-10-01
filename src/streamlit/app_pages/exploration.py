from pathlib import Path
import pandas as pd
import streamlit as st

from ziko_st_toc import table_of_contents

st.title("Data Exploration")

with st.sidebar:
    table_of_contents()

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "train.csv"

df = pd.read_csv(DATA_PATH)

st.write("### Presentation of data")
st.dataframe(df.head(10))

if st.checkbox("Show missing values"):
    st.dataframe(df.isna().sum())

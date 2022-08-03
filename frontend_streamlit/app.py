import streamlit as st
import requests
import pandas as pd

def main():
    st.title("Data from Backend")

    r = requests.get("http://0.0.0.0:5001/data")
    data = r.json()
    #st.json(data)

    df = pd.DataFrame.from_dict(data, orient='index')
    st.table(df)

if __name__ == "__main__":
    main()
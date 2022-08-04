import streamlit as st
import requests
import pandas as pd

def main():
    st.title("Data from Backend")

    #IP = "0.0.0.0"
    IP = "flask_base"
    r = requests.get(f"http://{IP}:5000/data")
    data = r.json()
    st.json(data)

    df = pd.DataFrame.from_dict(data, orient='index')
    st.table(df)

if __name__ == "__main__":
    main()
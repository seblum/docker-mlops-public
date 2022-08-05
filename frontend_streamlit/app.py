import streamlit as st
import requests
import pandas as pd
import os 

def main():

    PORT = os.environ.get("PORT")
    DB_SERVICE = os.environ.get("DB_SERVICE")

    st.title("Data from Backend")

    #DB_SERVICE = "flask_base"
    #PORT = "5000"
    r = requests.get(f"http://{DB_SERVICE}:{PORT}/data")
    data = r.json()
    st.json(data)

    df = pd.DataFrame.from_dict(data, orient='index')
    st.table(df)

if __name__ == "__main__":
    main()
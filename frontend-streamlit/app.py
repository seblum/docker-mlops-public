from time import sleep
import streamlit as st
import requests
import pandas as pd
import os 
import sys

def main():

    DB_SERVICE = os.environ.get("DB_SERVICE")
    KILL_IN_SECONDS = os.environ.get("KILL_IN_SECONDS")

    with st.sidebar:
        st.subheader("Environment variables")
        st.text(f"DB_SERVICE: {DB_SERVICE}")
        st.text(f"KILL_IN_SECONDS: {KILL_IN_SECONDS}")

    st.title("Frontend Deployment")
    #DB_SERVICE = "flask_base"
    #PORT = "5000"
    if DB_SERVICE is not None:
        r = requests.get(f"http://{DB_SERVICE}/data")
        data = r.json()
        st.subheader("Data from Backend")
        st.json(data)

        df = pd.DataFrame.from_dict(data, orient='index')
        st.table(df)

    if KILL_IN_SECONDS is not None:
        st.subheader("Kill in seconds")
        st.text(f"exit process in {KILL_IN_SECONDS}")

        KILL_IN_SECONDS = int(KILL_IN_SECONDS)
        my_bar = st.progress(0)

        step_size = KILL_IN_SECONDS/100
        my_bar.progress(1)
        for percent_complete in range(100):
            sleep(step_size)
            my_bar.progress(percent_complete + 1)
        st.warning("Streamlit App killed")
        sleep(1)
        # streamlit catches sys.exit()
        os._exit(1)

if __name__ == "__main__":
    main()
import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="Crime Query System", layout="centered")

st.title("🔎 Crime Data Query")
st.write("Query crime statistics from the distributed dataset using Apache Spark.")

# Input form
with st.form("query_form"):
    city = st.text_input("Enter City: ")
    crime_code = st.text_input("Enter Crime Code: ")
    crime_type = st.text_input("Enter Crime Type:  ", help="Example: Theft, Robbery")

    submitted = st.form_submit_button("Submit")

if submitted:
    with st.spinner("Fetching results..."):
        try:
            params = {}
            if city:
                params["city"] = city
            if crime_code:
                params["crime_code"] = crime_code   
            if crime_type:
                params["crime_type"] = crime_type   

            response = requests.get("http://localhost:5001/query", params=params)
            result = response.json()

            if result["status"] == "success":
                records = pd.read_json(result["data"])
                if not records.empty:
                    st.success("✅ Results:")
                    st.dataframe(records)
                else:
                    st.warning("No matching records found.")
            else:
                st.error(f"❌ Error: {result['message']}")

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

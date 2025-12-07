import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="COVID Dashboard", layout="wide")

st.title("🦠 COVID-19 Data Visualization Dashboard")

# Load COVID dataset
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/datasets/covid-19/main/data/countries-aggregated.csv"
    df = pd.read_csv(url)
    df["Date"] = pd.to_datetime(df["Date"])
    return df

df = load_data()

# Sidebar
st.sidebar.header("Filters")

# Country dropdown
countries = df["Country"].unique()
selected_country = st.sidebar.selectbox("Select a Country", sorted(countries))

# Filter data
filtered_df = df[df["Country"] == selected_country]

# Display basic stats
st.subheader(f"📌 COVID Stats for {selected_country}")

col1, col2, col3 = st.columns(3)
col1.metric("Confirmed", int(filtered_df["Confirmed"].max()))
col2.metric("Recovered", int(filtered_df["Recovered"].max()))
col3.metric("Deaths", int(filtered_df["Deaths"].max()))

# Line chart
fig = px.line(
    filtered_df,
    x="Date",
    y=["Confirmed", "Recovered", "Deaths"],
    title=f"COVID Trend Over Time - {selected_country}",
    labels={"value": "Count", "variable": "Category"},
)

st.plotly_chart(fig, use_container_width=True)


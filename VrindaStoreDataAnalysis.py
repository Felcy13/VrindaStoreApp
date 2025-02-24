import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet

st.title("VrindaStoreSalesApp")
st.write("This app analyzes and forecasts sales trends for Vrinda Store.")

df = pd.read_csv("Vrinda Store Data.csv") 

df["Date"] = pd.to_datetime(df["Date"])
df["Year-Month"] = df["Date"].dt.to_period("M")

df_forecast = df.groupby("Year-Month")["Qty"].sum().reset_index()
df_forecast["ds"] = pd.to_datetime(df_forecast["Year-Month"].astype(str))
df_forecast.rename(columns={"Qty": "y"}, inplace=True)

model = Prophet()
model.fit(df_forecast)

future = model.make_future_dataframe(periods=36, freq="M")
forecast = model.predict(future)

st.subheader("📈 Forecasted Sales")
fig, ax = plt.subplots()
ax.plot(forecast["ds"], forecast["yhat"], label="Forecast", color="blue")
ax.fill_between(forecast["ds"], forecast["yhat_lower"], forecast["yhat_upper"], alpha=0.2)
ax.set_xlabel("Date")
ax.set_ylabel("Quantity Sold")
ax.legend()
st.pyplot(fig)
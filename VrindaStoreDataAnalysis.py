import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_squared_error

def load_data():
    return pd.read_csv("Vrinda Store Data.csv")

df = load_data()
df['Date'] = pd.to_datetime(df['Date'])
df.columns = df.columns.str.strip()  # Remove spaces in column names

st.sidebar.header("🔍 Filter Options")
view_option = st.sidebar.radio("View Forecast By:", ["Channel", "Category"])
selected_option = st.sidebar.selectbox(
    f"Select {view_option}:", 
    ["All"] + sorted(df[view_option].unique())
)

filtered_df = df.copy()
if selected_option != "All":
    filtered_df = df[df[view_option] == selected_option]

filtered_df['Year-Month'] = filtered_df['Date'].dt.to_period('M')
monthly_sales = filtered_df.groupby('Year-Month')['Amount'].sum().reset_index()
monthly_sales['Year-Month'] = monthly_sales['Year-Month'].astype(str)
monthly_sales.rename(columns={'Year-Month': 'ds', 'Amount': 'y'}, inplace=True)
monthly_sales['ds'] = pd.to_datetime(monthly_sales['ds'])

train_size = int(len(monthly_sales) * 0.8)
train = monthly_sales[:train_size]
test = monthly_sales[train_size:]

model_sarima = SARIMAX(train['y'], order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))
sarima_fit = model_sarima.fit()

future_periods = 24
forecast_sarima = sarima_fit.get_forecast(steps=future_periods)
forecast_index = pd.date_range(start=test['ds'].max(), periods=future_periods, freq='M')
forecast_values = forecast_sarima.predicted_mean
conf_int = forecast_sarima.conf_int()

forecast_future = pd.DataFrame({
    'ds': forecast_index,
    'yhat': forecast_values.values,
    'yhat_lower': conf_int.iloc[:, 0].values,
    'yhat_upper': conf_int.iloc[:, 1].values
})

test_forecast = sarima_fit.get_forecast(steps=len(test))
rmse = np.sqrt(mean_squared_error(test['y'], test_forecast.predicted_mean))
mape = np.mean(np.abs((test['y'] - test_forecast.predicted_mean) / test['y'])) * 100

st.title("Inventory Sales Forecasting")
st.write(f"### Sales Forecast for **{selected_option if selected_option != 'All' else 'All Data'}**")

st.write(f"**RMSE:** {rmse:.2f}")
st.write(f"**MAPE:** {mape:.2f}%")

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(monthly_sales['ds'], monthly_sales['y'], label="Actual Sales", color='blue')
ax.plot(forecast_future['ds'], forecast_future['yhat'], label="Forecasted Sales", linestyle="dashed", color='red')
ax.fill_between(forecast_future['ds'], forecast_future['yhat_lower'], forecast_future['yhat_upper'], color='gray', alpha=0.3)
ax.set_xlabel("Date")
ax.set_ylabel("Sales Amount")
ax.set_title(f"Sales Forecast for {selected_option} ({view_option})")
ax.legend()
st.pyplot(fig)

st.subheader("Forecast Data")
st.write(forecast_future)

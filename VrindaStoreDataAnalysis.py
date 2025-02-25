import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import base64
import os
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_squared_error



def load_data():
    file_path = "Vrinda Store Data.csv"
    if not os.path.exists(file_path):
        st.error("Error: 'Vrinda Store Data.csv' not found. Please upload the file.")
        return None
    return pd.read_csv(file_path)


df = load_data()
if df is not None:
    df['Date'] = pd.to_datetime(df['Date'])
    df.columns = df.columns.str.strip()  # Remove spaces in column names


    page_bg_img = '''
    <style>
    .stApp {
        background-image: url("https://source.unsplash.com/1600x900/?warehouse,inventory");
        background-size: cover;
    }
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)


    st.title("Vrinda Sales Analysis - Inventory for Channels and Categories")
    st.write("#### By **Felcy Fernandes, Imperial Business School London**")
    st.write("""
    This dashboard helps **Vrinda Store** analyze its **sales inventory across different channels and categories**.  
    Using **SARIMA forecasting**, it predicts future sales trends, helping in **better stock management**.
    """)

 
    st.sidebar.header("Filter Options")
    view_option = st.sidebar.radio("View Forecast By:", ["Channel", "Category"])
    
    if view_option not in df.columns:
        st.error(f"Error: Column '{view_option}' not found in dataset.")
    else:
        selected_option = st.sidebar.selectbox(
            f"Select {view_option}:", 
            ["All"] + sorted(df[view_option].dropna().unique())
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

       
        try:
            model_sarima = SARIMAX(train['y'], order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))
            sarima_fit = model_sarima.fit(disp=False)
        except Exception as e:
            st.error(f"Error in SARIMAX model: {e}")
            sarima_fit = None

        if sarima_fit:
            # Forecasting
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

        
            st.subheader(f"Sales Forecast for {selected_option if selected_option != 'All' else 'All Data'}")
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

            st.success("This inventory forecasting tool helps **reduce stock shortages and improve planning!**") 

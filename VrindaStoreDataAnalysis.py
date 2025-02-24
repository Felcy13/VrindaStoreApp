{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "0902fced-55dc-44dc-93b2-1c0962b87b81",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: streamlit in c:\\users\\felcy\\pictures\\new folder\\new folder\\lib\\site-packages (1.32.0)\n",
      "Requirement already satisfied: altair<6,>=4.0 in c:\\users\\felcy\\pictures\\new folder\\new folder\\lib\\site-packages (from streamlit) (5.0.1)\n",
      "Requirement already satisfied: blinker<2,>=1.0.0 in c:\\users\\felcy\\pictures\\new folder\\new folder\\lib\\site-packages (from streamlit) (1.6.2)\n",
      "Requirement already satisfied: cachetools<6,>=4.0 in c:\\users\\felcy\\pictures\\new folder\\new folder\\lib\\site-packages (from streamlit) (5.3.3)\n",
      "Requirement already satisfied: click<9,>=7.0 in c:\\users\\felcy\\pictures\\new folder\\new folder\\lib\\site-packages (from streamlit) (8.1.7)\n",
      "Requirement already satisfied: numpy<2,>=1.19.3 in c:\\users\\felcy\\pictures\\new folder\\new folder\\lib\\site-packages (from streamlit) (1.26.0)\n",
      "Collecting packaging<24,>=16.8 (from streamlit)\n",
      "  Downloading packaging-23.2-py3-none-any.whl.metadata (3.2 kB)\n",
      "Requirement already satisfied: pandas<3,>=1.3.0 in c:\\users\\felcy\\pictures\\new folder\\new folder\\lib\\site-packages (from streamlit) (2.2.2)\n",
      "Requirement already satisfied: pillow<11,>=7.1.0 in c:\\users\\felcy\\pictures\\new folder\\new folder\\lib\\site-packages (from streamlit) (10.3.0)\n",
      "Requirement already satisfied: protobuf<5,>=3.20 in c:\\users\\felcy\\pictures\\new folder\\new folder\\lib\\site-packages (from streamlit) (3.20.3)\n",
      "Requirement already satisfied: pyarrow>=7.0 in c:\\users\\felcy\\pictures\\new folder\\new folder\\lib\\site-packages (from streamlit) (14.0.2)\n",
      "Requirement already satisfied: requests<3,>=2.27 in c:\\users\\felcy\\pictures\\new folder\\new folder\\lib\\site-packages (from streamlit) (2.32.2)\n",
      "Requirement already satisfied: rich<14,>=10.14.0 in c:\\users\\felcy\\pictures\\new folder\\new folder\\lib\\site-packages (from streamlit) (13.3.5)\n",
      "Requirement already satisfied: tenacity<9,>=8.1.0 in c:\\users\\felcy\\pictures\\new folder\\new folder\\lib\\site-packages (from streamlit) (8.2.2)\n",
      "Requirement already satisfied: toml<2,>=0.10.1 in c:\\users\\felcy\\pictures\\new folder\\new folder\\lib\\site-packages (from streamlit) (0.10.2)\n",
      "Requirement already satisfied: typing-extensions<5,>=4.3.0 in c:\\users\\felcy\\pictures\\new folder\\new folder\\lib\\site-packages (from streamlit) (4.11.0)\n",
      "Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in c:\\users\\felcy\\pictures\\new folder\\new folder\\lib\\site-packages (from streamlit) (3.1.37)\n",
      "Requirement already satisfied: pydeck<1,>=0.8.0b4 in c:\\users\\felcy\\pictures\\new folder\\new folder\\lib\\site-packages (from streamlit) (0.8.0)\n",
      "Requirement already satisfied: tornado<7,>=6.0.3 in c:\\users\\felcy\\appdata\\roaming\\python\\python312\\site-packages (from streamlit) (6.4.1)\n",
      "Requirement already satisfied: watchdog>=2.1.5 in c:\\users\\felcy\\pictures\\new folder\\new folder\\lib\\site-packages (from streamlit) (4.0.1)\n",
      "Requirement already satisfied: jinja2 in c:\\users\\felcy\\pictures\\new folder\\new folder\\lib\\site-packages (from altair<6,>=4.0->streamlit) (3.1.4)\n",
      "Requirement already satisfied: jsonschema>=3.0 in c:\\users\\felcy\\pictures\\new folder\\new folder\\lib\\site-packages (from altair<6,>=4.0->streamlit) (4.19.2)\n",
      "Requirement already satisfied: toolz in c:\\users\\felcy\\pictures\\new folder\\new folder\\lib\\site-packages (from altair<6,>=4.0->streamlit) (0.12.0)\n",
      "Requirement already satisfied: colorama in c:\\users\\felcy\\appdata\\roaming\\python\\python312\\site-packages (from click<9,>=7.0->streamlit) (0.4.6)\n",
      "Requirement already satisfied: gitdb<5,>=4.0.1 in c:\\users\\felcy\\pictures\\new folder\\new folder\\lib\\site-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.7)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in c:\\users\\felcy\\appdata\\roaming\\python\\python312\\site-packages (from pandas<3,>=1.3.0->streamlit) (2.9.0.post0)\n",
      "Requirement already satisfied: pytz>=2020.1 in c:\\users\\felcy\\pictures\\new folder\\new folder\\lib\\site-packages (from pandas<3,>=1.3.0->streamlit) (2024.1)\n",
      "Requirement already satisfied: tzdata>=2022.7 in c:\\users\\felcy\\pictures\\new folder\\new folder\\lib\\site-packages (from pandas<3,>=1.3.0->streamlit) (2023.3)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in c:\\users\\felcy\\pictures\\new folder\\new folder\\lib\\site-packages (from requests<3,>=2.27->streamlit) (2.0.4)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\felcy\\pictures\\new folder\\new folder\\lib\\site-packages (from requests<3,>=2.27->streamlit) (3.7)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in c:\\users\\felcy\\pictures\\new folder\\new folder\\lib\\site-packages (from requests<3,>=2.27->streamlit) (2.2.2)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\felcy\\pictures\\new folder\\new folder\\lib\\site-packages (from requests<3,>=2.27->streamlit) (2024.7.4)\n",
      "Requirement already satisfied: markdown-it-py<3.0.0,>=2.2.0 in c:\\users\\felcy\\pictures\\new folder\\new folder\\lib\\site-packages (from rich<14,>=10.14.0->streamlit) (2.2.0)\n",
      "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in c:\\users\\felcy\\appdata\\roaming\\python\\python312\\site-packages (from rich<14,>=10.14.0->streamlit) (2.18.0)\n",
      "Requirement already satisfied: smmap<5,>=3.0.1 in c:\\users\\felcy\\pictures\\new folder\\new folder\\lib\\site-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.0)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in c:\\users\\felcy\\pictures\\new folder\\new folder\\lib\\site-packages (from jinja2->altair<6,>=4.0->streamlit) (2.1.3)\n",
      "Requirement already satisfied: attrs>=22.2.0 in c:\\users\\felcy\\pictures\\new folder\\new folder\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (25.1.0)\n",
      "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in c:\\users\\felcy\\pictures\\new folder\\new folder\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (2023.7.1)\n",
      "Requirement already satisfied: referencing>=0.28.4 in c:\\users\\felcy\\pictures\\new folder\\new folder\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.30.2)\n",
      "Requirement already satisfied: rpds-py>=0.7.1 in c:\\users\\felcy\\pictures\\new folder\\new folder\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.10.6)\n",
      "Requirement already satisfied: mdurl~=0.1 in c:\\users\\felcy\\pictures\\new folder\\new folder\\lib\\site-packages (from markdown-it-py<3.0.0,>=2.2.0->rich<14,>=10.14.0->streamlit) (0.1.0)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\felcy\\appdata\\roaming\\python\\python312\\site-packages (from python-dateutil>=2.8.2->pandas<3,>=1.3.0->streamlit) (1.16.0)\n",
      "Downloading packaging-23.2-py3-none-any.whl (53 kB)\n",
      "   ---------------------------------------- 0.0/53.0 kB ? eta -:--:--\n",
      "   ------- -------------------------------- 10.2/53.0 kB ? eta -:--:--\n",
      "   --------------- ------------------------ 20.5/53.0 kB 217.9 kB/s eta 0:00:01\n",
      "   -------------------------------------- - 51.2/53.0 kB 372.4 kB/s eta 0:00:01\n",
      "   ---------------------------------------- 53.0/53.0 kB 342.2 kB/s eta 0:00:00\n",
      "Installing collected packages: packaging\n",
      "  Attempting uninstall: packaging\n",
      "    Found existing installation: packaging 24.1\n",
      "    Uninstalling packaging-24.1:\n",
      "      Successfully uninstalled packaging-24.1\n",
      "Successfully installed packaging-23.2\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install streamlit"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "6914489c-3a5d-4e1f-b546-deb76439abdf",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-02-23 22:31:57.632 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\felcy\\AppData\\Roaming\\Python\\Python312\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n",
      "22:31:58 - cmdstanpy - INFO - Chain [1] start processing\n",
      "22:31:59 - cmdstanpy - INFO - Chain [1] done processing\n",
      "C:\\Users\\felcy\\Pictures\\New folder\\New folder\\Lib\\site-packages\\prophet\\forecaster.py:1854: FutureWarning: 'M' is deprecated and will be removed in a future version, please use 'ME' instead.\n",
      "  dates = pd.date_range(\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "from prophet import Prophet\n",
    "\n",
    "st.title(\"📊 Vrinda Store Sales Forecasting App\")\n",
    "st.write(\"This app analyzes and forecasts sales trends for Vrinda Store.\")\n",
    "\n",
    "df = pd.read_csv(\"Vrinda Store Data.csv\") \n",
    "\n",
    "df[\"Date\"] = pd.to_datetime(df[\"Date\"])\n",
    "df[\"Year-Month\"] = df[\"Date\"].dt.to_period(\"M\")\n",
    "\n",
    "df_forecast = df.groupby(\"Year-Month\")[\"Qty\"].sum().reset_index()\n",
    "df_forecast[\"ds\"] = pd.to_datetime(df_forecast[\"Year-Month\"].astype(str))\n",
    "df_forecast.rename(columns={\"Qty\": \"y\"}, inplace=True)\n",
    "\n",
    "model = Prophet()\n",
    "model.fit(df_forecast)\n",
    "\n",
    "future = model.make_future_dataframe(periods=36, freq=\"M\")\n",
    "forecast = model.predict(future)\n",
    "\n",
    "st.subheader(\"📈 Forecasted Sales\")\n",
    "fig, ax = plt.subplots()\n",
    "ax.plot(forecast[\"ds\"], forecast[\"yhat\"], label=\"Forecast\", color=\"blue\")\n",
    "ax.fill_between(forecast[\"ds\"], forecast[\"yhat_lower\"], forecast[\"yhat_upper\"], alpha=0.2)\n",
    "ax.set_xlabel(\"Date\")\n",
    "ax.set_ylabel(\"Quantity Sold\")\n",
    "ax.legend()\n",
    "st.pyplot(fig)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d45695ca-cad0-4917-aa7e-410786ff61f4",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

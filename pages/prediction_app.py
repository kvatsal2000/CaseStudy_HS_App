import numpy as np
import pandas as pd
import streamlit as st
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv('clean.csv',parse_dates=['datetime'],index_col='datetime')
df.drop(columns = ['Unnamed: 0'], inplace =True)

scaler = MinMaxScaler()
feature_cols = df.columns
scaled_values = scaler.fit_transform(df.values)
df_normalized = pd.DataFrame(scaled_values, columns=feature_cols)


model_final = load_model('final_lstm_model.keras')


def predict_future_vals(future_steps):
    last_sequence = df_normalized.tail(24).to_numpy()
    future_predictions = []

    # Predict future values iteratively
    for a in range(future_steps):
        last_sequence_reshaped = last_sequence[np.newaxis, :, :]
        next_prediction = model_final.predict(last_sequence_reshaped, verbose=0)
        future_predictions.append(next_prediction.flatten())
        last_sequence = np.vstack([last_sequence[1:], next_prediction])

    # Convert predictions to NumPy array and apply inverse scaling
    future_predictions = np.array(future_predictions)
    df_pred = pd.DataFrame(scaler.inverse_transform(future_predictions), columns=feature_cols)
    return df_pred



# App



st.markdown("# :blue-background[Air Quality Prediction]")
st.sidebar.markdown("# Air Quality Prediction")

st.sidebar.markdown("## About the Model:")
st.sidebar.write("""The predictions are done using LSTM deep learning model.The model takes into account
            last 24 values to predict the next value.  """)

# User input for the number of steps to forecast
future_steps = st.number_input("Enter the number of steps ahead to forecast:", min_value=1, max_value=1000, value=10)

if st.button("Predict"):
    predictions_df = predict_future_vals(future_steps)
    st.write(f"Future Predictions for the Next {future_steps} Steps:")
    st.dataframe(predictions_df)



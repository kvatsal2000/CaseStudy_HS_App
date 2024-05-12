#!/bin/sh
echo "Streamlit app is running at http://127.0.0.1:8501 or http://localhost:8501"
streamlit run app.py --server.port=8501 --server.address=0.0.0.0

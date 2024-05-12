FROM python:3.11.7-slim

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

COPY start_streamlit.sh /app/start_streamlit.sh
RUN chmod +x /app/start_streamlit.sh

EXPOSE 8501

CMD ["/app/start_streamlit.sh"]


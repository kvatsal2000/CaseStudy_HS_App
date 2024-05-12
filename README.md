# CaseStudy_HS_App

## This repository is made for the Healthscope Graduate Data Scientist Case Study. It contains the Interactive web app created using streamlit.


- After cloning the repo, install the required packages using:
  
```  
pip install -r requirements.txt
```
- To run the application:

```
streamlit run app.py
```

- To build and run docker container:

```
docker build -t streamlit-app .
```

```
docker run -p 8501:8501 streamlit-app
```

*If the above command throws an error try changing the line endings in the start_streamlit.sh file from CRLF to LF.*


## This repository contains the Interactive web app created using streamlit for the UCI Air Quality dataset.


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

- *If the above command throws an error try changing the line endings in the start_streamlit.sh file from CRLF to LF.*
- *If the app does not run on the URL provided by docker, try http://localhost:8501 or http://127.0.0.1:8501 while the container is running.*


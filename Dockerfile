from python:3.9
WORKDIR /app
COPY app.py .
RUN pip install flask
cmd ["python", "app.py"]

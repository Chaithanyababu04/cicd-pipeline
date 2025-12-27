from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello, World!'
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)          

# This is a simple Flask application that returns "Hello, World!" when accessed at the root URL.

# To run this application, save it as app.py and execute it with Python.

# Make sure you have Flask installed in your environment. You can install it using pip:
# pip install Flask
# Then, run the application:
# python app.py 
# The application will be accessible at http://
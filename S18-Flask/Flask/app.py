from flask import Flask,render_template

app = Flask(__name__) #create a Flask application instance which will be WSGI application

@app.route('/') #define a route for the root URL
def home():
    return "<html><body><h1>Hello, hi Welcome to the Flask Code!</h1></body></html>" #return a simple HTML response when the root URL is accessed

@app.route('/index') #define a route for the /index URL
def index():
    return render_template('index.html') #render and return the index.html template when the /index URL is accessed


@app.route('/about.us') #define a route for the /about.us URL
def about_us():
    return render_template('about.html') #render and return the about.html template when the /about.us URL is accessed

if __name__ == "__main__":
    app.run(debug=True) #run the Flask application in debug mode
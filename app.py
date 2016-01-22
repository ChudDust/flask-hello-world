# ---- Flask Hello World ---- #

# import the Flask class from the Flask package

from flask import Flask

# create the application object

app = Flask(__name__)

# use decorators to link the function to a url

@app.route("/")
@app.route("/hello")

# define the view using a funciton, which returns a string

def hello_world():
    return "Hello, World!"
    
# start the development server using the run() method
if__name__=="__main__":
    app.run()    

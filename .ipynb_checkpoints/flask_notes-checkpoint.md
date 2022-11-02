Flask: micro web framework written in python.
Prereqs to using flask: python


installing flask: pip install flask-sqlalchemy
Hello World Flask:

from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return "Hello World!"

if __name__ == "__main__"
    app.run(debug = True)
    
Explanation: 
routing: @app.route('/') establishes route for app, a route is a way to map urls to specific functions. '/' is our root url
index function is bound to the root of our app
app.run(debug = True) runs app in debug mode


Creating Web Server API:
use flask_restful module
api = Api(app): wrap app in an api, located in flask_restful module

create resources by making new classes that inherit from resource class.
New resources must be registered, api.add_resource(New_Resource, URI)
URI: "/Resource/parameters <type: name>"
add_resource will register the routes with the framework using the given endpoint. Default endpoint using class name is made if no endpoint is given

Making requests:
import request
response = requests.get(Base_URL + resource_name) //returns json type object
returns must be json serializable ( just use a dictionary)

Different types of api resource requests: 
Post: creates new resource and associates it with the proper hierarchy. Returns dedicated URL
Put: creates a new resource or replaces a representation of the target resource with the request payload
Patch: Somewhat similar to put, it will modify the current resource contents 
Get: returns a represenational vew of the resources contents and data
Delete: deletes resource contents


Parsing Requests:
using reqparser from flask_restful will ensure that proper arguments are passed in with each request
Syntax: 
put_args = reqparse.RequestParser()
    RequestParser() sets argument to None if argument not provided
put_args.add_argument("argument", type = type, help = "Error Message", required = True/False)
Repeat line 47 for every argument 

if required is true, program will crash based on whether required param is true or not



Error handling:
flask_restful abort(abort_code, "Message"): will abort program and display error message

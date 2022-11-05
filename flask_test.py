from flask import Flask
from flask_restful import Api, Resource,reqparse,abort

app = Flask("__name__")
api = Api(app)


put_args = reqparse.RequestParser()
put_args.add_argument("name",type = str, help = "Invalid request", required = True)

file_types = ["json", "html", "jpg"]

qr_codes = {}
class QR_Code(Resource):
    
    def get(self):
        return "This is a QR_Code"
    def post(self, name):
        args = put_args.parse_args()
        file_type = args["name"].split('.')[1]
        
        if(file_type not in file_types):
            abort(404,"Invalid File Type")
        qr_codes[name] = {"args" : args, "file type" : file_type}
        
        return "QR_Code has been posted"
    



    

api.add_resource(QR_Code,"/QR_Code/ <str: name>")


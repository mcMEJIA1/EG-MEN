from flask import Flask ,jsonify ,request
from flask_cors import CORS
from controllers.mensaje import Mensaje

app = Flask(__name__)
CORS(app)

@app.route('/mensaje', methods=['GET'])
def getall():
    return (Mensaje.list())

@app.route('/mensaje', methods=['POST'])
def post():
    body = request.json
    return (Mensaje.post(body))

@app.route('/mensaje/<string:id_men>', methods=['DELETE'])
def delete(id_men):
    path =  id_men
    return (Mensaje.delete(path))

@app.route('/mensaje', methods=['PUT'])
def put():
    body = request.json
    return (Mensaje.put(body))

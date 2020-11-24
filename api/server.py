<<<<<<< HEAD
from flask import Flask , request
from flask import jsonify, request
from flask_cors import CORS
from controllers.mensaje import Mensaje
=======
from flask import Flask, request
from flask_cors import CORS
from controllers.Canal import Canal
>>>>>>> 4a410c7b4644a90b5a743415655b0d8f0820a488
from db.db import cnx

app = Flask(__name__)

<<<<<<< HEAD
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

=======

@app.route('/canal', methods=['GET'])
def getAll():
    return (Canal.get())

@app.route('/canal', methods=['POST'])
def post():
    body =  request.json
    return (Canal.post(body))

@app.route('/canal', methods=['DELETE'])
def delete():
    body = request.json
    return (Canal.delete(body))
>>>>>>> 4a410c7b4644a90b5a743415655b0d8f0820a488

if __name__ == '__main__':
 app.run(port = 3000, debug=True)

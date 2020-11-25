from flask import Flask, render_template, request, send_file
import requests
from flask_cors import CORS
import os
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage

app = Flask(__name__, template_folder='templates')
app.config['UPLOAD_FOLDER'] = './files'

back_route = 'http://35.193.197.93/mensaje'
canales = ['SMS','Email','WhatsApp']

@app.route('/listMensajes', methods=['GET'])
def getMensajes():
    res = requests.get(back_route)
    if res:
        mensajes = res.json()
    else:
        mensajes = {}
    print(mensajes)
    return render_template('mensajes.html', mensajes=mensajes)


@app.route('/crearMensaje', methods=['GET'])
def getMessages():
    return render_template('index.html', canales=canales)


@app.route('/enviarMensaje', methods=['POST'])
def postMensaje():

    mensaje = dict(request.values)
    print(mensaje)
    mensaje['remitente'] = 'evergreen@evergreen.com.co'
    mensaje['asunto'] = str(request.values['asunto'])
    mensaje['destinatario'] = str(request.values['destinatario'])
    mensaje['canal'] = str(request.values['tipo'])
    mensaje['cuerpo'] = str(request.values['cuerpo'])

    if request.values['estado']:
        mensaje['estado'] = 'pendiente'
    else:
        mensaje['estado'] = 'enviado'

    mensaje['adjunto'] = ''

    requests.post(back_route, json=mensaje)

    return (getMensajes())
    
@app.route('/delete/<string:message>')
def delete (message):
    requests.delete(back_route + '/' + message)
    return (getMensajes())


app.run(port=3001, host='0.0.0.0', debug=True)
<<<<<<< HEAD
from flask import Flask, render_template, request, send_file
import requests
from flask_cors import CORS
import os
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage

app = Flask(__name__, template_folder='templates', static_folder='static' )
app.config['UPLOAD_FOLDER'] = './files'

back_route = 'http://localhost:3000/mensaje'
canales = ['SMS','Email','WhatsApp']

@app.route('/listMensajes', methods=['GET'])
def getMensajes():
    mensajes = requests.get(back_route).json()
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

    f = request.files['adjunto']

    if f is None:
        mensaje['adjunto'] = ''
    else:
        nombreA = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], nombreA))
        route = nombreA
        mensaje['adjunto'] = route

    requests.post(back_route, json=mensaje)

    return (getMensajes())

@app.route('/descargar/<string:file>', methods=['GET'])
def descargar (file):
    path = 'files/' + file
    return send_file(path, as_attachment=True)
    
@app.route('/delete/<string:message>')
def delete (message):
    requests.delete(back_route + '/' + message)
    return (getMensajes())
=======
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

tipo_destinatarios = ['Simple', 'Grupal']
tipo_canales = ['SMS', 'Email','WhatsApp','Llamada']

@app.route('/listarCanales', methods=['GET'])
def listarCanales():
    canales = requests.get('http://localhost:3000/canal').json()
    #print(canales)
    return render_template('canales.html', canales=canales)


@app.route('/crearCanales', methods=['GET'])
def crearCanales():
    return render_template('listarCanales.html',tipo_destinatarios=tipo_destinatarios,tipo_canales=tipo_canales)


@app.route('/guardarCanales', methods=['POST'])
def guardarCanales():

    canal = dict(request.values)
    
    canal['nombre'] = str(request.form['nombre'])
    canal['tipo'] = str(request.form['tipo'])
    canal['tipo_destinatario'] = str(request.form['tipo_destinatario'])
    canal['fecha'] = str(request.form['fecha'])

    requests.post('http://localhost:3000/canal', json=canal)

    return (listarCanales())
>>>>>>> 4a410c7b4644a90b5a743415655b0d8f0820a488


app.run(port=3001, host='0.0.0.0', debug=True)
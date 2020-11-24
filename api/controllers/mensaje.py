from flask import jsonify, request
from db.db import cnx

class Mensaje:
    global cur  
    cur = cnx.cursor()
    
    def list():
        lista = []
        cur.execute("SELECT * FROM mensaje")
        rows = cur.fetchall()
        colums = [i[0] for i in cur.description]
        for row in rows:
            registro = zip(colums,row)
            json = dict(registro)
            lista.append(json)
        cnx.close
        return jsonify(results = lista)

    def post(body):
        data = (body['asunto'],body['cuerpo'],body['remitente'],body['destinatario'],body['adjunto'],body['canal'],body['estado'])
        sql = "INSERT INTO mensaje(asunto, cuerpo, remitente,destinatario, adjunto, canal, estado) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        cur.execute(sql,data)
        cnx.commit()
        return{'estado': "Insertado"}, 201

    def delete(id_men):
        sql = "DELETE FROM mensaje WHERE id_men =" + id_men
        cur.execute(sql)
        cnx.commit()
        return{'estado': "Eliminado"}, 200

    def put(body):
        data = (body['cuerpo'],body['id_men'], body['state'])
        estado = 'enviado'
        sql = "UPDATE mensaje SET cuerpo =(%s),destinatario =(%s) WHERE id_men=(%s) AND estado !=(%s)"
        print(sql)
        cur.execute(sql, data)
        cnx.commit()
        return{'estado': "Actualizado"}, 200
from app.model.dosen import Dosen
from app import response, app, db
from flask import request

def index():
    try:
        dosen = Dosen.query.all()
        data = formatArray(dosen)
        return response.success(data, "List Dosen Berhasil Ditampilkan")
    except Exception as e:
        print(e)

def formatArray(data):
    arrayDosen = []

    for i in data:
        arrayDosen.append(singleObject(i))

    return arrayDosen

def singleObject(data):
    dosen = {
        'id' : data.id,
        'nidn' : data.nidn,
        'nama' : data.nama,
        'phone' : data.phone,
        'alamat' : data.alamat
    }

    return dosen
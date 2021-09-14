from app.model.dosen import Dosen
from app.model.mahasiswa import Mahasiswa
from app import response, app, db
from flask import request

def index():
    try:
        dosen = Dosen.query.all()
        data = formatArrayDosen(dosen)
        return response.success(data, "List Dosen Berhasil Ditampilkan")
    except Exception as e:
        print(e)

def formatArrayDosen(data):
    arrayDosen = []

    for i in data:
        arrayDosen.append(singleDosen(i))

    return arrayDosen

def singleDosen(data):
    dosen = {
        'id' : data.id,
        'nidn' : data.nidn,
        'nama' : data.nama,
        'phone' : data.phone,
        'alamat' : data.alamat
    }

    return dosen

def detail(id):
    try:
        dosen = Dosen.query.filter_by(id=id).first()
        mahasiswa = Mahasiswa.query.filter((Mahasiswa.dosen_satu == id) | (Mahasiswa.dosen_dua == id))

        if not dosen:
            return response.badRequest([], 'Data Dosen Tidak Ada')

        dataMahasiswa = formatArrayMahasiswa(mahasiswa)
        data = formatDetailDosen(dosen, dataMahasiswa)

        return response.success(data, "Detail Dosen Berhasil Ditampilkan")

    except Exception as e:
        print(e)

def formatDetailDosen(dosen, mahasiswa):
    data = {
        'id' : dosen.id,
        'nidn' : dosen.nidn,
        'nama' : dosen.nama,
        'phone' : dosen.phone,
        'mahasiswa' : mahasiswa
    }

    return data

def singleMahasiswa(data):
    mahasiswa = {
        'id' : data.id,
        'nim' : data.nim,
        'nama' : data.nama,
        'phone' : data.phone
    }

    return mahasiswa

def formatArrayMahasiswa(data):
    arrayMahasiswa = []
    for i in data:
        arrayMahasiswa.append(singleMahasiswa(i))

    return arrayMahasiswa
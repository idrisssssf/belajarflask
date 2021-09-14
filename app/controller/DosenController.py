from app.model.dosen import Dosen
from app.model.mahasiswa import Mahasiswa
from app.controller.MahasiswaController import formatArrayMahasiswa
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

#Insert/Create Data Dosen
def saveDataDosen():
    try:
        input_nidn = request.form.get('nidn')
        input_nama = request.form.get('nama')
        input_phone = request.form.get('phone')
        input_alamat = request.form.get('alamat')

        dosen = Dosen(nidn=input_nidn, nama=input_nama, phone=input_phone, alamat=input_alamat)
        db.session.add(dosen)
        db.session.commit()

        return response.success('', 'Sukses Menambahkan Data Dosen')
    except Exception as e:
        print(e)

#Update Data Dosen
def updateDosen(id):
    try:
        nidn = request.form.get('nidn')
        nama = request.form.get('nama')
        phone = request.form.get('phone')
        alamat = request.form.get('alamat')

        input = [
            {
                'nidn': nidn,
                'nama': nama,
                'phone': phone,
                'alamat': alamat
            }
        ]

        dosen = Dosen.query.filter_by(id=id).first()

        dosen.nidn = nidn
        dosen.nama = nama
        dosen.phone = phone
        dosen.alamat = alamat

        db.session.commit()

        return response.success(input, 'Sukses update data!')
    except Exception as e:
        print(e)
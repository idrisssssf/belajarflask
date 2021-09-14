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
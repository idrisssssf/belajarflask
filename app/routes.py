from app import app
from app.controller import DosenController
from flask import request

@app.route('/')
def index():
    return "Hello Bro!"

#Get All Dosen & Create New Dosen
@app.route('/dosen', methods=['GET', 'POST'])
def dosen():
    if request.method == 'GET':
        return DosenController.index()
    else:
        return DosenController.saveDataDosen()

#Get Detail Dosen
@app.route('/dosen/<id>', methods=['GET'])
def detailDosen(id):
    return DosenController.detail(id)

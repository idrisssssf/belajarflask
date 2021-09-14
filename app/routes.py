from app import app
from app.controller import DosenController

@app.route('/')
def index():
    return "Hello Bro!"

#Get All Dosen
@app.route('/dosen', methods=['GET'])
def allDosen():
    return DosenController.index()

#Get Detail Dosen
@app.route('/dosen/<id>', methods=['GET'])
def detailDosen(id):
    return DosenController.detail(id)
from flask import Flask, render_template, url_for, redirect, request
import main
from pathlib import Path
import os
import shutil

app = Flask(__name__)


@app.route('/')
def index():
    folder_path = Path('static') / 'Trips'
    folders = [f.name.split('/')[-1] for f in folder_path.iterdir()]
    for i in folders:
        i = i[0].upper
    return render_template('index.html',items=folders)

@app.route('/generate', methods=['POST'])
def generate():
    main.run()
    return redirect('/')

@app.route('/upload', methods=['POST'])
def upload():
    files = request.files.getlist('files')
    folder_name = request.form['folder_name']
    upload_path = f'static/Trips/{folder_name}'
    os.makedirs(upload_path, exist_ok=True)

    for file in files:
        if file.filename:
            file.save(f'{upload_path}/{file.filename}')
    return redirect('/')

@app.route('/delete',methods=['POST'])
def delete():
    folder_name = request.form['folder_name']
    fpath = Path('static')/ 'Trips' / folder_name
    if fpath.exists():
        try:
            shutil.rmtree(fpath)
        except OSError as e:
            print('Error deleting file')

    return redirect('/')

if __name__ == '__main__':
   app.run(port=8000, debug=True)




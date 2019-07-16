from flask import render_template, request, redirect, url_for
from parsers.scholar import Scholar

from app import app

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/parse', methods=['POST'])
def parse():
   # print('Get parse request.\nData:')
   # print(request.form.getlist('tags[]'))
   # print(request.form['email'])
   sch = Scholar(request.form.getlist('tags[]'))
   print(sch.parsing())
   return redirect(url_for('index'))

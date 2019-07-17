from flask import render_template, request, redirect, url_for
from parsers.scholar import Scholar

from app import app

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/parse', methods=['POST'])
def parse():
   sch = Scholar(request.form.getlist('tags[]'))
   sch.parsing()
   return redirect(url_for('index'))

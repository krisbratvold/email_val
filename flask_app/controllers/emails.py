from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.email import Email

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success')
def show():
    return render_template('success.html', emails = Email.get_all())

@app.route('/create', methods=['POST'])
def create():
    if not Email.validate_email(request.form):
        return redirect('/')
    data = {
        'email' : request.form['email']
    }
    Email.create(data)
    return redirect('/success')

@app.route('/<id>/delete')
def delete(id):
    data = {
        'id': id,
    }
    Email.delete(data)
    return redirect("/success")


from flask import Blueprint, render_template, send_from_directory

user = Blueprint('user', __name__)

@user.route('/')
@user.route('/home')
def home():
    return render_template('index.html')

@user.route('/csv-download', methods=['GET', 'POST'])
def csv():
    return send_from_directory('csv', 'eq.csv', mimetype='text/csv', attachment_filename='eq.csv',as_attachment=True)
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import pykakasi
import os

app = Flask(__name__)

class UserInfo:
    def __init__(self, last_name, first_name, job, gender, message):
        self.last_name = last_name
        self.first_name = first_name
        self.job = job
        self.gender = gender
        self.message = message

@app.route('/signup')
def sign_up():
    return render_template('signup.html')

@app.route('/home', methods=["GET", "POST"])
def home():
    print(request.full_path)
    print(request.method)
    print(request.args)
    # user_info = UserInfo(
    #     request.args.get('last_name'),
    #     request.args.get('first_name'),
    #     request.args.get('job'),
    #     request.args.get('gender'),
    #     request.args.get('message')
    # )
    user_info = UserInfo(
        request.form.get('last_name'),
        request.form.get('first_name'),
        request.form.get('job'),
        request.form.get('gender'),
        request.form.get('message')
    )

    return render_template('home.html', user_info=user_info)

@app.route('/upload', methods=["GET","POST"])
def upload():
    if request.method == 'GET':
        return render_template('upload.html')
    elif request.method == 'POST':
        file = request.files['file']
        save_filename = secure_filename(file.filename)
        file.save(os.path.join("./static/image", save_filename))
        return redirect(url_for('uploaded_file', filename=save_filename))


@app.route('/uploaded_file/<string:filename>')
def uploaded_file(filename):
    return render_template('uploaded_file.html',filename=filename)


if __name__ == '__main__':
    app.run(debug=True)
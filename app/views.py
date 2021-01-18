from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from markupsafe import escape
from app import appInstance
from app.models import User


@appInstance.route('/list/<int:page>', methods=['GET', 'POST'])
def list(page):
    if request.method == 'GET':
        per_page = request.args.get('per_page')
        print(request.form.get('elements'))
        if per_page is None:
            per_page = 25
        else:
            per_page = int(per_page)
        users = User.query.paginate(per_page=per_page, page=page)
        return render_template('index.html', users=users, per_page=per_page)
    else:
        elements = int(request.form.get('elements'))
        users = User.query.paginate(per_page=elements, page=1)
        return render_template('index.html', users=users, per_page=elements)

@appInstance.route('/', methods=['GET'])
def index():
    return redirect('/list/1')

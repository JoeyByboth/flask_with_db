import json
import os

from flask import request, render_template, flash, redirect, url_for

from . import create_app, database
from .models import Cats

app = create_app()
app.secret_key = os.environ.get('SECRET_KEY', 'default_secret_key')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['GET'])
def fetch():
    cats = database.get_all(Cats)
    all_cats = []
    for cat in cats:
        new_cat = {
            "id": cat.id,
            "name": cat.name,
            "price": cat.price,
            "breed": cat.breed
        }

        all_cats.append(new_cat)
    return json.dumps(all_cats), 200


@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    price = request.form['price']
    breed = request.form['breed']

    database.add_instance(Cats, name=name, price=price, breed=breed)
    flash("Cat added successfully!")
    return redirect(url_for('index'))


@app.route('/remove/<cat_id>', methods=['DELETE'])
def remove(cat_id):
    database.delete_instance(Cats, id=cat_id)
    return json.dumps("Deleted"), 200


@app.route('/edit/<cat_id>', methods=['PATCH'])
def edit(cat_id):
    data = request.get_json()
    new_price = data['price']
    database.edit_instance(Cats, id=cat_id, price=new_price)
    return json.dumps("Edited"), 200

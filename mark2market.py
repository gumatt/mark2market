import os

from flask import Flask, render_template, request, redirect

from pymongo import MongoClient

MONGO_URL = os.environ.get('MONGOHQ_URL')
client = MongoClient(MONGO_URL)

# Specify the database
db = client.testapp
collection = db.accounts

app = Flask(__name__)


@app.route('/')
def index():
    accounts = collection.find()
    return render_template('index.html', accounts=accounts)


@app.route('/', methods=['POST'])
def post():
    account = {"name": request.form['name'], "description": request.form['description']}
    account_id = collection.insert(account)
    return redirect('/')

def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
    # port = int(os.environ.get("PORT", 5000))
    # app.run(host='0.0.0.0', port=port)

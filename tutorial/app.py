import os
import pyrebase
from config import config

from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = "adadada dd"
firebase = pyrebase.initialize_app(config)
db = firebase.database()

data = {"nae": "eugene"}
db.child("uss").push(data)

# a simple page that says hello
@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/eugene')
def uploadList():
  list={"food1":{"name":"apple", "taste":"5/10"}, "food2":"banana"}
  db.child("foods").child("good food").set(list)
  return "Done"

@app.route("/upload/<key>/<rating>")
def addRate(key, rating):
  listA = {"Rating": rating}
  db.child("foods").child(key).set(listA)
  return ("DONE!")

@app.route('/read/food/<name>')
def read_food(name):
  users = db.child("foods").child("good food").child(name).get().val()
  if (users is None):
    return ("Empty!")
  return (users)

import auth, search
app.register_blueprint(search.bp)

app.register_blueprint(auth.bp)

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))


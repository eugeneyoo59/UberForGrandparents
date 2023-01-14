import os

from flask import Flask, render_template

app = Flask(__name__)

# a simple page that says hello
@app.route('/')
def hello():
    return render_template("index.html")

import auth, search
app.register_blueprint(search.bp)

app.register_blueprint(auth.bp)

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
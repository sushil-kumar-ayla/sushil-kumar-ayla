#  This is test flask project
#todo: crate a virtual env.
#todo: install flask in the dir.
#todo: create a templates folder with same name
#todo: create a welcome page and home page as dirrent folder.
###############################################################
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    return "<p>welcom</p>"

@app.route('/product')
def products():
    return render_template('about.html')
    #return "render_template('product.html')"

@app.route('/templates')
def template():
    return render_template('welcome.html')
    #return "render_template('product.html')"

if __name__=="__main__":
    app.run(debug=True ,port=8000)


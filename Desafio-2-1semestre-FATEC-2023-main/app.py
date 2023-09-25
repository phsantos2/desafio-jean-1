from flask import Flask
from flask import render_template

app = Flask("__name__")

@app.route ("/")
def home ():
    return render_template ('home.html')

@app.route ("/home2.html")
def home2 ():
    return render_template ('home2.html')

@app.route ("/contato.html")
def contato ():
    return render_template ('contato.html')

@app.route ("/quem_somos.html")
def quem_somos ():
    return render_template ('quem_somos.html')
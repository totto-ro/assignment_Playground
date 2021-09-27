from flask import Flask
from flask import render_template

app = Flask( __name__ )

@app.route( '/play', methods=['GET'] )
def loadPlay():
    return render_template("index.html", box="lightskyblue", num=3)

@app.route( '/play/<int:num>', methods=['GET'] )
def loadPlayNum(num):
    return render_template("index.html", box="lightskyblue", num=num)

@app.route( '/play/<int:num>/<string:color>', methods=['GET'] )
def loadPlayNumColor(num, color):
    return render_template("index.html", num=num, box=color)

if __name__ == "__main__":
    app.run( debug = True )
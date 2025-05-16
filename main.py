import requests
from flask import Flask, render_template, jsonify

# Flask uygulamasını oluştur
app = Flask(__name__)

@app.route('/ligler')
def ligler():
    return render_template('ligler.html')

@app.route('/')
def anasayfa():
    return render_template('index.html')

@app.route('/yasalbahis')
def yasalbahis():
    return render_template('yasalbahis.html')


@app.route('/canlımaclar')
def canlımaclar():
    return render_template('canlımaclar.html')
@app.route('/discord')
def discord():
    return render_template('discord.html')



if __name__ == '__main__':
    app.run(debug=True)
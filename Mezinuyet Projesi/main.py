
from flask import Flask, render_template, jsonify


ligler = [
    {
        "isim": "Süper Lig",
        "ülke": "Türkiye",
        "takımlar": ["Galatasaray", "Fenerbahçe", "Beşiktaş", "Trabzonspor"]
    },
    {
        "isim": "Premier League",
        "ülke": "İngiltere",
        "takımlar": ["Manchester United", "Chelsea", "Liverpool", "Arsenal"]
    },
    {
        "isim": "La Liga",
        "ülke": "İspanya",
        "takımlar": ["Barcelona", "Real Madrid", "Atletico Madrid", "Sevilla"]
    },
    {
        "isim": "Serie A",
        "ülke": "İtalya",
        "takımlar": ["Juventus", "AC Milan", "Inter Milan", "Napoli"]
    },
    {
        "isim": "Bundesliga",
        "ülke": "Almanya",
        "takımlar": ["Bayern Münih", "Borussia Dortmund", "RB Leipzig", "Leverkusen"]
    }
]
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ligler')
def get_ligler():
    return jsonify(ligler)  # jsonify zaten ensure_ascii=False kullanır




@app.route('/takımlar')
def teams():
    return "<h2>Takımlar Sayfası</h2>"

if __name__ == '__main__':
    app.run(debug=True)
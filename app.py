import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=80')
    pokemons = response.json()['results']
    return render_template('index.html', pokemons=pokemons)

@app.route('/pokemon/<name>')
def pokemon_detail(name):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name}')
    pokemon = response.json()
    
    # ดึงข้อมูลประวัติย่อ (flavor text)
    species_response = requests.get(f'https://pokeapi.co/api/v2/pokemon-species/{name}')
    species = species_response.json()
    flavor_text_entries = species.get('flavor_text_entries', [])
    
    # เลือก flavor text ที่เป็นภาษาอังกฤษ
    flavor_text = next((entry['flavor_text'] for entry in flavor_text_entries if entry['language']['name'] == 'en'), 'No description available.')
    
    return render_template('pokemon_detail.html', pokemon=pokemon, flavor_text=flavor_text)

if __name__ == '__main__':
    app.run(debug=True)

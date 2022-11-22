# WHY = separate the python code from the HTML code and make it scaleable!


# import the flask  library for usage!
from flask import Flask, request, render_template
import json
from pprint import PrettyPrinter
import json
import requests
from dotenv import load_dotenv

load_dotenv()

# create an  instance of the flask server 
# (app or server)
app = Flask(__name__)

# create some routes!
@app.route('/')
def displayHomepage():
    return render_template('home.html')



# **********************************
SWAPI_URL = 'https://swapi.py4e.com/api/people/'

pp = PrettyPrinter(indent=4)

@app.route('/search', methods = ['GET', 'POST'])
def character_search():
    '''Show a form to search for Star Wars characters 
    and show resulting info from SWAPI'''
    print('***************************')
    if request.method == 'POST':
        # category = request.form.get('category')
        id_number = request.form.get('id_number')

        response = requests.get(f"{SWAPI_URL}{id_number}")
        print(f"{SWAPI_URL}{id_number}")

        character = json.loads(response.content)

        context = {
            'character': character
        }   

        pp.pprint(character)

        return render_template('character_search.html', **context)
    else:
        return render_template('character_search.html')





# turn the server on for serving!
if __name__ == "__main__":
    app.config['ENV'] = 'development'
    app.run(debug=True)
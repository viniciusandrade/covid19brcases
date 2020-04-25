# routes.py
from app import app  # aqui precisamos importar o app criado no __init__.py
from flask import render_template
import requests
from datetime import datetime

# Criando nossa primeira rota
@app.route('/')
def index():
    request = requests.get('https://api.covid19.finspect.me/covid19/total')

    world_total_data = request.json()[0]
    world_data = {
        key: "{:,}".format(value).replace(',', '.') for key, value in world_total_data.items() 
        if key == "confirmed" or key == "deaths" or key == "recovered"
    }

    return render_template('index.html', world_data=world_data)  

@app.route('/brasil')
def brazil():
    # Fazendo a requisição para a API pra ter os dados da tabela
    states_data_for_table = requests.get('https://api.covid19.finspect.me/brcovid19/map').json()

    # Fazendo a nova requisição para ter os casos por dia
    daily_cases_data = requests.get('https://api.covid19.finspect.me/brcovid19/day').json()

    cases_list = list()
    dates_list = list()
    
    for daily_data in daily_cases_data:
        cases_list.append(daily_data['qtd_confirmation'])
        dates_list.append(daily_data['label'])


    # Pegando a data atual
    date = datetime.now().strftime(format="%d/%m/%Y")

    return render_template('brazil.html', 
                        table_data=states_data_for_table, 
                        date=date,
                        cases_list=cases_list,
                        dates_list=dates_list,
                        )


@app.route('/mundo')
def world():
    return render_template("world.html", world="World")

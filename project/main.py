# main.py

from flask import Blueprint, render_template, jsonify
from flask_login import login_required, current_user
from flask_user import roles_required
from flask.wrappers import Response
import requests
from .db11 import Mysql
import json

main = Blueprint('main', __name__)


my_api_key = 'e0ceab0a0598e4e46dc24a0cd7d58cdc999c0b5e'
my_country = 'GB'
my_year = '2021'

calendarific_data = 'https://calendarific.com/api/v2/holidays?&api_key={api_key}&country={country}&year={year}'

calendaific_url = calendarific_data.format(
    api_key = my_api_key,
    country = my_country,
    year = my_year
)

#request the data from API
resp = requests.get(calendaific_url)
if resp.ok:
    calendarifics = resp.json()
    # store data as json in local server
    with open('weather.json', 'w') as f:
        json.dump(calendarifics,f)
else:
    print(resp.reason)

#default for login page
@main.route('/')
def index():
    return render_template('index.html')

#use GET to request all information
@main.route('/records/', methods=['GET']) 
@login_required
def get_records():
    return jsonify(calendarifics)

# use GET to select the holidays from database
@main.route('/records/holidays/', methods=['GET'])
def get_data():
    response = Mysql.select1()
    return Response(
        response=json.dumps(response),
        status=200,
        mimetype="application/json"
    )

#use POST to insert holidays
@main.route('/records/holidays/', methods=['POST'])
def add_holidays():
    for dic in calendarifics['response']['holidays']:
        response = Mysql.insert(dic)
        return jsonify(response)

# use put to update holidays
@main.route('/records/holidays/<oldname>/<newname>', methods=['PUT'])
def update_holidays(oldname,newname):
    a = oldname
    a.replace('%20', ' ')
    b=newname
    b.replace('%20', ' ')
    response = Mysql.update1(a,b)
    return jsonify(response)

# use DELETE to delete holidays
@main.route('/records/holidays/<name>', methods=['DELETE'])
def del_holidays(name):
    a = name
    a.replace('%20', ' ')
    response = Mysql.delete1(a)
    return jsonify(response)

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

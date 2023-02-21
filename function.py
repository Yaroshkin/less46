import json,datetime,requests
from flask import render_template


foot = "Serhii Yaroshkin\n+380-63-698-83-58"
title = 'HomeWork'
def hello_world():
    global foot
    global title
    time = datetime.datetime.now()
    return render_template("index.html", title=title, time=time, footer=foot)
def home():
    global foot
    time = datetime.datetime.now()
    global title
    response = requests.get("http://localhost:5000/home2")
    json_data = json.loads(response.text)
    hum = json_data.get('humidity')
    return render_template('hum.html', title=title, hum=hum, time=time, footer=foot)

def home_alone_2():
    global foot
    time = datetime.datetime.now()
    global title
    response = requests.get("http://localhost:5000/home2")
    json_data = json.loads(response.text)
    temp = json_data.get('temperature')
    return render_template('temp.html',title=title,temp=temp,time=time, footer=foot)

def meter():
    global foot
    global title
    return render_template('meter.html',title=title)

def ele():
    global foot
    time = datetime.datetime.now()
    global title
    response = requests.get("http://localhost:5000/home2")
    json_data = json.loads(response.text)
    met = json_data['meter']['electricity']['reading']
    met1 = json_data['meter']['electricity']['consumption']
    return render_template('ele.html',ele=met,ele1=met1,title=title,footer=foot)

def gaz():
    global foot
    time = datetime.datetime.now()
    global title
    response = requests.get("http://localhost:5000/home2")
    json_data = json.loads(response.text)
    gaz = json_data['meter']['gas']['reading']
    gaz_n = json_data['meter']['gas']['consumption']
    return render_template('gaz.html',gaz=gaz,gaz1=gaz_n,title=title,footer=foot)

def wat():
    global foot
    time = datetime.datetime.now()
    global title
    response = requests.get("http://localhost:5000/home2")
    json_data = json.loads(response.text)
    wat = json_data['meter']['water']['reading']
    wat_n = json_data['meter']['water']['consumption']
    return render_template('water.html',water=wat,water1=wat_n,title=title,footer=foot)

def boil():
    global foot
    time = datetime.datetime.now()
    global title
    response = requests.get("http://localhost:5000/home2")
    json_data = json.loads(response.text)
    boil = json_data['boiler']['isRun']
    boil_tem = json_data['boiler']['temperature']
    boil_pre = json_data['boiler']['pressure']
    return render_template('boiler.html',boil=boil,boil1=boil_tem,boil2=boil_pre,title=title,footer=foot)

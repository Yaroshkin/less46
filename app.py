import random

from flask import Flask, url_for
import function
import json

app = Flask(__name__)




@app.route('/')
def start():
    return function.hello_world()

@app.route('/<text>')
def text(text):
    if text == 'temperature':
        return function.home_alone_2()
    elif text == 'hum':
        return function.home()
    elif text == 'meter':
        return function.meter()
    elif text == 'boiler':
        return function.boil()

@app.route('/meter/<text>')
def text2(text):
    if text == 'ele':
        return function.ele()
    elif text == 'gaz':
        return function.gaz()
    elif text == 'water':
        return function.wat()

@app.route('/home2')
def api():
    obj = None
    with open(f'.{url_for("static", filename="example.json")}', 'r') as file:
        obj = json.load(file)

    obj['temperature'] = random.randint(-15, 25)
    obj['humidity'] = random.randint(0, 100)
    obj['meter']['electricity']['reading'] = round(random.uniform(12345.9, 12347.9), 3)
    obj['meter']['electricity']['consumption'] = round(random.uniform(0.1, 2.0), 1)
    obj['meter']['gas']['reading'] = round(random.uniform(2367.9, 2369.9), 3)
    obj['meter']['gas']['consumption'] = round(random.random(), 1)
    obj['meter']['water']['reading'] = round(random.uniform(1212.9, 1214.9), 3)
    obj['meter']['water']['consumption'] = round(random.uniform(0.1, 1.0), 1)
    obj['boiler']['isRun'] = random.choice([True, False])
    obj['boiler']['temperature'] = random.randint(60, 65)
    obj['boiler']['pressure'] = round(random.uniform(1.0, 2.0), 1)

    return json.dumps(obj)
    # return json.dumps(dict1)




if __name__ == '__main__':
    app.run(debug=True)

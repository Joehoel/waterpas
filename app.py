from flask import Flask, jsonify, render_template
from db import connection, cursor, get_all

app = Flask(__name__)

@app.route('/')
def index():
    data = get_all()
    
    return render_template('index.html', data=data)
    
@app.route('/data')
def data():
    data = get_all()
    
    return jsonify(data)



app.run(debug=True, host='0.0.0.0', port=8000)

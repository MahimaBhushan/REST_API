from flask import Flask, jsonify,request, render_template 
app=Flask(__name__)

stores = [
    {
        'name': 'My Wonderful Store',
        'items': [
            {
                'name': 'My Item',
                'price': 15.99
            }
        ]
    }
]
#POST-used to receive data in server point of view
#GET-used to send data back only in server point of view
#the browser will use POST to send us data and GET to receive data
#here we are the server. 
#So if we receive POST store we might have to create a store
#if we receive get store we have to send back a list of stores
#POST /store data: {name:}
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_jason()
    new_store = {
        'name': request_data['name'],
        'item': []
    }
    stores.append(new_store)
    return jsonify(new_store)
#GET /store/<string:name>
@app.route('/store/<string:name>')  #http://127.0.0.1:5000/store/some_name
def get_store(name):
     for store in stores:
         if store['name'] == name:
             return jsonify(store)
     return jsonify({'message': 'store not found'})


#GET /store
@app.route('/store')  #http://127.0.0.1:5000/store/some_name
def get_stores():
    return jsonify({'stores': stores})
#POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_jason()
    for k in stores:
         if k['name'] == name:
             new_item = {
                 'name': request_data['name'],
                 'prise': request_data['prise']
             }
             store['items'].append(new_item)
             return jsonify(new_item)
    return jsonify({'message': 'store not found '})
#GET /store/<string:name>/item
@app.route('/store/<string:name>/item')  
def get_item_in_store(name):
     for j in stores:
         if j['name'] == name:
             return jsonify({'items': store['items']})
     return jsonify({'message': 'store not found'})

app.run(port=5000)
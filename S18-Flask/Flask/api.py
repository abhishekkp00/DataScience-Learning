###Put and delete- HTTP Verbs
### Working With API's --json


from flask import Flask, jsonify, request


app = Flask(__name__)

##Initial data in to-do list
todos = [
    {'id': 1, 'task': 'Buy groceries', 'status': 'pending'},
    {'id': 2, 'task': 'Clean the house', 'status': 'pending'},
    {'id': 3, 'task': 'Finish the project', 'status': 'pending'}   
]

@app.route('/')
def home():
    return "Welcome to the To-Do List API!"

#GET: Retrieve all to-do items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(todos)


##Get the to-do item by id
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in todos if item['id'] == item_id), None)
    if item:
        return jsonify(item)
    else:
        return jsonify({'message': 'Item not found'}), 404

##Post : Create a new to-do item
@app.route('/items', methods=['POST'])
def create_item():
    if not request.json or 'task' not in request.json:
        return jsonify({'message': 'Invalid request'}), 400
    new_item = {
        'id': todos[-1]['id'] + 1 if todos else 1,
        'task': request.json['task'],
        'status': 'pending'
    }
    todos.append(new_item)
    return jsonify(new_item), 201
 
##Put : Update an existing to-do item
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    if item is None:
        return jsonify({'message': 'Item not found'}), 404
    if not request.json:
        return jsonify({'message': 'Invalid request'}), 400
    item = next((item for item in todos if item['id'] == item_id), None)
    if item:
        item['task'] = request.json.get('task', item['task'])
        item['status'] = request.json.get('status', item['status'])
        return jsonify(item)
    else:
        return jsonify({'message': 'Item not found'}), 404
    
##Delete : Remove a to-do item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = next((item for item in todos if item['id'] == item_id), None)
    if item:
        todos.remove(item)
        return jsonify({'message': 'Item deleted'})
    else:
        return jsonify({'message': 'Item not found'}), 404

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, request, jsonify
from flask_lambda import FlaskLambda
from flask_cors import CORS


app = FlaskLambda(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/test-todo-get', methods=['GET'])
def get_todo():
    # Implement your logic here
    return jsonify({
        'message': 'GET /test-get'
    }), 200

@app.route('/test-todo-post', methods=['POST'])
def post_todo():
    # Implement your logic here
    # extract req body data {id,name}
    data = request.get_json()
    id = data['id']
    name = data['name']
    print("id: ", id)
    print("name: ", name)
    return jsonify({
        'message': 'POST /test-get',
        'data': data
    }), 200

@app.route('/test-path-get/<todo_id>', methods=['GET'])
def get_todo_by_id(todo_id):
    # Implement your logic here
    print("i am path parameter :", todo_id)
    return jsonify({
        'message': f'GET /test-get/{todo_id}',
        'todo_id': todo_id
    }), 200

@app.route('/test-get-query', methods=['GET'])
def get_todo_query():
    query_params = request.args             # http://localhost:3000/someapi?name=asif&age=23
    # Implement your logic here
    name = query_params.get('name',"")
    age = query_params.get('age')
    return jsonify({
        'message': 'GET /test-get-query',
        'queryParams': query_params
    }), 200


if __name__ == '__main__':
    app.run(debug=True,port=5000)

def lambda_handler(event, context):
       print("event: ", event)
       return app(event, context)
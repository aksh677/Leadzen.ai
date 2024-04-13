from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = []

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    task = request.json.get('task')
    tasks.append(task)
    return jsonify({'message': 'Task added successfully'})

@app.route('/tasks/<int:index>', methods=['DELETE'])
def delete_task(index):
    if index < len(tasks):
        del tasks[index]
        return jsonify({'message': 'Task deleted successfully'})
    else:
        return jsonify({'error': 'Task index out of range'}), 400

@app.route('/tasks/<int:index>/complete', methods=['PUT'])
def complete_task(index):
    if index < len(tasks):
        tasks[index]['completed'] = True
        return jsonify({'message': 'Task marked as completed'})
    else:
        return jsonify({'error': 'Task index out of range'}), 400

if __name__ == '__main__':
    app.run(debug=True)

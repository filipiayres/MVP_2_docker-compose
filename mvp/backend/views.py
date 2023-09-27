from flask import Blueprint, jsonify, request
from apps.controllers import create_task, get_all_tasks, get_task_by_id, update_task, delete_task

views = Blueprint('views', __name__)

@views.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = get_all_tasks()
    return jsonify([task.to_dict() for task in tasks])

@views.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    task = get_task_by_id(id)
    if task:
        return jsonify(task.to_dict())
    return jsonify({'message': 'Task not found'}), 404

@views.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    task = create_task(data['title'])
    return jsonify(task.to_dict()), 201

@views.route('/tasks/<int:id>', methods=['PUT'])
def update_task_route(id):
    data = request.get_json()
    task = update_task(id, data['title'], data['completed'])
    if task:
        return jsonify(task.to_dict())
    return jsonify({'message': 'Task not found'}), 404

@views.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task_route(id):
    task = delete_task(id)
    if task:
        return jsonify(task.to_dict())
    return jsonify({'message': 'Task not found'}), 404

from flask import Blueprint, jsonify, request
import json
import os
import yaml


BASE_DIR = os.path.abspath(os.path.dirname(__file__))

views = Blueprint('swagger_views', __name__)

@views.route('/swagger.json')
def swagger():

    with open(f'{BASE_DIR}/swagger.yaml', 'r') as yaml_file:
        yaml_dict = yaml.safe_load(yaml_file)
        return jsonify(yaml_dict)
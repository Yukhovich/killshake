from flask import request
from flask_restx import Namespace, Resource, fields
from http import HTTPStatus

namespace = Namespace('termostat_control', 'Управление системой термостатирования')


@namespace.route('')
class term2(Resource):
    '''Получить состояние системы термостатирования'''

    @namespace.response(500, 'Internal Server error')
    def get(self):
        '''Получить состояние системы термостатирования'''

        return {
            'total_records': 1
        }

    @namespace.response(400, 'Entity with the given name already exists')
    @namespace.response(500, 'Internal Server error')
    def post(self):
        '''Установить состояние системы термостатирования'''

        if request.json['name'] == 'Entity name':
            namespace.abort(400, 'Entity with the given name already exists')

        return {
            'total_records': 1
        }




@namespace.route('/peltie')
class entity(Resource):
    '''Получить состояние системы Пельтье'''

    @namespace.response(404, 'Entity not found')
    @namespace.response(500, 'Internal Server error')
    def get(self):
        '''Получить состояние системы Пельтье'''

        return {
            'total_records': 1
        }

    @namespace.response(400, 'Entity with the given name already exists')
    @namespace.response(500, 'Internal Server error')
    def post(self):
        '''Установить состояние системы Пельтье'''

        if request.json['name'] == 'Entity name':
            namespace.abort(400, 'Entity with the given name already exists')

        return {
            'total_records': 1
        }


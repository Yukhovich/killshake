from flask import request
from flask_restx import Namespace, Resource, fields
from http import HTTPStatus

namespace = Namespace('optical_control', 'Управление оптическими датчиками')


@namespace.route('')
class term2(Resource):
    '''Колличество датчиков'''

    @namespace.response(500, 'Internal Server error')
    def get(self):
        '''Колличество датчиков'''

        return {
            'total_records': 1
        }

    @namespace.response(400, 'Entity with the given name already exists')
    @namespace.response(500, 'Internal Server error')
    def post(self):
        '''Установить состояние датчика'''

        if request.json['name'] == 'Entity name':
            namespace.abort(400, 'Entity with the given name already exists')

        return {
            'total_records': 1
        }




@namespace.route('/<int:entity_id>')
class entity(Resource):
    '''Установить состояние мотора'''

    @namespace.response(404, 'Entity not found')
    @namespace.response(500, 'Internal Server error')
    def get(self, entity_id):
        '''Получить состояние датчика'''

        return {
            'total_records': 1
        }




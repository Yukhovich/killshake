from flask import request
from flask_restx import Namespace, Resource, fields
from http import HTTPStatus

namespace = Namespace('control', 'Управление системы контрольных датчиков')


@namespace.route('')
class term(Resource):
    '''Колличество датчиков'''

    @namespace.response(500, 'Internal Server error')
    def get(self):
        '''Колличество датчиков'''

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




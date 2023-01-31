from flask import request
from flask import current_app as app
from flask_restx import Namespace, Resource, fields
from http import HTTPStatus
from killshake.modbus.modbushelper import ModbusHelper

namespace = Namespace('engine', 'Управление моторами')


@namespace.route('')
class ent(Resource):
    '''Управление моторами'''

    @namespace.response(500, 'Internal Server error')
    def get(self):
        '''Колличество моторов'''
        app.logger.info('[BEGIN] получение кол-во моторов')
        modbushelper = ModbusHelper()
        count = modbushelper.getCount()
        app.logger.info('[  END] получение кол-во моторов: %s', count)

        return {
            'total_records': 1
        }

    @namespace.response(400, 'Entity with the given name already exists')
    @namespace.response(500, 'Internal Server error')
    def post(self):
        '''Установить состояние мотора'''
        modbushelper = ModbusHelper()

        if request.json['name'] == 'Entity name':
            namespace.abort(400, 'Entity with the given name already exists')

        return {
            'total_records': 1
        }


@namespace.route('/<int:entity_id>')
class engine(Resource):
    '''Установить состояние мотора'''

    @namespace.response(404, 'Entity not found')
    @namespace.response(500, 'Internal Server error')
    def get(self, entity_id):
        '''Установить состояние мотора'''

        return {
            'total_records': 1
        }



from flask import request
from flask import current_app as app
from flask_restx import Namespace, Resource, fields
from http import HTTPStatus
from killshake.modbus.modbushelper import ModbusHelper

namespace = Namespace('modbushelper', 'Чтение регистров')

register_model = namespace.model('Entity', {
    'register_no': fields.String(
        required=True,
        description='номер регистра'
    ),
    'value': fields.String(
        required=True,
        description='значение'
    )
})

modbushelper = ModbusHelper()

@namespace.route('')
class modbusPost(Resource):

    @namespace.response(400, 'Entity with the given name already exists')
    @namespace.response(500, 'Internal Server error')
    @namespace.expect(register_model)
    @namespace.marshal_with(register_model, code=HTTPStatus.CREATED)
    def post(self):
        '''Установка значения для регистра'''

        reg_no = 0
        value = 0
        try:
            tmp_register_no = '0x' + request.json['register_no']
            tmp_value = '0x' + request.json['value']
            reg_no = int(tmp_register_no, 16)
            value = int(tmp_value, 16)
            app.logger.info('[BEGIN]  установка регистра %s значением %s', hex(reg_no), hex(value))
        except ValueError:
            app.logger.error('[ERROR]  установка регистра %s', register_no)
            namespace.abort(400, 'ERROR PARSING')


        return  {
            'register_no' : hex(reg_no),
            'value' : hex(modbushelper.setRegisterValue(reg_no, value))
        }

@namespace.route('/<register_no>')
class modbusGet(Resource):
    '''Чтение регистра'''

    @namespace.response(404, 'Entity not found')
    @namespace.response(500, 'Internal Server error')
    def get(self, register_no):
        '''Чтение регистра'''

        reg_no = 0
        try:
            tmp_register_no = '0x' + register_no
            reg_no = int(tmp_register_no, 16)
            app.logger.info('[BEGIN]  чтение регистра %s', hex(reg_no))
        except ValueError:
            app.logger.error('[ERROR]  чтение регистра %s', register_no)
            namespace.abort(400, 'ERROR PARSING')

        return {
            'register' : hex(reg_no),
            'value': hex(modbushelper.getRegisterValue(reg_no))
        }

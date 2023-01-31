from flask import request
from flask import current_app as app
from flask_restx import Namespace, Resource, fields
from http import HTTPStatus
import requests
import json

namespace = Namespace('entities', 'Entities fake endpoints')

entity_model = namespace.model('Entity', {
    'id': fields.Integer(
        readonly=True,
        description='Entity identifier'
    ),
    'name': fields.String(
        required=True,
        description='Entity name'
    )
})

@namespace.route('')
class entities2(Resource):
    '''Get entity'''

    @namespace.response(500, 'Internal Server error')
    @namespace.marshal_list_with(entity_model)
    def get(self):
        '''Тест'''
        entity_id = '2'
        app.logger.info('[REST - BEGIN] получение записи по id : %s', entity_id)
        r = requests.get('http://localhost:4000/documented_api/entities/' + entity_id)
        app.logger.info('[REST -   END] получение записи по id : %s', entity_id)
        return json.loads(r.content)

from flask import request
from flask import current_app as app
from flask_restx import Namespace, Resource, fields
from http import HTTPStatus
import logging

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

entity_list_model = namespace.model('EntityList', {
    'entities': fields.Nested(
        entity_model,
        description='List of entities',
        as_list=True
    ),
    'total_records': fields.Integer(
        description='Total number of entities',
    ),
})

entity_example = {'id': 1, 'name': 'Entity name'}
entity_list = [entity_example]

@namespace.route('')
class entities(Resource):
    '''Get entities list and create new entities'''

    @namespace.response(500, 'Internal Server error')
    @namespace.marshal_list_with(entity_list_model)
    def get(self):
        '''List with all the entities'''
        
        return {
            'entities': entity_list,
            'total_records': len(entity_list)
        }

    @namespace.response(400, 'Entity with the given name already exists')
    @namespace.response(500, 'Internal Server error')
    @namespace.expect(entity_model)
    @namespace.marshal_with(entity_model, code=HTTPStatus.CREATED)
    def post(self):
        '''Добавление новой записи'''

        if request.json['name'] == 'Entity name':
            namespace.abort(400, 'Entity with the given name already exists')

        new_entity_example = {'id': len(entity_list)+1, 'name': request.json['name']}
        entity_list.append(new_entity_example)


        return new_entity_example, 201


@namespace.route('/<int:entity_id>')
class entity(Resource):
    '''Read, update and delete a specific entity'''

    @namespace.response(404, 'Entity not found')
    @namespace.response(500, 'Internal Server error')
    @namespace.marshal_with(entity_model)
    def get(self, entity_id):
        '''Получение записи по ID'''

        try:
            app.logger.info('получение записи по id : %s', entity_id)
            result = next(item for item in entity_list if item['id'] == entity_id)
        except StopIteration:
            app.logger.info('Запись с id : %s не найдена', entity_id)
            namespace.abort(404, 'Entity not found')

        return result

    @namespace.response(400, 'Entity with the given name already exists')
    @namespace.response(404, 'Entity not found')
    @namespace.response(500, 'Internal Server error')
    @namespace.expect(entity_model, validate=True)
    @namespace.marshal_with(entity_model)
    def put(self, entity_id):
        '''Update entity information'''

        if request.json['name'] == 'Entity name':
            namespace.abort(400, 'Entity with the given name already exists')

        return entity_example

    @namespace.response(204, 'Request Success (No Content)')
    @namespace.response(404, 'Entity not found')
    @namespace.response(500, 'Internal Server error')
    def delete(self, entity_id):
        '''Delete a specific entity'''

        return '', 204

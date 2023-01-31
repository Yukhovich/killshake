from flask import Blueprint
from flask_restx import Api
from killshake.documented_endpoints.entities import namespace as entities_ns

blueprint = Blueprint('documented_api', __name__, url_prefix='/documented_api')

api_extension = Api(
    blueprint,
    title='KillShake REST-Database',
    version='1.0',
    description='',
    doc='/doc'
)

api_extension.add_namespace(entities_ns)

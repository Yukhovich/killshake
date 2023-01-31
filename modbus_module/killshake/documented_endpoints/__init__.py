from flask import Blueprint
from flask_restx import Api
from killshake.documented_endpoints.ent import namespace as ent_ns
from killshake.documented_endpoints.modbus import namespace as modbus_ns
from killshake.documented_endpoints.term import namespace as term_ns
from killshake.documented_endpoints.term2 import namespace as term2_ns
from killshake.documented_endpoints.term3 import namespace as term3_ns

blueprint = Blueprint('documented_api', __name__, url_prefix='/documented_api')

api_extension = Api(
    blueprint,
    title='KillShake REST-MODBUS',
    version='1.0',
    description='',
    doc='/doc'
)

api_extension.add_namespace(modbus_ns)
api_extension.add_namespace(ent_ns)
api_extension.add_namespace(term_ns)
api_extension.add_namespace(term2_ns)
api_extension.add_namespace(term3_ns)

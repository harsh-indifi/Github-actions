import json

from flask.views import MethodView
from flask import jsonify
from computation.calculation import Calculation
from computation.operations import Operations
from computation.utils import MyEncoder
from db_manager.query_manager.columns import APPLICATIONS_TABLE, \
    APPLICATIONS_TABLE_COLUMNS
from db_manager.query_manager.settings import applications_data


class Test(MethodView):

    def get(self):
        return {'health': True}


class OperationView(MethodView):
    def get(self):
        operation = Operations()
        operation.create_extension()
        operation.create_table(APPLICATIONS_TABLE, APPLICATIONS_TABLE_COLUMNS)
        operation.insert_into_table(APPLICATIONS_TABLE, applications_data)
        result = operation.fetch()
        operation.drop_table(APPLICATIONS_TABLE)
        operation.close_connection()
        return jsonify({'success': True, 'requestId': result[0]['requestId']})


class CalculationView(MethodView):

    def get(self):
        result = Calculation().add(9, 10)
        response_obj = {'result': result, 'success': True}
        response = json.loads(json.dumps(response_obj, cls=MyEncoder),
                              parse_float=lambda x: round(float(x), 4))
        return jsonify(response)

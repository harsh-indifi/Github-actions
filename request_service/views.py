import json
import pickle

from flask.views import MethodView
from flask import jsonify
from computation.calculation import Calculation
from computation.operations import Operations
from computation.utils import MyEncoder
from db_manager.query_manager.columns import APPLICATIONS_TABLE, \
    APPLICATIONS_TABLE_COLUMNS
from db_manager.query_manager.settings import applications_data
from extensions import cache


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
        key_name = "check"
        if cache.get(key_name) is None:
            result = Calculation().add(5, 10)
            pickled_object = pickle.dumps(result)
            cache.set(key_name, pickled_object, timeout=1728000)
        else:
            result = pickle.loads(cache.get(key_name))
        response_obj = {'result': result, 'success': True}
        response = json.loads(json.dumps(response_obj, cls=MyEncoder),
                              parse_float=lambda x: round(float(x), 4))
        return jsonify(response)

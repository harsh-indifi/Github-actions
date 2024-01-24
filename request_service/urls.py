from flask import Blueprint
from request_service.views import Test, CalculationView


ChildBP = Blueprint('child', __name__)

ChildBP.add_url_rule('/test', view_func=Test.as_view('test'))
ChildBP.add_url_rule('/calculation', view_func=CalculationView.as_view('calculation'))


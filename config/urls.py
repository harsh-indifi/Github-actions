from flask import Blueprint
from request_service.urls import ChildBP
from request_service.views import OperationView

MainBP = Blueprint('main', __name__)
MainBP.register_blueprint(ChildBP, url_prefix='/v1')
MainBP.add_url_rule('/operation', view_func=OperationView.as_view('operation'))

#hello this is harsh



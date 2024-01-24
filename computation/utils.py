import json
import math
import decimal
import datetime
import pandas as pd
import numpy as np

from uuid import UUID


class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        elif isinstance(obj, np.bool_):
            return bool(obj)
        elif isinstance(obj, UUID):
            return obj.__str__()
        elif isinstance(obj, datetime.datetime):
            return obj.__str__()
        elif isinstance(obj, datetime.date):
            return obj.__str__()
        elif isinstance(obj, pd.Series):
            return obj.to_dict()
        elif isinstance(obj, decimal.Decimal):
            return float(obj)
        else:
            return super(MyEncoder, self).default(obj)


def nan_to_none_dict(obj):
    """
    Function to convert NaN to None in a dictionary/list and rounding to 2 precision
    :param: obj
    :return:
    """
    for k, v in obj.items() if isinstance(obj, dict) else enumerate(obj):
        if isinstance(v, float) and math.isnan(v):
            obj[k] = None
        elif isinstance(v, (dict, list)):
            nan_to_none_dict(v)
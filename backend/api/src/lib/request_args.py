import types

from werkzeug.datastructures import ImmutableDict

def _filter_query_args(immutable_args, model):
    query_args=immutable_args.copy()
    CALLABLES = types.FunctionType, types.MethodType
    INVALID_FIELD_NAMES=['DoesNotExist', 'MultipleObjectsReturned']
    valid_keys=[key for key, value in model.__dict__.items() if not isinstance(value, CALLABLES) and "_" not in key and key not in INVALID_FIELD_NAMES]

    for key in immutable_args.keys():
        if key not in valid_keys:
            del query_args[key]

    return  query_args

class RequestArgs():
    def __new__(self, args: ImmutableDict, model) -> dict:
        return _filter_query_args(args, model)

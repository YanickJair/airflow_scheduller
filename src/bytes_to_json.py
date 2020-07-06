import json
from src.extract_column_from_sql import get_columns

def bytes_to_json(bytes_in: bytes) -> json:
    _json = bytes_in.decode('utf8').replace("\'", "\"")
    data = json.loads(_json)
    return data
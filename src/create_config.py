from src.bytes_to_json import bytes_to_json
from src.extract_column_from_sql import get_columns

from src.database import db_session
from src.models import DagRunConfig

def create_configuration(args):
    try:
        data = bytes_to_json(args)
        columns = get_columns(data["sql_query"])
        config = DagRunConfig(
            dag_id=int(data["dag_id"]),
            sql_query=data["sql_query"],
            db_connector=data["db_connector"],
            filename=data["filename"],
            columns=columns
        )
        
        db_session.add(config)
        db_session.commit()
        return {
            "status": True,
            "code": 200,
            "message": "Configuration successfully created"
        }
    except:
        raise
    return {
        "status": False,
        "code": 500,
        "message": "Configuration not created"
    }

def prepare_insert_query(dag_id: str, config) -> str:
    query = """
        INSERT INTO dag_configs(dag_id, config) VALUES({0}, '{1}');
    """.format(dag_id, config)
    return query
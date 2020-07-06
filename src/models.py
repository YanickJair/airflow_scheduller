from sqlalchemy import Column, Integer, String, Text, ARRAY
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import synonym

from src.database import Base

class DagRunConfig(Base):
    __tablename__ = 'dag_run_config'

    id = Column(Integer, primary_key=True)
    dag_id = Column(Integer, nullable=False, unique=True)
    sql_query = Column(Text(), nullable=True)
    _columns = Column(ARRAY(String(120)), nullable=True)
    db_connector = Column(String(80), nullable=True)
    filename = Column(String(80), nullable=True)

    def __init__(self, dag_id, sql_query, columns, db_connector, filename):
        self.dag_id = dag_id
        self.sql_query = sql_query
        self.columns = columns
        self.db_connector = db_connector
        self.filename = filename

    def __repr__(self):
        return '<Dag Run Config %r>' % (self.dag_id)

    def get_columns(self):
        return self._columns

    def set_columns(self, columns):
        if self._columns != columns:
            self._columns = columns
    
    @declared_attr
    def columns(self):
        return synonym('_columns', descriptor=property(self.get_columns, self.set_columns))

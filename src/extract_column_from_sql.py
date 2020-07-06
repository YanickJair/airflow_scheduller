import sql_metadata

TABLE_USER_COLUMNS = [
    "id", "first_name", "last_name", "avatar", "status", "joined_at", "email"
]

TABLE_STORE_COLUMNS = [
    "id", "name", "latitude", "longitude", "status", "address_name"
]

def get_columns(sql_query: str) -> list:
    if sql_query is not None:
        tables: list = sql_metadata.get_query_tables(sql_query)
        columns: list = sql_metadata.get_query_columns(sql_query)

        if len(columns) == 1:
            #* Return all columns
            if len(columns) == 1 and columns[0] == '*':
                if tables[0] == 'public.store':
                    columns = TABLE_STORE_COLUMNS
                else:
                    columns = TABLE_USER_COLUMNS
        return columns
        
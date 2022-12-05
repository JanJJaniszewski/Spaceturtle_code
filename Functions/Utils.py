from sqlalchemy import create_engine

import Config.config_main as cm
import Config.secrets as ss


def sql_connect():
    """
    Connects to SQL database
    :return: SQL database connection
    """
    engine = create_engine(f"mssql+pymssql://{cm.username}:{ss.password}@{cm.server}:1433/{cm.database}")
    conn = engine.connect()

    return conn
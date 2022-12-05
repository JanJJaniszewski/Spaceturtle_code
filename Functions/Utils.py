from xml.etree import ElementTree
import csv
import pandas as pd
import re
from sqlalchemy import create_engine
import pymssql


def sql_connect():
    """
    Connects to SQL database
    :return: SQL database connection
    """
    engine = create_engine("mssql+pymssql://spaceturtle:abKhzQip1|-l@spaceturtle.database.windows.net:1433/spaceturtle")
    conn = engine.connect()

    return conn
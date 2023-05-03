import os

from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker

from pyrelated.orm.base import Base


def test_dev():
    path_db = os.path.expanduser("~/.pyrelated/tmp.sqlite")
    if not os.path.exists(os.path.dirname(path_db)):
        os.makedirs(os.path.dirname(path_db))
    url_database = URL.create(drivername="sqlite", database=path_db)
    engine = create_engine(url_database)
    Base.metadata.create_all(bind=engine)
    sessionmaker(bind=engine)

from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

from pyrelated.orm.base import Base
from pyrelated.orm.publication import Publication


def test_construct_engine():
    engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)
    Base.metadata.create_all(bind=engine)

    pub1 = Publication()
    pub1.id = "1234"
    pub1.year = 2023
    pub1.title = "PyRelated: manage your bibliography"
    print("foo", pub1.arxiv_versions)

    with Session(engine) as session:
        session.add(pub1)
        session.flush()

        stmt = text("SELECT * FROM publications")
        result = session.execute(stmt)
        for ix, row in enumerate(result):
            print(f"{ix}, {row}")

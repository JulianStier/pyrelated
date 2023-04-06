from pyrelated.database import BibtexDatabase


def test_construct(tmp_path):
    db = BibtexDatabase(tmp_path)
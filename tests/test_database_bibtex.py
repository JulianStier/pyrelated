from pyrelated.database import BibtexDatabase


def test_construct(tmp_path):
    BibtexDatabase(tmp_path)

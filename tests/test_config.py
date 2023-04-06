import os

from pyrelated.config import Config, Cfg, flatten, old_flatten


def test_flatten():
    d1 = { "a": 5, "b": 3, "c": { "d": 8, "e": 4, "f": { "g": 1 } } }
    prefix_exp = {"foo": { "a": 5, "b": 3 }, "foo.c": { "d": 8, "e": 4 }, "foo.c.f": { "g": 1 } }
    noprefix_exp = { "a": 5, "b": 3, "c": { "d": 8, "e": 4 }, "c.f": { "g": 1 } }

    r_prefix = flatten(d1, prefix="foo")
    r_noprefix = flatten(d1)
    assert r_prefix == prefix_exp
    assert r_noprefix == noprefix_exp


def test_old_flatten():
    d1 = { "a": 5, "b": 3, "c": { "d": 8, "e": 4, "f": { "g": 1 } } }
    exp = { "a": 5, "b": 3, "c.d": 8, "c.e": 4, "c.f.g": 1}

    r1 = old_flatten(d1)
    assert r1 == exp


def test_default_config():
    cfg = Config()
    cfg.load_default()
    assert cfg.get(Cfg.NAMES_FILES_CONFIG) is not None


def test_save_default(tmp_path):
    path_file_config = os.path.join(tmp_path, "tmp-config.toml")
    cfg = Config()
    cfg.load_default()
    cfg.save(path_file_config)

    reloaded = Config()
    reloaded.load(path_file_config)
    for key in reloaded.keys():
        assert reloaded.get(key) == cfg.get(key)


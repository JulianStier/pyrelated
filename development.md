# Roadmap

**New Features**
- [ ]



# Practices & Conventions

## Publishing
```bash
poetry build
twine upload dist/*
```
- Create wheel files in *dist/*: ``poetry build``
- Install wheel in current environment with pip: ``pip install path/to/pyrelated/dist/pyrelated-0.1.0-py3-none-any.whl``


## Running github action locally
Install *https://github.com/nektos/act*.
Run ``act``


## Running pre-commit checks locally
- Execute pre-commit manually: ``poetry run pre-commit run --all-files``
- Update pre-commit: ``poetry run pre-commit autoupdate``
- Add pre-commit to your local git: ``poetry run pre-commit install``

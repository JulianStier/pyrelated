# pyrelated
With *pyrelated* you can search for related bibliography, persist and edit bibtex files and annotate them with custom taxonomy.
You can
- merge and manage bibtex entries in custom file paths
- create awesome lists with yaml and bibtex and use pyrelated to manage it
- search through and categorize your local bibtex files

**NOTE** this project is currently under development

**Install:**
- ``poetry add pyrelated``
- ``pip install pyrelated``


# Examples

## Application
**Loading**
- From bibtex ``pyrelated import publications.bib``
- From yaml ``pyrelated import backup.yaml``

**Writing**
- ``pyrelated export project-xyz publications.bib``
- ``pyrelated export project-xyz backup.yaml``

**Local DB**
- ``pyrelated context list``
- ``pyrelated context add project-xyz``
- ``pyrelated context delete projex-xyz``
- ``pyrelated stats``

**Searching**
- ``pyrelated search "Albert Einstein"`` - outputs results from the default search and caches locally
- ``pyrelated search --arxiv "1904.08166"`` - search arxiv with e.g. an arxiv identifier
- ``pyrelated search --semanticscholar "Alan M. Turing"``
- ``pyrelated search --scholarly "Albert Einstein"``
- ``pyrelated add "Albert Einstein"`` - search for bibtex entries with scholarly and add to your managed database interactively

**Configuration** of *pyrelated*
- ``pyrelated --db ./data``
- ``pyrelated config`` Show local config keys
- ``pyrelated config cache /home/name/.cache/pyrelated/`` Set another home cache folder for the current dir in *.pyrelated*


## Python API
```
import pyrelated

dbproxy = pyrelated.DatabaseProxy("./data")
db_yaml = dbproxy.use("yaml")
db_bibtex = dbproxy.use("bibtex")
db_yaml.last_modification
db_yaml.print_meta()
```

# Development
- Optional local config file for overwrites *./.pyrelated*
- Default global config directory *~/.config/pyrelated/*
- Default global config file name *.pyrelated*
- Default cache directory *~/.cache/pyrelated/*
- Default proxy config file name *pyrelated.toml*

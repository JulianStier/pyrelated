# pyrelated
Create awesome lists with yaml and bibtex and use pyrelated to manage it.


**Install:**
- ``poetry add pyrelated``
- ``pip install pyrelated``


# Examples
**Interface**
- ``pyrelated search "Albert Einstein"`` - outputs results from a scholarly search and caches locally
- ``pyrelated search --scholarly "Albert Einstein"``
- ``pyrelated add "Albert Einstein"`` - search for bibtex entries with scholarly and add to your managed database interactively
- ``pyrelated --db ./data``
- ``pyrelated config`` Show local config keys
- ``pyrelated config cache /home/name/.cache/pyrelated/`` Set another home cache folder for the current dir in *.pyrelated*

**API**
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


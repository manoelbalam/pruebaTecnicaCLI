# Prueba técnica - Desarrollador Python - Componente 2
###  Client line interface created with click

## Installation
After clone repo.
```sh
$ cd into..
$ python3 -m venv env
$ source env/bin/activate
(env) $ pip install -r requirements.txt
(env) $ python cli.py
```
## Usage
```sh
(env) $ python cli.py --help
Usage: cli.py [OPTIONS]

Options:
  -b, --backend TEXT             Backend address ex. localhost:8000 [required]
  -e, --endpoint [signup|login]  [required]
  -u, --useraccess TEXT          UserAccess
  -p, --passaccess TEXT          PassAccess
  -d, --date TEXT                date format YYYY-MM-DD [optional]
  --help                         Show this message and exit.
```

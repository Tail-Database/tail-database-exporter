# Tail Database Exporter

Python script that exports data from Tail Database on DataLayer using [tail-database-api](https://github.com/Tail-Database/tail-database-api).

Data is exported as JSON and a seperate process uploads it to a web server so [taildatabase.com](https://www.taildatabase.com/) can operate as a static site without running a full node in the cloud.

## How to run

### Install dependencies

```bash
python3 -m venv venv
. ./venv/bin/activate
python3 setup.py install
```

### Run the script

The default configuration assumes that [tail-database-api](https://github.com/Tail-Database/tail-database-api) is running locally.

```bash
python3 start.py
```

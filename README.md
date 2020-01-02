# AIDO

AIDO (Ideo) is an AI that helps you mange your schedules.

## Installation
```bash
$ pip install -r requirements.txt
```

## Run
You need to config your `ipconfig.yaml` file first and put the following line in the file. You can refer to `ipconfig-template.yaml` for more details.
```yaml
host: your.host.ip
```

Then you can run the Django server via
```bash
$ python manage.py runserver 0.0.0.0:8000
```

Finally, open a browser and type `http://127.0.0.1:8000/` to use your AIDO. Enjoy~
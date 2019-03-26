# poc

# Installation Instruction

- For installing all the required dependencies, execute following command:

```bash
pip install poc/requirements.txt
```

```bash
python poc/manage.py makemigrations
python poc/manage.py migrate
python poc/manage.py runserver
```

- If all the above commands run without any errors, visit `127.0.0.1` in your browser to view the GUI

- To be able to access the database execute following commands:

```bash
python poc/manage.py createsuperuser
# follow the prompts and then run:
python poc/manage.py runserver
```

- Then visit `127.0.0.1/admin` in your browser and click on TrendTable. For the latest entry refer the first record

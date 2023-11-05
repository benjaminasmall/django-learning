###Create the random key

- *create the virtual environment using the following command*
`
pip install virtualenv
virtualenv -p python3 venv
source activate venv/bin/activate
`

- *create a virtual environment and install the packages into it using the following command*
`pip install -r requirements.txt`

- *create a file `.env` and add the content of the `.env.sample` into it but with values you want to use
typically for local testing you would want to use the following settings*
`
SECRET_KEY=ANY_RANDOM_STRING_WILL_DO
DEBUG=True
ALLOWED_HOSTS=*
`

- *Alternatively to populate you could use SECRET_KEY using the following lines of code via running from commandline, which can be activated using `python manage.py shell`*

`from parser_app.utils import generate_secret_key
generate_secret_key()`

- *Run the following command to run the migrations*
`python manage.py migrate`

- *To run the parser, use the following commands*
`
python manage.py parser A.uff --sqlite
python manage.py parser A.uff --csv output.csv
`

- *To create a user use the following command, & fill in the other prompt*
`python manage.py createsuperuser`


- Final Notes
The SQL side of things are not catering duplication, if you re run the same command more than once, duplicates will be created, unless we add a constraint on the table Parser
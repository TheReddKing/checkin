# checkin

hackMIT checkin

[V 0.1] complete. This code is now usable
[Documentation] in progress

# Contributing

## Set up on local environment:

Requirements:

- npm v11.6.0 \* yarn
- python 3.6+

1. first create a python env wrapper `python -m venv env`
2. activate env wrapper `source env/source/activate`
3. run `pip install -r requirements.txt`
4. rename `example.config.py` to `config.py` and adjust settings
5. create a postgres database that matches your config file (more in SERVERSETUP.md)
6. Run `python manage.py db init`
7. Run `python manage.py db migrate`
8. Run `python manage.py db upgrade`
9. cd into `client`
10. run `yarn install`

optional:

0. Setup your admin username password combo in `start_script.py`
1. Run `python start_script.py 0` to create an admin user!

### Running

1. activate env wrapper `source env/source/activate`
2. run server `python run_server.py`
3. in another terminal window cd into `client`
4. run `yarn start`
5. open your browser to http://localhost:3000

You should have two processes running (backend and front end)

You're all set! Now it's time to use the online interface!
(But you can just mess around with start_script as well)

# Other Documents

AWSEC2_SERVERSETUP.md - Setting up on an EC2 Instance on AWS

Created by: TheReddKing

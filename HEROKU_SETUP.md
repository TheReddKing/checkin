## Set up on heroku

Last updated: 8/21/2019 by Kevin Fang

This assumes you have already gotten a running instance on localhost.
Create your `.env.prod` file!

After creating your heroku instance and adding it to the git repo (`heroku git:remote -a [herokuboxname]`)
Then run the following lines of code

```
heroku addons:create heroku-postgresql:hobby-dev
heroku buildpacks:add heroku/nodejs
heroku buildpacks:add heroku/python
sed 's/#[^("|'')]*$//;s/^#.*$//' .env.prod | \
xargs heroku config:set
```

Now you are set to launch your instance!

```
git push heroku master
```

Now we need to provision your database! -- Everytime you build this will destroy your db migration information. Therefore, don't expect to change your database :( _TODO(kevinfang)_
First `heroku run bash` to enter the heroku server

```
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
python start_script.py
```

This should finish setting up your entire server
Finally restart the server to update the SQL Database
`heroku restart`

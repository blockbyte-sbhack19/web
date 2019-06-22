# LendIt prototype using Django

Deprecated in favor of Flutter, see https://github.com/blockbyte-sbhack19/frontend


### HOW to run
`python manage.py migrate`     # create database

`python manage.py makemigrations`   # if you change anything in models.py

`python manage.py runserver`    # run app

# User area
Visit http://127.0.0.1:8000/

# Admin area
Visit http://127.0.0.1:8000/admin    
* login: admin 
* email: admin@admin.com 
* password: admin

### add a new app
`python manage.py startapp release`


### deploy to AWS

`ssh -i "blockbyte.pem" ubuntu@ec2-34-254-224-164.eu-west-1.compute.amazonaws.com`
`cd web`
`git pull`
`python manage.py makemigrations`
`python manage.py runserver`

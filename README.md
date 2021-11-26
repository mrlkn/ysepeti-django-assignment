### Note from dev:

__Normally I started this project with Flask, Pydantic and SQL Alchemy. I was writing all the SQL queries, validations, serializations and more yet it didn't finish in time of course and even with the extra time it was not going to finish, so I started a Django app the day before sending the assingment and developed this one. 
Because of this sitaution, I finished django project in very short time so it lacks tests unfortunately.. I am planning to add them at this weekend cause I hate code without test.__


# Yemeksepeti Assingment

Made with using Django, Python and fully dockerized. 

## How to run
```
docker-compose up --build
```
 *keep in mind that I didn't add any env variables and currently set to use `0.0.0.0` 
 as local host and `8000` as port.*
 
*If you need to change it you can find the settings in 
 build/bootstrap.sh dont forget to expose it in dockerfile*
 
 To attach the container
 ```
 docker exec -it $container_id bash
 ```
 
## API Docs
Application has [Swagger](https://swagger.io/) documentation, auto generated with Django Rest Framework Schemas

It can be found in the swagger.yaml

## Flake8
Application is flake8 compliant. I use [wemake-python-styleguide](https://wemake-python-stylegui.de/en/latest/) and violations can be found [here](https://wemake-python-stylegui.de/en/latest/pages/usage/violations/index.html)

After attaching to the docker container you can check it with `flake8` and configuration can be found in 
`app/.flake8`

## Mypy
Application is [mypy](http://mypy-lang.org/). compliant and has type hinting for all methods.

Configuration can be found in `app/mypy.ini`

Again after attaching to the docker container you can check it with `mypy .`

## Tests
WIP

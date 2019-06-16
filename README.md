## Backend Tickets

Para correr la aplicacion:

```
$ docker-compose up -d
```

Para ejecutar las migraciones:

```
$ docker-compose run web python manage.py migrate
```

Para crear un superusuario e ingresar al admin de django:

```
$ docker-compose run web python manage.py createsuperuser
```




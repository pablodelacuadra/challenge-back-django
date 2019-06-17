## Backend Tickets

1. Construir la imagen docker:

```
$ docker-compose build
```

2. Ejecutar las migraciones:

```
$ docker-compose run web python manage.py migrate
```

3. Para correr la aplicacion:

```
$ docker-compose up -d
```

4. Para crear un superusuario e ingresar al admin de django(opcional):

```
$ docker-compose run web python manage.py createsuperuser
```




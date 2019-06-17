## Backend Tickets

1. Construir la imagen docker:

```
$ docker-compose build
```

2. Ejecutar las migraciones:

```
$ docker-compose run web python manage.py migrate
```

3. Correr la aplicacion:

```
$ docker-compose up -d
```

4.  Crear un superusuario e ingresar al admin de django:

```
$ docker-compose run web python manage.py createsuperuser
```

4.  Crear permiso en administradoe de django:

$ En el modelo permission crear permiso **crear tickets**




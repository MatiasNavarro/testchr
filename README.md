# README
Este repositorio contiene dos aplicaciones de Django: "testapp" y "sea", las cuales obtienen información de dos fuentes diferentes y las almacenan en una base de datos PostgreSQL.

## Requisitos
- Python 3
- PostgreSQL

## Instalación
1. Clonar el repositorio
2. Crear un ambiente virtual
    ```bash
        $ python -m venv env
    ```
3. Activar el ambiente virtual con
    ```
        $ .\env\Scripts\activate
    ```
    en Windows o `source env/bin/activate` en Mac/Linux.
4. Instalar las dependencias con 
    ```bash
        $ pip install -r requirements.txt
    ```

5. Crear una base de datos en PostgreSQL
6. Configurar la conexión a la base de datos en testchr/settings.py
7. Realizar las migraciones: python manage.py makemigrations y python manage.py migrate
8.  Crear un superusuario: python manage.py createsuperuser
9.  Iniciar el servidor: python manage.py runserver

## Tarea 1: testapp
La tarea 1 consiste en obtener información de una API y mostrarla en una tabla en la página web. Para ello, se siguieron los siguientes pasos:
1. Crear la app testapp: 
    ```
        $ python manage.py startapp testapp
    ```
2. Agregar la app `testapp` en el archivo `settings.py` -> `INSTALLED_APPS`.
3. Definir el modelo correspondiente para los datos obtenidos de la API.
4. Crear el archivo `urls.py` y las carpetas `templates/testapp` que contiene los HTML de las vistas.
5. Generar los métodos necesarios en `views.py`:
   * `bike_info`: obtiene la información de la API.
   * `update_bike_stations`: obtiene la información y la guarda en la base de datos.
   * `show_bike_stations`: muestra los datos en una tabla desde la base de datos con ayuda de Bootstrap para una mejor visualización.
6. Crear el panel de administración para poder visualizar el modelo desde el panel de administración de Django.
7. Cear el superusuario para acceder al admin de Django con `$ python manage.py createsuperuser`.
8. Crear una base de datos en PostgreSQL.
9. Configurar la conexión a la base de datos en testchr/settings.py
10. Realizar las migraciones: `$ python manage.py makemigrations` y `$ python manage.py migrate`
11. Poner en marcha el servidor con el comando: 
    ```
        $ python manage.py runserver
    ``` 
12. Desde el navegador, acceder a los diferentes endpoints de manera local:
    * http://127.0.0.1:8000/testapp/bike-info/
    * http://127.0.0.1:8000/testapp/update-bike-stations/
    * http://127.0.0.1:8000/testapp/show-bike-stations/ 
13. Comprobar si se generaron los datos correctamente, también se puede verificar desde PostgreSQL o el mismo panel de administración de Django.


## Tarea 2: sea
Esta aplicación obtiene información de una tabla de un sitio web y la almacena en la base de datos. Para ello, se siguieron los siguientes pasos:

1. Crear la app sea:
    ```
    $ python manage.py startapp sea
    ```
2. Agregar la app sea en el archivo settings.py -> INSTALLED_APPS.
3. Definir el modelo correspondiente para los datos obtenidos de la tabla de la URL especificada.
4. Crear el archivo urls.py y las carpetas templates/sea que contiene los HTML de las vistas. 
5. Se utilizó BeautifulSoup para obtener los datos de la página web.
6. Generar 2 métodos en views.py:
   * `get_data_from_sea`: obtiene la info y la guarda en DB (cabe destacar que por problemas de timing se puso un limite a las primeras 10 paginas, si bien se obtiene el numero total de paginas el bucle que las recorre tiene un limite que el mismo se puede modificar para trae mas o menos datos).
   * `show_sea_projects`: muestra los datos en una tabla desde la DB con ayuda de bootstrap para mejor visualizacion.
7. Se creó el admin para poder visualizar el modelo desde el admin de Django. 
8. Se crearon y realizaron las migraciones con el comando `$ python manage.py makemigrations` y `$ python manage.py migrate`.
9. Por último, se puso en marcha el servidor con el comando 
    ```
        $ python manage.py runserver
    ``` 
    Desde el navegador se accede a los diferentes endpoints de manera local (localhost):
   * http://127.0.0.1:8000/sea/get-data-from-sea/
   * http://127.0.0.1:8000/sea/show-sea-projects/
10. Se puede comprobar si se generaron los datos correctamente a través del último enlace, o bien se puede verificar desde PostgreSQL o el mismo admin de Django.

### Django Admin 
Para acceder al Admin de Django se puede acceder a: http://127.0.0.1:8000/admin/ con el usuario y contraseñas generado con el comando `$ python manage.py createsuperuser`

## Ejecución 
1. Clonar el repositorio
2. Crear un ambiente virtual con `py -m venv env`
3. Activar el ambiente virtual con `.\env\Scripts\activate` en Windows o `source env/bin/activate` en Mac/Linux.
4. Instalar las dependencias con `pip install -r requirements.txt`
5. Configurar las credenciales de PostgresSQL en el archivo `testchr/settings.py` -> `DATABASES`
6. Realizar las migraciones: `$ python manage.py makemigrations` y `$ python manage.py migrate`
7. Crear un superusuario: `$ python manage.py createsuperuser`
8.  Correr el servidor local con `python manage.py runserver`

* Las diferentes URL's disponibles son:
  * Tarea 1: testapp
    * http://127.0.0.1:8000/testapp/bike-info/
    * http://127.0.0.1:8000/testapp/update-bike-stations/
    * http://127.0.0.1:8000/testapp/show-bike-stations/ 
  * Tarea 2: 
    * http://127.0.0.1:8000/sea/get-data-from-sea/
    * http://127.0.0.1:8000/sea/show-sea-projects/
  * Admin 
    * http://127.0.0.1:8000/admin/
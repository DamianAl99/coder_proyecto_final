# coder_proyecto_final
## El proyecto se trata de una Odontologia
### Este pagina tiene 3 secciones principales
#### *En la primera seccion se muestran los clientes de la odontologia, y tambien se muestra un formulario para agregar mas clientes en caso de ser necesario
#### *En la segunda seccion se muestran los servicios que ofrece de la odontologia, contiene tambien un formulario
#### *En la tercera seccion se muestran los servicio agendados por la odontologia, contiene tambien un formulario para agregar mas agendamientos
#### *Por ultimo tenemos el buscador en el nav/menu principal, donde podemos buscar los servicios que deseemos para saber con exactitud la info del mismo

## Para levantar el proyecto es necesario la libreria Django nada mas.
### Primer paso para tener las app a punto: python manage.py makemigrations
### Segundo paso para crear las tablas de cada app: python manage.py sqlmigrate schedules 0001
### -----------------------------------------------: python manage.py sqlmigrate services 0001
### -----------------------------------------------: python manage.py sqlmigrate employees 0001

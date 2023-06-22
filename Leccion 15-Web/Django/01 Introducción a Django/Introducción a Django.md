# Introduccióna Django


### ¿Qué es Django?


Django es un framework de Python que permite desarrollar el back-end de páginas web. Es decir, implementar la lógica que hay detrás de una página web que cuente con usuarios, bases de datos, etc. Django es un potente framewok usado por companías como Pinterest, Spotify o Instagram. 


### Creación de entorno virtual

```
mkdir djangoproject
```

```
cd djangoproject
```

```
pip install virtualenv
```

```
virtualenv venv
```

```
.\venv\Scripts\activate

.\venv\bin\activate
```

```
code .
```

```
Ctrl+shift+P 
> select interpreter
> python env:venv
```

### Instalación de Django sobre virtualenv

```
pip install django
```

```
django-admin --version
```

### Creación y ejecución del proyecto

```
django-admin startproject <nombre del proyecto> .
```

```
python manage.py runserver
```

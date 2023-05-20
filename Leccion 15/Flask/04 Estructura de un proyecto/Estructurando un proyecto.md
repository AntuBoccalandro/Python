# **Estructura de un proyecto**

Flask no tiene una estructura definida para construir un proyecto, esto hace que la estructura de una aplicación varíe mucho. 

# **Modelo Vista Controlador (MVC)**

La estructura base de una aplicación que aplique MCV (también conocido como MVT) sería la siguiente:
```bash
proyecto-flask/
├── app/
│   ├── __init__.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── usuario.py
│   │   └── ...
│   ├── controllers/
│   │   ├── __init__.py
│   │   ├── usuario_controller.py
│   │   └── ...
│   ├── views/
│   │   ├── __init__.py
│   │   ├── usuario/
│   │   │   ├── inicio.html
│   │   │   ├── registro.html
│   │   │   └── ...
│   │   └── ...
│   └── static/
│       ├── css/
│       ├── js/
│       └── img/
├── config.py
├── requirements.txt
├── run.py
└── README.md
```
El directorio "app" contiene el código fuente de la aplicación Flask.
* El archivo "init.py" es el punto de entrada de la aplicación y contiene la creación de la aplicación Flask y la configuración.
* El directorio "models" contiene los modelos de datos utilizados en la aplicación.
* El directorio "controllers" contiene los controladores que manejan las solicitudes HTTP y la lógica de la aplicación.
* El directorio "views" contiene las plantillas HTML utilizadas en la aplicación, organizadas por entidad.
* El directorio "static" contiene archivos estáticos, como hojas de estilo CSS, scripts JavaScript e imágenes utilizadas en la aplicación.

* El archivo "config.py" contiene la configuración de la aplicación, como configuraciones específicas de la base de datos o el correo electrónico.
* El archivo "requirements.txt" enumera todas las dependencias de Python necesarias para el proyecto, lo que facilita la instalación de las mismas en un nuevo entorno.
* El archivo "run.py" es el punto de entrada para ejecutar la aplicación Flask.
* El archivo "README.md" contiene información sobre el proyecto y cómo configurar y   ejecutar la aplicación.

## **Modelo Vista Controlador (MVC) mejorado**


```bash
│   .env
│   config.py
│   Notas de la estructura.txt
│   requirements.txt
│   run.py
│
└───app
    │   __init__.py
    │   __main__.py
    │
    ├───controller
    │       contacts_controller.py
    │
    ├───database
    │       connection.py
    │       contact_book.db
    │       contact_db.py
    │       security.py
    │
    ├───helpers
    │       helper.py
    │
    ├───models
    │       exceptions.py
    │       models.py
    │
    ├───routes
    │       api.py
    │       errors.py
    │       routes.py
    │       __init__.py
    │
    └───views
        ├───static
        │   ├───css
        │   │       bootstrap.min.css
        │   │       home.css
        │   │
        │   └───js
        │           bootstrap.bundle.min.js
        │
        └───templates
                home.html
                layout.html
                navigation.html
```

Esta estructura es algo más compleja pero permite una escalabilidad y tiene un diseño algo más consiso.


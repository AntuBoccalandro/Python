# **Distribución de aplicaciones**

Si se quiere distribuir alguna aplicación realizada en Python hay varias opciones, pero las que se abordarán será la de crear un archivo ejecutable, y crear contenedores de Docker.

# **Pyinstaller**

Es una utilidad que permite la creación de un archivo ejecutable que contiene tanto todas las dependencias de nuestro proyecto de Python como el propio intérprete, por lo que no hay que preocuparse por las dependencias del proyecto o como se ejecutará, ya que además incluye la posibilidad de exportar para Windows, Linux o Mac.

## **Preparar la aplicación**

En cuanto a esto respecta no es necesario una gran cantidad de acciones. Pero se deben evitar las importaciones relativas, así como también es ideal crear un archivo fuera del paquete de la aplicación llamado cli.py (el nombre no importa, pero por convención utilizaremos este). Y poco más, con esto ya estaría listo.

```bash
reader/
|
├── reader/
|   ├── __init__.py
|   ├── __main__.py
|   ├── config.cfg
|   ├── feed.py
|   └── viewer.py
|
├── cli.py
├── LICENSE
├── MANIFEST.in
├── README.md
├── setup.py
└── tests
```

En el archivo cli.py colocaremos el siguiente contenido:
```python
from reader.__main__ import main

if __name__ == '__main__':
    main()
```

## **Creación de un ejecutable**

Para ello deberemos ejecutar el siguiente comando, aunque este es personalizable.

**Crear ejecutable por defecto:**
```bash
pyinstaller cli.py
```

**Crear ejecutable con nombre personalizado:**
```bash
pyinstaller cli.py --name myApp
```

**Crear ejecutable en una sola carpeta:**
```bash
pyinstaller cli.py --onefile
```

**Crear ejecutable sin tests:**
```bash
pyinstaller cli.py --exclude-module=pytest
```

**Crear ejecutable de proyecto GUI:**
```bash
pyinstaller cli.py -w
```

# **Docker**

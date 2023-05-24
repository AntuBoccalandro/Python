# **servidores HTTP con Python**

Python incluye una funcionalidad que se puede lanzar directamente desde la línea de comandos que nos permite crear servidores HTTP. Además incluye librerías ya instaladas que nos permiten crear servidores, gestionar peticiones, etc.

# **CLI**

De forma predeterminada, Python sirve los archivos ubicados en su directorio de trabajo actual donde ejecutó el comando para iniciar el servidor. 

```python
# Servidor por defecto
python3 -m http.server # Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...

# Servidor en puerto específico
python3 -m http.server 8080 # Serving HTTP on 0.0.0.0 port 8080 (http://0.0.0.0:8080/) ...

# Servidor en IP y Puerto específico
python3 -m http.server -b 127.0.0.42 8080 # Serving HTTP on 127.0.0.42 port 8080 (http://127.0.0.42:8080/) ...

# Especificar directorio de inicio
python3 -m http.server -d ~/Pictures # Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```

# **Ejecutar un script de forma remota a través de la interfaz de pureta de enlace común (CGI)**

Common Gateway Interface (CGI) es un protocolo antiguo que ya no se utiliza en el desarrollo de aplicaciones web modernas, para sencillos proyectos puede ser una buena opción. 

## **Crear proyecto de CGI**

Se debe crear una carpeta si o si con el nombre `cgi-bin`. Dentro de esta carpeta se puede crear un archivo de Python sin un nombre específico.

**Archivo app.py**
```python
print(
    """\
Content-Type: text/html

<!DOCTYPE html>
<html lang="en">
<body>
<h1>Hello, World!</h1>
</body>
</html>"""
)
```

**Ejecutar el script de CGI, el parámetro --cgi es opcional**
```bash
python3 -m http.server --cgi
```

# **Servir contenido estático y dinámico**


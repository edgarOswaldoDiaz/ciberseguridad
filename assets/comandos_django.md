# Django** (entorno de desarrollo en Python)

---

## **Entorno y Proyecto**

```bash
# Crear un entorno virtual
python -m venv nombre_entorno

# Activar el entorno virtual (Linux/macOS)
source nombre_entorno/bin/activate

# Activar el entorno virtual (Windows)
nombre_entorno\Scripts\activate

# Desactivar entorno virtual
deactivate

# Instalar Django
pip install django

# Verificar versión de Django
python -m django --version
```

---

## **Crear y Configurar Proyecto**

```bash
# Crear proyecto Django
django-admin startproject nombre_proyecto

# Entrar al directorio del proyecto
cd nombre_proyecto

# Crear una aplicación dentro del proyecto
python manage.py startapp nombre_app

# Ejecutar servidor de desarrollo
python manage.py runserver

# Ejecutar servidor en un puerto específico
python manage.py runserver 8080
```

---

## **Migraciones y Base de Datos**

```bash
# Crear migraciones para modelos
python manage.py makemigrations

# Aplicar migraciones a la base de datos
python manage.py migrate

# Ver migraciones aplicadas
python manage.py showmigrations

# Crear un superusuario
python manage.py createsuperuser

# Acceder a la shell de Django
python manage.py shell
```

---

## **Administrar Aplicaciones**

```bash
# Registrar una nueva aplicación en settings.py
# Agregar nombre_app a INSTALLED_APPS

# Crear archivo admin.py para registrar modelos en el admin
# En nombre_app/admin.py:
from django.contrib import admin
from .models import Modelo

admin.site.register(Modelo)
```

---

## **Pruebas y Depuración**

```bash
# Ejecutar todas las pruebas
python manage.py test

# Ejecutar pruebas de una aplicación específica
python manage.py test nombre_app

# Ver rutas registradas en el proyecto
python manage.py show_urls  # (requiere django-extensions)
```

---

## **Herramientas Útiles**

```bash
# Instalar extensiones útiles de Django
pip install django-extensions

# Usar shell_plus (mejor shell con carga automática de modelos)
python manage.py shell_plus

# Generar un grafo de modelos (requiere Graphviz)
python manage.py graph_models -a -o modelo.png
```

---

## **Archivos Estáticos**

```bash
# Recolectar archivos estáticos (para producción)
python manage.py collectstatic
```

---

## **Autenticación y Sesiones**

```bash
# Crear una nueva app para autenticación personalizada
python manage.py startapp accounts

# Cambiar contraseña de un usuario desde consola
python manage.py changepassword nombre_usuario
```

---

## **Despliegue y Producción**

```bash
# Crear archivo requirements.txt
pip freeze > requirements.txt

# Instalar dependencias desde requirements.txt
pip install -r requirements.txt

# Configurar SECRET_KEY, DEBUG, ALLOWED_HOSTS en settings.py para producción
```

---

## **Comandos Útiles Extra**

```bash
# Ver todas las rutas del proyecto (requiere django-extensions)
python manage.py show_urls

# Crear un nuevo proyecto con una estructura específica
django-admin startproject --template=mi_template nombre_proyecto

# Crear un archivo fixtures (datos iniciales)
python manage.py dumpdata > datos.json

# Cargar datos desde un fixture
python manage.py loaddata datos.json
```

___________________________

> By CISO oswaldo.diaz 

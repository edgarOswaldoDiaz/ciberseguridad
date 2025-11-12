# Flask by Python

## **Instalación y Configuración**

```bash
# Instalar Flask
pip install Flask

# Crear entorno virtual
python -m venv venv

# Activar entorno virtual (Windows)
venv\Scripts\activate

# Activar entorno virtual (Mac/Linux)
source venv/bin/activate

# Desactivar entorno virtual
deactivate
```

## **Aplicación Básica**

```python
from flask import Flask

# Crear instancia de la aplicación
app = Flask(__name__)

# Ruta básica
@app.route('/')
def home():
    return 'Hello, World!'

# Ejecutar aplicación
if __name__ == '__main__':
    app.run(debug=True)
```

## **Rutas y Métodos HTTP**

```python
from flask import Flask, request

@app.route('/users')
def users():
    return 'Lista de usuarios'

@app.route('/users', methods=['POST'])
def create_user():
    return 'Usuario creado'

@app.route('/users/<int:user_id>')
def get_user(user_id):
    return f'Usuario ID: {user_id}'

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    return f'Usuario {user_id} actualizado'

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    return f'Usuario {user_id} eliminado'

# Métodos HTTP comunes
@app.route('/api/data', methods=['GET', 'POST', 'PUT', 'DELETE'])
def handle_data():
    if request.method == 'GET':
        return 'GET request'
    elif request.method == 'POST':
        return 'POST request'
    # ... etc
```

## **Manejo de Datos de Formularios y JSON**

```python
from flask import request, jsonify

# Obtener datos de formulario
@app.route('/form', methods=['POST'])
def handle_form():
    name = request.form['name']
    email = request.form['email']
    return f'Nombre: {name}, Email: {email}'

# Obtener datos JSON
@app.route('/api/json', methods=['POST'])
def handle_json():
    data = request.get_json()
    return jsonify(data)

# Obtener parámetros de consulta
@app.route('/search')
def search():
    query = request.args.get('q', '')
    page = request.args.get('page', 1, type=int)
    return f'Buscando: {query}, Página: {page}'
```

## **Renderizado de Plantillas**

```python
from flask import render_template

@app.route('/profile/<username>')
def profile(username):
    return render_template('profile.html', username=username)

@app.route('/users')
def users_list():
    users = ['Alice', 'Bob', 'Charlie']
    return render_template('users.html', users=users)

# Pasar múltiples variables
@app.route('/dashboard')
def dashboard():
    user_data = {
        'name': 'John',
        'age': 30,
        'city': 'New York'
    }
    posts = ['Post 1', 'Post 2', 'Post 3']
    return render_template('dashboard.html', user=user_data, posts=posts)
```

## **Redirecciones y URLs**

```python
from flask import redirect, url_for, abort

# Redirección
@app.route('/old-page')
def old_page():
    return redirect(url_for('new_page'))

@app.route('/new-page')
def new_page():
    return 'Nueva página'

# Redirección externa
@app.route('/google')
def google():
    return redirect('https://www.google.com')

# Abortar con error
@app.route('/secret')
def secret():
    abort(403)  # Forbidden

# Manejo de errores
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
```

## **Respuestas y JSON**

```python
from flask import jsonify, make_response

# Respuesta JSON simple
@app.route('/api/users')
def api_users():
    users = [{'id': 1, 'name': 'John'}, {'id': 2, 'name': 'Jane'}]
    return jsonify(users)

# Respuesta personalizada
@app.route('/custom')
def custom_response():
    response = make_response('Custom response', 200)
    response.headers['Content-Type'] = 'text/plain'
    return response

# Cookies
@app.route('/set-cookie')
def set_cookie():
    response = make_response('Cookie set')
    response.set_cookie('username', 'john_doe')
    return response
```

## **Manejo de Archivos y Subidas**

```python
from flask import request, flash, redirect, url_for
import os

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file selected')
            return redirect(request.url)
        
        file = request.files['file']
        if file.filename == '':
            flash('No file selected')
            return redirect(request.url)
        
        if file:
            filename = file.filename
            file.save(os.path.join('uploads', filename))
            return 'File uploaded successfully'
    
    return '''
    <form method="post" enctype="multipart/form-data">
        <input type="file" name="file">
        <input type="submit" value="Upload">
    </form>
    '''
```

## **Sesiones y Autenticación**

```python
from flask import session
import os

# Configuración de clave secreta
app.secret_key = 'your-secret-key'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Verificar credenciales (ejemplo)
        if username == 'admin' and password == 'password':
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            return 'Invalid credentials'
    
    return '''
    <form method="post">
        <input type="text" name="username" placeholder="Username">
        <input type="password" name="password" placeholder="Password">
        <input type="submit" value="Login">
    </form>
    '''

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return f'Welcome {session["username"]}'
    return redirect(url_for('login'))
```

## **Extensiones Comunes**

```python
# Flask-WTF (Formularios)
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

# Flask-SQLAlchemy (Base de datos)
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

# Flask-Login (Autenticación de usuarios)
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required

login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin, db.Model):
    # ... definición del modelo

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
```

## **Configuración y Variables de Entorno**

```python
import os
from dotenv import load_dotenv

load_dotenv()

# Configuración
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

app.config.from_object(Config)

# O configuración directa
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['DEBUG'] = True
```

## **Comandos Útiles de Flask CLI**

```bash
# Ejecutar la aplicación
flask run

# Ejecutar en modo desarrollo
export FLASK_ENV=development
flask run

# Crear base de datos (con Flask-SQLAlchemy)
flask shell
>>> db.create_all()

# Variables de entorno importantes
export FLASK_APP=app.py
export FLASK_ENV=production
```

## **Manejo de Errores**

```python
@app.errorhandler(404)
def not_found(error):
    return render_template('error.html', error='Página no encontrada'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('error.html', error='Error interno del servidor'), 500

@app.errorhandler(Exception)
def handle_exception(e):
    return render_template('error.html', error=str(e)), 500
```

## **Blueprints (Organización de aplicaciones grandes)**

```python
# admin.py
from flask import Blueprint

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/')
def admin_home():
    return 'Admin Panel'

# app.py
from admin import admin_bp
app.register_blueprint(admin_bp)
```

## **Validación y Formularios**

```python
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Email, Length, NumberRange

class UserForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=50)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    age = IntegerField('Age', validators=[NumberRange(min=0, max=120)])
    submit = SubmitField('Submit')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = UserForm()
    if form.validate_on_submit():
        # Procesar datos del formulario
        name = form.name.data
        email = form.email.data
        age = form.age.data
        return f'Registrado: {name}, {email}, {age}'
    return render_template('register.html', form=form)
```

---

## **Atajos y Tips**

- **Debug mode**: `app.run(debug=True)`
- **URL dinámicas**: `@app.route('/user/<username>')`
- **Tipos de variables**: `<int:id>`, `<float:price>`, `<path:subpath>`
- **Plantillas**: Usar Jinja2 (`{{ variable }}`, `{% if %}`, `{% for %}`)
- **Archivos estáticos**: Carpeta `static/` automáticamente servida
- **Plantillas**: Carpeta `templates/` para archivos HTML
________________________________________

> By CISO oswaldo.diaz 

# OWASP Top Ten 

El OWASP Top Ten es un documento de concientización estándar y una guía para desarrolladores y profesionales de la seguridad de aplicaciones web. Publicado por la Open Web Application Security Project (OWASP), una fundación sin fines de lucro, esta lista representa un consenso global sobre los 10 riesgos de seguridad más críticos para las aplicaciones web.

Se actualiza periódicamente (la última versión es de 2021) para reflejar la evolución del panorama de amenazas. No es una lista exhaustiva de todas las vulnerabilidades, sino que se enfoca en las más comunes y peligrosas, sirviendo como un punto de partida esencial para priorizar los esfuerzos de seguridad en el desarrollo y despliegue de aplicaciones web.

Cada vulnerabilidad de la lista se describe detalladamente, incluyendo cómo ocurre, su impacto potencial y las mejores prácticas para prevenirla y mitigarla.

## A01:2021 – Control de Acceso Roto (Broken Access Control)

**Descripción**
Ocurre cuando un usuario puede acceder a recursos o acciones para las que no tiene permiso (por ejemplo, ver o modificar datos de otros usuarios).

```python
# vulnerable.py
from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulamos una "base de datos" en memoria
USERS = {
    1: {"username": "alice", "role": "user", "data": "Datos de Alice"},
    2: {"username": "bob",   "role": "user", "data": "Datos de Bob"},
    3: {"username": "admin", "role": "admin","data": "Datos de Admin"},
}

def get_current_user():
    # Supongamos que extraemos el ID del usuario de un token
    return int(request.headers.get("X-User-ID", 0))

@app.route("/user/<int:user_id>")
def get_user_data(user_id):
    current = get_current_user()
    # SOLO revisamos que el usuario exista
    if user_id in USERS:
        return jsonify(USERS[user_id])
    return jsonify({"error": "Usuario no encontrado"}), 404
```

> **Problema**: Alice (ID 1) puede pedir `/user/2` y ver los datos de Bob.

---

### Reparación

```python
# fixed.py
from flask import Flask, request, jsonify, abort

app = Flask(__name__)

USERS = { ... }  # igual que antes

def get_current_user():
    return int(request.headers.get("X-User-ID", 0))

@app.route("/user/<int:user_id>")
def get_user_data(user_id):
    current = get_current_user()
    if user_id not in USERS:
        abort(404)
    # Control de acceso: solo el usuario mismo o admin
    user = USERS[current]
    if current != user_id and user.get("role") != "admin":
        abort(403)  # Forbidden
    return jsonify(USERS[user_id])
```

**Explicación**

* Se valida que el usuario autenticado sea el mismo que pide los datos o tenga rol de administrador.
* Se devuelven códigos HTTP 403/404 apropiados.

---

## A02:2021 – Fallas Criptográficas (Cryptographic Failures)

**Descripción**
Uso inadecuado o ausencia de cifrado para proteger datos sensibles (contraseñas, tokens, información PII).

```python
# vulnerable.py
import hashlib

def store_password(password):
    # Almacenamos solo el hash MD5 (débil y sin sal)
    h = hashlib.md5(password.encode()).hexdigest()
    # guardamos h en la base de datos...
    return h
```

> **Problema**: MD5 es susceptible a ataques de colisión y diccionario; sin sal, iguales contraseñas producen mismo hash.

---

### Reparación

```python
# fixed.py
import bcrypt

def store_password(password: str) -> bytes:
    # Genera automáticamente una sal fuerte y aplica bcrypt
    salt = bcrypt.gensalt(rounds=12)
    hashed = bcrypt.hashpw(password.encode(), salt)
    # guardamos `hashed` en la base de datos...
    return hashed

def verify_password(password: str, hashed: bytes) -> bool:
    return bcrypt.checkpw(password.encode(), hashed)
```

**Explicación**

* Se utiliza bcrypt con `gensalt()` para sal aleatoria y múltiples rondas de trabajo.
* Bcrypt está diseñado para ser lento y resistente a fuerza bruta.

---

## A03:2021 – Inyección (Injection)

**Descripción**
Ocurre cuando datos de entrada no confiables se incluyen en un comando o consulta sin validación, lo que permite modificar su ejecución (SQL, OS, LDAP…).

```python
# vulnerable.py
import sqlite3

def find_user(username):
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    # Construcción insegura de SQL
    query = f"SELECT * FROM users WHERE username='{username}'"
    cursor.execute(query)
    return cursor.fetchall()
```

> **Problema**: Si `username = "alice' OR '1'='1"`, la consulta devuelve todos los usuarios.

---

### Reparación

```python
# fixed.py
import sqlite3

def find_user(username):
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    # Consulta parametrizada
    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    return cursor.fetchall()
```

**Explicación**

* Uso de parámetros (`?`) en lugar de concatenar cadenas evita que el atacante inyecte SQL.

---

## A04:2021 – Diseño Inseguro (Insecure Design)

**Descripción**
Falta de controles de seguridad durante la fase de diseño (modelos de amenaza, validaciones, principios de mínimo privilegio).

> **Ejemplo**: No definir límites de tasa (rate limiting) ni políticas de bloqueo tras múltiples intentos fallidos en el login.

---

### Reparación

1. **Modelado de amenazas**: identificar posibles ataques (fuerza bruta, DoS…).
2. **Diseñar controles**:

   * Rate limiting.
   * Bloqueo temporal de cuenta.
   * Captchas en puntos críticos.

```python
# esquema conceptual (Flask + Flask-Limiter)
from flask import Flask, request
from flask_limiter import Limiter

app = Flask(__name__)
limiter = Limiter(app, key_func=lambda: request.remote_addr)

@app.route("/login", methods=["POST"])
@limiter.limit("5 per minute")
def login():
    # lógica de autenticación...
    return "OK"
```

**Explicación**

* Se introduce un limitador para evitar intentos masivos de acceso.

---

## A05:2021 – Configuración de Seguridad Incorrecta (Security Misconfiguration)

**Descripción**
Configuraciones por defecto inseguras, puertos abiertos, mensajes de error detallados, directorios expuestos.

```python
# vulnerable.py (Flask)
app = Flask(__name__)
app.debug = True  # DEBUG activado en producción
```

> **Problema**: En debug mode, se muestran trazas de pila con información sensible.

---

### Reparación

```python
# fixed.py
app = Flask(__name__)
app.debug = False
# Además, deshabilitar listados de directorios, configurar headers seguros:
from flask_talisman import Talisman
Talisman(app)  # añade Content-Security-Policy, HSTS, etc.
```

**Explicación**

* Desactivar modo debug en producción.
* Usar librerías como Flask‑Talisman para reforzar cabeceras de seguridad.

---

## A06:2021 – Vulnerabilidades y Componentes Desactualizados (Vulnerable and Outdated Components)

**Descripción**
Uso de librerías o frameworks con vulnerabilidades conocidas.

```bash
# requirements.txt
Flask==1.0.0
requests==2.20.0
```

> **Problema**: Versiones antiguas con CVEs sin parchear.

---

### Reparación

1. Revisar periódicamente con `pip list --outdated`.
2. Automatizar alertas (Dependabot, Snyk…).
3. Actualizar a versiones seguras:

```bash
# requirements.txt
Flask>=2.2.0
requests>=2.31.0
```

**Explicación**

* Mantener dependencias al día reduce la **superficie de ataque**.

---

## A07:2021 – Fallas de Identificación y Autenticación (Identification and Authentication Failures)

**Descripción**
Gestión deficiente de sesiones y autenticación (tokens predecibles, falta de expiración, no invalidar sesiones…).

```python
# vulnerable.py
session_token = username + "-token"
# El “token” se guarda en una cookie sin flags de seguridad:
resp.set_cookie("session", session_token)
```

> **Problema**: Token predecible y cookie sin `HttpOnly` ni `Secure`.

---

### Reparación

```python
# fixed.py
import secrets
from flask import Flask, request, make_response

app = Flask(__name__)

@app.route("/login", methods=["POST"])
def login():
    # tras validar credenciales:
    token = secrets.token_urlsafe(32)
    resp = make_response("Logged in")
    resp.set_cookie("session", token,
                    httponly=True, secure=True, samesite="Lax")
    # almacenar y relacionar token en servidor con el usuario
    return resp
```

**Explicación**

* Tokens generados con `secrets` no predecibles.
* Cookies protegidas con `HttpOnly`, `Secure` y `SameSite`.

---

## A08:2021 – Fallas en la Integridad de Software y Datos (Software and Data Integrity Failures)

**Descripción**
No verificar la integridad de componentes o datos críticos (actualizaciones, paquetes, archivos).

> **Ejemplo**: Descargar y ejecutar código sin validar firma.

```python
# vulnerable.py
import requests, subprocess

url = "https://example.com/tool.py"
code = requests.get(url).text
exec(code)  # ¡Peligro!
```

---

### Reparación

1. Descargar y **verificar firma** o checksum antes de ejecutar.
2. Evitar `exec()` de código externo.

```python
# fixed.py
import requests, hashlib

url = "https://example.com/tool.py"
r = requests.get(url)
expected_sha256 = "abc123..."  # obtenido de fuente confiable
h = hashlib.sha256(r.content).hexdigest()
if h != expected_sha256:
    raise ValueError("Integridad comprometida")
# Ahora es seguro procesar el contenido
```

**Explicación**

* Se valida que el contenido coincide con un checksum firmado.

---

## A09:2021 – Fallas de Registro y Monitoreo (Security Logging and Monitoring Failures)

**Descripción**
No generar logs suficientes o no monitorear eventos críticos (login, errores, accesos no autorizados).

```python
# vulnerable.py
def login(username, password):
    if authenticate(username, password):
        return "OK"
    else:
        return "Credenciales inválidas"
```

> **Problema**: No hay registro de intentos fallidos; imposible detectar ataques.

---

### Reparación

```python
# fixed.py
import logging

logging.basicConfig(filename="app.log",
                    level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s")

def login(username, password):
    if authenticate(username, password):
        logging.info(f"Login exitoso: {username}")
        return "OK"
    else:
        logging.warning(f"Login fallido: {username} desde {request.remote_addr}")
        return "Credenciales inválidas"
```

**Explicación**

* Se registra cada intento (exitoso o fallido) con timestamps.
* Facilita detección de patrones anómalos.

---

## A10:2021 – SSRF (Server-Side Request Forgery)

**Descripción**
La aplicación recibe una URL de usuario y realiza peticiones sin validar, permitiendo acceder a recursos internos (Intranet, metadata AWS…).

```python
# vulnerable.py
import requests
from flask import Flask, request

app = Flask(__name__)

@app.route("/fetch")
def fetch():
    url = request.args.get("url")
    resp = requests.get(url)  # peligro: puede ser 127.0.0.1, metadata, etc.
    return resp.text
```

---

### Reparación

```python
# fixed.py
import requests, urllib.parse
from flask import Flask, request, abort

app = Flask(__name__)

ALLOWED_DOMAINS = {"example.com", "api.example.com"}

@app.route("/fetch")
def fetch():
    raw = request.args.get("url", "")
    parsed = urllib.parse.urlparse(raw)
    # Validar esquema y dominio
    if parsed.scheme not in ("http", "https") or parsed.hostname not in ALLOWED_DOMAINS:
        abort(400)
    resp = requests.get(raw, timeout=5)
    return resp.text
```

**Explicación**

* Se filtran dominios permitidos y esquemas adecuados.
* Evita que un atacante apunte a direcciones internas o sensibles.

___________________

Referencia bibliogrráfica

> https://owasp.org/www-project-top-ten/

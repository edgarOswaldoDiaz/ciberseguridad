## Mitigación de OWASP Top 10 2021

|  OWASP  |                    Riesgo                    |                                                 Mitigación en esta app                                                |
| :-----: | :------------------------------------------: | :-------------------------------------------------------------------------------------------------------------------: |
| **A01** |       **Pérdida de Control de Acceso**       |                                JWT con roles en payload (por implementar) + middleware.                               |
| **A02** |           **Fallas Criptográficas**          |                             TLS 1.2/1.3 en Nginx; cifrado en tránsito; secretos en `.env`.                            |
| **A03** |                 **Inyección**                |                                Consultas parametrizadas a Neo4j; validación de inputs.                                |
| **A04** |              **Diseño Inseguro**             |                     Arquitectura de capas (presentación, lógica, datos); componentes actualizados.                    |
| **A05** |   **Configuración de Seguridad Incorrecta**  |                         `helmet`, CORS restringido, rate‑limit, HSTS, X‑Frame, X‑Content‑Type.                        |
| **A06** |    **Componentes Vulnerables y Obsoletos**   |                                 `npm audit`, dependencias actualizadas periódicamente.                                |
| **A07** | **Fallas de Identificación y Autenticación** |                JWT bien configurado; expiración corta; renovación vía refresh‑tokens (por implementar).               |
| **A08** | **Fallas de Integridad de Datos y Software** |                             Uso de firmas (JWT); HTTPS; control de versiones en el código.                            |
| **A09** |      **Fallas de Registro y Monitoreo**      |                               `winston` registra errores y accesos; logs centralizados.                               |
| **A10** |    **SSRF** (Server‑Side Request Forgery)    | No se hacen requests a URIs externas desde servidor; si fuera necesario, filtrar y validar destinos contra whitelist. |


**Archivos clave**

   * `package.json`
   * `.env`
   * `server.js` (Node.js + Neo4j)
   * `public/index.html` (HTML5)
   * `public/styles.css` (CSS3)
   * `nginx.conf`

---

## Estructura del proyecto

```
my‑app/
│
├─ .env
├─ package.json
├─ server.js
├─ nginx.conf
└─ public/
   ├─ index.html
   └─ styles.css
```

---

## Archivos clave

### `package.json`

```json
{
  "name": "my-app",
  "version": "1.0.0",
  "main": "server.js",
  "scripts": {
    "start": "node server.js"
  },
  "dependencies": {
    "dotenv": "^16.0.0",
    "express": "^4.18.2",
    "neo4j-driver": "^5.2.0",
    "helmet": "^6.0.0",
    "express-rate-limit": "^6.3.0",
    "cors": "^2.8.5",
    "winston": "^3.8.2"
  }
}
```

### `.env`

> **Nunca** subir este archivo a tu repositorio público.

```
PORT=3000
NEO4J_URI=bolt://localhost:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=TuPasswordSuperSecreto
JWT_SECRET=OtraClaveMuySecreta
```

### `server.js`

```js
require('dotenv').config();
const express = require('express');
const helmet = require('helmet');
const rateLimit = require('express-rate-limit');
const cors = require('cors');
const neo4j = require('neo4j-driver');
const winston = require('winston');
const jwt = require('jsonwebtoken');

const app = express();

// — Seguridad HTTP headers
app.use(helmet());

// — Límite de solicitudes para mitigar brute‑force
app.use(rateLimit({ windowMs: 15*60*1000, max: 100 }));

// — CORS restringido
app.use(cors({ origin: ['https://tu-dominio.com'] }));

app.use(express.json());

// — Logger de peticiones y errores
const logger = winston.createLogger({
  transports: [ new winston.transports.File({ filename: 'app.log' }) ]
});

// — Conexión Neo4j segura
const driver = neo4j.driver(
  process.env.NEO4J_URI,
  neo4j.auth.basic(process.env.NEO4J_USER, process.env.NEO4J_PASSWORD),
  { encrypted: 'ENCRYPTION_ON' }
);

// — Middleware de autenticación por JWT
function authenticate(req, res, next) {
  const token = req.headers['authorization']?.split(' ')[1];
  if (!token) return res.status(401).send('No token');
  jwt.verify(token, process.env.JWT_SECRET, (err, user) => {
    if (err) return res.status(403).send('Token inválido');
    req.user = user;
    next();
  });
}

// — Ejemplo de endpoint protegido
app.post('/api/nodes', authenticate, async (req, res) => {
  const session = driver.session();
  try {
    const { name, type } = req.body;
    // Validación y limpieza de inputs
    if (typeof name !== 'string' || typeof type !== 'string')
      return res.status(400).send('Datos inválidos');

    const result = await session.run(
      'CREATE (n:Node {name: $name, type: $type}) RETURN n',
      { name, type }
    );
    res.json(result.records[0].get('n').properties);
  } catch (err) {
    logger.error(err);
    res.status(500).send('Error interno');
  } finally {
    await session.close();
  }
});

app.use(express.static('public'));

app.listen(process.env.PORT, () => {
  console.log(`Servidor en puerto ${process.env.PORT}`);
});
```

### `public/index.html`

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta http‑equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Mi App Segura</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <header>
    <h1>Bienvenido a Mi App</h1>
  </header>
  <main>
    <form id="createNodeForm">
      <input type="text" id="name" placeholder="Nombre" required minlength="3" maxlength="30">
      <input type="text" id="type" placeholder="Tipo" required>
      <button type="submit">Crear Nodo</button>
    </form>
    <pre id="output"></pre>
  </main>
  <script>
    document.getElementById('createNodeForm').addEventListener('submit', async e => {
      e.preventDefault();
      const name = document.getElementById('name').value.trim();
      const type = document.getElementById('type').value.trim();
      // — Ejemplo de token: en producción pedir login y guardar JWT
      const token = localStorage.getItem('jwt');
      const res = await fetch('/api/nodes', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({ name, type })
      });
      document.getElementById('output').textContent = await res.text();
    });
  </script>
</body>
</html>
```

### `public/styles.css`

```css
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: Arial, sans‑serif; line-height: 1.6; padding: 1rem; }
header { background: #004466; color: #fff; padding: 1rem; border-radius: 0.5rem; }
main { margin-top: 1rem; }
form { display: flex; gap: 0.5rem; flex-wrap: wrap; }
input, button { padding: 0.5rem; border: 1px solid #ccc; border-radius: 0.25rem; }
button { cursor: pointer; }
pre { margin-top: 1rem; background: #f4f4f4; padding: 1rem; border-radius: 0.25rem; overflow-x: auto; }
```

### `nginx.conf`

```nginx
events { }
http {
  server {
    listen 80;
    server_name tu-dominio.com;

    # Redirigir HTTP → HTTPS
    return 301 https://$host$request_uri;
  }
  server {
    listen 443 ssl http2;
    server_name tu-dominio.com;

    # Certificados TLS
    ssl_certificate     /etc/ssl/certs/your.crt;
    ssl_certificate_key /etc/ssl/private/your.key;
    ssl_protocols       TLSv1.2 TLSv1.3;
    ssl_prefer_server_ciphers on;

    # Encabezados de seguridad
    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;
    add_header X-Frame-Options "DENY" always;
    add_header X-Content-Type-Options "nosniff" always;

    location / {
      proxy_pass http://127.0.0.1:3000;
      proxy_http_version 1.1;
      proxy_set_header Upgrade $http_upgrade;
      proxy_set_header Connection 'upgrade';
      proxy_set_header Host $host;
      proxy_cache_bypass $http_upgrade;
    }
  }
}
```

---

## Descripción de los componentes

* **HTML5/CSS3**: validación en cliente, atributos `required`, `minlength`, `maxlength` y saneamiento al enviar.
* **Node.js + Express**:

  * `helmet` para HTTP headers seguros
  * `express-rate-limit` para mitigar ataques de fuerza bruta
  * `cors` configurado a orígenes de confianza
  * Validación y tipado de datos en servidor
* **Neo4j**: conexión cifrada (`ENCRYPTION_ON`), credenciales en entorno, consultas parametrizadas para evitar inyección.
* **JWT**: autenticación stateless, firma con `HS256` usando clave secreta fuerte.
* **Winston**: registro centralizado de eventos, errores y accesos.
* **Nginx**: terminación TLS, HTTP→HTTPS, cabeceras HSTS/X-Frame/X-Content-Type, proxy inverso seguro.

---

> **Notas adicionales de implementación**
>
> * **Control de Roles (A01)**: diseñar un esquema RBAC y comprobar en `authenticate` que `req.user.role` tenga permiso para cada ruta.
> * **Actualizaciones (A06)**: incorporar un CI/CD que corra `npm audit` y escanee vulnerabilidades de imágenes Docker, OS, etc.
> * **Monitoreo (A09)**: conectar Winston a un SIEM o servicio de alerta (Elastic, Splunk, Datadog).


#### docker-compose.yml 

1. **neo4j**: base de datos gráfica
2. **app**: tu servidor Node.js (+ Neo4j driver)
3. **nginx**: proxy inverso con TLS terminación

```yaml
version: '3.8'

services:
  neo4j:
    image: neo4j:5.2
    container_name: myapp_neo4j
    env_file:
      - .env
    environment:
      # Sobre-escribe sólo si no está en .env:
      NEO4J_AUTH: "${NEO4J_USER}/${NEO4J_PASSWORD}"
    volumes:
      - neo4j_data:/data
      - neo4j_logs:/logs
    ports:
      - "7687:7687"   # Bolt
      - "7474:7474"   # HTTP
    networks:
      - myapp_net

  app:
    build: .
    container_name: myapp_node
    env_file:
      - .env
    depends_on:
      - neo4j
    ports:
      - "3000:3000"
    networks:
      - myapp_net

  nginx:
    image: nginx:latest
    container_name: myapp_nginx
    depends_on:
      - app
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
      - ./certs:/etc/ssl:ro
    networks:
      - myapp_net

volumes:
  neo4j_data:
  neo4j_logs:

networks:
  myapp_net:
    driver: bridge
```

---

### ¿Cómo funciona?

* **env\_file**
  Carga tu `.env` (puerto, credenciales Neo4j, JWT\_SECRET, etc.) sin incluirlo en el repositorio.

* **neo4j**

  * Expone Bolt (`7687`) y HTTP (`7474`) para administración y conexión desde la app.
  * Guarda datos y logs en volúmenes persistentes.

* **app**

  * Se construye con tu `Dockerfile` (que debería exponer el puerto 3000 y copiar `server.js`, `package.json`, etc.).
  * `depends_on: neo4j` asegura que la base de datos intente arrancar primero.

* **nginx**

  * Monta tu `nginx.conf` y los certificados TLS (en `./certs/your.crt` y `your.key`).
  * Redirige HTTP → HTTPS y hace proxy a `app:3000`.

---

### Pasos para arrancar

Raíz del proyecto:

   * `Dockerfile` para tu aplicación Node.js
   * `.env` con tus variables
   * `nginx.conf` (como en el ejemplo previo)
   * Certificados TLS en `./certs/`

Ejecuta en terminal:

   ```bash
   docker-compose up --build -d
   ```

Comprueba:

   * `http://tu-dominio.com` redirige a HTTPS.
   * Tu app Node.js responde en `https://tu-dominio.com`.
   * Neo4j accesible en `bolt://localhost:7687` y UI en `http://localhost:7474`.


____________________

> By CISO oswaldo.diaz 

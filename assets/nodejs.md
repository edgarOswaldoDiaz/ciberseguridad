# Node.js

---

## Gestión de versiones de Node

| Comando                       | Descripción                                        |
| ----------------------------- | -------------------------------------------------- |
| `nvm install <versión>`       | Instala la versión especificada de Node.js         |
| `nvm use <versión>`           | Activa la versión especificada en la sesión actual |
| `nvm ls`                      | Lista todas las versiones instaladas               |
| `nvm alias default <versión>` | Establece la versión por defecto                   |

---

## Inicialización de Proyecto

| Comando              | Descripción                                                  |
| -------------------- | ------------------------------------------------------------ |
| `npm init`           | Crea `package.json` paso a paso                              |
| `npm init -y`        | Crea `package.json` con valores por defecto                  |
| `npm init <paquete>` | Inicializa con un template (p.ej. `npm init express@latest`) |

---

## Gestión de Paquetes (npm)

| Comando                        | Descripción                                       |
| ------------------------------ | ------------------------------------------------- |
| `npm install <paquete>`        | Instala y añade dependencia en `package.json`     |
| `npm install --save-dev <pkg>` | Instala como dependencia de desarrollo            |
| `npm uninstall <paquete>`      | Desinstala paquete y lo quita de `package.json`   |
| `npm update`                   | Actualiza todas las dependencias                  |
| `npm outdated`                 | Muestra dependencias desactualizadas              |
| `npm audit`                    | Revisa vulnerabilidades                           |
| `npm audit fix`                | Intenta corregir automáticamente vulnerabilidades |

---

## Scripts en package.json

```jsonc
{
  "scripts": {
    "start": "node index.js",
    "dev": "nodemon src/app.js",
    "test": "jest",
    "build": "webpack --mode production",
    "lint": "eslint ."
  }
}
```

| Comando            | Descripción                                  |
| ------------------ | -------------------------------------------- |
| `npm run <script>` | Ejecuta un script definido en `package.json` |
| `npm start`        | Alias de `npm run start`                     |

---

## Herramientas de Desarrollo

| Herramienta / Paquete         | Uso típico                            |
| ----------------------------- | ------------------------------------- |
| **nodemon**                   | Reinicia servidor al detectar cambios |
| **eslint**                    | Linter de JavaScript                  |
| **prettier**                  | Formateador de código                 |
| **webpack**                   | Bundler de módulos                    |
| **babel-cli**                 | Transpila ES6+ a ES5                  |
| **jest**, **mocha**, **chai** | Frameworks de testing                 |
| **pm2**                       | Gestor de procesos en producción      |

> **Instalación global**:
>
> ```bash
> npm install -g nodemon pm2 eslint
> ```

---

## Estructura típica de proyecto

```
my-app/
├─ node_modules/
├─ src/
│  ├─ app.js
│  ├─ routes/
│  ├─ controllers/
│  └─ models/
├─ public/
│  ├─ index.html
│  └─ assets/
├─ tests/
├─ .env
├─ .eslintrc.js
├─ package.json
└─ webpack.config.js
```

---

## Variables de Entorno

| Comando                      | Descripción                                                 |
| ---------------------------- | ----------------------------------------------------------- |
| `npm install dotenv`         | Manejo de variables de entorno                              |
| `require('dotenv').config()` | Carga `.env` en `process.env`                               |
| `.env`                       | Archivo donde definir variables (no subir a repos públicos) |

---

## NPX: Ejecutar paquetes sin instalarlos

| Comando                        | Descripción                                 |
| ------------------------------ | ------------------------------------------- |
| `npx create-react-app my-app`  | Crea una app React sin instalar globalmente |
| `npx express-generator my-app` | Generador de esqueleto Express              |
| `npx nodemon src/app.js`       | Ejecuta `nodemon` sin instalación global    |

---

## Depuración (Debug)

| Comando                              | Descripción                                     |
| ------------------------------------ | ----------------------------------------------- |
| `node --inspect index.js`            | Inicia con protocolo de debugging               |
| `node --inspect-brk index.js`        | Para antes de ejecutar para colocar breakpoints |
| Chrome DevTools → `chrome://inspect` | Conectar debugger al proceso Node               |

---

## Deployment

| Herramienta    | Comando / Notas                                            |
| -------------- | ---------------------------------------------------------- |
| **Heroku CLI** | `heroku create` / `git push heroku main`                   |
| **PM2**        | `pm2 start index.js` / `pm2 save`                          |
| **Docker**     | `docker build -t my-app .` / `docker run -p 3000:3000 ...` |

---

### Resumen rápido

```bash
# Versión de Node
node -v

# Inicializar proyecto
npm init -y

# Instalar dependencias
npm install express mongoose cors

# Paquetes de dev
npm install --save-dev nodemon eslint

# Ejecutar en desarrollo
npm run dev

# Ejecutar en producción
npm start

# Auditar vulnerabilidades
npm audit fix
```

____________

> By CISO oswaldo.diaz

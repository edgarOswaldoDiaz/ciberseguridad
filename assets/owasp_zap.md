# Cheat Sheet - OWASP ZAP 

---

### Iniciar ZAP

| Comando                                                         | Descripción                                 |
| --------------------------------------------------------------- | ------------------------------------------- |
| **Linux/macOS**<br/>`~/ZAP/zap.sh`                              | Lanza interfaz gráfica de ZAP               |
| **Windows**<br/>`zap.bat`                                       | Lanza interfaz gráfica de ZAP               |
| **Modo daemon**<br/>`zap.sh -daemon -port 8080 -host 127.0.0.1` | Ejecuta ZAP en background como servicio API |

---

### ZAP en Docker

| Comando                                                                                             | Descripción                                         |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------- |
| `docker pull owasp/zap2docker-stable`                                                               | Descarga la última imagen estable de ZAP            |
| `docker run -u zap -p 8080:8080 -i owasp/zap2docker-stable zap.sh -daemon -port 8080 -host 0.0.0.0` | Arranca ZAP en modo daemon dentro de un contenedor  |
| `docker run --rm owasp/zap2docker-stable zap-baseline.py -t http://example.com -r reporte.html`     | Escaneo básico (baseline) con generación de reporte |
| `docker run --rm owasp/zap2docker-stable zap-full-scan.py -t http://example.com`                    | Escaneo completo “full-scan”                        |
| `docker run --rm owasp/zap2docker-stable zap-api-scan.py -t http://example.com -f openapi.json`     | Escaneo basado en definición OpenAPI/Swagger        |

---

### `zap-cli` (CLI Python)

> *(Requiere `pip install zap-cli`)*

| Comando                                  | Descripción                                     |
| ---------------------------------------- | ----------------------------------------------- |
| `zap-cli start`                          | Inicia ZAP en modo daemon                       |
| `zap-cli status`                         | Verifica si ZAP está listo                      |
| `zap-cli open-url http://site.com`       | Abre la URL en el navegador interno de ZAP      |
| `zap-cli spider http://site.com`         | Lanza un spider para explorar el sitio          |
| `zap-cli active-scan http://site.com`    | Inicia un escaneo activo                        |
| `zap-cli alerts --output alerts.json`    | Exporta las alertas encontradas en formato JSON |
| `zap-cli report -o reporte.html -f html` | Genera reporte (HTML, XML, Markdown…)           |
| `zap-cli shutdown`                       | Apaga el demonio de ZAP                         |

---

### API Python con `python-owasp-zap-v2.4`

```python
from zapv2 import ZAPv2

zap = ZAPv2(apikey='TU_API_KEY', proxies={'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'})

# 1. Acceder URL
zap.core.access_url('http://example.com', recurse=True)

# 2. Spider
scan_id = zap.spider.scan('http://example.com')
while int(zap.spider.status(scan_id)) < 100:
    pass  # espera

# 3. Active Scan
ascan_id = zap.ascan.scan('http://example.com')
while int(zap.ascan.status(ascan_id)) < 100:
    pass  # espera

# 4. Obtener alertas
alerts = zap.core.alerts()
print(alerts)
```

---

### Comandos de Contexto y Usuarios (API)

| Llamada API                                                                   | Propósito                                  |
| ----------------------------------------------------------------------------- | ------------------------------------------ |
| `zap.context.new_context('MyContext')`                                        | Crea un nuevo contexto                     |
| `zap.context.include_in_context('MyCtx', '.*')`                               | Incluye todas las URLs en el contexto      |
| `zap.authentication.set_authentication_method(contextId, 'formBased', {...})` | Configura método de autenticación          |
| `zap.users.new_user(contextId, 'user1')`                                      | Crea usuario para pruebas de autenticación |
| `zap.users.set_user_enabled(contextId, userId, True)`                         | Activa/desactiva usuario                   |
| `zap.users.set_user_credentials(contextId, userId, {...})`                    | Define credenciales del usuario            |

---

### Comandos de Sesión

| Llamada API                          | Descripción                       |
| ------------------------------------ | --------------------------------- |
| `zap.core.new_session('sesionZAP')`  | Crea nueva sesión                 |
| `zap.core.load_session('sesionZAP')` | Carga sesión previamente guardada |
| `zap.core.save_session('sesionZAP')` | Guarda sesión actual              |

---

### Atajos de Teclado (UI)

| Tecla          | Acción                                            |
| -------------- | ------------------------------------------------- |
| `Ctrl+Shift+S` | Guardar sesión                                    |
| `Ctrl+Shift+L` | Cargar sesión                                     |
| `F12`          | Mostrar/ocultar consola de logs                   |
| `F10`          | Mostrar/ocultar panel de API                      |
| `Ctrl+H`       | Historial de peticiones HTTP                      |
| `Ctrl+T`       | Abrir nueva pestaña de pestañas (Requests/Alerts) |

---

### Generación de Reportes

| Comando CLI                                     | Descripción              |
| ----------------------------------------------- | ------------------------ |
| `report.html` en UI → botón “Generate Report”   | Reporte rápido en HTML   |
| `zap-cli report -o report.md -f md`             | Reporte en Markdown      |
| `zap-api-scan.py --report-file zap-report.html` | Reporte tras escaneo API |

---

#### Tip Extra

* **API Key**: si arrancas en modo daemon, genera una clave con `zap.sh -daemon -config api.key=TU_LLAVE`.
* **Logs Verbosos**: `zap.sh -daemon -config logger.level=DEBUG`.

---
> By CISO oswaldo.diaz

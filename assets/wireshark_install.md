# Instalación de Wireshark

1. **Actualizar repositorios**

   ```bash
   sudo apt update
   ```

2. **Instalar el paquete**

   ```bash
   sudo apt install wireshark
   ```

3. **Permitir capturas sin privilegios root**
   Durante la instalación, te preguntará si los usuarios no-root pueden capturar paquetes. Selecciona **Sí**.
   Si no lo hiciste entonces, ejecuta:

   ```bash
   sudo dpkg-reconfigure wireshark-common
   ```

   Marca **Yes** cuando pregunte.

4. **Agregar tu usuario al grupo `wireshark`**

   ```bash
   sudo usermod -aG wireshark $USER
   ```

   Luego, cierra sesión y vuelve a iniciarla (o reinicia) para que el cambio surta efecto.

---

## Verificar instalación y permisos

1. Comprueba que Wireshark está instalado:

   ```bash
   wireshark --version
   ```

   Debe salir algo como `Wireshark 4.x.x (v4.x.x-release)`.

2. Verifica que puedas listar las interfaces de red sin sudo:

   ```bash
   tshark -D
   ```

   Debe mostrar una lista de interfaces (por ejemplo `1. eth0`, `2. wlan0`, …).

---

## Captura básica con interfaz gráfica

1. **Inicia Wireshark**
   Desde el menú de aplicaciones o:

   ```bash
   wireshark &
   ```

2. **Selecciona la interfaz**
   En la ventana principal verás todas las interfaces activas. Haz doble clic sobre la que quieras monitorear (por ejemplo `eth0` o `wlan0`).

3. **Iniciar captura**
   Se abrirá la vista de paquetes en tiempo real. Para detenerla, haz clic en el botón rojo ■ (Stop).

4. **Guardar captura**
   Ve a **File → Save As…** y elige un nombre, por ejemplo `captura.pcapng`.

---

## Ejemplo práctico: analizar tráfico HTTP

Supongamos que quieres capturar y analizar peticiones HTTP a un servidor web local.

1. **Generar tráfico HTTP**
   En otra terminal:

   ```bash
   curl http://example.com/
   ```

2. **Aplicar filtro de visualización**
   En la caja de filtros de Wireshark, escribe:

   ```
   http.request
   ```

   y presiona Enter. Así verás sólo los paquetes que contienen peticiones HTTP.

3. **Inspeccionar un paquete**

   * Haz clic en un paquete de tipo `GET / HTTP/1.1`.
   * En el panel intermedio verás la jerarquía de protocolos: Ethernet → IP → TCP → HTTP.
   * Expande **Hypertext Transfer Protocol** para leer encabezados como `Host: example.com`, `User-Agent: …`, etc.

4. **Seguir el flujo TCP**
   Con un paquete HTTP seleccionado, haz clic derecho → **Follow → TCP Stream**.
   Verás la conversación completa de solicitud y respuesta en texto plano.

---

## Uso de filtros avanzados

* **Filtrar por dirección IP**

  ```
  ip.addr == 192.168.1.100  
  ```
* **Ver solo paquetes DNS**

  ```
  dns
  ```
* **Capturar sólo TCP en la interfaz (filtro de captura)**
  En “Capture → Options” pon en *Capture filter*:

  ```
  tcp
  ```
* **Mostrar paquetes TLS (HTTPS)**

  ```
  tls
  ```

---

## Captura y análisis desde línea de comandos

1. **Capturar con `tshark`**

   ```bash
   tshark -i wlan0 -f "port 80" -w http_only.pcapng
   ```

   * `-i wlan0`: interfaz
   * `-f "port 80"`: filtro de captura BPF (solo puerto 80)
   * `-w`: escribir a archivo

2. **Leer y filtrar**

   ```bash
   tshark -r http_only.pcapng -Y "http.request" -V
   ```

   * `-r`: leer captura
   * `-Y`: filtro de visualización
   * `-V`: modo verboso (desglosa cada campo)

---

¡Perfecto, Shamara! 🚀 Te preparé un **Cheat Sheet de Wireshark** con los comandos y filtros más usados para análisis de tráfico de red. Lo dividí en secciones prácticas para que sea fácil de consultar.

---

# 📝 Wireshark Cheat Sheet

## 🔹 Comandos básicos en terminal (Linux)

* **Capturar tráfico en interfaz específica:**

  ```bash
  sudo wireshark -i eth0
  ```

* **Listar interfaces disponibles:**

  ```bash
  tshark -D
  ```

* **Captura con `tshark` (modo CLI):**

  ```bash
  tshark -i wlan0 -c 100
  ```

  (captura 100 paquetes en wlan0)

* **Guardar captura:**

  ```bash
  tshark -i eth0 -w captura.pcap
  ```

* **Leer archivo `.pcap`:**

  ```bash
  wireshark captura.pcap
  ```

---

## 🔹 Filtros de captura (aplicados **antes** de capturar)

(Sintaxis tipo `tcpdump`)

* **Host específico:**
  `host 192.168.1.10`
* **Red completa:**
  `net 192.168.1.0/24`
* **Protocolo:**
  `tcp` | `udp` | `icmp`
* **Puerto:**
  `port 80`
* **IP origen/destino:**
  `src host 10.0.0.1`
  `dst host 8.8.8.8`
* **Combinaciones:**
  `tcp port 443 and host 8.8.8.8`

---

## 🔹 Filtros de visualización (aplicados **después** de capturar)

(Sintaxis propia de Wireshark)

### 🔸 Protocolo

* `http` → Solo tráfico HTTP
* `dns` → Consultas DNS
* `icmp` → Pings y mensajes ICMP

### 🔸 IP

* `ip.addr == 192.168.1.5` → Cualquier tráfico de esa IP
* `ip.src == 10.0.0.1` → IP origen
* `ip.dst == 8.8.8.8` → IP destino
* `ip.addr == 192.168.1.5 && tcp.port == 443`

### 🔸 Puertos

* `tcp.port == 80`
* `udp.port == 53`

### 🔸 Contenido

* `http.request` → Solo peticiones HTTP
* `http.response.code == 200` → Respuestas HTTP 200 OK
* `frame contains "password"` → Paquetes que contienen la palabra "password"

### 🔸 Combinaciones

* `ip.src == 192.168.1.5 && tcp.port == 443`
* `(http || dns) && ip.addr == 192.168.1.5`

---

## 🔹 Atajos útiles en interfaz Wireshark

* **Ctrl + E** → Iniciar/detener captura
* **Ctrl + K** → Aplicar filtro
* **Ctrl + Shift + F** → Buscar dentro de paquetes
* **Ctrl + Shift + P** → Estadísticas de protocolo
* **Ctrl + H** → Seguir flujo TCP

---

## 🔹 Estadísticas rápidas

* **Estadísticas → Protocol Hierarchy** → Uso de protocolos
* **Estadísticas → Conversations** → Conversaciones por IP
* **Estadísticas → Endpoints** → Tráfico por dispositivo

---

👉 Este Cheat Sheet cubre lo esencial para capturar, filtrar y analizar tráfico.

¿Quieres que lo prepare en **PDF bonito tipo póster (one-page)** para imprimir o prefieres que te lo organice en **Markdown/tablas** para consulta rápida en digital?


Aquí tienes una **descripción detallada en español** de cada uno de los comandos y utilidades que acompañan a **Wireshark** (CLI y Extcap). Estas herramientas permiten capturar, procesar, convertir y analizar tráfico de red y archivos `.pcap`.

---

# 📘 Comandos de Wireshark y utilidades

### 🔹 `androiddump`

Extcap que permite capturar tráfico desde dispositivos Android conectados mediante **ADB (Android Debug Bridge)**.
Requiere tener instalado el **SDK de Android**. Muy útil para analizar tráfico en apps móviles.

---

### 🔹 `capinfos`

Muestra información detallada de archivos de captura (`.pcap`, `.pcapng`).
Ejemplo de datos: número de paquetes, tamaño del archivo, duración de la captura, timestamps, hashes MD5/SHA, etc.
Se usa para obtener estadísticas rápidas sin abrir Wireshark.

---

### 🔹 `captype`

Identifica y muestra el **tipo de archivo de captura** (formato soportado por Wireshark).
Ejemplo: pcap, pcapng, etc. Útil cuando no se conoce el origen de un archivo.

---

### 🔹 `ciscodump`

Extcap que permite capturar tráfico directamente desde un dispositivo **Cisco** remoto (IOS, IOS-XE, ASA, EPC) mediante **SSH**.
Muy usado por administradores de red para depuración remota.

---

### 🔹 `dumpcap`

Herramienta ligera dedicada únicamente a **capturar tráfico** de red y guardarlo en un archivo.
Wireshark y TShark la usan internamente. Soporta privilegios elevados y rotación de archivos para capturas largas.

---

### 🔹 `editcap`

Permite **editar y/o convertir archivos de captura**.
Funciones: eliminar paquetes, cortar rangos de tiempo, extraer subconjuntos, cambiar formato (pcap ↔ pcapng), anonimizar datos.

---

### 🔹 `etwdump`

Extcap que habilita la captura desde **Event Tracing for Windows (ETW)**, una infraestructura de logging de bajo nivel de Windows.
Se usa para correlacionar eventos del sistema operativo con tráfico de red.

---

### 🔹 `extcap`

Interfaz que permite integrar **herramientas externas** como si fueran interfaces nativas en Wireshark.
Ejemplos: androiddump, ciscodump, wifidump, etwdump.

---

### 🔹 `falcodump`

Extcap que conecta con **Falco**, un motor de seguridad basado en eBPF/Sysdig, y vuelca los logs como si fueran paquetes capturados.
Ideal para análisis de eventos de seguridad en tiempo real.

---

### 🔹 `idl2wrs`

Generador que convierte archivos **CORBA IDL (Interface Definition Language)** en plugins de Wireshark, para decodificar protocolos CORBA personalizados.

---

### 🔹 `mergecap`

Combina dos o más archivos de captura en uno solo.
Se asegura de que los paquetes queden ordenados cronológicamente si es necesario.
Ejemplo: unir capturas de varias interfaces.

---

### 🔹 `mmdbresolve`

Lee direcciones **IPv4 e IPv6** y muestra información de **geolocalización IP** usando bases MaxMind (GeoLite2/GeoIP2).
Ejemplo: `echo 8.8.8.8 | mmdbresolve`

---

### 🔹 `randpkt`

Generador de **paquetes de red aleatorios** con diferentes protocolos.
Muy útil para pruebas de robustez en analizadores de tráfico.

---

### 🔹 `randpktdump`

Extcap que usa `randpkt` para generar **capturas aleatorias** en formato PCAP, simulando tráfico ficticio.

---

### 🔹 `rawshark`

Versión en línea de comandos que procesa paquetes en crudo desde archivos o pipes.
Muestra información en texto plano (sin GUI), útil para scripting y automatización.

---

### 🔹 `reordercap`

Reordena un archivo de captura según las **marcas de tiempo** de los paquetes.
Útil cuando los paquetes se grabaron fuera de orden (ej. varias fuentes de captura).

---

### 🔹 `sshdig`

Extcap que captura **llamadas al sistema** desde un host remoto a través de SSH (usando un binario de captura remoto).
Enfocado en análisis de seguridad y debugging.

---

### 🔹 `sshdump`

Similar a `ciscodump`, permite capturar tráfico desde un **host remoto vía SSH**.
Soporta sistemas genéricos (no solo Cisco). Muy usado para auditoría.

---

### 🔹 `stratoshark`

Analizador de **llamadas al sistema y registros de eventos**, orientado a correlacionar procesos del sistema con el tráfico capturado.

---

### 🔹 `text2pcap`

Convierte un **hexdump ASCII** (copiado de logs, correos, debugging) en un archivo `.pcap` válido.
Útil para reconstruir tráfico a partir de registros textuales.

---

### 🔹 `tshark`

Versión en línea de comandos de Wireshark.
Permite **capturar y analizar tráfico** sin interfaz gráfica.
Muy flexible: filtros, salida en JSON/CSV, integración con scripts.

---

### 🔹 `udpdump`

Extcap que implementa un **receptor UDP**, utilizado para recibir tráfico exportado por dispositivos de red (ej. Aruba routers) y guardarlo en formato PCAP.

---

### 🔹 `wifidump`

Extcap que habilita la captura de **tráfico Wi-Fi** desde un host remoto mediante SSH.
Útil para auditorías inalámbricas distribuidas.

---

### 🔹 `wireshark-filter`

Referencia completa de la **sintaxis de filtros de visualización**.
Ejemplo: `ip.addr == 192.168.1.1 && tcp.port == 443`

---

### 🔹 `wireshark`

La herramienta principal con interfaz gráfica.
Permite **capturar, analizar, filtrar, decodificar y visualizar** tráfico de red en tiempo real o desde archivos.


__________________________

Referencia

> https://www.wireshark.org/docs/

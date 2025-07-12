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

## Comentarios

* **Guarda tus capturas** con nombres y fechas claras (p.ej. `2025-07-12_iface-eth0.pcapng`).
* **Usa filtros de captura** (BPF) para reducir datos redundantes y uso de disco.
* **Aplica filtros de visualización** para centrarte solo en el tráfico que te interesa.
* **Deshabilita la resolución DNS** (View → Name Resolution) si los nombres tardan mucho en resolverse.
* **Anota tus hallazgos** usando comentarios en el archivo: selecciona un paquete → Packet Comment.

__________________________

Referencia

> https://www.wireshark.org/docs/

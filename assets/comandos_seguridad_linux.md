Ubuntu 24.04, al igual que otras distribuciones basadas en Linux, ofrece una gran cantidad de comandos y herramientas enfocadas en la **seguridad del sistema**. A continuación, te presento una lista de los comandos más relevantes relacionados con la seguridad, junto con ejemplos prácticos de su uso.

---

## 🔐 **Comandos para gestión de usuarios y permisos**

### `useradd`, `usermod`, `userdel`
- **Propósito:** Crear, modificar o eliminar usuarios.
- **Ejemplo:**
  ```bash
  sudo useradd -m nuevo_usuario
  sudo passwd nuevo_usuario
  sudo usermod -aG sudo nuevo_usuario
  sudo userdel -r usuario_a_eliminar
  ```

### `groupadd`, `groupdel`, `gpasswd`
- **Propósito:** Gestión de grupos.
- **Ejemplo:**
  ```bash
  sudo groupadd desarrolladores
  sudo gpasswd -a juan desarrolladores
  ```

### `passwd`
- **Propósito:** Cambiar contraseñas de usuarios.
- **Ejemplo:**
  ```bash
  sudo passwd root   # Deshabilitar o cambiar contraseña del root
  ```

### `chage`
- **Propósito:** Configurar expiración de cuentas.
- **Ejemplo:**
  ```bash
  sudo chage -M 90 usuario_seguro  # Expira la cuenta cada 90 días
  ```

---

## 🔒 **Control de acceso y privilegios**

### `sudo`
- **Propósito:** Ejecutar comandos con privilegios elevados.
- **Ejemplo:**
  ```bash
  sudo apt update
  ```

### `visudo`
- **Propósito:** Editar el archivo `/etc/sudoers` de forma segura.
- **Ejemplo:**
  ```bash
  sudo visudo
  ```

### `su`
- **Propósito:** Cambiar a otro usuario (por defecto, root).
- **Ejemplo:**
  ```bash
  su - root
  ```

---

## 🔍 **Auditoría y registro de eventos**

### `journalctl`
- **Propósito:** Ver logs del sistema.
- **Ejemplo:**
  ```bash
  sudo journalctl -u ssh
  ```

### `last`
- **Propósito:** Mostrar últimos inicios de sesión.
- **Ejemplo:**
  ```bash
  last
  ```

### `lastlog`
- **Propósito:** Ver último inicio de sesión de todos los usuarios.
- **Ejemplo:**
  ```bash
  lastlog
  ```

### `auditd` / `ausearch` / `aureport`
- **Propósito:** Auditoría del sistema en tiempo real.
- **Instalación:**
  ```bash
  sudo apt install auditd
  ```
- **Ejemplo:**
  ```bash
  sudo ausearch -k login_attempts
  sudo aureport --summary
  ```

---

## 🔐 **Seguridad de red y firewall**

### `ufw` (Uncomplicated Firewall)
- **Propósito:** Gestionar el firewall.
- **Ejemplo:**
  ```bash
  sudo ufw enable
  sudo ufw status
  sudo ufw allow ssh
  sudo ufw deny from 192.168.1.100
  ```

### `iptables` / `nftables`
- **Propósito:** Reglas de firewall avanzadas.
- **Ejemplo:**
  ```bash
  sudo iptables -L -v
  sudo nft list ruleset
  ```

### `ss` / `netstat`
- **Propósito:** Ver conexiones activas.
- **Ejemplo:**
  ```bash
  ss -tulnp
  netstat -antp
  ```

---

## 🛡️ **Herramientas de detección de intrusos y análisis**

### `fail2ban`
- **Propósito:** Bloquear IPs tras múltiples intentos fallidos de autenticación.
- **Instalación:**
  ```bash
  sudo apt install fail2ban
  ```
- **Ejemplo:**
  ```bash
  sudo systemctl status fail2ban
  sudo fail2ban-client status ssh
  ```

### `chkrootkit` / `rkhunter`
- **Propósito:** Detectar rootkits.
- **Instalación y uso:**
  ```bash
  sudo apt install chkrootkit rkhunter
  sudo rkhunter --check
  sudo chkrootkit
  ```

---

## 🔑 **Cifrado y firma digital**

### `gpg`
- **Propósito:** Cifrar y firmar archivos.
- **Ejemplo:**
  ```bash
  gpg -c archivo_secreto.txt     # Cifra con contraseña
  gpg -d archivo_secreto.txt.gpg # Descifra
  ```

### `openssl`
- **Propósito:** Herramienta para TLS/SSL, generar certificados, cifrado, etc.
- **Ejemplo:**
  ```bash
  openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365
  openssl enc -aes-256-cbc -in file.txt -out file.enc
  ```

---

## 📁 **Permisos de archivos y directorios**

### `chmod`
- **Propósito:** Cambiar permisos.
- **Ejemplo:**
  ```bash
  chmod 600 archivo_privado.txt
  ```

### `chown`
- **Propósito:** Cambiar propietario/grupo.
- **Ejemplo:**
  ```bash
  sudo chown usuario:grupo archivo.txt
  ```

### `getfacl` / `setfacl`
- **Propósito:** Control de listas de acceso extendidas.
- **Ejemplo:**
  ```bash
  setfacl -m u:usuario:r-x carpeta_segura/
  getfacl carpeta_segura/
  ```

---

## 🧼 **Limpieza y revisión del sistema**

### `find`
- **Propósito:** Buscar archivos peligrosos o sin dueño.
- **Ejemplo:**
  ```bash
  find / -nouser -o -nogroup
  find /tmp -perm -o=w
  ```

### `updatedb` / `locate`
- **Propósito:** Buscar archivos rápidamente.
- **Ejemplo:**
  ```bash
  sudo updatedb
  locate .ssh
  ```

---

## 🔄 **Actualizaciones y parcheo**

### `apt`
- **Propósito:** Instalar actualizaciones de seguridad.
- **Ejemplo:**
  ```bash
  sudo apt update && sudo apt upgrade
  sudo apt install unattended-upgrades
  ```

### `unattended-upgrades`
- **Propósito:** Actualizar paquetes automáticamente.
- **Configuración:**
  ```bash
  sudo dpkg-reconfigure -plow unattended-upgrades
  ```

---

## ✅ **Resumen rápido por categorías**

| Categoría | Comandos |
|----------|----------|
| Usuarios y grupos | `useradd`, `usermod`, `passwd`, `groupadd`, `chage` |
| Acceso privilegiado | `sudo`, `visudo`, `su` |
| Logs y auditoría | `journalctl`, `last`, `auditd`, `ausearch` |
| Firewall y redes | `ufw`, `iptables`, `ss`, `netstat` |
| Detección de amenazas | `fail2ban`, `rkhunter`, `chkrootkit` |
| Cifrado | `gpg`, `openssl` |
| Permisos de archivos | `chmod`, `chown`, `setfacl` |
| Limpieza y búsqueda | `find`, `locate` |
| Actualizaciones | `apt`, `unattended-upgrades` |

---

Si necesitas profundizar en alguna categoría específica (como auditoría, cifrado o hardening), dime y puedo darte guías más detalladas.

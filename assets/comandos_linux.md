# Cheat Sheet - Comandos Linux 

---

## Gestión de paquetes (APT)

| Comando                      | Descripción                                 |
| ---------------------------- | ------------------------------------------- |
| `sudo apt update`            | Actualiza la lista de paquetes              |
| `sudo apt upgrade`           | Actualiza todos los paquetes instalados     |
| `sudo apt install <paquete>` | Instala un paquete                          |
| `sudo apt remove <paquete>`  | Elimina un paquete (sin configuraciones)    |
| `sudo apt purge <paquete>`   | Elimina paquete y archivos de configuración |
| `sudo apt autoremove`        | Elimina dependencias huérfanas              |
| `sudo apt search <término>`  | Busca paquetes                              |
| `apt show <paquete>`         | Muestra información de un paquete           |

---

## Navegación de archivos

| Comando                   | Descripción                            |
| ------------------------- | -------------------------------------- |
| `ls`                      | Lista archivos en el directorio actual |
| `ls -l`                   | Lista detallada                        |
| `ls -a`                   | Muestra archivos ocultos               |
| `cd <ruta>`               | Cambia al directorio especificado      |
| `pwd`                     | Muestra el directorio actual           |
| `mkdir <directorio>`      | Crea un directorio                     |
| `rmdir <directorio>`      | Elimina un directorio vacío            |
| `rm <archivo>`            | Elimina un archivo                     |
| `rm -r <directorio>`      | Elimina un directorio y su contenido   |
| `cp <orig> <dest>`        | Copia archivo/directorio               |
| `cp -r <orig> <dest>`     | Copia recursivamente                   |
| `mv <orig> <dest>`        | Mueve o renombra                       |
| `find . -name "<patrón>"` | Busca archivos por nombre              |

---

## Permisos y usuarios

| Comando                               | Descripción                  |
| ------------------------------------- | ---------------------------- |
| `sudo <comando>`                      | Ejecuta como superusuario    |
| `chmod [u/g/o/a][+/-][r/w/x] archivo` | Cambia permisos              |
| `chown <usuario>:<grupo> <archivo>`   | Cambia propietario y grupo   |
| `id`                                  | Muestra tu UID, GID y grupos |
| `whoami`                              | Muestra el usuario actual    |
| `adduser <usuario>`                   | Crea un nuevo usuario        |
| `passwd <usuario>`                    | Cambia contraseña de usuario |
| `usermod -aG <grupo> <usuario>`       | Añade usuario a un grupo     |
| `deluser <usuario>`                   | Elimina un usuario           |

---

## Gestión de procesos

| Comando                     | Descripción                              |
| --------------------------- | ---------------------------------------- |
| `ps aux`                    | Lista procesos en ejecución              |
| `top` / `htop`              | Monitor interactivo de procesos          |
| `kill <PID>`                | Envía SIGTERM a un proceso               |
| `kill -9 <PID>`             | Envía SIGKILL (forzado)                  |
| `pkill <nombre_proceso>`    | Mata procesos por nombre                 |
| `nice -n <valor> <comando>` | Ejecuta con prioridad modificada         |
| `renice <valor> -p <PID>`   | Cambia prioridad de proceso en ejecución |

---

## Redes

| Comando                          | Descripción                                     |
| -------------------------------- | ----------------------------------------------- |
| `ip addr show`                   | Muestra interfaces y direcciones IP             |
| `ip link set <interfaz> up/down` | Activa/desactiva interfaz                       |
| `ping <host>`                    | Envía paquetes ICMP para comprobar conectividad |
| `traceroute <host>`              | Rastrear ruta de paquetes                       |
| `netstat -tulpn` / `ss -tulpn`   | Muestra puertos y sockets en escucha            |
| `curl -I <url>`                  | Obtiene cabeceras HTTP                          |
| `wget <url>`                     | Descarga archivo                                |
| `iptables -L`                    | Lista reglas de firewall (legacy)               |
| `ufw status`                     | Muestra estado de UFW (firewall sencillo)       |
| `sudo ufw allow <puerto>`        | Permite tráfico en el puerto                    |

---

## Almacenamiento y discos

| Comando                               | Descripción                       |
| ------------------------------------- | --------------------------------- |
| `df -h`                               | Espacio en disco (humano)         |
| `du -sh <ruta>`                       | Tamaño de directorio              |
| `lsblk`                               | Lista discos y particiones        |
| `fdisk -l`                            | Información de particiones        |
| `mount <dispositivo> <punto_montaje>` | Monta un dispositivo              |
| `umount <punto_montaje>`              | Desmonta un dispositivo           |
| `mkfs.ext4 <dispositivo>`             | Formatea con ext4                 |
| `blkid`                               | Muestra UUID y tipo de filesystem |

---

## Información del sistema

| Comando          | Descripción                          |                      |
| ---------------- | ------------------------------------ | -------------------- |
| `uname -a`       | Información del kernel               |                      |
| `uname -r`       | Versión del kernel                   |                      |
| `lsb_release -a` | Versión de Ubuntu                    |                      |
| `hostnamectl`    | Info de hostname y sistema operativo |                      |
| \`dmesg          | less\`                               | Registros del kernel |
| `journalctl -e`  | Registros del sistema (systemd)      |                      |
| `free -h`        | Memoria libre y usada                |                      |
| `uptime`         | Tiempo desde el último reinicio      |                      |
| `lscpu`          | Información de CPU                   |                      |

---

## Compresión y Archivos

| Comando                               | Descripción                      |
| ------------------------------------- | -------------------------------- |
| `tar -cvf archivo.tar <archivos>`     | Crea archivo tar                 |
| `tar -xvf archivo.tar`                | Extrae archivo tar               |
| `tar -czvf archivo.tar.gz <archivos>` | Crea tar comprimido con gzip     |
| `tar -xzvf archivo.tar.gz`            | Extrae tar.gz                    |
| `zip archivo.zip <archivos>`          | Comprime en ZIP                  |
| `unzip archivo.zip`                   | Descomprime ZIP                  |
| `gzip <archivo>`                      | Comprime con gzip (orig.arch.gz) |
| `gunzip <archivo>.gz`                 | Descomprime gzip                 |

---

## Edición de texto

| Comando                     | Descripción                     |
| --------------------------- | ------------------------------- |
| `nano <archivo>`            | Editor de texto sencillo        |
| `vim <archivo>`             | Editor de texto avanzado        |
| `gedit <archivo>`           | Editor gráfico (GUI)            |
| `cat <archivo>`             | Muestra contenido de un archivo |
| `less <archivo>`            | Pagina texto (adelante/atrás)   |
| `head -n <N> <archivo>`     | Muestra primeras N líneas       |
| `tail -n <N> <archivo>`     | Muestra últimas N líneas        |
| `grep "<patrón>" <archivo>` | Busca texto                     |

---

## Otros comandos útiles

| Comando                                | Descripción                                  |
| -------------------------------------- | -------------------------------------------- |
| `alias ll='ls -lh'`                    | Define alias permanente (`~/.bashrc`)        |
| `history`                              | Muestra historial de comandos                |
| `ssh user@host`                        | Conexión SSH                                 |
| `scp origen destino`                   | Copia segura de archivos                     |
| `screen` / `tmux`                      | Multiplexor de terminal                      |
| `cron` / `crontab -e`                  | Programación de tareas                       |
| `watch <comando>`                      | Ejecuta y refresca comando cada 2 s          |
| `uptime`                               | Muestra tiempo de actividad y carga promedio |
| `env` / `printenv`                     | Muestra variables de entorno                 |
| `export VAR=valor`                     | Define variable de entorno                   |
| `sudo reboot` / `sudo shutdown -h now` | Reinicio / Apagado del sistema               |

---

> By CISO oswaldo.diaz

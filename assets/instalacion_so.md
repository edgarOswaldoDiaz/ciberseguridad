## **Instalación de Sistemas Operativos en Entornos Físicos**

### **1. ¿Qué es un entorno físico?**

Un entorno físico se refiere al hardware tangible donde se ejecutan los sistemas operativos. Esto incluye computadoras personales, servidores, estaciones de trabajo, equipos industriales, entre otros. A diferencia de los entornos virtuales o en la nube, en los entornos físicos hay un contacto directo con el hardware real, lo que requiere mayor atención en compatibilidad, controladores y configuración del sistema.

---

### **2. Tipos de Sistemas Operativos Comunes en Seguridad**

* **Windows Server / Windows 10/11**
* **Distribuciones Linux (Ubuntu, CentOS, Debian, Kali, etc.)**
* **BSD, Unix (menos común, pero usado en ciertos entornos críticos)**

Claro, Shamara. A continuación te presento una **tabla comparativa de sistemas operativos comunes en entornos físicos**, enfocada en sus características clave relevantes para ciberseguridad:

---

### 🧩 **Tabla: Sistemas Operativos y sus Características para Entornos Físicos**

| **Sistema Operativo**                | **Tipo**                  | **Uso Común**                                           | **Ventajas**                                                                               | **Desventajas**                                                                      | **Herramientas de Seguridad Nativas**                    |
| ------------------------------------ | ------------------------- | ------------------------------------------------------- | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | -------------------------------------------------------- |
| **Windows 10/11**                    | Cliente                   | Estaciones de trabajo, laptops                          | Interfaz amigable, compatibilidad con software comercial, integración con Active Directory | Propenso a malware si no se actualiza, licencia costosa                              | Windows Defender, BitLocker, Firewall, AppLocker         |
| **Windows Server**                   | Servidor                  | Servidores de archivos, AD, DNS, web                    | Gestión centralizada (Group Policy), soporte empresarial, herramientas administrativas     | Mayor consumo de recursos, dependencia de GUI                                        | Windows Defender AV, Group Policy, Hyper-V, WAC          |
| **Ubuntu (Desktop/Server)**          | Cliente/Servidor          | Desarrolladores, servidores web, laboratorios           | Comunidad amplia, libre, estable, versátil, compatible con muchas herramientas open source | Curva de aprendizaje para nuevos usuarios                                            | ufw, AppArmor, fail2ban, iptables, auditd                |
| **Debian**                           | Servidor                  | Servidores estables, entornos críticos                  | Muy estable, conservador en actualizaciones, alta seguridad                                | Software menos actualizado                                                           | SELinux/AppArmor, iptables, fail2ban                     |
| **CentOS / Rocky Linux / AlmaLinux** | Servidor                  | Infraestructura empresarial, servidores corporativos    | Compatible con RHEL, soporte a largo plazo                                                 | Menor soporte de escritorio, CentOS ya no tiene soporte oficial                      | SELinux, firewalld, auditd                               |
| **Kali Linux**                       | Cliente especial          | Pruebas de penetración, laboratorios forenses           | Incluye más de 600 herramientas de hacking ético, soporte para hardware especializado      | No apto como sistema principal, puede ser malinterpretado por políticas corporativas | Nmap, Wireshark, Metasploit, John, etc.                  |
| **Arch Linux**                       | Cliente/Servidor avanzado | Usuarios avanzados, entornos personalizados             | Extremadamente personalizable, muy actualizado                                             | No apto para principiantes, mantenimiento continuo                                   | firewalld, iptables, herramientas de auditoría avanzadas |
| **macOS (Apple)**                    | Cliente                   | Profesionales creativos, desarrollo, dispositivos Apple | Alta integración hardware-software, interfaz pulida, menos malware que Windows             | Hardware propietario, menos soporte empresarial, licencia costosa                    | Gatekeeper, XProtect, FileVault, sandboxing nativo       |
| **FreeBSD**                          | Servidor                  | Firewalls, routers, sistemas embebidos, hosting web     | Seguridad sólida, rendimiento de red, ZFS, jails                                           | Menor compatibilidad con software moderno                                            | pf (packet filter), jails, audit framework               |

---

### ✅ **Notas adicionales:**

* **Sistemas como Ubuntu Server, Debian y Rocky Linux** son ampliamente usados en entornos de ciberseguridad y DevOps por su estabilidad, soporte a largo plazo y compatibilidad con herramientas de seguridad.
* **Kali Linux** es una herramienta más que un sistema operativo de uso diario. Se instala en físico solo cuando se necesita acceso a hardware específico como WiFi o Bluetooth.
* **Windows Server** sigue siendo un estándar en muchas organizaciones, especialmente en redes basadas en Active Directory.
* **macOS** y **FreeBSD** ofrecen altos niveles de seguridad, pero tienen usos más específicos y entornos de hardware limitados.

---

¿Quieres que esta tabla la convierta en un formato editable (Word o Excel), o que forme parte de una presentación para tu diplomado?


---

### **3. Requisitos Previos para la Instalación**

Antes de instalar un sistema operativo, se deben considerar varios aspectos críticos:

#### a. **Compatibilidad de hardware**

* Arquitectura del procesador (32-bit vs. 64-bit)
* Cantidad de RAM y espacio en disco
* Tarjetas de red y controladores

Claro, Shamara. A continuación te presento una **tabla de requisitos previos** para la instalación de los sistemas operativos mencionados anteriormente, considerando factores como arquitectura, RAM mínima, espacio en disco, tipo de sistema de archivos compatible, y medio de instalación habitual:

---

### 🧩 **Tabla: Requisitos Previos para Instalar Sistemas Operativos en Entornos Físicos**

| **Sistema Operativo**          | **Arquitectura**  | **RAM Mínima**            | **Espacio en Disco (mínimo)**   | **Sistema de Archivos Soportado** | **Medio de Instalación Común** |
| ------------------------------ | ----------------- | ------------------------- | ------------------------------- | --------------------------------- | ------------------------------ |
| **Windows 10/11**              | 64 bits           | 4 GB (8 GB recomendado)   | 64 GB (128+ GB recomendado)     | NTFS, FAT32                       | USB booteable, DVD             |
| **Windows Server**             | 64 bits (x64)     | 8 GB (16+ GB recomendado) | 32–50 GB base (más según roles) | NTFS                              | USB, DVD, red (PXE)            |
| **Ubuntu Desktop**             | 64 bits (x86\_64) | 4 GB (8 GB óptimo)        | 25 GB (50+ GB recomendado)      | ext4, Btrfs, XFS                  | USB, DVD                       |
| **Ubuntu Server**              | 64 bits           | 512 MB (2 GB recomendado) | 2 GB (20+ GB recomendado)       | ext4, LVM                         | USB, PXE, red                  |
| **Debian (Desktop/Server)**    | 64 bits           | 512 MB (1 GB mínimo)      | 10 GB (20–30 GB recomendado)    | ext4, XFS, Btrfs                  | USB, DVD, red                  |
| **CentOS / Rocky / AlmaLinux** | 64 bits           | 1 GB (2–4 GB recomendado) | 10 GB mínimo (más si GUI)       | ext4, XFS                         | USB, ISO, red (PXE)            |
| **Kali Linux**                 | 64 bits           | 2 GB (4+ GB recomendado)  | 20 GB (mínimo)                  | ext4, LVM                         | USB booteable                  |
| **Arch Linux**                 | 64 bits           | 512 MB (2 GB recomendado) | 2–5 GB base (personalizable)    | ext4, Btrfs, XFS, F2FS            | USB, netboot                   |
| **macOS (Apple)**              | ARM64 (M1+) / x64 | 4 GB (8+ GB recomendado)  | 35–60 GB                        | APFS, HFS+                        | USB, recuperación de red       |
| **FreeBSD**                    | 64 bits (amd64)   | 512 MB (1 GB recomendado) | 1.5–4 GB mínimo                 | UFS, ZFS                          | USB, DVD, red                  |

---

### ✅ **Notas importantes:**

* **RAM y espacio en disco recomendados** varían según el uso (servidor web, servidor de base de datos, estación de trabajo, etc.).
* Los **entornos sin interfaz gráfica** (como Ubuntu Server o Arch) requieren mucho menos recursos que sus equivalentes con GUI.
* **ZFS y LVM** requieren más memoria y CPU para gestionarse eficientemente, pero ofrecen ventajas de integridad de datos y snapshots.
* Para arquitecturas modernas, casi todos los sistemas están enfocados a **64 bits**, salvo en dispositivos muy antiguos o sistemas embebidos.

---

¿Te gustaría que esta tabla también esté en formato Excel o en un archivo Word como parte de una guía técnica?



#### b. **Medio de instalación**

* USB booteable, DVD, o medios de red (PXE Boot)
* Imagen ISO oficial y verificada (hash MD5/SHA256 para verificar integridad)

#### c. **Planificación del particionado**

* Tabla de particiones: MBR vs. GPT
* Sistema de archivos: NTFS, ext4, xfs, etc.
* Esquema sugerido para seguridad: partición separada para `/home`, `/var`, `/tmp` (en Linux)

---

### **4. Proceso de Instalación Paso a Paso**

#### a. **Preparación del medio de instalación**

* Descargar la imagen ISO del sitio oficial
* Crear USB booteable (herramientas: Rufus, balenaEtcher, dd en Linux)

#### b. **Configuración de la BIOS/UEFI**

* Establecer prioridad de arranque
* Habilitar/disabling Secure Boot o Legacy Mode si es necesario

#### c. **Ejecución del asistente de instalación**

* Elegir idioma, teclado y zona horaria
* Particionar el disco (manual o automático)
* Crear usuario(s) y establecer contraseñas seguras
* Seleccionar software adicional (servidores, herramientas de red, etc.)

#### d. **Instalación del sistema operativo**

* Copia de archivos
* Instalación del gestor de arranque (GRUB, Windows Boot Manager)
* Reinicio y verificación del arranque correcto


Claro, Shamara. A continuación te presento una **tabla comparativa detallada del proceso de instalación paso a paso** para los sistemas operativos **Microsoft Windows 11** y **Ubuntu 24.04 LTS**, enfocada en entornos físicos:

---

### 🧩 **Tabla: Proceso de Instalación Paso a Paso – Windows 11 vs Ubuntu 24.04**

| **Etapa**                                 | **Windows 11**                                                                                                                                                            | **Ubuntu 24.04 LTS**                                                                                                                                     |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1. Preparación del medio**              | Descargar la ISO desde el sitio oficial de Microsoft y crear un USB booteable con **Rufus** u otra herramienta.                                                           | Descargar la ISO desde el sitio oficial de Ubuntu. Crear un USB booteable con **balenaEtcher**, **Startup Disk Creator** o **Rufus**.                    |
| **2. Configuración de BIOS/UEFI**         | Entrar a BIOS/UEFI (tecla DEL/F2). Habilitar **UEFI**, deshabilitar Secure Boot si se usan controladores no firmados. Establecer USB como primer dispositivo de arranque. | Igual que en Windows: configurar **UEFI**, y opcionalmente deshabilitar Secure Boot si se requiere. Elegir USB como prioridad de arranque.               |
| **3. Arranque desde USB**                 | El sistema inicia el instalador gráfico de Windows.                                                                                                                       | El sistema inicia el instalador de Ubuntu ("Try Ubuntu" o "Install Ubuntu").                                                                             |
| **4. Configuración regional e idioma**    | Selección de idioma, zona horaria, distribución del teclado.                                                                                                              | Igual: seleccionar idioma, zona horaria, distribución de teclado.                                                                                        |
| **5. Licencia y requisitos**              | Aceptar los términos de licencia de Microsoft. Se verifica si el equipo cumple con TPM 2.0 y Secure Boot.                                                                 | No requiere aceptar una licencia propietaria. Se omite verificación de hardware TPM.                                                                     |
| **6. Tipo de instalación**                | Seleccionar: actualización o instalación limpia. En instalación limpia, se elige el disco y se formatea (NTFS).                                                           | Elegir: instalación normal o mínima. Puede instalar software de terceros (drivers, codecs). Elegir disco y crear particiones manual o automática (ext4). |
| **7. Particionamiento del disco**         | Crear/seleccionar particiones (automático o manual). Requiere al menos una partición principal NTFS.                                                                      | Particionamiento automático o manual. Suele crearse al menos: `/`, `/home`, `swap`.                                                                      |
| **8. Configuración de usuario**           | Crear nombre de usuario y contraseña. Puede asociarse a cuenta Microsoft o crear cuenta local.                                                                            | Crear usuario, contraseña y nombre del equipo. No se requiere cuenta en línea.                                                                           |
| **9. Instalación del sistema**            | Copia de archivos, instalación de funciones del sistema, configuración de servicios. Reinicia automáticamente.                                                            | Copia de archivos, instalación del sistema base, configuración de GRUB. Reinicia automáticamente.                                                        |
| **10. Post-instalación**                  | Primera configuración: privacidad, red, idioma adicional, inicio de sesión. Se puede integrar a red corporativa.                                                          | Finaliza configuración: actualizaciones, instalación de controladores adicionales y configuración del sistema.                                           |
| **11. Seguridad inicial sugerida**        | Activar Windows Update, habilitar firewall, activar BitLocker si es posible, revisar Defender.                                                                            | Ejecutar `sudo apt update && sudo apt upgrade`, habilitar UFW (`ufw enable`), revisar usuarios y servicios habilitados.                                  |
| **12. Instalación de software adicional** | Usar Microsoft Store o instaladores `.exe` de fuentes confiables.                                                                                                         | Usar `apt`, Ubuntu Software o instalar paquetes `.deb` firmados.                                                                                         |

---

### ✅ **Observaciones importantes:**

* **Windows 11** es más exigente con los requisitos de hardware (TPM 2.0, Secure Boot, CPU compatible).
* **Ubuntu 24.04** permite mayor flexibilidad, especialmente en máquinas más antiguas.
* Ubuntu puede usarse como **LiveCD** para probar el sistema antes de instalar.
* Ambas plataformas pueden configurarse de forma segura post-instalación, pero Ubuntu ofrece más control técnico por defecto.

---

¿Te gustaría que esta tabla se convierta en una guía en PDF o en una presentación? También puedo crear un checklist práctico para laboratorio.



---

### **5. Recomendaciones de Seguridad Iniciales**

Una vez instalado el sistema operativo, es crucial asegurar el entorno antes de ponerlo en producción:

#### a. **Aplicación de parches y actualizaciones**

* Usar repositorios oficiales o WSUS (en Windows)

#### b. **Creación de usuarios con principio de mínimo privilegio**

* Evitar uso continuo del usuario root o administrador

#### c. **Desactivación de servicios innecesarios**

* Evaluar qué servicios se ejecutan por defecto
* Deshabilitar puertos abiertos innecesarios

#### d. **Instalación de herramientas de seguridad**

* Firewall (ufw, firewalld, Windows Defender Firewall)
* Antivirus y/o EDR
* SSH seguro: deshabilitar root login, usar autenticación por clave

#### e. **Auditoría básica del sistema**

* Comprobación de logs de instalación
* Configuración de syslog o herramientas SIEM para eventos futuros


¡Con gusto, Shamara! A continuación te presento una descripción detallada de las **recomendaciones iniciales de seguridad** que deben aplicarse en **Windows 11** y **Ubuntu 24.04 LTS**, una vez instalado el sistema operativo en un entorno físico, con el fin de establecer una base sólida para un entorno seguro.

---

## 🔐 Recomendaciones Iniciales de Seguridad

### 🪟 **Windows 11**

| **Categoría**                             | **Recomendación**                                                                                                                                                                  |
| ----------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Actualizaciones del sistema**           | - Activar Windows Update y configurar la instalación automática de actualizaciones de seguridad.<br>- Verificar parches acumulativos y drivers.                                    |
| **Antivirus y protección en tiempo real** | - Verificar que **Microsoft Defender** esté activo.<br>- Configurar la protección contra ransomware y el control de acceso a carpetas.                                             |
| **Cifrado de disco**                      | - Activar **BitLocker** para cifrar la unidad de disco. Especialmente crítico en equipos portátiles.                                                                               |
| **Firewall**                              | - Verificar que el **Firewall de Windows** esté activo en todos los perfiles (privado, público, dominio).<br>- Crear reglas específicas según servicios permitidos.                |
| **Control de cuentas de usuario (UAC)**   | - Mantener UAC habilitado en nivel alto para evitar elevación de privilegios sin confirmación.                                                                                     |
| **Cuentas de usuario**                    | - Usar cuentas **con permisos limitados** para tareas diarias.<br>- Deshabilitar cuentas predeterminadas innecesarias.<br>- Usar autenticación con PIN, Windows Hello o biometría. |
| **Contraseñas seguras**                   | - Establecer políticas de contraseñas fuertes (mínimo 12 caracteres, complejas y rotación periódica).                                                                              |
| **Microsoft Defender SmartScreen**        | - Activar para protección contra sitios web maliciosos y aplicaciones no verificadas.                                                                                              |
| **Aplicaciones y servicios**              | - Desinstalar software innecesario.<br>- Restringir servicios que no se usan (por ejemplo, Remote Desktop si no es requerido).                                                     |
| **Registro de eventos**                   | - Activar y revisar el **Visor de eventos**, especialmente eventos relacionados con inicios de sesión, fallos y cambios de políticas.                                              |

---

### 🐧 **Ubuntu 24.04 LTS**

| **Categoría**                                | **Recomendación**                                                                                                                                       |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Actualizaciones del sistema**              | - Ejecutar `sudo apt update && sudo apt upgrade` tras la instalación.<br>- Habilitar actualizaciones automáticas con `unattended-upgrades`.             |
| **Firewall**                                 | - Activar **UFW** (Uncomplicated Firewall):<br>`sudo ufw enable`<br>`sudo ufw default deny incoming`<br>`sudo ufw allow ssh` (si es necesario).         |
| **Cuentas de usuario**                       | - Evitar usar el usuario root directamente.<br>- Crear cuentas con permisos limitados y usar `sudo` para tareas administrativas.                        |
| **Contraseñas seguras**                      | - Usar contraseñas fuertes y únicas.<br>- Configurar expiración de contraseñas si es un entorno multiusuario.                                           |
| **Cifrado de disco**                         | - Si no se activó durante la instalación, considerar cifrar particiones con **LUKS**.<br>- Cifrar directorios sensibles como `/home` si aplica.         |
| **Servicios y puertos**                      | - Revisar servicios activos con `ss -tuln` o `netstat -tulnp`.<br>- Deshabilitar servicios innecesarios con `systemctl disable nombre-servicio`.        |
| **Actualización del kernel y software base** | - Hacer uso de `sudo apt full-upgrade` periódicamente.<br>- Verificar vulnerabilidades del kernel.                                                      |
| **Auditoría de seguridad**                   | - Instalar y configurar herramientas como **Fail2Ban**, **rkhunter** y **chkrootkit**.                                                                  |
| **Protecciones adicionales**                 | - Activar **AppArmor** o configurar **SELinux** (aunque AppArmor viene habilitado por defecto).<br>- Usar `auditd` para monitorear eventos del sistema. |
| **Registro de eventos**                      | - Configurar revisión de logs con `journalctl` y `logrotate`.<br>- Monitorear accesos fallidos con `lastb` y `faillog`.                                 |

---

## 🧠 Buenas prácticas generales

* **Principio de mínimo privilegio:** Solo los usuarios que lo requieran deben tener permisos elevados.
* **Segmentación de red:** Aislar servicios críticos en diferentes subredes (por ejemplo, acceso SSH, bases de datos, escritorio remoto).
* **Educación del usuario:** Capacitar sobre ingeniería social, phishing, y prácticas de navegación segura.

---

¿Te gustaría que compile estas recomendaciones en una guía visual o formato PDF como parte del material de tu diplomado? También puedo incluir scripts básicos de hardening para ambos sistemas.



---

### **6. Aplicación en Ciberseguridad**

Instalar un sistema operativo de manera segura en un entorno físico es un paso fundamental en cualquier infraestructura de seguridad. Una instalación mal hecha puede dejar puertas abiertas desde el primer día. Además:

* Permite establecer un sistema base sólido para aplicar políticas de hardening
* Facilita el cumplimiento de normativas como ISO 27001, NIST, o CIS Benchmarks
* Sirve como base para implementar servidores de monitoreo, firewalls, o honeypots

---

### **7. Casos de Uso**

* Estaciones de trabajo seguras para analistas SOC
* Equipos de administración para servidores en red interna
* Servidores de archivos, DNS, correo o controladores de dominio en redes empresariales

---

¿Te gustaría que prepare también una presentación en PowerPoint o una ficha técnica basada en esta explicación?


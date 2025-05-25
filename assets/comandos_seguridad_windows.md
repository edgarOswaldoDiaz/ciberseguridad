## **Comandos y Herramientas de Seguridad en microsoft Windows 11**

### **`net user`** Muestra información sobre cuentas de usuario locales.

#### Ejemplo:
```cmd
net user
```
Muestra todos los usuarios del sistema.

```cmd
net user Administrador
```
Muestra detalles del usuario "Administrador".

---

### **`net localgroup`** Muestra o modifica grupos locales.

#### Ejemplo:
```cmd
net localgroup Usuarios
```
Muestra los miembros del grupo "Usuarios".

```cmd
net localgroup Usuarios nombreUsuario /add
```
Agrega un usuario al grupo "Usuarios".

---

### **`whoami`** Muestra el nombre del usuario actual o información detallada del token de seguridad.

#### Ejemplo:
```cmd
whoami
```
Muestra el nombre del usuario actual.

```cmd
whoami /priv
```
Muestra privilegios del usuario actual (ej.: SeDebugPrivilege, SeShutdownPrivilege).

---

### **`sc` (Service Control)** Permite gestionar servicios del sistema, útiles para revisar o deshabilitar servicios potencialmente peligrosos.

#### Ejemplo:
```cmd
sc query winmgmt
```
Consulta el estado del servicio WMI (Windows Management Instrumentation).

```cmd
sc config winmgmt start= disabled
```
Deshabilita el arranque automático del servicio WMI.

---

### **`icacls`** Controla permisos de archivos y carpetas.

#### Ejemplo:
```cmd
icacls C:\Users\Public\Documentos
```
Muestra los permisos NTFS de la carpeta especificada.

```cmd
icacls C:\Datos /grant Usuarios:F
```
Otorga permiso total (F = Full control) al grupo "Usuarios" sobre la carpeta Datos.

---

### **`auditpol` (Security Policy Audit)** Configura y muestra políticas de auditoría del sistema.

#### Ejemplo:
```cmd
auditpol /get /category:*
```
Muestra todas las categorías de auditoría activas.

```cmd
auditpol /set /category:"Logon/Logoff" /success:enable /failure:enable
```
Activa la auditoría de inicio de sesión exitoso y fallido.

---

### **`secedit`** Herramienta avanzada para exportar, analizar e importar configuraciones de seguridad.

#### Ejemplo:
```cmd
secedit /export /cfg c:\seg.cfg
```
Exporta la política de seguridad actual a un archivo.

```cmd
secedit /validate c:\seg.cfg
```
Valida que el archivo de configuración tenga formato correcto.

---

### **`gpresult`** Muestra información sobre las políticas de grupo aplicadas.

#### Ejemplo:
```cmd
gpresult /r
```
Muestra resumen de políticas de grupo aplicadas al usuario y equipo.

```cmd
gpresult /H report.html
```
Genera un informe HTML detallado sobre políticas de grupo.

---

### **`powershell Get-NetFirewallRule`** Muestra reglas del firewall de Windows.

#### Ejemplo:
```powershell
Get-NetFirewallRule -Name "RemoteDesktop*"
```
Muestra las reglas del firewall relacionadas con Escritorio Remoto.

```powershell
Get-NetFirewallRule -Direction Inbound | Where-Object {$_.Action -eq "Allow"}
```
Lista todas las reglas entrantes permitidas.

---

### **`certutil`** Utilidad para gestionar certificados y la infraestructura de clave pública (PKI).

#### Ejemplo:
```cmd
certutil -viewstore -user root
```
Muestra los certificados raíz confiados por el usuario actual.

```cmd
certutil -hashfile C:\ruta\archivo.exe SHA256
```
Calcula el hash SHA256 de un archivo para verificar su integridad.

---

### **`cipher`** Administra cifrado EFS (Encrypting File System).

#### Ejemplo:
```cmd
cipher /c C:\Users\Public\Archivo.txt
```
Muestra si un archivo está cifrado.

```cmd
cipher /w:C:\Datos
```
Limpia espacios no asignados en la carpeta especificada para evitar recuperación de datos borrados.

---

### **`sfc` y `DISM`** Herramientas para reparar archivos del sistema (integridad del sistema).

#### Ejemplo:
```cmd
sfc /scannow
```
Escanea y repara archivos del sistema dañados.

```cmd
DISM /Online /Cleanup-Image /RestoreHealth
```
Repara la imagen del sistema operativo antes de ejecutar `sfc`.

---

### **`wmic`** *(Obsoleto en futuras versiones, pero aún funcional en Win11)* Herramienta para consultar hardware y software del sistema.

#### Ejemplo:
```cmd
wmic startup list full
```
Muestra programas que inician automáticamente.

```cmd
wmic process list brief
```
Lista procesos activos.

---

### **`netsh advfirewall`** Gestiona configuración del firewall avanzado.

#### Ejemplo:
```cmd
netsh advfirewall firewall add rule name="Bloquear Puerto 80" dir=in action=block protocol=TCP localport=80
```
Bloquea conexiones entrantes en el puerto TCP 80.

```cmd
netsh advfirewall set currentprofile state on
```
Activa el firewall en el perfil actual.

---

### **`eventvwr`** Accede al Visor de eventos, útil para revisar logs de seguridad.

#### Ejemplo:
```cmd
eventvwr
```
Abre el visor de eventos.

En la interfaz puedes navegar a:
> **Windows Logs > Security**  
Para ver eventos como logins, cambios de contraseña, auditorías, etc.

---

## Recomendaciones Adicionales

- Usar **PowerShell** en lugar de CMD cuando sea posible, ya que ofrece mayor flexibilidad.
- Siempre ejecutar estos comandos desde una **consola con permisos elevados (como administrador)**.
- En entornos empresariales, combinar con **Group Policy (GPO)** para políticas centralizadas.

-------

Referencias Arbitradas 

> Microsoft Corporation. (2023). *Command-Line Reference*. Recuperado de https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/windows-commands

> Microsoft Corporation. (2023). *Secedit command*. Recuperado de https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/secedit

> Microsoft Corporation. (2023). *Auditpol command-line options*. Recuperado de https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/auditpol

> Microsoft Corporation. (2023). *Net User*. Recuperado de https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/net-user

> Microsoft Corporation. (2023). *Whoami*. Recuperado de https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/whoami

> Microsoft Corporation. (2023). *Icacls*. Recuperado de https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/icacls

> Microsoft Corporation. (2023). *Net Localgroup*. Recuperado de https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/net-localgroup

> Microsoft Corporation. (2023). *Using the SC tool*. Recuperado de https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/sc-config

> Microsoft Corporation. (2023). *Windows PowerShell cmdlets for the firewall*. Recuperado de https://learn.microsoft.com/en-us/powershell/module/netsecurity/?view=windowsserver2022-ps

> Microsoft Corporation. (2023). *Certutil*. Recuperado de https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/certutil

> Microsoft Corporation. (2023). *Cipher*. Recuperado de https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/cipher

> Microsoft Corporation. (2023). *SFC (System File Checker)*. Recuperado de https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/sfc

> Microsoft Corporation. (2023). *Deployment Image Servicing and Management (DISM)*. Recuperado de https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/dism---deployment-image-servicing-and-management

> Microsoft Corporation. (2023). *Netsh commands for Windows Firewall*. Recuperado de https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/hh831484(v=ws.11)

> Microsoft Corporation. (2023). *Event Viewer*. Recuperado de https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/eventvwr

> Kim, D., & Solomon, M. G. (2021). *Fundamentals of Windows Security*. Sybex.

> Rhodes-Ousley, M. (2022). *Windows Server 2022: Administering Essential Administration Tasks*. Apress.

>Basta, A., Zgola, M., & Stavroulakis, P. (2021). *Computer and Information Security Handbook* (3rd ed.). Morgan Kaufmann.

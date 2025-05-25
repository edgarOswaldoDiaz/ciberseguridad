# **Registro y Gestión de Usuarios en Sistemas Operativos**

En un entorno de ciberseguridad, la gestión de usuarios es fundamental para mantener la seguridad de los sistemas operativos. Esto incluye la creación, modificación, eliminación y auditoría de cuentas de usuario, así como la asignación de permisos adecuados para evitar accesos no autorizados.

## **Gestión de Usuarios en Linux**

En Linux, los usuarios y grupos se gestionan mediante comandos en terminal. La información de usuarios se almacena en los archivos:
- `/etc/passwd` → Datos de usuarios.
- `/etc/shadow` → Contraseñas encriptadas.
- `/etc/group` → Grupos del sistema.

### **Creación de Usuarios**
Para crear un usuario en Linux, se usa el comando `useradd` o `adduser` (dependiendo de la distribución).

#### **Ejemplo: Crear un usuario**
```bash
sudo useradd -m -s /bin/bash usuario1
```
- `-m`: Crea el directorio home del usuario (`/home/usuario1`).
- `-s /bin/bash`: Establece la shell por defecto.

#### **Establecer contraseña**
```bash
sudo passwd usuario1
```
Se pedirá ingresar y confirmar la nueva contraseña.

---

### **Modificación de Usuarios**
El comando `usermod` permite modificar propiedades de un usuario existente.

#### **Ejemplo: Cambiar el shell del usuario**
```bash
sudo usermod -s /usr/sbin/nologin usuario1
```
(Impide que el usuario inicie sesión interactiva).

#### **Ejemplo: Añadir un usuario a un grupo secundario**
```bash
sudo usermod -aG sudo usuario1
```
(Agrega `usuario1` al grupo `sudo`, permitiéndole ejecutar comandos como administrador).

---

### **Eliminación de Usuarios**
Para eliminar un usuario, se usa `userdel`.

#### **Ejemplo: Eliminar un usuario y su directorio home**
```bash
sudo userdel -r usuario1
```
- `-r`: Elimina también el directorio `/home/usuario1`.

---

### **Gestión de Grupos**
Los grupos permiten asignar permisos a múltiples usuarios.

#### **Crear un grupo**
```bash
sudo groupadd desarrolladores
```

#### **Añadir usuario a un grupo**
```bash
sudo usermod -aG desarrolladores usuario1
```

#### **Ver grupos de un usuario**
```bash
groups usuario1
```

---

### **Bloquear y Desbloquear Usuarios**
Para evitar accesos no autorizados, se puede bloquear una cuenta.

#### **Bloquear usuario**
```bash
sudo passwd -l usuario1
```
(Desactiva la autenticación por contraseña).

#### **Desbloquear usuario**
```bash
sudo passwd -u usuario1
```

---

## **Gestión de Usuarios en Windows**

En Windows, la gestión de usuarios puede realizarse mediante:
- **Interfaz gráfica** (Administración de equipos).
- **CMD** (Command Prompt) o **PowerShell**.

### **2.1. Creación de Usuarios en CMD**
#### **Ejemplo: Crear un nuevo usuario**
```cmd
net user usuario1 P@ssw0rd /add
```
- `usuario1`: Nombre del usuario.
- `P@ssw0rd`: Contraseña asignada.

#### **Añadir usuario al grupo "Administradores"**
```cmd
net localgroup Administradores usuario1 /add
```

---

### **Modificación de Usuarios**
#### **Cambiar contraseña**
```cmd
net user usuario1 N3wP@ssw0rd
```

#### **Deshabilitar una cuenta**
```cmd
net user usuario1 /active:no
```

#### **Eliminar un usuario**
```cmd
net user usuario1 /delete
```

---

### **Gestión de Grupos en PowerShell**
PowerShell ofrece mayor flexibilidad para administrar usuarios.

#### **Listar todos los usuarios**
```powershell
Get-LocalUser
```

#### **Crear un nuevo usuario**
```powershell
New-LocalUser -Name "usuario2" -Password (ConvertTo-SecureString "P@ssw0rd" -AsPlainText -Force)
```

#### **Añadir usuario a un grupo**
```powershell
Add-LocalGroupMember -Group "Administradores" -Member "usuario2"
```

---

## **Buenas Prácticas de Seguridad en la Gestión de Usuarios**

**Principio de Mínimo Privilegio**: Asignar solo los permisos necesarios.
   - En Linux: Evitar usar `sudo` para usuarios normales.
   - En Windows: No asignar a todos el grupo "Administradores".

**Contraseñas Seguras**:
   - Usar `passwd` en Linux o `net user` en Windows para exigir complejidad.
   - Ejemplo en Linux para configurar política de contraseñas:
     ```bash
     sudo nano /etc/login.defs
     ```
     (Modificar `PASS_MAX_DAYS`, `PASS_MIN_DAYS`, etc.).

**Auditoría de Usuarios**:
   - En Linux: `last` (muestra últimos inicios de sesión).
   - En Windows: `Get-EventLog -LogName Security` (PowerShell).

**Deshabilitar Cuentas Innecesarias**:
   - En Linux: `usermod -L` o `passwd -l`.
   - En Windows: `net user /active:no`.


---
Referencias bibliográficas arbitradas 

> **Nemeth, E., Snyder, G., Hein, T. R., Whaley, B., & Mackin, D.** (2017). *UNIX and Linux System Administration Handbook* (5th ed.). Pearson.  
   - **Relevancia**: Cubre administración de usuarios en Linux, permisos, seguridad y hardening de sistemas.  

> **Microsoft.** (2021). *Windows Server Administration Fundamentals*. Microsoft Press.  
   - **Relevancia**: Explica gestión de usuarios en entornos Windows, políticas de grupo y seguridad.  

> **Stallings, W., & Brown, L.** (2018). *Computer Security: Principles and Practice* (4th ed.). Pearson.  
   - **Relevancia**: Fundamentos de seguridad en sistemas operativos, incluyendo autenticación y control de acceso.  

> **Shotts, W.** (2019). *The Linux Command Line: A Complete Introduction* (2nd ed.). No Starch Press.  
   - **Relevancia**: Detalla comandos esenciales para gestión de usuarios en Linux (`useradd`, `usermod`, `passwd`, etc.).  

> **Easttom, C.** (2020). *Computer Security Fundamentals* (4th ed.). Pearson IT Certification.  
   - **Relevancia**: Aborda buenas prácticas en gestión de usuarios, hardening y mitigación de riesgos.  

## **¿Qué son las políticas de seguridad?**  
Son un conjunto de reglas y configuraciones predefinidas que determinan cómo un sistema operativo (SO) debe gestionar:  
- **Autenticación y acceso** (quién puede ingresar y con qué privilegios).  
- **Contraseñas** (complejidad, caducidad, historial).  
- **Auditoría** (registro de eventos como inicios de sesión, cambios críticos).  
- **Configuración de servicios y firewall** (qué puertos y aplicaciones están permitidos).  
- **Cifrado de datos** (protección de información sensible).  

Estas políticas pueden aplicarse en sistemas **Microsoft Windows, Linux o en la nube** (AWS, Azure, GCP).

## **Tipos de políticas de seguridad**  

### **Políticas de contraseñas**  
- **Longitud mínima**: Ej. 12 caracteres.  
- **Complejidad**: Uso de mayúsculas, números y símbolos.  
- **Caducidad**: Cambio obligatorio cada 90 días.  
- **Historial**: Evitar reutilización de contraseñas anteriores.  

**Ejemplo en Windows**:  
```  
Local Security Policy → Account Policies → Password Policy  
```  
**Ejemplo en Linux**:  
```  
/etc/pam.d/common-password (configurar módulos PAM)  
```  

### **Políticas de bloqueo de cuentas**  
- **Límite de intentos fallidos**: Bloqueo tras 5 intentos.  
- **Tiempo de bloqueo**: 30 minutos antes de permitir reintento.  

**Ejemplo en Windows**:  
```  
Account Lockout Policy → Lockout threshold: 5 attempts  
```  

### **Políticas de auditoría (Logging)**  
Registrar eventos como:  
- Inicios de sesión exitosos/fallidos.  
- Cambios en permisos o archivos críticos.  

**Ejemplo en Linux**:  
```  
auditd (herramienta de auditoría)  
```  

### **Políticas de firewall**  
- **Reglas de entrada/salida**: Permitir solo puertos necesarios (ej. SSH 22, HTTP 80).  
- **Denegar tráfico no autorizado**.  

**Ejemplo en Windows**:  
```  
Windows Defender Firewall → Advanced Settings  
```  
**Ejemplo en Linux**:  
```  
iptables / ufw (Uncomplicated Firewall)  
```  

### **Políticas de cifrado**  
- **BitLocker (Windows)** o **LUKS (Linux)** para discos.  
- **SSL/TLS** para comunicaciones seguras.  

# Comandos de seguridad 

- [Comando de seguridad en Ms. Windows](assets/comandos_seguridad_windows.md)
- [Comandos de seguridad en Ubuntu - Linux](assets/comandos_seguridad_linux.md)

______________

Referencias arbitradas 

> **National Institute of Standards and Technology (NIST)**. (2020). *Security and Privacy Controls for Information Systems and Organizations* (NIST Special Publication 800-53, Revision 5). U.S. Department of Commerce.  
   - **Enlace**: [https://doi.org/10.6028/NIST.SP.800-53r5](https://doi.org/10.6028/NIST.SP.800-53r5)  
   - **Relevancia**: Estándar para políticas de seguridad, controles de acceso y auditoría.  

> **Microsoft**. (2022). *Windows 10 and Windows 11 Security Baseline*. Microsoft Docs.  
   - **Enlace**: [https://docs.microsoft.com/en-us/windows/security/threat-protection/security-compliance-toolkit-10](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-compliance-toolkit-10)  
   - **Relevancia**: Guía oficial para políticas de seguridad en Windows (Password Policy, Account Lockout, Firewall).  

> **Center for Internet Security (CIS)**. (2023). *CIS Benchmarks: Hardening Guidelines for Linux and Windows*.  
   - **Enlace**: [https://www.cisecurity.org/cis-benchmarks/](https://www.cisecurity.org/cis-benchmarks/)  
   - **Relevancia**: Configuraciones recomendadas para hardening de SO (ej. `/etc/pam.d/`, `iptables`).  

> **Amazon Web Services (AWS)**. (2021). *AWS Security Best Practices*. AWS Whitepapers.  
   - **Enlace**: [https://docs.aws.amazon.com/whitepapers/latest/aws-security-best-practices/welcome.html](https://docs.aws.amazon.com/whitepapers/latest/aws-security-best-practices/welcome.html)  
   - **Relevancia**: Políticas de IAM, Security Groups y cifrado en la nube.  

> **Stallings, W., & Brown, L.** (2018). *Computer Security: Principles and Practice* (4th ed.). Pearson.  
   - **ISBN**: 978-0134794105  
   - **Relevancia**: Fundamentos teóricos de políticas de seguridad, autenticación y auditoría (capítulos 4 y 5).  

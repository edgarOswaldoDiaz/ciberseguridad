# **Seguridad en Microsoft Windows Server**

## **1.1. Introducción y Objetivos**
La seguridad en Windows Server es fundamental para proteger los recursos críticos de una organización, como datos, aplicaciones y servicios. Los objetivos principales incluyen:

- **Proteger la infraestructura** contra amenazas internas y externas.
- **Garantizar la confidencialidad, integridad y disponibilidad** de los datos.
- **Implementar políticas de seguridad** basadas en estándares como CIS Benchmarks o Microsoft Security Baselines.
- **Auditar y monitorear** el cumplimiento de las políticas de seguridad.

---

## **1.2. Seguridad en Windows Server**
Windows Server incluye múltiples características de seguridad integradas, como:

- **Firewall de Windows:**  
  Configuración básica de reglas de entrada/salida.  
  ```powershell
  # Habilitar el firewall
  Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled True

  # Agregar una regla de entrada para permitir tráfico HTTP
  New-NetFirewallRule -DisplayName "Allow HTTP" -Direction Inbound -Protocol TCP -LocalPort 80 -Action Allow
  ```

- **BitLocker:**  
  Cifrado de discos para proteger datos sensibles.  
  ```powershell
  # Habilitar BitLocker en un volumen
  Enable-BitLocker -MountPoint "C:" -EncryptionMethod Aes256 -UsedSpaceOnly
  ```

- **Windows Defender Antivirus:**  
  Protección contra malware.  
  ```powershell
  # Actualizar firmas de Defender
  Update-MpSignature

  # Ejecutar un escaneo rápido
  Start-MpScan -ScanType Quick
  ```

---

## **1.3. Seguridad en Active Directory. Políticas Base**
Active Directory (AD) es un componente crítico que requiere políticas de seguridad robustas:

### **Políticas de Grupo (GPOs)**
- **Política de Contraseñas:**  
  ```powershell
  # Configurar longitud mínima de contraseña (8 caracteres)
  Set-ADDefaultDomainPasswordPolicy -Identity dominio.com -MinPasswordLength 8 -ComplexityEnabled $true
  ```

- **Bloquear cuentas tras intentos fallidos:**  
  ```powershell
  # Configurar bloqueo de cuenta tras 5 intentos fallidos
  Set-ADAccountPolicy -Identity dominio.com -LockoutThreshold 5 -LockoutDuration 00:30:00
  ```

### **Política de Auditoría**
- **Habilitar auditoría de eventos críticos:**  
  ```powershell
  # Auditar inicio de sesión fallido
  Auditpol /set /subcategory:"Logon" /failure:enable
  ```

---

## **1.4. Analizadores de Políticas Base**
Herramientas para evaluar el cumplimiento de políticas de seguridad:

### **Microsoft Security Compliance Toolkit (SCT)**
  - Incluye herramientas como **Policy Analyzer** para comparar GPOs.  
  ```powershell
  # Descargar plantillas de seguridad de Microsoft
  Invoke-WebRequest -Uri "https://aka.ms/securitybaselines" -OutFile "C:\baselines.zip"
  ```

### **LGPO (Local Group Policy Object)**
  - Permite aplicar políticas desde la línea de comandos.  
  ```powershell
  # Importar una política de seguridad desde un archivo
  LGPO.exe /g "C:\SecurityPolicy\GPOBackup"
  ```

---

## **1.5. Herramientas de Análisis de Configuración de Seguridad**

### **Microsoft Baseline Security Analyzer (MBSA)**
  - Escanea vulnerabilidades en Windows Server.  
  ```powershell
  # Ejecutar MBSA desde línea de comandos
  mbsacli /target 192.168.1.100 /n os+iis+sql
  ```

### **Security Configuration Wizard (SCW)**
  - Guía en la configuración segura de roles de servidor.  
  ```powershell
  # Iniciar SCW
  scw.exe
  ```

### **PowerShell Desired State Configuration (DSC)**
  - Automatiza la configuración de seguridad.  
  ```powershell
  # Configurar un servidor para cumplir con una línea base de seguridad
  Configuration SecureServerConfig {
      Node "SERVER01" {
          WindowsFeature DisableSMB1 {
              Name = "FS-SMB1"
              Ensure = "Absent"
          }
      }
  }
  SecureServerConfig -OutputPath "C:\DSCConfig"
  Start-DscConfiguration -Path "C:\DSCConfig" -Wait -Verbose
  ```

### **Nessus / OpenVAS**
  - Escaneo de vulnerabilidades externas.  
  ```bash
  # Ejemplo de escaneo con OpenVAS (desde Linux)
  openvas-cli --target=192.168.1.100 --profile="Full and fast"
  ```

---

### **Conclusión**
La seguridad en Windows Server requiere un enfoque integral que combine políticas de grupo, herramientas de auditoría y análisis automatizado. La implementación de estas medidas reduce riesgos y garantiza el cumplimiento de normativas como **ISO 27001, NIST o CIS**.

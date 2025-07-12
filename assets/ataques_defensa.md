# Generación de Escenarios de Ataque y Defensa en Ciberseguridad

Consiste en la creación metódica de narrativas de ciberataques hipotéticos pero basados en amenazas reales, junto con los correspondientes planes, técnicas y herramientas de defensa. Estos escenarios se ejecutan en entornos controlados (laboratorios, entornos virtualizados, sandboxes) para evaluar la resiliencia de sistemas, políticas de seguridad y la capacidad del equipo.

**Metodología Detallada:**

1.  **Definición de Objetivos y Alcance:**
    *   **Ataque:** ¿Qué se quiere "robar" (datos, credenciales)? ¿Qué sistema se quiere comprometer? ¿Se busca denegación de servicio? ¿Propagación lateral?
    *   **Defensa:** ¿Qué activos proteger (servidores, BD, redes)? ¿Qué nivel de detección se busca? ¿Se prueba el plan de respuesta a incidentes (IRP)? ¿Se valida la preservación de evidencias?
    *   **Reglas de Compromiso (RoE):** Límites claros (ej: no atacar producción, horarios, técnicas prohibidas).

2.  **Investigación y Modelado de Amenazas:**
    *   Identificar adversarios relevantes (script kiddies, crimen organizado, APTs, insider threats).
    *   Seleccionar Tácticas, Técnicas y Procedimientos (TTPs) del marco MITRE ATT&CK.
    *   Analizar vulnerabilidades específicas del entorno simulado.

3.  **Diseño del Escenario de Ataque (Red Team):**
    *   **Narrativa:** Crear una historia creíble (ej: "Un actor de amenaza persistente (APT) busca exfiltrar datos financieros").
    *   **Fases:**
        *   *Reconocimiento:* Escaneo (Nmap), OSINT (theHarvester), Footprinting.
        *   *Acceso Inicial:* Phishing (simulado con GoPhish), explotación de vulnerabilidad pública (Metasploit), credenciales débiles.
        *   *Ejecución:* Ejecutar malware simulado (Cobalt Strike Beacon), comandos remotos.
        *   *Persistencia:* Crear tareas programadas, backdoors, usuarios ocultos.
        *   *Escalada de Privilegios:* Abuso de sudo, explotación local (WinPEAS/LinPEAS).
        *   *Evasión de Defensas:* Desactivar EDRs simulado, ofuscación, living-off-the-land (LOLBAS/LOLBIN).
        *   *Movimiento Lateral:* Pass-the-Hash, PSExec, RDP.
        *   *Recolección y Exfiltración:* Buscar archivos sensibles, comprimir datos, exfiltrar vía DNS tunneling o HTTPS simulado.
    *   **Herramientas:** Seleccionar y configurar herramientas para cada fase (Kali Linux, Metasploit Framework, Cobalt Strike simulado, scripts personalizados).

4.  **Diseño del Escenario de Defensa (Blue Team):**
    *   **Prevención:** Configurar cortafuegos (iptables/pfSense), parcheo simulado, hardening de sistemas, segmentación de red.
    *   **Detección:** Reglas SIEM (Elastic Stack, Splunk simulado) para alertar sobre actividades sospechosas (logon failures fuera de horario, procesos inusuales, tráfico de exfiltración). IDS/IPS (Snort/Suricata).
    *   **Respuesta:** Activar el IRP simulado. Roles y responsabilidades claras.
    *   **Análisis Forense y Preservación de Evidencias (Objetivo clave del módulo):**
        *   *Identificación:* Qué sistemas/registros son relevantes (logs de autenticación, firewall, SIEM, memoria RAM, discos afectados).
        *   *Recolección:* Usar herramientas forenses (FTK Imager, dd, Guymager) para crear copias bit-a-bit *inmutables* de discos/volúmenes. Capturar tráfico de red (PCAPs con Wireshark/Tcpdump). Volcado de memoria (Magnet RAM Capture, Volatility).
        *   *Cadena de Custodia:* Documentar rigurosamente quién, cuándo, cómo y dónde se recogió cada evidencia. Usar hashes (MD5, SHA-256) para garantizar integridad.
        *   *Almacenamiento Seguro:* Guardar evidencias en medios inalterables (discos forenses con write-blockers) en un lugar seguro. Cumplir normativas (NIST SP 800-86, ISO 27037).
        *   *Análisis:* Analizar copias forenses (sin alterar originales) para determinar causa raíz, alcance, TTPs usados. Timeline de eventos.

5.  **Ejecución Controlada:**
    *   El Red Team ejecuta el ataque paso a paso.
    *   El Blue Team monitorea, detecta, responde y recopila evidencias según procedimientos.

6.  **Análisis Post-Ejercicio (Debriefing):**
    *   Revisar detalladamente las acciones de ambos equipos.
    *   Evaluar efectividad de detecciones, respuestas y preservación de evidencias.
    *   Identificar brechas de seguridad, fallos en procesos o herramientas.
    *   Documentar lecciones aprendidas y generar recomendaciones de mejora.

**Ejemplos Descriptivos:**

1.  **Escenario: Ataque de Ransomware (Ej: Simulación de LockBit 3.0)**
    *   **Ataque (Red Team):**
        *   *Fase 1:* Phishing con documento Office malicioso (macros) dirigido a contabilidad.
        *   *Fase 2:* Ejecución de payload inicial, descarga de ransomware, desactivación de copias de sombra (vssadmin) y backups.
        *   *Fase 3:* Cifrado de archivos en servidor de archivos y estaciones de trabajo clave. Deja nota de rescate.
        *   *Técnicas:* T1566.001 (Phishing Spearattachment), T1059.005 (Command and Scripting Interpreter: Visual Basic), T1486 (Data Encrypted for Impact).
    *   **Defensa y Preservación (Blue Team):**
        *   *Detección:* Alerta del EDR por comportamiento anómalo (vssadmin + proceso cifrando masivamente). Alerta del SIEM por tráfico C2 saliente inusual.
        *   *Respuesta:* Aislamiento inmediato de hosts afectados (desconexión de red). Activación de IRP.
        *   *Preservación:* Copia forense de la memoria RAM de una máquina recién infectada antes de apagarla. Copia bit-a-bit del disco de un servidor afectado usando write-blocker. Captura completa del tráfico de red (PCAP) durante la infección. Recolección de logs de EDR, SIEM, firewall, servidor de archivos. Documentación minuciosa de la cadena de custodia para cada evidencia. Cálculo de hashes. Almacenamiento seguro.
        *   *Análisis Forense:* Determinar vector inicial (correo específico), alcance del cifrado, tipo de ransomware, posibles datos exfiltrados previos al cifrado (usando PCAPs y logs).

2.  **Escenario: Amenaza Persistente Avanzada (APT) - Exfiltración de Datos (Ej: Simulación estilo Lazarus Group)**
    *   **Ataque (Red Team):**
        *   *Fase 1:* Explotar vulnerabilidad en VPN (ej: CVE-2023-46805) para acceso inicial.
        *   *Fase 2:* Escalada de privilegios en el servidor de la VPN comprometido.
        *   *Fase 3:* Movimiento lateral hacia el dominio interno usando credenciales robadas. Persistencia mediante servicio Windows oculto.
        *   *Fase 4:* Búsqueda de datos sensibles (archivos de diseño, propiedad intelectual) en servidores específicos.
        *   *Fase 5:* Exfiltración lenta y sigilosa de datos comprimidos y ofuscados vía protocolo HTTPS hacia un servidor C2 externo, camuflado como tráfico normal.
        *   *Técnicas:* T1190 (Exploit Public-Facing Application), T1068 (Exploitation for Privilege Escalation), T1078.002 (Valid Accounts: Domain Accounts), T1021.002 (Remote Services: SMB/Windows Admin Shares), TA0010 (Exfiltration), T1048.003 (Exfiltration Over Alternative Protocol: Exfiltration Over Unencrypted/Obfuscated Non-C2 Protocol).
    *   **Defensa y Preservación (Blue Team):**
        *   *Detección:* Correlación en SIEM de múltiples eventos: intentos fallidos de acceso a recursos sensibles desde una cuenta nueva, tráfico HTTPS anómalo en volumen/destino desde un host interno específico, logs de acceso a archivos sensibles fuera de horario.
        *   *Respuesta:* Investigación proactiva basada en alertas. Contención del host sospechoso y cuentas comprometidas.
        *   *Preservación:* Volcado de memoria del host comprometido donde se observa actividad sospechosa. Copia forense de sus discos. Recolección de logs de autenticación (Domain Controller), logs de acceso a archivos (servidor de archivos), logs de proxy/firewall para el tráfico HTTPS sospechoso. Captura de tráfico de red (PCAP) dirigido al dominio C2. Documentación exhaustiva de todo el proceso de investigación inicial y recolección.
        *   *Análisis Forense:* Identificar el malware en memoria/disco, determinar la ruta de acceso inicial (archivo de exploit en el servidor VPN), mapear el movimiento lateral, reconstruir los archivos exfiltrados y la técnica de exfiltración.

3.  **Escenario: Amenaza Interna Maliciosa (Ej: Empleado Descontento)**
    *   **Ataque (Red Team):**
        *   *Fase 1:* Usuario legítimo (simulado) con acceso a información confidencial.
        *   *Fase 2:* Copia masiva de datos de clientes y propiedad intelectual a un USB personal.
        *   *Fase 3:* Intento de sabotaje: borrado lógico de directorios compartidos críticos (`del /s /q` o `rm -rf`).
        *   *Fase 4:* Creación de una cuenta administrativa oculta para acceso futuro remoto.
        *   *Técnicas:* T1078.001 (Valid Accounts: Default Accounts - abusar de permisos existentes), T1530 (Data from Cloud Storage Object - o Data from Network Shared Drive), T1485 (Data Destruction), T1136.002 (Create Account: Domain Account).
    *   **Defensa y Preservación (Blue Team):**
        *   *Detección:* Alertas DLP (Prevención de Pérdida de Datos) por copia masiva a USB. Alertas del SIEM por creación de cuentas privilegiadas inusuales o comandos de borrado masivo ejecutados por un usuario.
        *   *Respuesta:* Confiscación inmediata del dispositivo USB. Deshabilitación de la cuenta del usuario. Investigación del alcance del borrado (restaurar de backups).
        *   *Preservación:* Imagen forense del USB confiscado (con write-blocker). Copia de los logs de DLP, logs de actividad de archivos en el servidor compartido, logs de creación de cuentas en el Domain Controller, logs de comandos ejecutados (si hay EDR o logging avanzado). Revisión de logs de acceso físico si aplica. Cadena de custodia para el USB.
        *   *Análisis Forense:* Recuperar datos del USB para confirmar información robada. Analizar logs para determinar la secuencia exacta de acciones del usuario interno. Buscar evidencias de premeditación (búsquedas previas, scripts preparados).

__________________-
Referencias Bibliográficas

> MITRE. (2023). *MITRE ATT&CK®: Design and Philosophy*. https://attack.mitre.org/docs/ATTACK_Design_and_Philosophy_March_2020.pdf  

> Kent, K., Chevalier, S., Grance, T., & Dang, H. (2006). *Guide to Integrating Forensic Techniques into Incident Response* (Special Publication 800-86). National Institute of Standards and Technology (NIST). https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-86.pdf  

> Scarfone, K., Grance, T., & Masone, K. (2008). *Computer Security Incident Handling Guide* (Special Publication 800-61 Rev. 2). National Institute of Standards and Technology (NIST). https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-61r2.pdf  

> Tipton, H. F., & Krause, M. (Eds.). (2018). *Information Security Management Handbook* (6th ed., Vol. 7). Auerbach Publications.  

> Kruse, W. G., & Heiser, J. G. (2001). *Computer Forensics: Incident Response Essentials*. Addison-Wesley Professional.  

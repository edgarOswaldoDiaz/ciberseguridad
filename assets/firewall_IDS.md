# Configuración de firewalls y sistemas de detección de intrusos (IDS)**  

#### **Configuración de Firewalls**  
**Definición:**  
Dispositivos o software que controlan el tráfico entre redes (ej. Internet y red interna) mediante reglas predefinidas.  

**Elementos clave de configuración:**  
- **Políticas de acceso:**  
  - Reglas de *allow/deny* basadas en direcciones IP, puertos, protocolos (TCP/UDP/ICMP) y servicios (HTTP, SSH).  
  - Ejemplo: `Permitir tráfico HTTPS (puerto 443) solo desde IPs autorizadas`.  
- **Zonas de seguridad:**  
  - Segmentación de redes (ej. *DMZ* para servidores públicos, zona interna para recursos críticos).  
- **Stateful Inspection:**  
  - Monitoreo de estados de conexión (ej. permitir respuestas a solicitudes internas, bloquear tráfico no solicitado).  
- **Configuración de NAT/PAT:**  
  - Enmascaramiento de IPs internas para ocultar la topología de red.  
- **Reglas predeterminadas:**  
  - Política de "denegar todo" como base, agregando excepciones explícitas.  

**Buenas prácticas:**  
- Actualizar firmas de amenazas regularmente.  
- Auditoría mensual de reglas para eliminar redundancias.  
- Habilitar logging para correlación con SIEM (ej. Splunk, ELK).  

---

#### **Configuración de Sistemas de Detección de Intrusos (IDS)**  
**Definición:**  
Herramientas que monitorean tráfico o sistemas para identificar actividades maliciosas mediante análisis de patrones o comportamientos anómalos.  

**Tipos y configuración:**  
- **Network-based IDS (NIDS):**  
  - Ubicación: En puntos estratégicos (ej. antes/después del firewall).  
  - Configuración de sensores:  
    - Sintonización de firmas (ej. ataques DDoS, escaneo de puertos).  
    - Uml de reglas personalizadas en *Snort* o *Suricata* (ej. alertar sobre tráfico SSH no autorizado).  
- **Host-based IDS (HIDS):**  
  - Monitoreo de logs, integridad de archivos y procesos en endpoints (ej. *OSSEC*, *Wazuh*).  

**Métodos de detección:**  
- **Por firmas:** Compara tráfico con patrones de ataques conocidos.  
- **Por anomalías:** Machine Learning para detectar desviaciones del comportamiento normal (ej. tráfico en horas no laborales).  

**Parámetros esenciales:**  
- Umbrales de alerta (ej. 10 intentos fallidos de SSH = posible ataque de fuerza bruta).  
- Integración con firewalls para respuestas automatizadas (ej. bloquear IP maliciosa).  

---

#### **Integración Firewall-IDS para Detección de Vulnerabilidades**  
- **Flujo de trabajo:**  
  1. Firewall filtra tráfico no autorizado.  
  2. IDS analiza tráfico permitido para detectar patrones sospechosos (ej. exploits en tráfico HTTP).  
  3. Alertas enviadas a SIEM para correlación (ej. identificar IPs atacantes recurrentes).  
- **Beneficios:**  
  - **Defensa en profundidad:** Mitiga falsos negativos de firewalls.  
  - **Respuesta proactiva:** Bloqueo automático mediante IPS (sistema de prevención).  

---

#### **Desafíos Comunes**  
- **Falsos positivos:** Reglas mal ajustadas generan alertas irrelevantes.  
- **Rendimiento:** Configuraciones complejas pueden saturar ancho de banda (ej. inspección profunda en NGFW).  
- **Actualización continua:** Requiere mantenimiento de firmas y parches (ej. vulnerabilidades de día cero).  

_______________

Referencias Bibliográficas 

> Stallings, W., & Brown, L. (2018). *Computer Security: Principles and Practice* (4th ed.). Pearson.  

> Scarfone, K., & Mell, P. (2007). *Guide to Intrusion Detection and Prevention Systems (IDPS)*. NIST Special Publication 800-94. National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-94  

> Northcutt, S., & Novak, J. (2001). *Network Intrusion Detection* (3rd ed.). New Riders.  

> Cheswick, W. R., Bellovin, S. M., & Rubin, A. D. (2003). *Firewalls and Internet Security: Repelling the Wily Hacker* (2nd ed.). Addison-Wesley Professional.  

> Bejtlich, R. (2005). *The Tao of Network Security Monitoring: Beyond Intrusion Detection*. Addison-Wesley Professional.  

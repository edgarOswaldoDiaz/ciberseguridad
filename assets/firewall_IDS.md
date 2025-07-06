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

## Firewalls vs. Sistemas de Detección de Intrusos (IDS)

| Característica | Firewall | Sistema de Detección de Intrusos (IDS) |
|---|---|---|
| **Definición** | Un sistema de seguridad de red que monitorea y controla el tráfico de red entrante y saliente, basándose en un conjunto de reglas de seguridad preestablecidas. Actúa como una barrera entre una red de confianza y una que no lo es (ej. Internet). | Un sistema de seguridad que monitorea el tráfico de red y/o la actividad del sistema en busca de patrones sospechosos o violaciones de políticas de seguridad. Su función principal es detectar amenazas y alertar sobre ellas. |
| **Función Principal** | **Filtrar y controlar el tráfico.** Su objetivo es permitir o bloquear el tráfico basándose en reglas específicas (direcciones IP, puertos, protocolos, etc.) para prevenir el acceso no autorizado y proteger la red. Es una medida preventiva. | **Detectar y alertar sobre intrusiones.** Su objetivo es identificar actividades maliciosas, anomalías o violaciones de seguridad que ya han logrado pasar las primeras líneas de defensa, y notificar a los administradores. Es una medida de detección. |
| **Mecanismo de Acción** | **Bloquea activamente** el tráfico que no cumple con las reglas establecidas. Actúa como un "portero" que decide quién entra y quién sale. | **Monitorea y analiza el tráfico de forma pasiva.** No interrumpe el flujo de datos. Su función es observar y generar alertas cuando detecta algo inusual o malicioso. |
| **Ubicación Típica** | Se posiciona en el perímetro de la red, entre la red interna y la red externa (Internet), o entre segmentos de red internos para controlar el flujo de información. | Puede ubicarse en puntos estratégicos de la red para monitorear el tráfico (NIDS) o en hosts individuales para supervisar la actividad del sistema (HIDS). |
| **Tipos Comunes** | - **Filtrado de paquetes:** Inspecciona encabezados de paquetes (IP de origen/destino, puertos, protocolos).\<br\>- **Inspección de estado (Stateful):** Rastrea el estado de las conexiones activas para permitir o denegar el tráfico.\<br\>- **Firewalls de aplicación (Proxy):** Opera en la capa de aplicación, examinando el contenido real de los datos.\<br\>- **Firewalls de Próxima Generación (NGFW):** Combinan funcionalidades de firewall tradicional con IDS/IPS, control de aplicaciones, filtrado de URL, etc.\<br\>- **Basados en hardware/software/nube/host.** | - **Basados en firmas:** Comparan patrones de tráfico con una base de datos de firmas de ataques conocidos.\<br\>- **Basados en anomalías:** Establecen una línea base de comportamiento normal y detectan desviaciones.\<br\>- **Basados en red (NIDS):** Monitorean todo el tráfico de la red.\<br\>- **Basados en host (HIDS):** Monitorean la actividad en un sistema específico (registros de eventos, cambios en archivos, etc.). |
| **Respuesta a Amenazas** | **Preventiva:** Evita que las amenazas lleguen a la red en primer lugar, bloqueando el tráfico. | **Reactiva (solo alerta):** Una vez detectada una amenaza, genera una alerta (correo electrónico, SMS, etc.) para que los administradores tomen medidas. No tiene la capacidad de bloquear el tráfico por sí mismo (a diferencia de un IPS). |
| **Ejemplos de Detección/Prevención** | - Bloquear accesos a puertos específicos.\<br\>- Denegar tráfico de IPs maliciosas conocidas.\<br\>- Restringir el acceso a ciertos sitios web.\<br\>- Establecer reglas para permitir solo ciertos protocolos. | - Detectar un escaneo de puertos.\<br\>- Identificar intentos de inicio de sesión fallidos repetidos.\<br\>- Reconocer patrones de ataque de desbordamiento de búfer.\<br\>- Alertar sobre el uso de firmas de malware conocidas. |
| **Fortalezas** | - Primera línea de defensa.\<br\>- Esencial para la segmentación de la red.\<br\>- Control preciso sobre el flujo de tráfico.\<br\>- Fácil de configurar para reglas básicas. | - Detecta ataques internos y externos.\<br\>- Identifica ataques de día cero (con detección de anomalías).\<br\>- Proporciona visibilidad profunda del tráfico y eventos del sistema.\<br\>- Útil para el análisis forense. |
| **Limitaciones** | - No detecta ataques dentro del tráfico permitido.\<br\>- No analiza el contenido a fondo (a menos que sea un firewall de aplicación o NGFW).\<br\>- No detecta ataques internos o amenazas que provienen de dentro de la red. | - Genera muchos falsos positivos (especialmente los basados en anomalías).\<br\>- Requiere una gestión constante y ajuste de reglas.\<br\>- No previene el ataque directamente; solo alerta.\<br\>- Puede ser abrumador si no se gestionan bien las alertas (fatiga de alertas). |
| **Complementariedad** | Son complementarios. El firewall actúa como la "puerta" que controla el tráfico, mientras que el IDS actúa como el "vigilante" que observa lo que sucede detrás de la puerta y dentro de la casa. La combinación de ambos ofrece una defensa por capas más robusta. |

_______________

Referencias Bibliográficas 

> Stallings, W., & Brown, L. (2018). *Computer Security: Principles and Practice* (4th ed.). Pearson.  

> Scarfone, K., & Mell, P. (2007). *Guide to Intrusion Detection and Prevention Systems (IDPS)*. NIST Special Publication 800-94. National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-94  

> Northcutt, S., & Novak, J. (2001). *Network Intrusion Detection* (3rd ed.). New Riders.  

> Cheswick, W. R., Bellovin, S. M., & Rubin, A. D. (2003). *Firewalls and Internet Security: Repelling the Wily Hacker* (2nd ed.). Addison-Wesley Professional.  

> Bejtlich, R. (2005). *The Tao of Network Security Monitoring: Beyond Intrusion Detection*. Addison-Wesley Professional.  

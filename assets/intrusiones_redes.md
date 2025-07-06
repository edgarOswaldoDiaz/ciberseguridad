# Detección de intrusiones y vulnerabilidades en redes

La **detección de intrusiones y vulnerabilidades en redes** es un proceso esencial dentro del monitoreo de redes, cuyo objetivo es identificar y gestionar amenazas y debilidades que puedan comprometer la seguridad de los sistemas informáticos. Este tema se alinea con el propósito del módulo de garantizar la seguridad de la red mediante la supervisión del tráfico y la resolución proactiva de riesgos. A continuación, se detalla el tema en cinco aspectos clave:

#### **Definición de intrusiones y vulnerabilidades**
- **Intrusiones**: Se refieren a intentos no autorizados de acceder, dañar o interrumpir sistemas y redes. Ejemplos incluyen ataques de denegación de servicio (DoS), inyecciones de malware o explotación de credenciales robadas. Estas acciones suelen buscar comprometer la confidencialidad, integridad o disponibilidad de la información.
- **Vulnerabilidades**: Son fallos o debilidades en software, hardware o configuraciones de red que pueden ser explotados por atacantes. Por ejemplo, una versión desactualizada de un sistema operativo o un puerto abierto innecesariamente representan vulnerabilidades comunes.

La identificación de estos elementos es el primer paso para proteger una red frente a ciberataques y garantizar su funcionamiento seguro.

#### **Métodos de detección**
Existen herramientas y técnicas especializadas para detectar intrusiones y vulnerabilidades:
- **Sistemas de Detección de Intrusiones (IDS)**: Monitorean el tráfico de red en tiempo real para identificar actividades sospechosas. Hay dos tipos principales:
  - **Basados en firmas**: Comparan el tráfico con una base de datos de patrones de ataques conocidos.
  - **Basados en anomalías**: Detectan desviaciones del comportamiento normal de la red, lo que puede indicar una amenaza emergente.
- **Escáneres de vulnerabilidades**: Analizan sistemas y redes para identificar debilidades específicas, como software sin parches, configuraciones inseguras o puertos expuestos.

Estas herramientas permiten a los administradores de red obtener una visión clara del estado de seguridad y responder a tiempo ante posibles incidentes.

#### **Importancia en la ciberseguridad**
La detección de intrusiones y vulnerabilidades es un pilar fundamental para:
- **Prevenir ataques**: Identificar y corregir vulnerabilidades antes de que sean explotadas reduce el riesgo de intrusiones exitosas.
- **Mitigar incidentes**: La detección temprana de intrusiones permite una respuesta rápida, minimizando el impacto en la red.
- **Cumplir normativas**: Muchas regulaciones de seguridad (como ISO 27001 o PCI DSS) exigen monitoreo continuo y gestión de riesgos, lo que hace indispensable este enfoque.

En el contexto del diplomado, este tema resalta cómo el monitoreo activo contribuye a la protección de datos sensibles y a la continuidad operativa de las organizaciones.

#### **Ejemplos prácticos**
- **Detección de intrusiones**: Un IDS basado en anomalías detecta un aumento repentino en el tráfico hacia un servidor, lo que podría indicar un ataque DoS, permitiendo al equipo de seguridad bloquear la fuente maliciosa.
- **Detección de vulnerabilidades**: Un escáner identifica que un router utiliza credenciales predeterminadas, alertando al administrador para cambiarlas y evitar accesos no autorizados.

Estos casos muestran, aplicables al monitoreo de redes, muestran cómo las técnicas de detección se traducen en acciones concretas para mejorar la seguridad.

#### **Desafíos y consideraciones**
Implementar sistemas de detección enfrenta retos como:
- **Falsos positivos**: Alertas generadas por actividades legítimas que se confunden con amenazas, lo que puede agotar recursos de análisis.
- **Mantenimiento**: Las herramientas requieren actualizaciones frecuentes de firmas y definiciones de vulnerabilidades para mantenerse efectivas.
- **Capacitación**: Configurar y gestionar estas soluciones demanda conocimientos técnicos avanzados, un aspecto clave a desarrollar en el diplomado.

## Detección de Intrusiones vs. Detección de Vulnerabilidades en Redes

| Característica         | Detección de Intrusiones (IDS/IPS)                                 | Detección de Vulnerabilidades (Escaneo de Vulnerabilidades/Pentesting) |
| :--------------------- | :----------------------------------------------------------------- | :--------------------------------------------------------------------- |
| **Objetivo Principal** | Identificar y/o prevenir actividades maliciosas en tiempo real o casi real una vez que ocurren. | Identificar debilidades y fallos de seguridad en sistemas y aplicaciones antes de que sean explotados. |
| **Naturaleza** | **Reactiva y/o proactiva (IPS):** Monitorea el tráfico y el comportamiento para detectar anomalías o firmas de ataques. | **Proactiva:** Busca debilidades conocidas y potenciales puntos de entrada para ataques. |
| **Enfoque** | Se centra en el **comportamiento** y los **patrones de ataque** (firmas) para detectar actividades no autorizadas. | Se centra en las **configuraciones incorrectas, software obsoleto, fallos de diseño o implementación** que pueden ser explotados. |
| **Momento de Acción** | **Durante o después** de un intento de ataque/intrusión (IDS). **Antes y durante** para prevenir (IPS). | **Antes** de que ocurra un ataque, para identificar y corregir las debilidades. |
| **Métodos/Técnicas** | **Basado en firmas:** Compara el tráfico con una base de datos de patrones de ataque conocidos.\<br\>**Basado en anomalías:** Detecta desviaciones del comportamiento normal de la red.\<br\>**Basado en políticas/protocolos:** Monitorea el cumplimiento de políticas de seguridad predefinidas. | **Escaneo de vulnerabilidades:** Utiliza herramientas automatizadas para identificar vulnerabilidades conocidas en sistemas y aplicaciones.\<br\>**Pruebas de penetración (Pentesting):** Simula ataques reales para explotar vulnerabilidades y evaluar la efectividad de los controles de seguridad. |
| **Herramientas Comunes** | Snort, Suricata, Zeek (Bro), PRTG, Cisco Firepower, IBM QRadar (SIEM con capacidades IDS/IPS). | Nessus, OpenVAS, Qualys, Acunetix, Burp Suite (para aplicaciones web), Metasploit (para pentesting). |
| **Tipo de Detección** | Tráfico de red malicioso, escaneos de puertos, intentos de explotación, actividad de malware, violaciones de políticas, movimiento lateral dentro de la red. | Puertos abiertos, servicios no seguros, software desactualizado con vulnerabilidades conocidas, configuraciones predeterminadas débiles, contraseñas predecibles, errores de programación, inyecciones SQL. |
| **Salida/Resultado** | Alertas, registros de eventos, bloqueo de tráfico (IPS), terminación de sesiones. | Informes detallados de vulnerabilidades encontradas, su severidad, posibles impactos y recomendaciones para remediarlas. |
| **Rol en la Seguridad** | **Defensa en profundidad:** Actúa como una capa de monitoreo y respuesta para detectar y mitigar ataques en curso. | **Análisis proactivo de riesgos:** Ayuda a entender la postura de seguridad de una organización y priorizar la remediación de debilidades. |
| **Complementariedad** | Ambos son cruciales y complementarios. Un sistema de detección de intrusiones puede alertar sobre intentos de explotación de vulnerabilidades que no fueron corregidas. La detección de vulnerabilidades reduce la superficie de ataque que los IDS/IPS necesitan monitorear. | Son dos pilares fundamentales de una estrategia de ciberseguridad integral. Las vulnerabilidades identificadas pueden ser objetivos para intrusiones. |
| **Ejemplo** | Un IDS detecta un alto volumen de conexiones a un puerto específico y genera una alerta porque coincide con la firma de un escaneo de puertos conocido. | Un escáner de vulnerabilidades identifica que un servidor web está ejecutando una versión antigua de Apache con una vulnerabilidad conocida de desbordamiento de búfer. |

En resumen, la **detección de vulnerabilidades** se enfoca en encontrar las "grietas" en tu armadura antes de la batalla, mientras que la **detección de intrusiones** se encarga de alertarte (o defenderte activamente) cuando alguien intenta explotar esas grietas o ya ha logrado entrar. Ambas son esenciales para una postura de ciberseguridad robusta.

_______________________

Referencias bibliográficas en formato APA

> Guías BibUpo. (2024). *Seguridad informática*. Universidad Pablo de Olavide. https://guiasbib.upo.es/seguridad_informatica  
   (Ofrece una visión general de conceptos de ciberseguridad aplicables al monitoreo de redes).

> Kaspersky. (2021). *¿Qué es la ciberseguridad?*. https://latam.kaspersky.com/resource-center/definitions/what-is-cybersecurity  
   (Introduce fundamentos de ciberseguridad, incluyendo detección de amenazas).

> Scielo. (2020). *Sistemas para la detección de intrusiones en redes de datos de instituciones de salud*. http://scielo.sld.cu/scielo.php?script=sci_arttext&pid=S1024-94352020000400012  
   (Explora aplicaciones prácticas de IDS en entornos específicos).

> INCIBE. (2020). *¿Qué son y para qué sirven los SIEM, IDS e IPS?*. https://www.incibe.es/protege-tu-empresa/blog/que-son-y-para-que-sirven-siem-ids-ips  
   (Describe herramientas de detección y su rol en la seguridad de redes).


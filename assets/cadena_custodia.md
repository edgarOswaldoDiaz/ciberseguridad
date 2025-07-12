# Cadena de Custodia en Incidentes de Ciberseguridad

La Cadena de Custodia en Incidentes de Ciberseguridad es el registro documentado y auditado de la posesión, control, manejo y transferencia de una evidencia digital, desde el momento de su identificación y recolección hasta su presentación en un proceso legal o investigación. Su objetivo primordial es asegurar la integridad, autenticidad y fiabilidad de la evidencia, garantizando que no ha sido alterada, contaminada o perdida en ninguna etapa. Esto implica registrar meticulosamente quién tuvo acceso a la evidencia, cuándo la tuvo, qué acciones realizó sobre ella y cómo la transfirió a la siguiente persona o ubicación. Cada paso debe ser inalterable y verificable, a menudo mediante el uso de hashes criptográficos que confirman que los datos no han cambiado. Una cadena de custodia robusta es crucial para que la evidencia digital sea admisible en un tribunal o para que los hallazgos de una investigación forense sean creíbles. Sin ella, la validez de la evidencia podría ser cuestionada, invalidando potencialmente todo el esfuerzo de respuesta a un incidente y socavando la capacidad de perseguir a los atacantes.

### Importancia en el Contexto Legal y Técnico

La cadena de custodia es fundamental porque las evidencias digitales poseen características únicas que las hacen especialmente vulnerables a la alteración, corrupción o destrucción. A diferencia de las evidencias físicas tradicionales, los datos digitales pueden ser modificados sin dejar rastros visibles, copiados infinitamente sin degradación y pueden existir en múltiples ubicaciones simultáneamente.

### Principios Fundamentales

1. Integridad : La evidencia debe mantenerse íntegra y sin alteraciones desde su recolección hasta su análisis final. Esto se logra mediante el uso de funciones hash criptográficas (como SHA-256) que generan una "huella digital" única de la evidencia.

2. Autenticidad : Debe poder demostrarse que la evidencia es genuina y proviene de la fuente declarada, sin haber sido falsificada o sustituida.

3. Confiabilidad : Los métodos y herramientas utilizados deben ser técnicamente sólidos y reconocidos por la comunidad forense.

4. Admisibilidad : La evidencia debe cumplir con los requisitos legales para ser admitida en procedimientos judiciales.

### Fases de la Cadena de Custodia

#### Fase 1: Identificación y Preservación
Esta fase inicial implica la identificación de dispositivos, sistemas y datos que puedan contener evidencias relevantes. Se debe actuar rápidamente para evitar la pérdida de datos volátiles y prevenir la alteración de evidencias.

**Ejemplo:** En un incidente de ransomware, el equipo de respuesta identifica que el servidor de archivos principal ha sido comprometido. Inmediatamente proceden a aislar el sistema de la red y crear una imagen forense del disco duro antes de que el malware pueda causar más daño o autodestruirse.

#### Fase 2: Recolección y Documentación
Durante esta fase se extraen las evidencias digitales utilizando herramientas especializadas y se documenta meticulosamente cada acción realizada.

**Ejemplo:** Un investigador forense utiliza la herramienta dd en Linux para crear una copia bit a bit del disco duro comprometido. El proceso se documenta registrando la fecha, hora, herramienta utilizada, comandos ejecutados y el hash SHA-256 resultante: `dd if=/dev/sda of=/evidence/disk_image.dd bs=512 conv=noerror,sync`. El hash generado (ejemplo: 3b7a4f5c2e1d8a9b6c5e4f3a2b1c9d8e7f6a5b4c3d2e1f9a8b7c6d5e4f3a2b1c) se registra en el formulario de cadena de custodia.

#### Fase 3: Análisis y Examen
Las evidencias son analizadas utilizando herramientas forenses especializadas, manteniendo siempre la integridad de los datos originales mediante el trabajo con copias.

**Ejemplo:** Un analista forense examina los logs de un firewall para identificar conexiones sospechosas durante un ataque de exfiltración de datos. Utiliza herramientas como Wireshark para analizar el tráfico de red capturado y identifica conexiones hacia direcciones IP conocidas por estar asociadas con grupos de ciberdelincuentes.

#### Fase 4: Almacenamiento y Preservación
Las evidencias deben almacenarse en condiciones controladas que garanticen su integridad a largo plazo.

**Ejemplo:** Las imágenes forenses se almacenan en un servidor seguro con acceso restringido, respaldadas en medios de almacenamiento redundantes y con verificaciones periódicas de integridad mediante comparación de hashes.

#### Fase 5: Presentación y Testimonio
En esta fase final, las evidencias y los hallazgos se presentan de manera clara y comprensible para audiencias técnicas y no técnicas.

### Documentación Requerida

#### Formulario de Cadena de Custodia
Este documento debe incluir:
- Identificación única de la evidencia
- Descripción detallada del elemento
- Fecha, hora y lugar de recolección
- Nombre y firma del recolector
- Propósito de la recolección
- Registro de todas las transferencias
- Condiciones de almacenamiento
- Valores hash para verificación de integridad

#### Bitácora de Actividades
Registro cronológico de todas las acciones realizadas sobre las evidencias, incluyendo:
- Fecha y hora de cada acción
- Persona responsable
- Descripción detallada de la actividad
- Herramientas utilizadas
- Resultados obtenidos

### Herramientas y Tecnologías

#### Herramientas de Adquisición
- **FTK Imager**: Para crear imágenes forenses de discos duros y dispositivos de almacenamiento
- **dd (Linux)**: Herramienta de línea de comandos para copia bit a bit
- **MSAB XRY**: Especializada en extracción de datos de dispositivos móviles

#### Herramientas de Análisis
- **Autopsy**: Plataforma de análisis forense digital de código abierto
- **EnCase**: Suite comercial para análisis forense
- **Volatility**: Especializada en análisis de memoria RAM

#### Herramientas de Verificación
- **HashCalc**: Para generar y verificar hashes de archivos
- **NIST NSRL**: Base de datos de hashes de archivos conocidos

### Desafíos Específicos en Ciberseguridad

#### Volatilidad de Datos
Los datos en memoria RAM, conexiones de red activas y procesos en ejecución son extremadamente volátiles y pueden perderse al apagar el sistema.

**Ejemplo:** Durante la investigación de un ataque de memoria, es crucial capturar un volcado de la memoria RAM antes de apagar el sistema, ya que puede contener contraseñas, claves de cifrado y evidencias del malware que no están presentes en el disco duro.

#### Cifrado y Ofuscación
Los atacantes frecuentemente utilizan técnicas de cifrado para ocultar sus actividades y datos.

**Ejemplo:** Un atacante utiliza herramientas como VeraCrypt para cifrar archivos robados antes de exfiltrarlos. Los investigadores deben identificar y preservar las claves de cifrado o buscar métodos alternativos para acceder a los datos.

#### Evidencias Distribuidas
En entornos cloud y sistemas distribuidos, las evidencias pueden estar dispersas en múltiples ubicaciones geográficas y jurisdiccionales.

**Ejemplo:** Un ataque DDoS puede involucrar botnets distribuidas globalmente, requiriendo coordinación internacional para recolectar evidencias de múltiples proveedores de servicios en diferentes países.

### Consideraciones Legales y Normativas

#### Normativas Internacionales
- **ISO/IEC 27037**: Directrices para la identificación, recolección, adquisición y preservación de evidencias digitales
- **ISO/IEC 27042**: Directrices para el análisis e interpretación de evidencias digitales
- **RFC 3227**: Directrices para la recolección y archivo de evidencias

#### Normativas Nacionales (México)
- **Ley Federal de Protección de Datos Personales en Posesión de los Particulares**
- **Código Federal de Procedimientos Penales**
- **Metodología para el Análisis de Evidencia Digital** del CNS (Centro Nacional de Seguridad)

### Mejores Prácticas

#### Preparación Previa
- Establecer procedimientos documentados antes de que ocurra un incidente
- Capacitar al personal en técnicas de preservación de evidencias
- Mantener herramientas forenses actualizadas y calibradas

#### Durante el Incidente
- Actuar rápidamente para preservar evidencias volátiles
- Documentar exhaustivamente todas las acciones
- Mantener la cadena de custodia sin interrupciones
- Utilizar múltiples métodos de verificación de integridad

#### Después del Incidente
- Realizar revisiones post-incidente para identificar áreas de mejora
- Mantener las evidencias disponibles para futuras investigaciones
- Actualizar procedimientos basándose en lecciones aprendidas



## Herramientas para la Cadena de Custodia en Incidentes de Ciberseguridad

| Categoría de Herramienta | Tipo de Herramienta | Descripción y Funcionalidad | Herramientas Específicas / Ejemplos |
|---|---|---|---|
| **Adquisición y Preservación de Evidencia** | **Imaginadores Forenses / Creadores de Imagen Bit a Bit** | Permiten crear copias exactas (imágenes forenses) de dispositivos de almacenamiento (discos duros, USB, móviles) a nivel de bit, garantizando que el original no se altere. Estas herramientas también calculan valores hash (MD5, SHA1, SHA256) para verificar la integridad de la copia. | **EnCase Forensic (Guidance Software):** Una de las más completas y utilizadas para adquisición, análisis y reporte. \<br\> **FTK Imager (AccessData):** Herramienta gratuita para crear imágenes forenses de varios tipos de medios. \<br\> **Autopsy/Sleuth Kit:** Software de código abierto para análisis forense, incluye funciones para la adquisición. \<br\> **dd (Disk Dump) / DCFLDD (Digital Forensics CDD):** Herramientas de línea de comandos en sistemas Unix/Linux para copiar datos brutos. \<br\> **Magnet AXIOM Acquire:** Herramienta de Magnet Forensics para la adquisición de evidencia. |
| | **Bloqueadores de Escritura (Write Blockers)** | Dispositivos de hardware o software que impiden cualquier modificación en el dispositivo de origen mientras se realiza la adquisición de la imagen forense. Son esenciales para mantener la inalterabilidad de la evidencia original. | **Bloqueadores de escritura de hardware:** Tableau (por ejemplo, Tableau TD4, Forensic Imager), Logicube. \<br\> **Bloqueadores de escritura de software:** Algunas herramientas forenses integran esta funcionalidad. |
| **Documentación y Registro** | **Sistemas de Gestión de Casos Forenses** | Software diseñado para gestionar todos los aspectos de una investigación forense, incluyendo la documentación detallada de la evidencia, el registro de la cadena de custodia, los hallazgos y los informes. Permiten una trazabilidad completa de cada paso. | **CaseGuard:** Plataforma de administración de evidencia digital. \<br\> **Magnet AXIOM:** Integra funcionalidades de gestión de casos. \<br\> **EnCase Forensic:** Incluye módulos para la gestión de casos y reportes. \<br\> **Herramientas personalizadas / bases de datos:** Muchas organizaciones desarrollan sus propios sistemas para adaptarse a sus necesidades específicas. |
| | **Formularios y Plantillas de Cadena de Custodia** | Documentos estandarizados (físicos o digitales) que se utilizan para registrar cada transferencia, acceso, análisis y disposición de la evidencia. Deben incluir información como fecha, hora, persona que entrega, persona que recibe, descripción de la evidencia, número de caso, etc. | **Plantillas de CoC (Chain of Custody) impresas:** Formularios predefinidos para registro manual. \<br\> **Documentos electrónicos:** Hojas de cálculo (Excel) o bases de datos simples con campos específicos para CoC. \<br\> **Módulos de CoC en herramientas de gestión de evidencia:** Integrados en softwares forenses y de gestión de casos. |
| **Análisis Forense (con trazabilidad)** | **Herramientas de Análisis Forense Digital** | Software que permite examinar las imágenes forenses o copias de la evidencia para identificar, extraer y analizar información relevante (archivos eliminados, artefactos de internet, registros de eventos, etc.) sin modificar la copia de trabajo. | **EnCase Forensic:** Para análisis de sistemas de archivos, recuperación de datos, etc. \<br\> **FTK (Forensic Toolkit):** Análisis de grandes volúmenes de datos, correos electrónicos, etc. \<br\> **Autopsy:** Interfaz gráfica para Sleuth Kit, útil para análisis de sistemas de archivos y recuperación. \<br\> **Volatility Framework:** Para análisis de memoria RAM, identificando procesos maliciosos, conexiones de red, etc. \<br\> **X-Ways Forensics:** Herramienta forense integral con potentes capacidades de análisis. |
| | **Herramientas de Hash y Verificación de Integridad** | Programas que calculan y comparan valores hash criptográficos (MD5, SHA1, SHA256) de los archivos o imágenes. Cualquier cambio en la evidencia resultaría en un valor hash diferente, lo que indicaría una alteración. | **md5sum, sha1sum, sha256sum (Linux/Unix):** Utilidades de línea de comandos. \<br\> **HashCalc (Windows):** Utilidad GUI para Windows. \<br\> **Integradas en herramientas forenses:** La mayoría de los imaginadores y analizadores forensos calculan y verifican hashes automáticamente. |
| **Almacenamiento y Seguridad** | **Contenedores de Evidencia / Bolsas Anti-Tamper** | Envases físicos sellados que muestran signos de manipulación si se intentan abrir, garantizando que la evidencia física (discos duros, memorias USB, etc.) no ha sido comprometida durante el almacenamiento o transporte. | **Bolsas de evidencia de seguridad con sellado numerado y resistente a la manipulación.** \<br\> **Contenedores de almacenamiento seguros:** Armarios o cajas con cerradura y control de acceso. |
| | **Sistemas de Gestión de Evidencia Digital (DEMS)** | Plataformas que proporcionan un entorno seguro y centralizado para almacenar, gestionar y controlar el acceso a la evidencia digital. Ofrecen funciones de registro de auditoría, control de versiones y, a menudo, integran la funcionalidad de cadena de custodia. | **Soluciones SaaS o locales de DEMS:** Varias empresas ofrecen este tipo de plataformas para agencias de aplicación de la ley y equipos de respuesta a incidentes. \<br\> **Sistemas de gestión de documentos con controles de acceso estrictos.** |
| **Automatización y Trazabilidad** | **Plataformas de Orquestación, Automatización y Respuesta de Seguridad (SOAR)** | Permiten automatizar tareas repetitivas en la respuesta a incidentes, incluyendo la recolección inicial de evidencia y la documentación de ciertos pasos, lo que puede contribuir a una cadena de custodia más eficiente y consistente. | **Splunk Phantom:** Plataforma SOAR que puede automatizar flujos de trabajo de respuesta a incidentes. \<br\> **IBM Resilient Security Orchestration, Automation and Response (SOAR Platform).** \<br\> **TheHive Project:** Plataforma de código abierto para la respuesta a incidentes y gestión de casos. |
| | **Software de Gestión de Registros y Logs (SIEM)** | Aunque no son herramientas directas de cadena de custodia, los SIEM recolectan y correlacionan logs de diversos sistemas, lo que puede ser crucial para reconstruir la secuencia de eventos de un incidente y, por lo tanto, para respaldar la integridad de la evidencia. | **Splunk Enterprise Security.** \<br\> **IBM QRadar.** \<br\> **Microsoft Sentinel.** \<br\> **ELK Stack (Elasticsearch, Logstash, Kibana).** |

____________________
Referencias Bibliográficas

> Casey, E., & Rose, C. (2022). *Digital evidence and computer crime: Forensic science, computers, and the internet* (4th ed.). Academic Press.

> Kessler, G. C. (2020). Anti-forensics and the digital investigator. In *Advances in Digital Forensics XVI* (pp. 3-18). Springer International Publishing.

> Malin, C. H., Casey, E., & Aquilina, J. M. (2021). *Malware forensics field guide for Windows systems: Digital forensics field guides* (2nd ed.). Syngress Publishing.

> Reith, M., Carr, C., & Gunsch, G. (2021). An examination of digital forensic models. *International Journal of Digital Evidence*, 15(3), 23-41. https://doi.org/10.1016/j.ijde.2021.03.002

> Sammons, J. (2023). *The basics of digital forensics: The primer for getting started in digital forensics* (3rd ed.). Elsevier.

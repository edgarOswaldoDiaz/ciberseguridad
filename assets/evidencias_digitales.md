# Preservación y Manejo de Evidencias Digitales en Ciberseguridad

**Principios Fundamentales (Reglas de Oro):**

1.  **Minimizar la Alteración:** La acción de recolección debe alterar lo menos posible la fuente original de los datos.
2.  **Documentar Todo:** Cada paso, herramienta utilizada, persona involucrada, fecha, hora y acción realizada debe ser registrada meticulosamente.
3.  **Preservar la Cadena de Custodia:** Registro cronológico e ininterrumpido que documenta quién tuvo posesión de la evidencia, cuándo, por qué y qué se hizo con ella.
4.  **Validar y Verificar:** Utilizar herramientas validadas y métodos aceptados para garantizar que los datos copiados son idénticos a los originales (Hashes: MD5, SHA-1, SHA-256).
5.  **Cumplir con la Legalidad:** Todo el proceso debe realizarse dentro del marco legal aplicable (leyes locales, normativas de privacidad, órdenes judiciales).

**Fases Clave del Proceso con Ejemplos Descriptivos:**

1.  **Identificación:**
    *   **Qué es:** Reconocer y localizar fuentes potenciales de evidencia digital relevante para el incidente (ej: ataque ransomware, robo de datos).
    *   **Ejemplo Descriptivo:** Tras un ataque de phishing que comprometió cuentas de correo, se identifican:
        *   **El servidor de correo:** Registros (logs) de acceso, autenticación, envío/recepción del correo malicioso.
        *   **La estación de trabajo del usuario afectado:** Disco duro (archivos temporales, historial del navegador donde se hizo clic en el enlace malicioso, memoria RAM que podría contener malware activo).
        *   **El firewall y el IDS/IPS:** Registros de tráfico de red mostrando conexiones hacia la dirección IP del atacante.
        *   **Dispositivos de respaldo:** Cintas o discos de backup que podrían contener versiones no comprometidas de los datos.
        *   **Dispositivos móviles del usuario (si aplica):** Si accedió al correo desde su teléfono.

2.  **Recolección (Adquisición):**
    *   **Qué es:** La captura física o lógica de los datos identificados, priorizando la integridad.
    *   **Métodos Clave:**
        *   **Adquisición Forense (Bit-by-Bit/Imagen Forense):** Crear una copia exacta, sector por sector, de un dispositivo de almacenamiento (disco duro, USB, SSD). *Ejemplo: Usar una write-blocker (bloqueador de escritura) conectado al disco de la estación de trabajo comprometida y una herramienta como FTK Imager o dd para crear una imagen forense (.E01, .AFF4) del disco completo. Se calcula el hash (SHA-256) del disco original y de la imagen para verificar la integridad.*
        *   **Recolección de Datos Volátiles:** Captura de información en la memoria RAM (procesos activos, conexiones de red, claves de cifrado). *Ejemplo: Usar herramientas como Volatility o Magnet RAM Capture en la estación de trabajo comprometida ANTES de apagarla, para capturar el contenido de la memoria RAM, donde podría residir el ransomware descifrado.*
        *   **Recolección de Registros (Logs):** Extracción segura de archivos de registro de servidores, firewalls, IDS/IPS. *Ejemplo: Exportar los logs del servidor de correo (formato syslog o nativo) usando conexiones seguras (SSH, SFTP) y calculando su hash inmediatamente después.*
        *   **Recolección de Paquetes de Red (PCAP):** Captura del tráfico de red. *Ejemplo: Configurar un puerto espejo (SPAN port) en el switch para redirigir el trágo de la red afectada a una estación donde se ejecuta Wireshark o tcpdump para capturar el tráfico en tiempo real durante el ataque.*
    *   **Documentación:** Registrar hora de inicio/fin de la adquisición, herramienta usada (versión), hash de origen y destino, persona responsable, número de serie del dispositivo, descripción física.

3.  **Preservación:**
    *   **Qué es:** Almacenar y proteger la evidencia recolectada para prevenir alteraciones, daños o acceso no autorizado.
    *   **Acciones Clave:**
        *   **Almacenamiento Seguro:** Guardar los dispositivos físicos (discos originales) y las copias forenses (imágenes) en un lugar seguro con control de acceso físico (armario con llave, sala de evidencia con acceso restringido) y ambiental (control de temperatura y humedad).
        *   **Protección de Copias Digitales:** Almacenar las imágenes forenses y datos recolectados en medios de solo lectura (WORM - Write Once Read Many) o en sistemas seguros con controles de integridad (ej: usando hashes periódicos para verificar que no han cambiado).
        *   **Cadena de Custodia:** Iniciar y mantener un formulario de cadena de custodia que acompañe a toda evidencia física o digital. Cada transferencia de custodia debe ser registrada con fecha, hora, motivo, firmas del que entrega y del que recibe. *Ejemplo: El investigador que creó la imagen forense la guarda en un disco externo nuevo, sella el disco en una bolsa antiestática y de evidencia, etiqueta la bolsa con un ID único, e inicia el formulario de cadena de custodia. Luego se la entrega al responsable del almacén de evidencia, quien firma el formulario al recibirla.*

4.  **Análisis:**
    *   **Qué es:** Examinar la evidencia preservada utilizando técnicas y herramientas forenses para extraer información relevante, reconstruir eventos y entender el alcance y método del ataque. **¡CRUCIAL!: El análisis se realiza SOBRE LA COPIA FORENSE (la imagen), NUNCA sobre la evidencia original.**
    *   **Ejemplos de Análisis:**
        *   *En la imagen forense del disco del usuario:* Buscar el correo de phishing en la bandeja de entrada o spam, analizar el archivo adjunto malicioso (ej: .docm) en un sandbox, examinar el historial del navegador para ver la URL del enlace phishing y sitios visitados después del clic, buscar indicadores de compromiso (IOCs) como nombres de archivos sospechosos o claves de registro modificadas por malware.
        *   *En la captura de memoria RAM:* Buscar procesos maliciosos inyectados, cadenas de texto que revelen comandos del atacante o claves de cifrado, conexiones de red establecidas a IPs maliciosas.
        *   *En los logs del servidor de correo:* Identificar la dirección IP de origen del correo phishing, otros destinatarios internos que lo recibieron, intentos fallidos de inicio de sesión posteriores al ataque.
        *   *En los PCAPs:* Filtrar el tráfico para encontrar la comunicación entre el equipo infectado y el servidor de comando y control (C2) del atacante, extraer archivos transferidos, identificar el protocolo usado.

5.  **Presentación e Informe:**
    *   **Qué es:** Documentar los hallazgos del análisis de manera clara, concisa, objetiva y técnicamente precisa, en un formato comprensible para la audiencia objetivo (gerencia, equipos legales, tribunales). Incluir cómo se preservó la integridad y se mantuvo la cadena de custodia.
    *   **Contenido Clave:** Resumen ejecutivo, metodología utilizada (herramientas, pasos), descripción del incidente, análisis detallado de la evidencia (con hallazgos específicos y su relevancia), conclusiones, recomendaciones de remediación, apéndices (copias de la cadena de custodia, hashes, logs relevantes anonimizados si es necesario).

**Desafíos Comunes:**

*   **Volatilidad de Datos:** La memoria RAM se pierde al apagar. La prioridad es capturarla primero.
*   **Tamaño y Complejidad:** Grandes volúmenes de datos (Big Data, almacenamiento en la nube) requieren herramientas y tiempo eficientes.
*   **Cifrado:** Datos o dispositivos cifrados dificultan el acceso y análisis.
*   **Tecnologías Emergentes:** IoT, dispositivos móviles, cloud computing presentan nuevos retos para la recolección forense.
*   **Plazos Legales:** Investigaciones pueden tener límites de tiempo estrictos.

---
## Decálogo para la Preservación de Evidencias Digitales (INCIBE)

Para asegurar la validez y utilidad de las **evidencias digitales** en cualquier proceso legal o investigación, es crucial seguir un protocolo riguroso. Este decálogo, basado en la guía del Instituto Nacional de Ciberseguridad (INCIBE), te ayudará a preservar adecuadamente la información digital:

1.  **Actúa con prontitud:** El tiempo es oro en la **evidencia digital**. Cuanto antes inicies el proceso de preservación, menor será el riesgo de alteración o pérdida de datos. La volatilidad de la información digital exige una respuesta rápida.

2.  **Asegura la integridad:** La **integridad de la evidencia** es fundamental. Esto significa garantizar que la información no ha sido modificada, alterada o corrompida desde el momento de su recolección. Utiliza herramientas de *hashing* (como MD5 o SHA256) para crear una huella digital que demuestre su inalterabilidad.

3.  **Documenta cada paso:** Lleva un registro exhaustivo de todo el proceso de preservación. Anota la fecha, hora, personas involucradas, herramientas utilizadas, y cualquier observación relevante. Esta **cadena de custodia** es vital para la credibilidad de la evidencia.

4.  **Minimiza la manipulación:** Evita interactuar directamente con el dispositivo o sistema que contiene la **evidencia original**. Siempre que sea posible, trabaja sobre copias forenses (imágenes bit a bit) para no alterar el estado original de la información.

5.  **Utiliza herramientas forenses:** Emplea *software* y *hardware* especializados en **informática forense**. Estas herramientas están diseñadas para recolectar y preservar evidencia de manera segura y reproducible, garantizando la fiabilidad del proceso.

6.  **Protege la escena digital:** Considera el entorno digital como una escena del crimen. Aísla el sistema o la red para evitar que se sigan produciendo cambios o que se comprometa más información. Desconecta de la red si es necesario, pero con precaución para no perder datos volátiles.

7.  **Preserva la volatilidad:** Prioriza la recolección de **información volátil** antes que la persistente. Datos como la memoria RAM, conexiones de red activas o procesos en ejecución pueden desaparecer al apagar el sistema.

8.  **Copia forense antes que nada:** Siempre realiza una **copia forense exacta** del soporte original. Esta copia debe ser idéntica bit a bit al original y verificable mediante *hashing*. Nunca trabajes directamente sobre el original a menos que sea estrictamente necesario y no haya otra opción.

9.  **Almacena de forma segura:** Una vez recolectada y copiada, la **evidencia digital** debe almacenarse en un lugar seguro y controlado. Protege los soportes de almacenamiento de posibles daños físicos, accesos no autorizados o condiciones ambientales adversas.

10. **Prepara para el análisis:** Aunque el decálogo se centra en la preservación, ten en cuenta que la **evidencia** deberá ser analizada posteriormente. Asegúrate de que los formatos y métodos de preservación permitan un análisis forense eficaz y que la evidencia sea comprensible para los expertos.

_______________
Referencias Bibliográficas

> **Agencia de Gobierno Electrónico y Tecnologías de la Información y Comunicación (AGETIC) & Oficina Nacional de Tecnologías de Información (ONTI). (2020). *Guía de Preservación Digital y Gestión de Evidencias Digitales*. La Paz, Bolivia: Autor.**  

> **Casey, E. (2011). *Digital Evidence and Computer Crime: Forensic Science, Computers, and the Internet* (3rd ed.). Academic Press.**  

> **Instituto Nacional de Ciberseguridad (INCIBE). (2021). *Guía de actuación: Preservación de evidencias digitales*. León, España: Autor.**  

> **Sammons, J. (2015). *The Basics of Digital Forensics: The Primer for Getting Started in Digital Forensics* (2nd ed.). Syngress.**  

> **International Organization for Standardization (ISO) & International Electrotechnical Commission (IEC). (2018). *ISO/IEC 27037:2018 Information technology — Security techniques — Guidelines for identification, collection, acquisition and preservation of digital evidence*. ISO.**  

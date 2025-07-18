# Legislación y Normativas Aplicables en la Preservación de Evidencias Digitales

La legislación y normativas aplicables en la preservación de evidencias digitales constituyen un marco legal esencial que garantiza la validez, integridad y admisibilidad de la información electrónica en procesos judiciales y administrativos. Este conjunto de leyes, reglamentos y estándares técnicos aborda los desafíos inherentes a la volatilidad y facilidad de alteración de los datos digitales. A nivel internacional, tratados como el Convenio de Budapest sobre Ciberdelincuencia ofrecen principios para la cooperación y armonización legislativa, mientras que normativas como el Reglamento General de Protección de Datos (GDPR) de la Unión Europea impactan indirectamente al establecer marcos para el manejo de datos personales, lo cual puede incluir evidencia digital.

En el ámbito nacional, cada jurisdicción desarrolla sus propias leyes de enjuiciamiento criminal, civil o mercantil que especifican los requisitos para la obtención, cadena de custodia y presentación de pruebas electrónicas. Esto incluye la necesidad de asegurar la autenticidad, integridad y no repudio de la evidencia desde su recolección hasta su análisis y exhibición en juicio. Las normativas técnicas complementan la legislación, proporcionando guías sobre herramientas forenses, procedimientos de adquisición de imágenes disco, análisis de metadatos, y el uso de firmas digitales y sellos de tiempo para probar la inalterabilidad. La observancia de este marco dual es crucial para evitar la nulidad de la prueba y asegurar un proceso justo basado en evidencia digital confiable.

La preservación de evidencias digitales constituye un elemento fundamental en la investigación de ciberataques y delitos informáticos. Este proceso debe realizarse bajo un marco legal y normativo estricto que garantice la integridad, autenticidad y admisibilidad de las pruebas digitales en procedimientos judiciales. La legislación y normativas aplicables varían según la jurisdicción, pero existen estándares internacionales que proporcionan directrices uniformes para la gestión adecuada de evidencias digitales.

## Marco Legal Internacional

### Normativas ISO/IEC

La serie de normas ISO/IEC 27000 proporciona el marco más reconocido internacionalmente para la gestión de evidencias digitales:

#### ISO/IEC 27037:2012
Esta norma establece directrices específicas para la identificación, recopilación, adquisición y preservación de evidencia digital. Define tres principios fundamentales que gobiernan la evidencia digital:
- **Integridad**: La evidencia debe permanecer íntegra y sin alteraciones
- **Autenticidad**: Se debe poder verificar que la evidencia es genuina
- **Confiabilidad**: Los procedimientos deben ser reproducibles y verificables

**Ejemplo práctico**: Al realizar una imagen forense de un disco duro comprometido, se debe utilizar herramientas que generen hashes criptográficos (MD5, SHA-1, SHA-256) tanto antes como después del proceso de copia, documentando cada paso en una cadena de custodia detallada.

#### ISO/IEC 27035:2023
A diferencia de la ISO 27037, esta norma cubre todo el proceso investigativo de incidentes de seguridad, desde la planificación y detección hasta la presentación de conclusiones. Establece un marco estructurado para la respuesta a incidentes que incluye la preservación de evidencias como parte integral del proceso.

**Ejemplo práctico**: Durante un ataque de ransomware, la ISO 27035 requiere la documentación inmediata del estado del sistema, la preservación de logs críticos y la implementación de medidas de contención que no comprometan la integridad de las evidencias.

### Normativas Regionales

#### Unión Europea
La UE ha implementado un marco regulatorio robusto que incluye:

- **Ley de Ciberseguridad de la UE (Cybersecurity Act)**: Introduce un marco de certificación de ciberseguridad a escala europea
- **Reglamento (UE) 2024/2847 (Reglamento de Ciberresiliencia)**: Establece requisitos horizontales de ciberseguridad para productos con elementos digitales
- **Reglamento eIDAS**: Proporciona un marco jurídico común para servicios de confianza y identificación electrónica

**Ejemplo práctico**: Una empresa que opera en múltiples países de la UE debe asegurar que sus procedimientos de preservación de evidencias cumplan con los estándares de certificación europeos, incluyendo el uso de servicios de sellado de tiempo cualificados para garantizar la integridad temporal de las evidencias.

#### España
El ordenamiento jurídico español incluye:

- **Código de Derecho de la Ciberseguridad**: Compilación de normativas aplicables
- **Ley 34/2002 de Servicios de la Sociedad de la Información**: Regula aspectos relacionados con evidencias digitales
- **Norma UNE 71505-1:2013**: Estándar español para tecnologías de la información en el ámbito forense

**Ejemplo práctico**: Un perito informático en España debe seguir los procedimientos establecidos en la UNE 71505-1 para la adquisición de evidencias, incluyendo la utilización de herramientas homologadas y la generación de informes periciales que cumplan con los requisitos procesales españoles.

## Principios Fundamentales de la Cadena de Custodia

### Documentación Integral
Todo proceso de preservación debe incluir:
- Fecha y hora exactas de cada actuación
- Identificación del responsable de cada paso
- Descripción detallada de los procedimientos empleados
- Condiciones ambientales y técnicas del proceso

### Inmutabilidad
Las evidencias deben preservarse en su estado original, utilizando:
- Técnicas de imagen forense bit a bit
- Algoritmos hash para verificación de integridad
- Sistemas de almacenamiento con protección contra escritura

### Trazabilidad
Se debe mantener un registro completo de:
- Quién tuvo acceso a las evidencias
- Cuándo se realizó cada acceso
- Qué acciones se ejecutaron
- Dónde se almacenaron las evidencias

## Ejemplos Descriptivos de Aplicación

### Caso 1: Ataque de Phishing Corporativo
**Escenario**: Una empresa detecta un ataque de phishing dirigido que ha comprometido credenciales de empleados.

**Aplicación normativa**:
- **ISO 27037**: Se aplica para la recopilación de logs de servidor de correo, preservación de emails maliciosos y captura de evidencias en estaciones de trabajo comprometidas
- **ISO 27035**: Se utiliza para estructurar la respuesta al incidente, incluyendo la clasificación del evento, análisis de impacto y coordinación con autoridades

**Procedimiento específico**:
1. Aislamiento inmediato de sistemas comprometidos sin apagarlos
2. Captura de memoria volátil (RAM) antes de cualquier otra acción
3. Creación de imágenes forenses de discos duros utilizando herramientas como FTK Imager
4. Preservación de logs de red y sistemas de seguridad
5. Documentación fotográfica del estado físico de los equipos

### Caso 2: Filtración de Datos Sensibles
**Escenario**: Se descubre que información confidencial de clientes ha sido exfiltrada de la base de datos corporativa.

**Aplicación normativa**:
- **Reglamento GDPR**: Requiere notificación a autoridades de protección de datos en 72 horas
- **ISO 27037**: Guía la preservación de evidencias de la base de datos, logs de acceso y sistemas de monitoreo
- **Legislación local**: Determina los requisitos específicos para la colaboración con autoridades judiciales

**Procedimiento específico**:
1. Suspensión inmediata de accesos sospechosos sin alertar al posible perpetrador
2. Preservación de snapshots de base de datos
3. Captura de logs de aplicaciones web y sistemas de autenticación
4. Análisis de tráfico de red para identificar patrones de exfiltración
5. Coordinación con equipos legales para cumplir con requisitos regulatorios

### Caso 3: Ataque de Ransomware
**Escenario**: Un ataque de ransomware ha cifrado sistemas críticos de una organización.

El ransomware es una de las amenazas cibernéticas más persistentes y dañinas de la actualidad. Se clasifica en varios tipos, cada uno con características y modos de operación distintos. A continuación, se presenta una tabla detallada que describe los tipos de ransomware más comunes:

**Tipos de Ransomware**

| Tipo de Ransomware | Descripción | Modus Operandi | Ejemplos Comunes | Impacto Típico |
|---|---|---|---|---|
| **Ransomware de Cifrado (Cryptoransomware / Filecoders)** | Es el tipo más común y peligroso. Cifra los archivos del usuario, haciéndolos inaccesibles. La única forma de recuperar los datos es obteniendo la clave de descifrado, que solo posee el atacante, a cambio de un rescate. | Utiliza algoritmos de cifrado potentes para bloquear archivos individuales o carpetas completas. Se propaga a menudo a través de correos electrónicos de phishing, descargas maliciosas o exploits de vulnerabilidades. | CryptoLocker, WannaCry, Ryuk, REvil (Sodinokibi), LockBit, Dharma, Petya (en algunas variantes) | Pérdida total de acceso a datos críticos y sistemas hasta que se pague el rescate o se restaure desde copias de seguridad. Alto riesgo de pérdida permanente de datos si no se paga o no hay copias de seguridad. |
| **Ransomware de Bloqueo (Locker Ransomware / Screenlockers)** | A diferencia del ransomware de cifrado, este tipo no cifra los archivos, sino que bloquea completamente el acceso al dispositivo o sistema operativo, mostrando una pantalla de bloqueo con la demanda de rescate. | Impide la interacción con el sistema operativo mostrando una ventana a pantalla completa. A menudo se hace pasar por una advertencia de alguna autoridad gubernamental o policial, alegando una infracción legal para exigir una "multa". | Reveton, Winlocker, NotPetya (considerado un "wiper" debido a su irreversibilidad en algunos casos) | Inutilización total del dispositivo. Menos dañino en términos de datos si no hay cifrado, pero muy disruptivo al impedir el uso del equipo. |
| **Scareware** | Es un tipo de malware que se hace pasar por un software antivirus legítimo o una herramienta de limpieza de sistema, que "detecta" problemas ficticios en el dispositivo. Luego, insta al usuario a pagar para solucionar estos problemas inexistentes o para eliminar supuestas amenazas. | Muestra ventanas emergentes, alertas y mensajes constantes que simulan ser avisos de seguridad. Puede no cifrar archivos ni bloquear el sistema por completo, pero es molesto y busca engañar al usuario para que pague. | Algunos programas de "optimización" falsos o "antivirus" fraudulentos. | Puede ser menos dañino en cuanto a la pérdida de datos, pero genera estrés y engaña a los usuarios para que gasten dinero innecesariamente. Algunos scareware pueden evolucionar para incluir funcionalidades de bloqueo. |
| **Doxware (Leakware / Ransomware de Exfiltración de Datos)** | Combina el cifrado o bloqueo con la amenaza de publicar datos sensibles y confidenciales de la víctima si no se paga el rescate. Añade una capa de presión adicional a la extorsión. | Primero, roba datos sensibles de la víctima. Luego, los cifra o bloquea el acceso al sistema, y amenaza con hacer públicos los datos robados en sitios web o foros si no se cumple la demanda de rescate. | Maze, Egregor, Conti (muchas variantes modernas de ransomware de cifrado incorporan esta táctica de doble extorsión) | Pérdida de acceso a datos y, además, un grave riesgo de exposición de información confidencial, lo que puede acarrear daños reputacionales, multas por incumplimiento de normativas de privacidad y otras consecuencias legales y financieras. |
| **Ransomware como Servicio (RaaS)** | Es un modelo de negocio en el que los desarrolladores de ransomware (operadores) crean el malware y lo venden o alquilan a otros ciberdelincuentes (afiliados) a cambio de una tarifa o un porcentaje de los rescates pagados. | Los desarrolladores proporcionan la infraestructura y el código del ransomware, mientras que los afiliados se encargan de la distribución y ejecución de los ataques. Los pagos de rescate se comparten entre ellos. | Cerber, GandCrab, DarkSide, BlackCat (ALPHV) | Facilita a individuos con menos conocimientos técnicos la realización de ataques de ransomware a gran escala, democratizando el acceso a herramientas de extorsión. Aumenta la frecuencia y sofisticación de los ataques. |
| **Ransomware Móvil** | Diseñado específicamente para atacar dispositivos móviles, como smartphones y tabletas. Puede cifrar archivos, bloquear el dispositivo o simplemente mostrar alertas falsas para extorsionar al usuario. | Se propaga a través de aplicaciones maliciosas descargadas de tiendas no oficiales, enlaces de phishing o mensajes de texto. A menudo, busca bloquear la pantalla del dispositivo. | Simplocker, Cyber.Police (variante móvil de Reveton) | Inutiliza el dispositivo móvil, impide el acceso a contactos, fotos y aplicaciones. En algunos casos, puede cifrar los datos almacenados en el dispositivo. |
| **Wiper (Ransomware Destructivo / Destructor de Datos)** | Aunque a veces se presenta como ransomware, su objetivo principal no es la extorsión económica, sino la destrucción irreversible de datos o la inhabilitación del sistema, incluso si se paga el rescate. | Borra o corrompe permanentemente los datos del sistema, a menudo sobrescribiéndolos o cifrándolos de forma que no se puedan recuperar incluso con la clave. Suele ser utilizado por actores de estados-nación o hacktivistas. | NotPetya (en su variante más devastadora), Shamoon, KillDisk | Destrucción masiva e irrecuperable de datos y sistemas, causando daños operacionales graves y duraderos. |
| **Ransomware de Desarrollo Progresivo** | Amenaza con eliminar datos de forma gradual si el rescate no se paga en un tiempo estipulado, creando una sensación de urgencia y pánico en la víctima. | Elimina o corrompe una porción de los archivos en intervalos de tiempo definidos (por ejemplo, cada hora) hasta que se paga el rescate, o hasta que transcurre el tiempo límite y todos los datos son eliminados. | Jigsaw (conocido por su inspiración en la película "Saw") | Presión psicológica extrema sobre la víctima, resultando en la pérdida parcial o total de datos si no se actúa rápidamente. |

**Aplicación normativa**:
- **ISO 27035**: Estructura la respuesta integral al incidente
- **ISO 27037**: Orienta la preservación de evidencias antes de intentar la recuperación
- **Normativas sectoriales**: Pueden requerir notificaciones específicas (sector financiero, salud, etc.)

**Procedimiento específico**:
1. Desconexión inmediata de redes para evitar propagación
2. Preservación de sistemas infectados en su estado actual
3. Captura de muestras del malware para análisis posterior
4. Documentación de archivos cifrados y notas de rescate
5. Análisis de vectores de entrada sin alterar evidencias

## Desafíos en la Implementación

### Jurisdiccionales
- Diferencias en marcos legales entre países
- Requisitos específicos para colaboración internacional
- Variaciones en admisibilidad de evidencias digitales

### Técnicos
- Evolución constante de tecnologías
- Complejidad de sistemas distribuidos en la nube
- Cifrado y técnicas de ocultación avanzadas

### Organizacionales
- Necesidad de personal especializado
- Costos de implementación de herramientas especializadas
- Coordinación entre equipos técnicos y legales

## Notas

La preservación efectiva de evidencias digitales requiere un enfoque multidisciplinario que integre conocimientos técnicos, legales y procedimentales. Las normativas internacionales como ISO/IEC 27037 y 27035 proporcionan un marco sólido, pero deben complementarse con el conocimiento específico de las legislaciones locales y sectoriales. La implementación exitosa de estos marcos normativos es esencial para asegurar que las evidencias digitales mantengan su valor probatorio y puedan ser utilizadas efectivamente en procedimientos judiciales o investigaciones internas.

La formación continua del personal especializado y la actualización constante de procedimientos son elementos críticos para mantener la efectividad de los procesos de preservación de evidencias en un entorno de amenazas cibernéticas en constante evolución.

_____________________________
Referencias Bibliográficas

> Comisión Europea. (2024). *Ley de Ciberseguridad de la UE*. Configurar el futuro digital de Europa. https://digital-strategy.ec.europa.eu/es/policies/cybersecurity-act

> Organización Internacional de Normalización. (2012). *ISO/IEC 27037:2012 - Information technology - Security techniques - Guidelines for identification, collection, acquisition and preservation of digital evidence*. ISO/IEC.

> Organización Internacional de Normalización. (2023). *ISO/IEC 27035:2023 - Information technology - Security techniques - Information security incident management*. ISO/IEC.

> Perito Informático Fernando Amador Díaz. (2025). *ISO 27037: Lineamientos para el manejo de evidencia digital*. https://fernandoamador.com.mx/informatica-forense/iso-27037-lineamientos-evidencia-digital/

> Unión Europea. (2024). *Reglamento (UE) 2024/2847 del Parlamento Europeo y del Consejo, de 23 de octubre de 2024, relativo a los requisitos horizontales de ciberseguridad para los productos con elementos digitales*. Diario Oficial de la Unión Europea.

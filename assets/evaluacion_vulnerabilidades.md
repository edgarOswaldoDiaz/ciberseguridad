# Evaluación de vulnerabilidades en sistemas

La Evaluación de Vulnerabilidades en sistemas es un proceso fundamental en ciberseguridad que busca identificar y analizar las debilidades, fallos o brechas de seguridad existentes en la infraestructura tecnológica de una organización, incluyendo hardware, software, redes, aplicaciones y configuraciones. El objetivo principal es descubrir estos "agujeros" antes de que actores maliciosos puedan explotarlos para obtener acceso no autorizado, robar información, causar interrupciones o comprometer la integridad de los sistemas. Se emplean diversas metodologías, desde escaneos automatizados con herramientas especializadas hasta revisiones manuales exhaustivas, para detectar problemas como software desactualizado, configuraciones incorrectas, contraseñas débiles o fallos en la lógica de las aplicaciones. Los resultados de esta evaluación permiten a las organizaciones comprender su "superficie de ataque", priorizar las vulnerabilidades según su riesgo y, lo más importante, implementar las medidas correctivas necesarias, como la aplicación de parches, la reconfiguración de sistemas o la mejora de las políticas de seguridad, fortaleciendo así su postura de seguridad y reduciendo significativamente la probabilidad de un ciberataque exitoso.

## Fases de la evaluación de vulnerabilidades

1. **Planificación y Alcance**

   * Definir sistemas, redes y aplicaciones a evaluar.
   * Establecer criterios de éxito, calendario y responsables.
   * Obtener autorización por escrito (acuerdo de pruebas) para evitar impactos legales o de continuidad.

2. **Recopilación de Información (Reconocimiento)**

   * Inventario de activos (hardware, software, servicios).
   * Descubrimiento de red (mapa de red, direcciones IP, puertos abiertos).
   * Recolección de metadatos (versiones de SO, aplicaciones, parches instalados).

3. **Identificación de Vulnerabilidades**

   * **Escaneo automatizado**: uso de herramientas (p.ej. **Nessus**, **OpenVAS**, **Qualys**) para detectar CVEs, configuraciones inseguras, contraseñas débiles.
   * **Pruebas manuales**: validación de falsos positivos, explotación controlada de vulnerabilidades, revisión de código o configuraciones críticas.

4. **Análisis y Priorización**

   * Asignar métricas de riesgo (CVSS, OWASP Risk Rating, DREAD).
   * Evaluar el **impacto** (confidencialidad, integridad, disponibilidad) y **probabilidad** de explotación.
   * Generar matriz de criticidad (p.ej. Alto/Medio/Bajo).

5. **Reporte de Resultados**

   * **Contenido mínimo**:

     * Resumen ejecutivo (para la dirección).
     * Descripción detallada de cada vulnerabilidad.
     * Evidencia (capturas, logs, output de escáner).
     * Clasificación de riesgo y recomendaciones de remediación.
   * **Formato**: escribir en lenguaje claro y estructurado, con secciones para desarrollo y anexos técnicos.

6. **Remediación y Validación**

   * Aplicar parches, actualizaciones, cambios de configuración.
   * Re-ejecutar escaneos para confirmar mitigación.
   * Documentar lecciones aprendidas y actualizar políticas de seguridad.

---

## Metodologías y estándares

* **OWASP Testing Guide**: enfoque en aplicaciones web.
* **NIST SP 800-115**: guía de técnicas de pruebas de seguridad.
* **ISO/IEC 27001 y 27002**: incluye requisitos para análisis de vulnerabilidades.


## Guías y Estándares para la Evaluación de Vulnerabilidades

| Estándar/Guía | Enfoque Principal | Puntos Clave en Evaluación de Vulnerabilidades | Relevancia para Aplicaciones Web | Notas Adicionales |
| :------------ | :---------------- | :------------------------------------------- | :------------------------------- | :----------------- |
| **OWASP Testing Guide (OTG)** | Pruebas de seguridad de aplicaciones web. | Proporciona una metodología detallada y una lista exhaustiva de casos de prueba para identificar vulnerabilidades técnicas y lógicas en aplicaciones web. Incluye secciones sobre: \<br\> - Recopilación de información \<br\> - Gestión de configuración \<br\> - Autenticación y autorización \<br\> - Gestión de sesiones \<br\> - Entrada de datos y validación (Inyección SQL, XSS, etc.) \<br\> - Manejo de errores \<br\> - Criptografía \<br\> - Lógica de negocio \<br\> - Pruebas de cliente (ej. JavaScript, DOM) \<br\> - Pruebas de API web (REST, SOAP) | **Extremadamente relevante.** Es la guía de referencia **específica** para la auditoría de seguridad de aplicaciones web. Cubre una amplia gama de vectores de ataque comunes a las aplicaciones web. | Desarrollada por la Open Web Application Security Project (OWASP), una comunidad global sin fines de lucro. Se actualiza periódicamente para reflejar nuevas amenazas y técnicas de ataque. Complementa otras guías con su enfoque altamente técnico y práctico. |
| **NIST SP 800-115: Guía de Técnicas de Pruebas de Seguridad de Información** | Guía general para la planificación, ejecución y análisis de pruebas de seguridad. | Aborda un espectro más amplio de pruebas, incluyendo: \<br\> - **Pruebas de vulnerabilidad:** Identificación de vulnerabilidades en sistemas y redes. \<br\> - **Pruebas de penetración (Penetration Testing):** Simulación de ataques reales para identificar debilidades explotables. \<br\> - **Evaluaciones de seguridad:** Revisiones de configuraciones, arquitectura, políticas y procedimientos. \<br\> Ofrece orientación sobre la fase de preparación, ejecución (con diferentes técnicas como escaneo, revisión de código, fuzzing), y post-ejecución (análisis de resultados, reporte). | **Relevante.** Proporciona un marco metodológico para integrar las pruebas de seguridad de aplicaciones web (como las descritas en OWASP OTG) dentro de un programa de pruebas de seguridad más amplio. Aunque no es específico de aplicaciones web, sus principios son aplicables a la identificación de vulnerabilidades en ellas. | Publicada por el National Institute of Standards and Technology (NIST) de EE. UU. Es una guía fundamental para organizaciones que buscan establecer un programa robusto de pruebas de seguridad en su TI. Distingue claramente entre escaneo de vulnerabilidades y pruebas de penetración. |
| **ISO/IEC 27001: Sistemas de Gestión de la Seguridad de la Información (SGSI)** | Marco para establecer, implementar, mantener y mejorar un SGSI. | Requiere que las organizaciones **identifiquen y gestionen los riesgos de seguridad de la información**, lo que inherentemente incluye la evaluación de vulnerabilidades. Específicamente, en el Anexo A (controles de seguridad), se mencionan requisitos relacionados con: \<br\> - **A.12.6 Gestión de vulnerabilidades técnicas:** Exige la identificación proactiva de vulnerabilidades y la toma de acciones apropiadas. \<br\> - **A.14.2.8 Pruebas de seguridad de desarrollo:** Relacionado con la realización de pruebas de seguridad en el ciclo de vida de desarrollo de software, lo que incluye la detección de vulnerabilidades en aplicaciones. | **Indirectamente relevante pero fundamental.** ISO 27001 no especifica cómo realizar una evaluación de vulnerabilidades, pero **exige** que las organizaciones la realicen como parte de su SGSI. Las aplicaciones web, al ser activos de información críticos, deben ser cubiertas por este requisito. | Estándar internacional para la certificación de SGSI. Su enfoque es la gestión de riesgos de seguridad a nivel organizacional. La certificación ISO 27001 demuestra un compromiso formal con la seguridad de la información. |
| **ISO/IEC 27002: Código de práctica para los controles de seguridad de la información** | Guía de implementación de los controles de seguridad de la información. | Proporciona directrices detalladas para la implementación de los controles mencionados en el Anexo A de ISO 27001. En relación con la evaluación de vulnerabilidades, se enfoca en: \<br\> - **12.6.1 Gestión de las vulnerabilidades técnicas:** Aconseja procesos para obtener información sobre vulnerabilidades, evaluarlas, y tomar medidas oportunas. \<br\> - **14.2.8 Pruebas de seguridad en el desarrollo de software y sistemas:** Proporciona orientación sobre la importancia de integrar las pruebas de seguridad a lo largo del ciclo de vida de desarrollo, incluyendo la realización de pruebas de vulnerabilidad en aplicaciones. | **Indirectamente relevante pero proporciona orientación vital.** Ofrece el "cómo" para cumplir con los requisitos de ISO 27001 en cuanto a la gestión y pruebas de vulnerabilidades en aplicaciones, incluyendo las web. | Es un estándar complementario a ISO 27001, que detalla las mejores prácticas para los controles de seguridad. Ayuda a las organizaciones a interpretar e implementar los requisitos de seguridad de ISO 27001 de manera efectiva. |

**En Resumen:**

  * **OWASP Testing Guide** es la biblia para las pruebas de seguridad **prácticas y técnicas** de aplicaciones web.
  * **NIST SP 800-115** proporciona el **marco metodológico general** para la realización de pruebas de seguridad, que puede incluir las pruebas de aplicaciones web.
  * **ISO/IEC 27001 y 27002** establecen el **requisito organizacional y la guía de mejores prácticas** para gestionar los riesgos de seguridad y, por ende, la necesidad de realizar evaluaciones de vulnerabilidades en todos los activos de información, incluidas las aplicaciones web, como parte de un SGSI.

Para una evaluación integral de la seguridad de las aplicaciones web, lo ideal es combinar los principios de gestión de riesgos de ISO 27001/27002 con las metodologías de pruebas detalladas de OWASP OTG, en el marco de un programa de pruebas estructurado como el propuesto por NIST SP 800-115.


---

## Herramientas representativas

| Tipo de herramienta         | Ejemplos                | Uso principal                                                 |
| --------------------------- | ----------------------- | ------------------------------------------------------------- |
| Escáner de vulnerabilidades | Nessus, OpenVAS, Qualys | Identificación automática de CVEs, configuraciones inseguras. |
| Escáner web                 | OWASP ZAP, Burp Suite   | Detección de XSS, SQLi, CSRF y otros fallos web.              |
| Análisis de configuraciones | Lynis, CIS-CAT          | Revisión de configuración de sistemas operativos.             |
| Contraseñas y fuerza bruta  | Hydra, John the Ripper  | Evaluación de políticas de contraseñas, hashes.               |

---

## Buenas prácticas

* **Frecuencia regular**: realizar evaluaciones trimestrales o antes/depués de cambios mayores.
* **Seguridad por capas**: no depender de un solo escáner, combinar enfoques manuales y automáticos.
* **Gestión del ciclo de vida**: integrar hallazgos en el proceso de desarrollo (DevSecOps).
* **Capacitación continua**: mantener al equipo actualizado en nuevas vulnerabilidades y herramientas.
* **Reporte claro y accionable**: enfocar recomendaciones en actividades concretas y priorizadas.

---

## Laboratorio de ciberseguridad

  1. Montar un laboratorio con contenedores.
  2. Ejecutar escaneos con OWASP ZAP.
  3. Analizar resultados, redactar un informe y proponer remediaciones.
  4. Aplicar parches/configuraciones y validar la mitigación.

_______________________
Referencias bibliográficas

> Scarfone, K., & Mell, P. (2008). Guide to Security Assessment and Testing (NIST Special Publication 800‑115). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-115

> OWASP Foundation. (2021). OWASP Testing Guide Version 4. The Open Web Application Security Project. Recuperado de https://owasp.org/www-project-web-security-testing-guide/

> International Organization for Standardization. (2013). ISO/IEC 27001:2013 – Information technology — Security techniques — Information security management systems — Requirements. ISO.

> McGraw, G. (2006). Software Security: Building Security In. Addison‑Wesley Professional.

> Northcutt, S., Shenk, J., Winters, J., & London, P. (2000). Network Security Assessment: Know Your Network. O’Reilly Media.

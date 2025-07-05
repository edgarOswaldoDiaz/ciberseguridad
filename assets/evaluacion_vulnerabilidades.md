# Evaluación de vulnerabilidades en sistemas

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


# Técnicas de mitigación de riesgos de seguridad

## Clasificación de controles de mitigación

1. **Controles preventivos**
   Diseñados para evitar que ocurra un incidente de seguridad.

   * Ejemplo: Gestión de parches, hardening de sistemas, políticas de acceso.

2. **Controles detectivos**
   Permiten identificar y alertar sobre actividades anómalas o intentos de ataque.

   * Ejemplo: Sistemas de detección de intrusos (IDS), monitoreo de logs, análisis de tráfico.

3. **Controles correctivos**
   Minimizan el impacto de un incidente y restauran la operación normal.

   * Ejemplo: Planes de respuesta a incidentes, recuperación ante desastres, copias de seguridad.

---

## Principales técnicas de mitigación

| Categoría                   | Técnica                               | Descripción breve                                                                                                                       |
| --------------------------- | ------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| **Gestión de parches**      | Patch Management                      | Proceso sistemático de identificación, prueba y despliegue de actualizaciones de software para corregir vulnerabilidades conocidas.     |
| **Endurecimiento**          | System Hardening                      | Eliminación de servicios innecesarios, cierre de puertos abiertos, configuración segura de OS y aplicaciones.                           |
| **Control de acceso**       | Principio de mínima privilegio        | Asignar a cada usuario y proceso únicamente los permisos estrictamente necesarios para sus funciones.                                   |
| **Autenticación**           | Autenticación multifactor (MFA)       | Implementar capas adicionales (por ejemplo, token, biometría) para verificar la identidad del usuario.                                  |
| **Seguridad de red**        | Segmentación y firewalls              | Dividir la red en zonas de seguridad y utilizar firewalls perimetrales/inter-zonas para controlar el tránsito.                          |
| **Cifrado**                 | Cifrado de datos en tránsito y reposo | Uso de protocolos (TLS, IPSec) y cifrado en disco para proteger la confidencialidad e integridad de la información.                     |
| **Detección**               | IDS/IPS                               | Sistemas de Detección/Prevención de Intrusos para identificar patrones maliciosos y bloquear ataques en tiempo real.                    |
| **Respaldo y recuperación** | Backups y DRP                         | Políticas de copias de seguridad regulares y Plan de Recuperación ante Desastres para restaurar sistemas críticos rápidamente.          |
| **Educación**               | Capacitación y concienciación         | Programas periódicos de formación en seguridad para usuarios y administradores sobre buenas prácticas y amenazas emergentes.            |
| **Evaluación continua**     | Pruebas de penetración y auditorías   | Ejecución recurrente de pentests y auditorías internas/externas para validar la efectividad de los controles y detectar nuevas brechas. |

---

## Metodología de implementación

1. **Análisis de riesgos**

   * Asignar nivel de riesgo a cada activo (impacto × probabilidad).
   * Determinar qué técnicas aplican mejor a cada vulnerabilidad identificada.

2. **Definición de políticas y procedimientos**

   * Establecer estándares de configuración (baselines) y flujos de trabajo para gestión de parches, backups y controles de acceso.

3. **Despliegue y configuración**

   * Automatizar parches y hardening con herramientas de gestión centralizada.
   * Configurar MFA, firewalls y cifrado siguiendo guías de fabricantes y frameworks (p.ej. CIS Benchmarks).

4. **Monitoreo y ajuste**

   * Implementar SIEM para correlación de eventos.
   * Revisar métricas clave (tiempo medio de parcheo, número de incidentes, ratios de detección) y ajustar controles.

5. **Validación continua**

   * Programar escaneos periódicos, pentesting y revisiones de configuración.
   * Incorporar hallazgos en el ciclo DevSecOps, cerrando el ciclo de mejora continua.

---

## Buenas prácticas

* **Automatización**: reducir errores humanos en despliegue de parches y configuración.
* **Defensa en profundidad**: combinar varias capas de controles para aumentar la resiliencia.
* **Documentación y registro**: mantener bitácoras de parches, cambios de configuración e incidentes.
* **Pruebas en entornos controlados**: validar actualizaciones y nuevas configuraciones en entornos de staging antes de producción.
* **Colaboración interdepartamental**: alinear TI, Seguridad y Operaciones para una respuesta coordinada.

___________________
Referencias bibliográficas 

> Souppaya, M., & Scarfone, K. (2020). *Guide to Enterprise Patch Management Technologies* (NIST Special Publication 800‑40 Rev. 4). National Institute of Standards and Technology. [https://doi.org/10.6028/NIST.SP.800-40r4](https://doi.org/10.6028/NIST.SP.800-40r4)

> Joint Task Force Transformation Initiative. (2020). *Security and Privacy Controls for Information Systems and Organizations* (NIST Special Publication 800‑53 Rev. 5). National Institute of Standards and Technology. [https://doi.org/10.6028/NIST.SP.800-53r5](https://doi.org/10.6028/NIST.SP.800-53r5)

> International Organization for Standardization. (2022). *ISO/IEC 27002:2022 – Information technology — Security techniques — Code of practice for information security controls*. ISO.

> Stallings, W. (2021). *Effective Cybersecurity: A Guide to Using Best Practices and Standards* (2nd ed.). Addison‑Wesley Professional.

> Easttom, C. (2020). *Computer Security Fundamentals* (4th ed.). Pearson.

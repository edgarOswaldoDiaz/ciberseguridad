# Gestión de parches y actualizaciones de seguridad

---

## Ciclo de vida de la gestión de parches

1. **Inventario de activos**

   * Registro detallado de hardware, sistemas operativos, aplicaciones y versiones instaladas.
   * Herramientas: CMDB, escáneres de red.

2. **Detección y evaluación de parches**

   * Monitorización de boletines de proveedores (Microsoft, Linux distros, fabricantes de hardware).
   * Clasificación de críticas según CVSS y calendario de publicación.

3. **Priorización**

   * Basada en **riesgo** (impacto × probabilidad) y **exposición** (sistemas expuestos a Internet, datos sensibles).
   * Asignar niveles: Urgente (0–7 días), Alto (7–30 días), Medio/Bajo (>30 días).

4. **Prueba en entorno controlado**

   * Validar que el parche no genere incompatibilidades ni interrupciones.
   * Uso de entornos de staging o laboratorios de pruebas.

5. **Despliegue y automatización**

   * Herramientas de despliegue centralizado: WSUS, SCCM, Ansible, Puppet, Chef, SCC.
   * Programación de ventanas de mantenimiento, con notificación a usuarios y respaldos previos.

6. **Verificación y auditoría**

   * Reescanear sistemas para confirmar que los parches se aplicaron correctamente.
   * Generar reportes y registrar incidentes de fallo o revocación.

7. **Monitoreo continuo y métricas**

   * Indicadores clave: tiempo medio de parcheo (MTTP), tasa de éxito de despliegues, número de excepciones.
   * Ajustar políticas según resultados y lecciones aprendidas.

---
## Marco regulatorio - Frameworks

## **Tabla Comparativa: NIST SP 800-40 Rev. 4 vs ISO/IEC 27002:2022 – Gobernanza en Gestión de Parches y Vulnerabilidades**

| Criterio | **NIST SP 800-40 Rev. 4 (Guide to Enterprise Patch Management)** | **ISO/IEC 27002:2022 – Sección 5.16: Gestión de Cambios & Sección 5.23: Gestión de Vulnerabilidades** |
|--------|------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| **Objetivo principal** | Proporcionar directrices para establecer un programa efectivo de gestión de parches en entornos empresariales. | Establecer buenas prácticas para gestionar cambios seguros en sistemas y manejar las vulnerabilidades identificadas. |
| **Enfoque** | Técnico-operativo: centrado en el ciclo de vida del parche, desde identificación hasta despliegue y verificación. | Organizacional y normativo: define controles generales para asegurar procesos de cambio y mitigación de vulnerabilidades. |
| **Ámbito** | Gestión de parches de software como parte de la ciberseguridad operativa. | Gestión integral del riesgo asociado a cambios en activos e identificación y tratamiento de vulnerabilidades. |

### **Gestión del Proceso de Parcheo**

| Elemento | **NIST SP 800-40 Rev. 4** | **ISO/IEC 27002:2022 – Sección 5.23 (Vulnerabilidad)** |
|---------|----------------------------|--------------------------------------------------------|
| **Identificación de parches** | Recomienda suscribirse a fuentes confiables de información de seguridad (ej.: CVE, US-CERT, proveedores). | Requiere monitoreo continuo de fuentes de inteligencia de amenazas y vulnerabilidades relevantes. |
| **Evaluación de impacto** | Evaluar criticidad del sistema y severidad del parche antes de implementarlo. | Clasificar vulnerabilidades según su gravedad y exposición real. |
| **Pruebas previas al despliegue** | Realizar pruebas en entornos controlados para evitar incompatibilidades o interrupciones. | No prescribe métodos técnicos, pero sugiere evaluar el impacto de cambios antes de aplicarlos. |
| **Despliegue y priorización** | Priorizar parches críticos basados en CVSS, criticidad del activo y exposición. | Promover acciones correctivas prioritarias para vulnerabilidades altas y críticas. |
| **Verificación posterior** | Confirmar aplicación exitosa y revisar logs de cumplimiento. | Validar que se hayan corregido las vulnerabilidades reportadas. |
| **Documentación y registro** | Documentar todo el proceso, incluyendo excepciones, retrasos y justificaciones. | Registrar cambios realizados y medidas tomadas ante vulnerabilidades. |

### **Integración con Gestión de Cambios**

| Elemento | **NIST SP 800-40 Rev. 4** | **ISO/IEC 27002:2022 – Sección 5.16 (Gestión de Cambios)** |
|---------|----------------------------|----------------------------------------------------------|
| **Relación con cambios** | Los parches son considerados cambios técnicos que deben integrarse al marco general de gestión de cambios. | Define requisitos para evaluar y autorizar cambios que puedan afectar la seguridad de la información. |
| **Aprobación formal** | Se requiere aprobación antes de aplicar parches críticos en producción. | Los cambios deben ser evaluados por comités de control de cambios (CCB) y documentados formalmente. |
| **Rollback planificado** | Recomienda tener planes de reversión en caso de fallos tras la aplicación de parches. | Exige planes de contingencia para revertir cambios no exitosos. |
| **Seguimiento post-cambio** | Monitoreo constante tras la aplicación del parche para detectar problemas. | Verificación continua de la estabilidad y seguridad después del cambio. |

### **Gobernanza y Rol de las Partes Interesadas**

| Elemento | **NIST SP 800-40 Rev. 4** | **ISO/IEC 27002:2022** |
|---------|----------------------------|--------------------------|
| **Responsables** | Equipo de TI/seguridad responsable de parcheo; administradores de sistemas. | Comités de gestión de cambios; equipos de seguridad y operaciones. |
| **Políticas y procedimientos** | Deben existir políticas claras sobre tiempos máximos de aplicación de parches (SLAs). | Definir roles y responsabilidades para todos los tipos de cambios y vulnerabilidades. |
| **Supervisión ejecutiva** | Involucrar a la dirección en la definición de niveles de tolerancia al riesgo y priorización de parches. | Alta dirección debe garantizar que los cambios y vulnerabilidades sean gestionados conforme al ISMS. |
| **Capacitación** | Capacitar a personal técnico en herramientas, procesos y mejores prácticas de parcheo. | Promover concientización sobre los riesgos asociados a los cambios y vulnerabilidades. |

### **Herramientas y Automatización**

| Elemento | **NIST SP 800-40 Rev. 4** | **ISO/IEC 27002:2022** |
|---------|----------------------------|--------------------------|
| **Uso de herramientas automatizadas** | Recomienda usar soluciones de gestión de parches automatizadas (SCCM, WSUS, etc.). | Apoya el uso de tecnologías que faciliten el monitoreo y respuesta a cambios y vulnerabilidades. |
| **Inventario de activos** | Es fundamental mantener inventarios actualizados para identificar qué equipos necesitan parches. | Requiere inventario de activos para evaluar el impacto de cambios y el estado de vulnerabilidades. |
| **Integración con otros controles** | Integración con SIEM, IDS/IPS, EDR, y sistemas de gestión de vulnerabilidades. | Promueve la coordinación entre controles de seguridad y procesos de gestión del ciclo de vida. |

---

## Desafíos comunes

* **Complejidad y diversidad de entornos**: múltiples sistemas operativos, versiones y aplicaciones.
* **Ventanas de mantenimiento reducidas** en infraestructuras críticas 24×7.
* **Falsos positivos y dependencias**: algunos parches pueden generar fallos en servicios interrelacionados.
* **Gestión de excepciones**: definir cuándo y cómo aplazar o denegar un parche, documentando el riesgo residual.

---

## Buenas prácticas

* **Automatizar** al máximo: reducción de errores manuales y aceleración de despliegues.
* **Definir SLAs internos** de parcheo según criticidad.
* **Comunicación y coordinación** previa con equipos de operaciones y usuarios.
* **Respaldo completo** antes de cualquier actualización mayor.
* **Incorporar parcheo en DevSecOps**: pruebas de parcheo en pipelines de CI/CD.
* **Revisión y actualización periódica** de políticas de gestión de parches.

---

Referencias bibliográficas

> Souppaya, M., & Scarfone, K. (2020). *Guide to Enterprise Patch Management Technologies* (NIST Special Publication 800‑40 Rev. 4). National Institute of Standards and Technology. [https://doi.org/10.6028/NIST.SP.800-40r4](https://doi.org/10.6028/NIST.SP.800-40r4)

> International Organization for Standardization. (2022). *ISO/IEC 27002:2022 – Information technology — Security techniques — Code of practice for information security controls*. ISO.

> Merkow, J., & Breithaupt, J. (2014). *Information Security: Principles and Practice* (2nd ed.). Addison‑Wesley Professional.

> Whitman, M. E., & Mattord, H. J. (2017). *Principles of Incident Response and Disaster Recovery*. Cengage Learning.

> Stallings, W. (2018). *Effective Cybersecurity: A Guide to Using Best Practices and Standards* (2nd ed.). Addison‑Wesley Professional.

# Técnicas de mitigación de riesgos de seguridad

Las Técnicas de Mitigación de Riesgos de Seguridad son el conjunto de acciones y controles implementados para reducir la probabilidad de ocurrencia de un riesgo o minimizar su impacto si este se materializa. Tras identificar y evaluar las vulnerabilidades, estas técnicas buscan fortalecer la postura de seguridad. Incluyen medidas proactivas como la aplicación de parches y actualizaciones de software, la configuración segura de sistemas y redes, la implementación de controles de acceso robustos, el cifrado de datos sensibles y la segmentación de redes. También abarcan la concienciación y capacitación del personal, la creación de planes de respuesta a incidentes y la realización de copias de seguridad. La elección de la técnica adecuada depende de la naturaleza del riesgo y el nivel de impacto, buscando un equilibrio costo-beneficio para proteger los activos críticos de una organización.

## Clasificación de controles de mitigación

---

## 1. **Controles Preventivos**
### Definición:
Los controles preventivos están diseñados para **evitar que ocurra un incidente de seguridad**. Su objetivo es reducir la probabilidad de que una amenaza materialice un ataque exitoso.

### Propósito:
- Bloquear amenazas antes de que causen daño.
- Reducir las superficies de ataque.
- Proteger activos críticos mediante barreras iniciales.

### Ejemplos:
- **Firewalls**: Filtran el tráfico entrante y saliente para bloquear conexiones no autorizadas.
- **Sistemas de prevención de intrusiones (IPS)**: Detectan y bloquean intentos de intrusión en tiempo real.
- **Autenticación fuerte (2FA/MFA)**: Verifica la identidad del usuario antes de permitir el acceso a sistemas.
- **Políticas de contraseñas seguras**: Impiden el uso de credenciales débiles.
- **Control de acceso físico**: Uso de tarjetas magnéticas, biometría, guardias de seguridad.
- **Parcheo y actualización de software**: Corrige vulnerabilidades conocidas antes de que sean explotadas.
- **Cifrado de datos**: Protege información sensible incluso si es interceptada.

### Importancia:
Estos controles son fundamentales como primera línea de defensa y forman parte del principio de "defensa en profundidad".

---

## 2. **Controles Detectivos**
### Definición:
Los controles detectivos tienen como finalidad **identificar y alertar sobre actividades anómalas o intentos de ataque** que ya están sucediendo o han tenido lugar.

### Propósito:
- Detectar amenazas que pudieran haber evitado los controles preventivos.
- Generar alertas tempranas para una respuesta rápida.
- Facilitar la investigación posterior mediante registros de actividad.

### Ejemplos:
- **Sistemas de detección de intrusiones (IDS)**: Monitorean el tráfico en busca de patrones sospechosos.
- **Monitoreo de logs (SIEM)**: Agregan y analizan registros de eventos de múltiples fuentes para detectar anomalías.
- **Software de detección de malware**: Identifica código malicioso mediante firmas o comportamiento.
- **Intrusion Detection Systems (IDS) basados en host o red**.
- **Alertas de acceso no autorizado**: Notificaciones cuando se intenta acceder a recursos restringidos.
- **Análisis de comportamiento del usuario (UEBA - User and Entity Behavior Analytics)**: Detecta comportamientos fuera de lo normal.

### Importancia:
Estos controles son esenciales para responder rápidamente a incidentes que pasaron desapercibidos inicialmente. Sin ellos, muchos ataques podrían continuar sin ser notados por semanas o meses.

---

## 3. **Controles Correctivos**
### Definición:
Los controles correctivos buscan **minimizar el impacto de un incidente ya ocurrido** y **restaurar la operación normal** lo más rápido posible.

### Propósito:
- Limitar los daños una vez que se detecta un incidente.
- Restablecer los servicios afectados.
- Recuperar la integridad, disponibilidad y confidencialidad de los datos.

### Ejemplos:
- **Planes de respuesta a incidentes (IRP - Incident Response Plan)**: Guían los pasos a seguir durante un ataque.
- **Backups regulares**: Permiten restaurar datos perdidos o corrompidos.
- **Desconexión automática o manual de sistemas comprometidos**: Para evitar la propagación del daño.
- **Reinstalación o reimagen de equipos infectados**: Elimina malware persistente.
- **Actualización de políticas de seguridad post-incidente**: Mejora la protección tras aprender de la experiencia.
- **Recuperación ante desastres (DRP - Disaster Recovery Plan)**: Restablece operaciones tras fallos catastróficos.
- **Bloqueo de cuentas comprometidas**: Prevenir acceso adicional no autorizado.

### Importancia:
Estos controles son vitales para la continuidad del negocio y la recuperación tras un evento adverso. Ayudan a cumplir con estándares de resiliencia y tiempos de recuperación aceptables (RTO/RPO).

**RTO (Recovery Time Objective)** y **RPO (Recovery Point Objective)** son métricas clave en la gestión de la continuidad del negocio y la recuperación ante desastres en sistemas de TI.

- **RTO (Objetivo de Tiempo de Recuperación)**: Es el tiempo máximo aceptable que un sistema, aplicación o proceso puede estar inactivo tras un fallo antes de que cause un daño significativo al negocio. Por ejemplo, si el RTO de un sistema es de 4 horas, significa que la empresa puede tolerar hasta 4 horas de inactividad antes de que se vea gravemente afectada. Un RTO bajo indica la necesidad de soluciones de recuperación rápidas, como sistemas de respaldo en caliente.

- **RPO (Objetivo de Punto de Recuperación)**: Es la cantidad máxima de datos que una empresa puede permitirse perder, medida en tiempo, entre la última copia de seguridad y el momento del fallo. Por ejemplo, si el RPO es de 1 hora, significa que se podrían perder hasta 1 hora de datos generados antes del incidente. Un RPO bajo requiere respaldos frecuentes o replicación en tiempo real.

**Ejemplo práctico**:
- Un banco con un sistema crítico (como transacciones en línea) podría tener un RTO de 30 minutos (debe volver a operar en media hora) y un RPO de 5 minutos (solo puede perder 5 minutos de transacciones).
- Una tienda en línea menos crítica podría tolerar un RTO de 24 horas y un RPO de 4 horas, ya que el impacto de la pérdida de datos o tiempo de inactividad es menor.

En resumen, **RTO** mide el tiempo de inactividad tolerable, y **RPO** mide la cantidad de datos que se pueden perder. Ambos son esenciales para diseñar estrategias de recuperación y determinar la inversión en infraestructura de respaldo.

---

## Resumen Comparativo:

| Tipo de Control     | Objetivo Principal                      | Momento de Aplicación        | Ejemplo Clave                  |
|---------------------|----------------------------------------|-------------------------------|--------------------------------|
| **Preventivo**      | Evitar que ocurra un incidente         | Antes del incidente           | Firewall, autenticación MFA    |
| **Detectivo**       | Identificar actividades sospechosas    | Durante o poco después del ataque | IDS, monitoreo de logs         |
| **Correctivo**      | Minimizar daño y restaurar operación   | Después del incidente         | Respuesta a incidentes, backups |

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

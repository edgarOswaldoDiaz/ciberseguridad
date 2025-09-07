# Implementación

La implementación se centra en los procesos y actividades relacionados con la forma en que una organización construye e implementa componentes de software y sus defectos relacionados.

Las actividades dentro de la función de implementación tienen el mayor impacto en la vida diaria de los desarrolladores. El objetivo conjunto es enviar un software que funcione de forma fiable con el mínimo de defectos.

| Actividad             | Descripción                                                                                                                                                                                                                                     | Ejemplos                                                                                                                                                                                                                                                                                                                        |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Construcción segura   | Garantizar que el proceso de construcción (build) del software incorpore controles de seguridad desde el código fuente hasta el artefacto final. Incluye uso de herramientas automáticas que detecten defectos y dependencias inseguras.        | 1. Integrar análisis estático (SAST) en el pipeline de CI/CD para bloquear builds con vulnerabilidades críticas.<br>2. Escaneo de dependencias con herramientas como OWASP Dependency-Check para identificar bibliotecas con CVE conocidas.<br>3. Firmado digital de artefactos para asegurar su integridad.                    |
| Implementación segura | Asegurar que el despliegue y la configuración de la aplicación en producción o entornos intermedios se realicen con prácticas que minimicen la exposición a riesgos. Implica revisión de configuraciones, gestión de secretos y endurecimiento. | 1. Uso de gestores de configuración (Ansible, Terraform) con plantillas seguras que eviten valores por defecto inseguros.<br>2. Almacenamiento de credenciales en un vault (HashiCorp Vault, Azure Key Vault) en lugar de ficheros de configuración planos.<br>3. Diseño de redes segmentadas y firewalls para limitar accesos. |
| Gestión de defectos   | Establecer un ciclo de vida para identificar, rastrear, priorizar y corregir vulnerabilidades y fallos de seguridad reportados. Incluye métricas de tiempo de resolución y procesos de reproceso.                                               | 1. Registrar cada hallazgo en un sistema de seguimiento (JIRA, GitHub Issues) con clasificación de severidad y SLA asociados.<br>2. Realizar retesting automatizado de parches con pruebas de regresión de seguridad.<br>3. Mantener un backlog de vulnerabilidades y revisar mensualmente su evolución.                        |

**Detalle ampliado por punto:**

* **Construcción segura:**

  * Se basa en asegurar que cada artefacto compilado proviene de un código revisado y escaneado.
  * Ejemplo: bloquear automáticamente el merge de pull requests si SAST detecta inyección SQL o XSS de alto riesgo.

* **Implementación segura:**

  * Abarca tanto la configuración de la propia aplicación como la del entorno que la ejecuta (servidores, contenedores, orquestadores).
  * Ejemplo: usar políticas de admisión en Kubernetes para rechazar pods que monten contenedores con privilegios elevados.

* **Gestión de defectos:**

  * Va más allá de la simple corrección: mide tiempos de respuesta, efectividad de parches y previene la reintroducción de fallos.
  * Ejemplo: después de resolver una vulnerabilidad, automatizar una build que ejecute pruebas de seguridad para asegurarse de que el mismo defecto no reaparezca en futuras versiones.
________________

> https://owaspsamm.org/model/

> By CISO oswaldo.diaz 

# Operaciones

La función de negocio de operaciones abarca las actividades necesarias para garantizar que la confidencialidad, la integridad y la disponibilidad se mantengan durante toda la vida operativa de una aplicación y sus datos asociados. Una mayor madurez con respecto a esta función de negocio proporciona una mayor seguridad de que la organización es resistente frente a las interrupciones operativas y responde a los cambios en el panorama operativo.

| Proceso                        | Descripción clave                                                                                                                                         | Ejemplo práctico                                                                                                                                                                                         |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Gestión de incidentes**      | Ciclo de vida de respuesta a incidentes: detección y análisis, contención, erradicación, recuperación y lecciones aprendidas.                             | Un SIEM alerta sobre exfiltración de datos; el servidor comprometido se aísla (quarantine), se parchea el plugin vulnerable, se restauran servicios y se realiza un workshop para mejorar el parcheo.    |
| **Gestión del medio ambiente** | Control y aseguramiento de los entornos (dev, test, prod) mediante infraestructuras como código, hardening, separación de ambientes y gestión de cambios. | Uso de Terraform con distintos workspaces (dev, staging, prod) y Ansible/Chef para verificar checklist de hardening tras cada despliegue, asegurando configuraciones idénticas y seguras.                |
| **Gestión operativa**          | Mantenimiento diario de la seguridad en producción: parcheo programado, monitoreo continuo, backups y DRP, control de acceso y gestión de cambios.        | Cada primer martes de mes se aplican parches en servidores; pruebas automáticas en staging; monitoreo de sistemas 48 h post-despliegue; reviews trimestrales de accesos para revocar permisos obsoletos. |

_______________________

> By CISO oswaldo.diaz

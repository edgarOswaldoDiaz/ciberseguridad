# Gobernanza** en OWASP SAMM

---

## Estrategia y métricas

**Objetivo:**
Definir y mantener una estrategia de seguridad de software alineada con los objetivos de negocio, y establecer métricas que permitan medir el progreso y justificar las inversiones en seguridad.

| Nivel de madurez  | Qué implica                                                    | Ejemplo práctico                                                                                                                                                                                  |
| ----------------- | -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1. Inicial**    | No existe estrategia formal; las métricas son ad hoc.          | - El equipo de desarrollo anota de manera esporádica el número de vulnerabilidades encontradas en un sprint.                                                                                      |
| **2. Definido**   | Hay una estrategia documentada y métricas básicas.             | - Se publica un plan anual de seguridad que define objetivos (p.ej., reducir XSS en 50%).<br>- Se reportan mensual­mente: # de hallazgos en pentests, # de CVEs parcheados.                       |
| **3. Medido**     | Métricas cuantitativas vinculadas a KPIs de negocio.           | - Se correlaciona el % de vulnerabilidades críticas resueltas vs. tasa de despliegues exitosos.<br>- Se usan dashboards (p.ej., en Grafana) con indicadores de tiempo medio de resolución (MTTR). |
| **4. Optimizado** | Estrategia dinámica basada en datos históricos y benchmarking. | - Se ajustan recursos del equipo de seguridad según tendencias de incidentes.<br>- Se comparan métricas con peers de la industria para fijar metas (“benchmarking”).                              |

> **Ejemplo de implementación**
> Una fintech define como KPI: “<u>Reducir en un 75% las vulnerabilidades críticas detectadas en escaneos automáticos al cabo de 12 meses</u>”. Para ello:
>
> 1. Documenta la estrategia en un playbook de seguridad.
> 2. Establece un tablero con gráficas semanales de # de vulnerabilidades por severidad.
> 3. Revisa trimestralmente los resultados en junta de dirección y revisa el presupuesto de herramientas de SAST/DAST.

---

## Políticas y cumplimientos

**Objetivo:**
Crear, comunicar y hacer cumplir políticas de seguridad y alinearlas con regulaciones legales, estándares de la industria y requerimientos internos.

| Nivel de madurez  | Qué implica                                                           | Ejemplo práctico                                                                                                                                                         |
| ----------------- | --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **1. Inicial**    | Políticas informales o inexistentes; cumplimiento reactivo.           | - “Hacemos lo que podemos” cuando un auditor externo exige controles mínimos.                                                                                            |
| **2. Definido**   | Políticas documentadas y revisadas periódicamente; controles básicos. | - Existe una política de “<u>uso aceptable</u>” de componentes de terceros.<br>- Se realizan auditorías anuales de cumplimiento ISO/IEC 27001.                           |
| **3. Medido**     | Medición del grado de cumplimiento y procesos de remediación.         | - Se generan reportes trimestrales: % de servicios con registro de auditoría habilitado.<br>- Se automatiza la comprobación de configuraciones seguras (CIS Benchmarks). |
| **4. Optimizado** | Gobierno de políticas con ciclos de mejora continua y automatización. | - Las políticas se versionan en Git; cada PR dispara validaciones automáticas.<br>- Integración de reglas de compliance (p.ej., PCI‑DSS) en pipelines CI/CD.             |

> **Ejemplo de implementación**
> En una empresa de salud que debe cumplir HIPAA:
>
> 1. Publica una “Política de manejo de datos sensibles” que describe cifrado, acceso y retención.
> 2. Integra un escáner de configuración (InSpec, Chef) que verifica que todos los servidores de producción cumplen con la política.
> 3. Cada hallazgo genera automáticamente un ticket en el sistema de gestión para su remediación.

---

## Educación y orientación

**Objetivo:**
Proveer formación continua, guías y apoyo a todos los participantes del ciclo de vida del software, para que la seguridad sea parte integral de su día a día.

| Nivel de madurez  | Qué implica                                                    | Ejemplo práctico                                                                                                                                                            |
| ----------------- | -------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1. Inicial**    | Formación esporádica; depende de la buena voluntad individual. | - Un par de charlas al año sobre OWASP Top 10, sin seguimiento.                                                                                                             |
| **2. Definido**   | Plan de formación regular y materiales básicos disponibles.    | - Cursos trimestrales obligatorios sobre “Seguridad en APIs REST”.<br>- Repositorio interno con plantillas de threat modeling.                                              |
| **3. Medido**     | Evaluaciones y métricas de efectividad de la formación.        | - Se realiza un examen post‑curso y se mide la reducción de hallazgos de seguridad en proyectos entrenados.<br>- Se llevan estadísticas de asistencia y rendimiento.        |
| **4. Optimizado** | Programa de embajadores de seguridad y mentoring continuo.     | - Cada equipo tiene un “Security Champion” que recibe formación avanzada y guía localmente.<br>- Se organiza un Capture The Flag interno mensual para consolidar conceptos. |

> **Ejemplo de implementación**
> Una plataforma de e‑commerce:
>
> 1. Identifica y forma a un “Security Champion” en cada squad (equipo Ágil).
> 2. Publica guías “in‑context” (p.ej., snippets de código seguro disponibles en el IDE mediante plugin).
> 3. Mide el impacto: tras 6 meses, los proyectos con champion presentan un 40 % menos de hallazgos en code review.

---

**¿Cómo empezar?**

1. **Diagnóstico inicial:** Mide tu madurez en cada práctica (puedes usar la hoja de puntajes de OWASP SAMM).
2. **Roadmap de mejora:** Prioriza las iniciativas de mayor impacto (p.ej., automatizar métricas antes que crear un CTF interno).
3. **Pilotos y ajustes:** Implementa en un grupo pequeño (un par de squads) y ajusta procesos antes del despliegue global.

________________

> By CISO oswaldo.diaz

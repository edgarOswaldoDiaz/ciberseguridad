# Laboratorio de ciberseguridad

## Arquitectura general del laboratorio

1. **Host principal**

   * Máquina física o VM con Ubuntu 24.04 LTS.
   * Alojamiento de Docker Engine o Podman, y de un orchestrador ligero (Docker Compose o Kubernetes tipo k3s).

2. **Red interna segmentada**

   * VLAN o red virtual “lab-net” para aislar contenedores del resto del entorno.
   * Firewall (p. ej. UFW o nftables en el host) para controlar accesos entrantes/salientes.

3. **Registro de contenedores**

   * Un registry privado (p. ej. **Docker Registry** o **Harbor**) para almacenar imágenes propias.

4. **Almacenamiento compartido**

   * Volúmenes Docker (o NFS) para persistencia de datos de herramientas y proyectos.

5. **Orquestación y despliegue**

   * **Docker Compose** para laboratorios simples.
   * **K3s** (Kubernetes ligero) si quieres experimentar con clusters.

---

## Preparación del host Ubuntu 24.04

1. **Actualización y paquetes base**

   ```bash
   sudo apt update && sudo apt upgrade -y
   sudo apt install -y curl git ufw
   ```

2. **Instalar Docker Engine**

   ```bash
   # Dependencias
   sudo apt install -y ca-certificates gnupg lsb-release
   # Clave GPG y repositorio
   curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo tee /usr/share/keyrings/docker-archive-keyring.gpg
   echo \
     "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] \
     https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" \
     | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
   sudo apt update
   sudo apt install -y docker-ce docker-ce-cli containerd.io
   sudo usermod -aG docker $USER
   ```

3. **Instalar Docker Compose v2**

   ```bash
   sudo apt install -y docker-compose-plugin
   ```

4. **Configurar firewall básico**

   ```bash
   sudo ufw default deny incoming
   sudo ufw default allow outgoing
   # Permitir SSH (si remoto)
   sudo ufw allow ssh
   # Más reglas según tu topología
   sudo ufw enable
   ```

---

## Orquestación del laboratorio

### 3.1. Docker Compose

* Crea un directorio raíz, p. ej. `~/lab-cybersec/`.
* Dentro, un fichero `docker-compose.yml` que defina servicios de:

  * **DVWA** (vulnerable web app)
  * **WebGoat** (app educativa)
  * **OWASP ZAP**
  * **Metasploit Framework**
  * **ELK Stack** (Elasticsearch, Logstash, Kibana) o **Graylog**
  * **Registry privado**

Ejemplo muy simplificado:

```yaml
version: '3.8'
services:
  dvwa:
    image: vulnerables/web-dvwa
    ports: ["8081:80"]
    networks: [lab-net]

  webgoat:
    image: webgoat/webgoat-8.0
    ports: ["8080:8080"]
    networks: [lab-net]

  owasp-zap:
    image: owasp/zap2docker-weekly
    command: ["zap.sh", "-daemon", "-port", "8090"]
    ports: ["8090:8090"]
    networks: [lab-net]

  elk:
    image: sebp/elk
    ports: ["5601:5601","9200:9200","5044:5044"]
    networks: [lab-net]

networks:
  lab-net:
    driver: bridge
```

> **Tip:** usa **volúmenes nombrados** para persistir datos (DB de Metasploit, índices de Elasticsearch, reportes de ZAP…).

### Kubernetes ligero (k3s)

Si optas por un cluster más “real”:

1. Instala k3s en tu host:

   ```bash
   curl -sfL https://get.k3s.io | sh -
   ```
2. Usa **Helm** para desplegar chart de DVWA, WebGoat, ZAP, ELK, etc.
3. Define **Namespaces** por proyecto o tipo de herramienta.

---

## Herramientas open‑source recomendadas

| Categoría                   | Herramienta                           | Contenedor / Repo                                |
| --------------------------- | ------------------------------------- | ------------------------------------------------ |
| Web vulnerables             | DVWA, WebGoat, Juice Shop             | `vulnerables/web-dvwa`<br>`webgoat/webgoat-8.0`  |
| Escaneo de seguridad web    | OWASP ZAP, Nikto, Wapiti              | `owasp/zap2docker-weekly`                        |
| Pen‑testing                 | Metasploit Framework, Armitage        | `metasploitframework/metasploit`                 |
| Monitoreo de red            | Zeek, Suricata                        | `zeek/zeek`<br>`jasonish/suricata`               |
| SIEM / Log management       | ELK Stack, Graylog, Wazuh             | `sebp/elk`<br>`graylog/graylog`<br>`wazuh/wazuh` |
| CI/CD seguridad             | GitLab‑CE, Jenkins + OWASP ZAP plugin | `gitlab/gitlab-ce`<br>`jenkins/jenkins`          |
| Gestión de vulnerabilidades | OpenVAS / Greenbone                   | `greenbone/gvm`                                  |

---

## Flujo de trabajo 

1. **Desarrollo web**

   * Los desarrolladores levantan sus contenedores de apps (p. ej. Node.js, Python/Flask, PHP).
   * Se conectan a la red `lab-net`.

2. **Pruebas automáticas**

   * Al hacer push al repo GitLab, Jenkins ejecuta un pipeline que:

     1. Construye la imagen del proyecto.
     2. Despliega temporalmente en un namespace o stack Compose.
     3. Corre **OWASP ZAP** (scans pasivos y activos).
     4. Publica un reporte en Kibana / Graylog.

3. **Pentesting manual**

   * Accede a **Metasploit** o **Armitage** desde su contenedor.
   * Usa proxies (ZAP) y **Burp Suite Community** (instalado en host o contenedor) para interceptar tráfico.

4. **Monitorización y análisis**

   * Todo el tráfico de red entre contenedores pasa por un sensor Zeek/Suricata.
   * Logs consolidados en Elasticsearch/Wazuh.
   * Creación de dashboards de alertas y anomalías.

---

## Buenas prácticas y seguridad del lab

* **Aislamiento fuerte:** mantén el host separado de tu LAN de producción (usa VLAN o una VM-hypervisor).
* **Snapshots:** haz imágenes base de tu VM antes de cada gran cambio.
* **Actualizaciones periódicas:** configura un job de Ansible o cron para aplicar parches (principalmente en las herramientas).
* **Control de acceso:** usuarios de Docker/GitLab distintos de root; autenticación fuerte (LLaves SSH, 2FA).
* **Backups:** exporta volúmenes (`docker volume export`) y snapshots de bases de datos semanalmente.
* **Documentación:** versiona tu `docker-compose.yml`, manifests de k3s, pipelines CI/CD y playbooks Ansible en un repo dedicado.

__________________
> By CISO Oswaldo.Diaz

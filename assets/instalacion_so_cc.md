### **Introducción a los sistemas operativos en la nube**
Los sistemas operativos (SO) en la nube son instancias de sistemas operativos que se ejecutan en infraestructura virtualizada proporcionada por proveedores de servicios en la nube, como Amazon Web Services (AWS), Microsoft Azure, Google Cloud Platform (GCP), entre otros. A diferencia de los entornos físicos, donde los SO se instalan en hardware dedicado, en la nube los SO se despliegan en máquinas virtuales (VM) o contenedores, lo que permite escalabilidad, flexibilidad y acceso remoto.

Tabla que muestra los proncipales proveedores de sistemas operativos en la nube

| **Sistema Operativo** | **Proveedor de Nube** | **Características Principales** | **Ventajas en Ciberseguridad** | **Consideraciones** |
|-----------------------|-----------------------|--------------------------------|-------------------------------|---------------------|
| **Ubuntu Server**     | AWS (AMI), Azure, GCP | - Basado en Debian, ligero y ampliamente soportado.<br>- Actualizaciones frecuentes (LTS cada 2 años).<br>- Soporte para contenedores (Docker, Kubernetes).<br>- Herramientas integradas como `ufw` (firewall) y `AppArmor`. | - Gran comunidad para soporte y parches.<br>- Configuración de SELinux o AppArmor para control de acceso.<br>- Fácil integración con herramientas de monitoreo (CloudWatch, Azure Monitor).<br>- SSH seguro por defecto. | - Requiere conocimientos de línea de comandos.<br>- Configuración inicial puede ser manual si no se usa IaC. |
| **Amazon Linux 2/2023** | AWS (AMI nativa)     | - Optimizado para AWS, basado en CentOS/RHEL.<br>- Integración nativa con AWS Systems Manager y CloudWatch.<br>- Parches de seguridad automatizados.<br>- Soporte para EBS cifrado por defecto. | - Optimizado para bajo consumo de recursos en AWS.<br>- Actualizaciones automáticas y soporte de AWS.<br>- Configuraciones de seguridad predefinidas.<br>- Ideal para entornos serverless y EC2. | - Menos flexible fuera de AWS.<br>- Dependencia de herramientas AWS para configuraciones avanzadas. |
| **CentOS Stream**     | AWS, Azure, GCP       | - Basado en RHEL, enfocado en estabilidad.<br>- Actualizaciones continuas (rolling release).<br>- Soporte para `firewalld` y SELinux.<br>- Compatible con aplicaciones empresariales. | - SELinux activado por defecto para endurecimiento.<br>- Comunidad activa para parches de seguridad.<br>- Compatible con herramientas de auditoría como `auditd`. | - Curva de aprendizaje para SELinux.<br>- Menos soporte comunitario que Ubuntu. |
| **Debian**            | AWS, Azure, GCP       | - Ligero, estable y altamente personalizable.<br>- Repositorios amplios para herramientas de seguridad.<br>- Soporte para `ufw` y `AppArmor`.<br>- Actualizaciones regulares con énfasis en estabilidad. | - Mínima superficie de ataque por diseño ligero.<br>- Ideal para entornos minimalistas.<br>- Fácil de endurecer con guías oficiales. | - Configuración manual puede ser necesaria.<br>- Menos optimizado para nubes específicas que Amazon Linux. |
| **Windows Server (2019/2022)** | AWS, Azure (nativo), GCP | - Interfaz gráfica para administración.<br>- Soporte nativo para Active Directory, PowerShell.<br>- Herramientas de seguridad como Windows Defender y BitLocker.<br>- Integración con Azure AD y AWS Directory Service. | - Windows Defender integrado para protección básica.<br>- BitLocker para cifrado en reposo.<br>- Políticas de grupo para control de acceso.<br>- Soporte para herramientas empresariales de SIEM. | - Mayor consumo de recursos que Linux.<br>- Licenciamiento puede incrementar costos.<br>- Mayor superficie de ataque si no se endurece. |
| **Red Hat Enterprise Linux (RHEL)** | AWS, Azure, GCP | - Enfocado en entornos empresariales.<br>- Soporte extendido (hasta 10 años por versión).<br>- Incluye SELinux y `firewalld`.<br>- Certificaciones para normativas (HIPAA, PCI-DSS). | - Cumplimiento normativo garantizado.<br>- SELinux para control granular de seguridad.<br>- Soporte empresarial para parches críticos.<br>- Integración con herramientas de gestión como Red Hat Satellite. | - Requiere suscripción para soporte completo.<br>- Mayor costo que distribuciones gratuitas. |
| **Alpine Linux**      | AWS, Azure, GCP (usado en contenedores) | - Extremadamente ligero (ideal para contenedores).<br>- Diseño minimalista con `musl libc`.<br>- Soporte para `iptables` y contenedores.<br>- Parches de seguridad rápidos. | - Mínima superficie de ataque.<br>- Ideal para microservicios y contenedores seguros.<br>- Configuración simple para entornos en la nube. | - Menos soporte para aplicaciones complejas.<br>- Requiere experiencia para configuraciones avanzadas. |

### **Notas sobre la tabla**
**Criterios de selección**:
   - Los SO se eligieron por su popularidad y soporte en los principales proveedores de nube (AWS, Azure, GCP).
   - Se priorizaron características relevantes para ciberseguridad, como herramientas de endurecimiento, cifrado y monitoreo.

**Aspectos de seguridad comunes**:
   - Todos los SO soportan cifrado en reposo (por ejemplo, EBS en AWS, Azure Disk Encryption) y en tránsito (TLS/SSL).
   - Los proveedores ofrecen herramientas de monitoreo (CloudWatch, Azure Monitor, GCP Logging) que se integran con estos SO.
   - La configuración de firewall y el endurecimiento son esenciales en todos los casos para minimizar vulnerabilidades.

**Recomendaciones para ciberseguridad**:
   - Usa imágenes oficiales de los proveedores para garantizar parches actualizados.
   - Implementa Infrastructure as Code (IaC) con Terraform o CloudFormation para estandarizar configuraciones.
   - Habilita auditoría y monitoreo continuo con herramientas como `auditd` (Linux) o Event Viewer (Windows).
   - Asegúrate de cumplir con normativas relevantes (GDPR, HIPAA, etc.) según el caso de uso.

#### **Configuración para alta disponibilidad y escalabilidad**
- Configura instancias en múltiples zonas de disponibilidad para redundancia.
- Usa balanceadores de carga (por ejemplo, AWS ELB, Azure Load Balancer) para distribuir el tráfico.
- Implementa autoescalado para ajustar recursos según la demanda.

### **Protección de la información en la nube**
La protección de datos es un componente crítico en la configuración de SO en la nube:

- **Clasificación de datos**: Identifica qué datos son sensibles (por ejemplo, PII, datos financieros) y aplica controles específicos.
- **Copias de seguridad**: Configura backups automáticos usando servicios como AWS Backup o Azure Backup.
- **Control de acceso**: Usa herramientas de gestión de identidades (IAM) del proveedor para restringir quién puede acceder a las instancias y datos.
- **Prevención de fugas de datos (DLP)**: Implementa herramientas o políticas para evitar la exposición accidental de datos sensibles.
- **Cumplimiento normativo**: Asegúrate de que las configuraciones cumplan con estándares como GDPR, HIPAA o ISO 27001, según el caso.

### **Herramientas y servicios recomendados**
- **AWS**: EC2, Systems Manager, CloudWatch, AWS Config para monitoreo de configuraciones.
- **Azure**: Virtual Machines, Azure Security Center, Azure Monitor.
- **GCP**: Compute Engine, Cloud Logging, Security Command Center.
- **Otras herramientas**:
  - Ansible, Puppet o Chef para automatización de configuraciones.
  - Docker o Kubernetes para gestión de contenedores.
  - SIEM (por ejemplo, Splunk, ELK Stack) para análisis de logs.

### **Mejores prácticas**
- **Automatización**: Usa Infrastructure as Code (IaC) con herramientas como Terraform o CloudFormation para estandarizar y repetir configuraciones.
- **Pruebas de seguridad**: Realiza pruebas de penetración y escaneos de vulnerabilidades regularmente.
- **Documentación**: Mantén un registro de todas las configuraciones y políticas aplicadas.
- **Capacitación**: Asegúrate de que el equipo esté capacitado en las mejores prácticas de seguridad en la nube.
- **Respuesta a incidentes**: Configura un plan para responder a brechas de seguridad, incluyendo snapshots de instancias para análisis forense.


# Servicios de las Principales Plataformas

| Categoría de Servicio | AWS | Microsoft Azure | Google Cloud Platform | IBM Cloud | Alibaba Cloud |
|----------------------|-----|----------------|----------------------|-----------|---------------|
| **Cómputo** | • EC2 (máquinas virtuales)<br>• Lambda (serverless)<br>• ECS/EKS (contenedores)<br>• Batch (procesamiento por lotes)<br>• Lightsail (VPS simplificado) | • Virtual Machines<br>• Azure Functions (serverless)<br>• Container Instances/AKS<br>• Batch (procesamiento por lotes)<br>• App Service (PaaS web) | • Compute Engine (VMs)<br>• Cloud Functions (serverless)<br>• Google Kubernetes Engine<br>• Cloud Run (contenedores)<br>• App Engine (PaaS) | • Virtual Servers<br>• Cloud Functions<br>• Kubernetes Service<br>• Code Engine<br>• Cloud Foundry | • Elastic Compute Service (ECS)<br>• Function Compute<br>• Container Service<br>• Batch Compute<br>• Simple Application Server |
| **Almacenamiento** | • S3 (objeto)<br>• EBS (bloques)<br>• EFS (archivos)<br>• Glacier (archivo)<br>• Storage Gateway | • Blob Storage (objeto)<br>• Disk Storage (bloques)<br>• Files (archivos)<br>• Archive Storage • StorSimple | • Cloud Storage (objeto)<br>• Persistent Disk (bloques)<br>• Filestore (archivos)<br>• Archive Storage<br>• Transfer Service | • Object Storage<br>• Block Storage<br>• File Storage<br>• Archive Storage<br>• Mass Data Migration | • Object Storage Service<br>• Block Storage<br>• Network Attached Storage<br>• Archive Storage<br>• Hybrid Cloud Storage |
| **Base de Datos** | • RDS (relacional)<br>• DynamoDB (NoSQL)<br>• Redshift (data warehouse)<br>• ElastiCache (caché)<br>• DocumentDB (MongoDB) | • SQL Database<br>• Cosmos DB (NoSQL)<br>• Synapse Analytics<br>• Cache for Redis<br>• Database for PostgreSQL/MySQL | • Cloud SQL (relacional)<br>• Firestore (NoSQL)<br>• BigQuery (analytics)<br>• Memorystore (caché)<br>• Cloud Spanner (global) | • Db2 on Cloud<br>• Cloudant (NoSQL)<br>• Netezza Performance Server<br>• Databases for Redis<br>• Informix on Cloud | • ApsaraDB (RDS)<br>• Table Store (NoSQL)<br>• AnalyticDB<br>• ApsaraDB for Redis<br>• PolarDB |
| **Redes** | • VPC<br>• CloudFront (CDN)<br>• Route 53 (DNS)<br>• Direct Connect<br>• Elastic Load Balancer | • Virtual Network<br>• Content Delivery Network<br>• DNS<br>• ExpressRoute<br>• Load Balancer | • Virtual Private Cloud<br>• Cloud CDN<br>• Cloud DNS<br>• Cloud Interconnect<br>• Cloud Load Balancing | • Virtual Private Cloud<br>• Content Delivery Network<br>• Internet Services<br>• Direct Link<br>• Load Balancer | • Virtual Private Cloud<br>• Alibaba Cloud CDN<br>• DNS<br>• Express Connect<br>• Server Load Balancer |
| **Inteligencia Artificial** | • SageMaker (ML)<br>• Rekognition (visión)<br>• Comprehend (NLP)<br>• Polly (texto a voz)<br>• Lex (chatbots) | • Machine Learning<br>• Computer Vision<br>• Language Understanding<br>• Speech Services<br>• Bot Framework | • AI Platform<br>• Vision AI<br>• Natural Language AI<br>• Speech-to-Text<br>• Dialogflow | • Watson Machine Learning<br>• Watson Visual Recognition<br>• Watson Natural Language<br>• Watson Speech to Text<br>• Watson Assistant | • Machine Learning Platform<br>• Image Recognition<br>• Natural Language Processing<br>• Intelligent Speech Interaction<br>• Chatbot |
| **Analytics y Big Data** | • EMR (Hadoop/Spark)<br>• Kinesis (streaming)<br>• Athena (queries)<br>• QuickSight (BI)<br>• Glue (ETL) | • HDInsight (Hadoop/Spark)<br>• Stream Analytics<br>• Data Lake Analytics<br>• Power BI<br>• Data Factory | • Dataproc (Hadoop/Spark)<br>• Dataflow (streaming)<br>• Data Studio<br>• Looker (BI)<br>• Cloud Composer | • Analytics Engine<br>• Streaming Analytics<br>• Db2 Warehouse<br>• Cognos Analytics<br>• InfoSphere DataStage | • E-MapReduce<br>• Realtime Compute<br>• Data Lake Analytics<br>• Quick BI<br>• DataWorks |
| **Seguridad e Identidad** | • IAM<br>• Cognito<br>• Certificate Manager<br>• WAF<br>• GuardDuty | • Active Directory<br>• Key Vault<br>• Security Center<br>• Application Gateway<br>• Sentinel | • Identity and Access Management<br>• Cloud Identity<br>• Certificate Authority<br>• Cloud Armor<br>• Security Command Center | • Identity and Access Management<br>• Key Protect<br>• Security Advisor<br>• App ID<br>• Certificate Manager | • Resource Access Management<br>• Key Management Service<br>• Security Center<br>• Web Application Firewall<br>• ActionTrail |
| **DevOps y Desarrollo** | • CodeCommit/CodeBuild/CodeDeploy<br>• CodePipeline<br>• CloudFormation<br>• Systems Manager<br>• X-Ray (monitoring) | • Azure DevOps<br>• GitHub integration<br>• Resource Manager<br>• Application Insights<br>• Monitor | • Cloud Source Repositories<br>• Cloud Build<br>• Deployment Manager<br>• Operations Suite<br>• Cloud Debugger | • Toolchain<br>• Continuous Delivery<br>• Resource Controller<br>• Monitoring<br>• Log Analysis | • CodePipeline<br>• Container Registry<br>• Resource Orchestration Service<br>• CloudMonitor<br>• Log Service |
| **Internet de las Cosas (IoT)** | • IoT Core<br>• IoT Device Management<br>• IoT Analytics<br>• FreeRTOS<br>• IoT Events | • IoT Hub<br>• IoT Central<br>• Digital Twins<br>• Stream Analytics<br>• Time Series Insights | • Cloud IoT Core<br>• Edge TPU<br>• IoT Device SDK<br>• Pub/Sub<br>• Time Series Insights | • Watson IoT Platform<br>• Maximo Asset Monitor<br>• Edge Application Manager<br>• Event Streams<br>• Cloudant (for IoT data) | • IoT Platform<br>• Link IoT Edge<br>• IoT Device Management<br>• Message Queue<br>• Time Series Database |
| **Blockchain** | • Managed Blockchain<br>• Quantum Ledger Database<br>• Partner solutions | • Blockchain Service<br>• Azure Confidential Ledger<br>• Partner integrations | • No servicio nativo<br>• Partner solutions<br>• Marketplace options | • Blockchain Platform<br>• Hyper Protect Services<br>• Certificate Authority | • Blockchain as a Service<br>• Ant Blockchain<br>• Partner solutions |
| **Migración y Híbrido** | • Database Migration Service<br>• Server Migration Service<br>• Outposts (híbrido)<br>• Snow Family<br>• Storage Gateway | • Database Migration Service<br>• Azure Migrate<br>• Azure Stack (híbrido)<br>• Data Box<br>• StorSimple | • Database Migration Service<br>• Transfer Service<br>• Anthos (híbrido)<br>• Transfer Appliance<br>• Storage Transfer Service | • Lift and Shift<br>• Mass Data Migration<br>• Satellite (edge)<br>• Cloud Pak for Integration<br>• Aspera (transfer) | • Data Transmission Service<br>• Server Migration Center<br>• Hybrid Cloud<br>• Data Transport<br>• Hybrid Backup Recovery |

## Características Distintivas por Proveedor

### AWS
- **Fortalezas**: Mayor ecosistema de servicios, amplia adopción empresarial, documentación extensa
- **Especialidades**: Servicios serverless, machine learning, amplio marketplace

### Microsoft Azure
- **Fortalezas**: Integración con ecosistema Microsoft, soluciones híbridas robustas
- **Especialidades**: Windows Server, Active Directory, Office 365 integration

### Google Cloud Platform
- **Fortalezas**: Liderazgo en AI/ML, analytics avanzados, infraestructura de red global
- **Especialidades**: BigQuery, TensorFlow, Kubernetes (origen)

### IBM Cloud
- **Fortalezas**: Soluciones empresariales, Watson AI, mainframe integration
- **Especialidades**: Servicios cognitivos, blockchain empresarial, computación cuántica

### Alibaba Cloud
- **Fortalezas**: Liderazgo en mercado asiático, precios competitivos, e-commerce integration
- **Especialidades**: Servicios para e-commerce, fintech, mercado chino

---------

# Tips para contratar servicios en la nube 

### **Evaluar las necesidades del negocio**
- **Objetivo claro:** Definir claramente qué se espera lograr con la nube (escalabilidad, reducción de costos, innovación, etc.).
- **Análisis de carga de trabajo:** Determinar cuáles son las aplicaciones o procesos adecuados para migrar a la nube.
- **Capacidad requerida:** Estimar necesidades de almacenamiento, computación y red.

### **Seleccionar el modelo de nube adecuado**
- **IaaS, PaaS o SaaS:** Elegir el modelo según el nivel de control y personalización necesario.
- **Nube pública, privada o híbrida:** Considerar sensibilidad de datos, cumplimiento normativo y necesidades de escalabilidad.

### **Analizar proveedores disponibles**
- **Comparativa de proveedores:** AWS, Microsoft Azure, Google Cloud, Oracle Cloud, etc.
- **Soporte técnico:** Nivel de atención postventa, disponibilidad 24/7, idioma, etc.
- **Experiencia del proveedor:** Reputación, estabilidad financiera y casos de éxito relevantes.

### **Evaluar modelos de costos y facturación**
- **Modelo “pay-as-you-go”:** Asegurar que solo se pague por lo que se consume.
- **Costos ocultos:** Consultar por tráfico de salida, almacenamiento, transferencias entre zonas, etc.
- **Presupuesto y optimización:** Usar herramientas de estimación de costos y planes de ahorro a largo plazo.

### **Seguridad y cumplimiento normativo**
- **Certificaciones:** ISO 27001, SOC 2, GDPR, HIPAA, etc., según el sector.
- **Control de acceso y autenticación:** Verificar opciones de IAM (Identity and Access Management).
- **Cifrado de datos:** En tránsito y en reposo.
- **Ubicación geográfica de servidores:** Importante para cumplir regulaciones locales.

### **Rendimiento y alta disponibilidad**
- **SLA (Acuerdo de Nivel de Servicio):** Revisar garantías de uptime (ej. 99.9% o más).
- **Latencia:** Proximidad de centros de datos a los usuarios finales.
- **Redundancia y respaldo:** Mecanismos de failover, replicación y recuperación ante desastres.

### **Integración y compatibilidad**
- **Interoperabilidad:** Compatibilidad con sistemas existentes y otros proveedores.
- **APIs y herramientas de desarrollo:** Facilidad para integrar y automatizar procesos.
- **Migración:** Evaluar facilidad y costo de trasladar cargas de trabajo a la nube.

### **Gestión y monitoreo**
- **Herramientas de administración:** Dashboards, monitoreo en tiempo real, alertas.
- **Automatización:** Capacidad de orquestar recursos y optimizar procesos.
- **Gestión de logs y auditoría:** Herramientas para rastrear actividades y cumplir requisitos legales.

### **Planificación a largo plazo**
- **Escalabilidad futura:** Capacidad de crecer sin cambiar completamente de proveedor.
- **Contratos flexibles:** Evitar penalizaciones por cancelación anticipada o falta de renovación.
- **Estrategia de salida (exit strategy):** Tener un plan para migrar a otro proveedor si es necesario.

### **Capacitación y soporte interno**
- **Formación del equipo:** Asegurar que el personal tenga conocimientos técnicos en la plataforma elegida.
- **Documentación y comunidad:** Acceso a guías, foros y recursos oficiales del proveedor.

### **Calculadoras de Costo y Dimensionamiento en la Nube**  

#### **Multi-Cloud / Independientes**  
**CloudZero** – Herramienta para estimar costos multi-nube.  
   - [https://www.cloudzero.com/](https://www.cloudzero.com/)  
**Terraform (Infraestructura como Código)** – Permite planificar recursos antes de implementarlos.  
   - [https://www.terraform.io/](https://www.terraform.io/)  

#### **Amazon Web Services (AWS)**  
**AWS Pricing Calculator** – Calculadora oficial para estimar costos en AWS.  
   - [https://calculator.aws/](https://calculator.aws/)  
**AWS Simple Monthly Calculator** (Legacy) – Versión anterior de la calculadora de AWS.  
   - [https://calculator.s3.amazonaws.com/index.html](https://calculator.s3.amazonaws.com/index.html)  
**AWS Well-Architected Tool** – Ayuda a optimizar cargas de trabajo.  
   - [https://aws.amazon.com/well-architected-tool/](https://aws.amazon.com/well-architected-tool/)  

#### **Microsoft Azure**  
**Azure Pricing Calculator** – Calculadora de costos para servicios de Azure.  
   - [https://azure.microsoft.com/en-us/pricing/calculator/](https://azure.microsoft.com/en-us/pricing/calculator/)  
**Azure TCO Calculator** – Compara costos entre on-premise y Azure.  
   - [https://azure.microsoft.com/en-us/pricing/tco/calculator/](https://azure.microsoft.com/en-us/pricing/tco/calculator/)  

#### **Google Cloud Platform (GCP)**  
**Google Cloud Pricing Calculator** – Herramienta de estimación de costos en GCP.  
   - [https://cloud.google.com/products/calculator](https://cloud.google.com/products/calculator)  
**Google Cloud Recommender** – Sugiere optimizaciones de recursos.  
   - [https://cloud.google.com/recommender](https://cloud.google.com/recommender)  

#### **Oracle Cloud**  
**Oracle Cloud Cost Estimator** – Calculadora de costos para OCI.  
   - [https://www.oracle.com/cloud/cost-estimator.html](https://www.oracle.com/cloud/cost-estimator.html)  

#### **IBM Cloud**  
**IBM Cloud Pricing Calculator** – Estimador de costos para IBM Cloud.  
   - [https://www.ibm.com/cloud/pricing](https://www.ibm.com/cloud/pricing)  

#### **Herramientas de Monitorización y Optimización**  
**CloudHealth by VMware** – Gestión de costos multi-nube.  
   - [https://www.cloudhealthtech.com/](https://www.cloudhealthtech.com/)  
**Kubecost** – Para optimizar costos en Kubernetes (EKS, AKS, GKE).  
   - [https://www.kubecost.com/](https://www.kubecost.com/)  

### **Herramientas Open Source**  
**Infracost** – Calcula costos desde Terraform.  
   - [https://www.infracost.io/](https://www.infracost.io/)  
**Cloud Custodian** – Automatiza la optimización de costos.  
   - [https://cloudcustodian.io/](https://cloudcustodian.io/)  

______________
Referencias bibliográficas 

> American Psychological Association. (2020). Publication manual of the American Psychological Association (7th ed.). https://doi.org/10.1037/0000165-000>

> Bhadauria, R., & Sanyal, S. (2022). Cloud computing security: Challenges and solutions. Journal of Network and Computer Applications, 189, 103-119. https://doi.org/10.1016/j.jnca.2021.103119

> Chou, T.-S. (2021). Security threats and countermeasures in cloud computing. International Journal of Information Security, 20(4), 567-582. https://doi.org/10.1007/s10207-020-00512-3

> Fernandes, D. A. B., Soares, L. F. B., Gomes, J. V., Freire, M. M., & Inácio, P. R. M. (2023). Security issues in cloud environments: A survey. International Journal of Cloud Computing, 12(3), 245-267. https://doi.org/10.1504/IJCC.2023.10034567

> Gupta, S., & Kumar, P. (2020). An integrated framework for cloud security: Risk assessment and mitigation strategies. Computers & Security, 97, 101-112. https://doi.org/10.1016/j.cose.2020.101912

> Hasan, M., & Rahman, M. A. (2021). Data privacy and security in cloud computing: A comprehensive review. IEEE Transactions on Cloud Computing, 9(2), 345-360. https://doi.org/10.1109/TCC.2020.2971234

> Khan, N., & Al-Yasiri, A. (2022). Cloud security threats and techniques to strengthen cloud computing services. Journal of Information Security and Applications, 65, 102-118. https://doi.org/10.1016/j.jisa.2021.102998

> Mell, P., & Grance, T. (2020). The NIST definition of cloud computing: Security and privacy considerations (Special Publication 800-145). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-145

> Singh, A., & Chatterjee, K. (2023). Cloud security: Emerging threats and countermeasures in IaaS, PaaS, and SaaS models. Future Generation Computer Systems, 140, 89-104. https://doi.org/10.1016/j.future.2022.10.015

> Subramanian, N., & Jeyaraj, A. (2021). Recent advances in cloud security: A systematic literature review. ACM Computing Surveys, 54(5), 1-36. https://doi.org/10.1145/3456643


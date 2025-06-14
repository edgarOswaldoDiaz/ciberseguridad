# Proceso para Instalar el Sistema Operativo Microsoft Windows Server
### **Instalación Detallada de Windows Server 2019 en un Servidor Físico**  

*Requisitos Previos:*  
1. **Hardware:**  
   - CPU: Procesador de 64 bits a 1.4 GHz o superior (mínimo 2 núcleos).  
   - RAM: Mínimo 512 MB (recomendado 2 GB para *Essentials*, 16 GB para *Datacenter*).  
   - Almacenamiento: 32 GB de espacio libre (SSD recomendado).  
   - Tarjeta de red: Adaptador Ethernet compatible (1 Gbps o superior).  

2. **Software:**  
   - Imagen ISO de Windows Server 2019 ([Descarga desde Microsoft Evaluation Center](https://www.microsoft.com/en-us/evalcenter/evaluate-windows-server-2019)).  
   - Herramienta para crear USB booteable: Rufus o Media Creation Tool.  
   - Clave de producto (si no es evaluación).  

3. **Preparación:**  
   - Backup de datos existentes en el servidor.  
   - Verificar compatibilidad de hardware con el fabricante (drivers RAID, NIC, etc.).  

---

### **Proceso Paso a Paso:**  
#### **1. Preparar Medio de Instalación (USB Booteable)**  
   a. Descargar la ISO de Windows Server 2019.  
   b. Insertar USB vacío (≥8 GB).  
   c. Usar **Rufus** (Configuración recomendada):  
      - *Esquema de partición:* GPT (para UEFI) o MBR (para BIOS heredado).  
      - *Sistema de archivos:* NTFS.  
      - Ejecutar Rufus > Seleccionar ISO > Iniciar.  

#### **2. Configurar BIOS/UEFI del Servidor**  
   a. Reiniciar servidor y acceder a BIOS/UEFI (tecla: F2, F10, DEL, ESC según fabricante).  
   b. Verificar ajustes:  
      - *Boot Order:* Priorizar USB.  
      - *Modo de arranque:* UEFI o Legacy (coherente con el USB).  
      - *Virtualization Technology (VT-x):* Habilitado (si se usará Hyper-V).  
      - *Secure Boot:* Deshabilitado (si instalas en Legacy).  
   c. Guardar cambios y reiniciar.  

#### **3. Iniciar Instalación**  
   a. Al arrancar desde USB, aparecerá el logo de Windows.  
   b. **Configuración inicial:**  
      - *Idioma, formato de hora y moneda, teclado:* Seleccionar opciones.  
      - Clic en **Siguiente** > **Instalar ahora**.  
   c. **Introducir clave de producto:**  
      - Ingresar clave o seleccionar *"No tengo clave"* (versión de evaluación).  
   d. **Seleccionar edición:**  
      - Elegir entre *Standard* o *Datacenter* (ambas en **Experiencia de escritorio** o **Core**).  
      - *Recomendado:* "Experiencia de escritorio" (interfaz gráfica).  

#### **4. Particionamiento del Disco**  
   a. **Tipo de instalación:** *"Personalizada: instalar solo Windows"*.  
   b. **Administración de discos:**  
      - Si el disco tiene particiones, eliminarlas todas (reserva espacio para sistema).  
      - Seleccionar *"Unallocated Space"* > **Nuevo**.  
      - *Tamaño de partición:* Asignar espacio (mínimo 32 GB).  
      - **Formatear en NTFS** (Windows creará particiones reservadas automáticamente).  
   c. Seleccionar la partición principal > **Siguiente**.  

#### **5. Instalación y Primer Reinicio**  
   a. El sistema copiará archivos, instalará características y actualizará.  
   b. **Reinicio automático:** Extraer USB tras el primer reinicio (evitar ciclo de arranque).  

#### **6. Configuración Inicial Post-Instalación**  
   a. **Establecer contraseña de Administrador:**  
      - Crear una contraseña compleja (mínimo 8 caracteres, mayúsculas, números).  
   b. **Acceder al Escritorio:** Iniciar sesión con *Administrador*.  

---

### **Configuración Básica Post-Instalación**  
#### **1. Configurar Red**  
   a. Ir a **Administrador del Servidor > Servidor Local**.  
   b. Hacer clic en *"Ethernet"* (nombre de interfaz) > Propiedades > Configurar dirección IP:  
      - Asignar IP estática, máscara, gateway y DNS.  

#### **2. Unir Dominio o Grupo de Trabajo**  
   a. **Administrador del Servidor > Servidor Local > Grupo de trabajo:**  
      - Clic en *"Cambiar"* > Unir a dominio (ej: `miempresa.local`) o dejar grupo de trabajo.  
   b. Ingresar credenciales de dominio si es necesario.  

#### **3. Actualizaciones de Seguridad**  
   a. Abrir **Windows Update** (en Herramientas Administrativas).  
   b. Buscar actualizaciones > Instalar todas las críticas.  

#### **4. Instalar Drivers Faltantes**  
   a. Verificar **Administrador de dispositivos** (controladores con alerta amarilla).  
   b. Usar drivers del fabricante del servidor (HP, Dell, Lenovo) desde USB/CD.  

#### **5. Activar Windows**  
   a. **Servidor Local > Propiedades del sistema:**  
      - Clic en *"Activar Windows"* e ingresar clave.  

---

### **Configuración Opcional Avanzada**  
- **Agregar Roles:** DNS, AD Domain Services, DHCP (vía *Administrador del Servidor > Administrar > Agregar roles*).  
- **Habilitar Escritorio Remoto:**  
  - *Servidor Local > Configuración de acceso remoto:* Permitir conexiones remotas.  
- **Firewall de Windows:** Configurar reglas de entrada/salida según necesidades.  

---

### **Solución de Problemas Comunes**  
- **Error "No se encontraron unidades":**  
  - Requiere drivers de almacenamiento (RAID/SATA). Descargar del fabricante, copiar a USB e instalar durante particionamiento (botón **"Cargar controlador"**).  
- **Arranque en bucle:**  
  - Verificar modo UEFI/Legacy en BIOS y coherencia con USB.  
- **Problemas de red:**  
  - Instalar drivers de NIC manualmente.  

### **Notas Finales**  
- **Licenciamiento:** La versión de evaluación dura 180 días (convertible a licencia completa con clave).  
- **Recomendación:** Usar modo **Core** para servidores de producción (menor superficie de ataque).  

## Referencias Adicionales
- [Documentación Oficial de Microsoft para Windows Server](https://docs.microsoft.com/en-us/windows-server/)
- [Guías de Seguridad para Windows Server](https://docs.microsoft.com/en-us/windows-server/security/security-and-assurance)
- [Video](https://www.youtube.com/watch?v=0OI8i9K0ZbE)

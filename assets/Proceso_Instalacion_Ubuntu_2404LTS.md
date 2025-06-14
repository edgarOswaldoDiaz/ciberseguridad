# Proceso para Instalar el Sistema Operativo Ubuntu 24.04 LTS

*Requisitos Previos:*  
1. **Hardware:**  
   - CPU: Procesador x86-64 de 2 GHz o superior (mínimo 2 núcleos).  
   - RAM: Mínimo 1 GB (recomendado 4 GB para producción).  
   - Almacenamiento: 25 GB de espacio libre (SSD recomendado para rendimiento).  
   - Tarjeta de red: Adaptador Ethernet compatible.  

2. **Software:**  
   - Imagen ISO de Ubuntu Server 24.04 LTS ([Descarga oficial](https://ubuntu.com/download/server)).  
   - Herramienta para crear USB booteable: **Rufus** (Windows), **BalenaEtcher** (multi-plataforma), o `dd` (Linux/macOS).  

3. **Preparación:**  
   - Backup de datos existentes.  
   - Verificar compatibilidad de hardware (especialmente controladores RAID/NIC).  
   - Tener acceso a Internet (para actualizaciones durante la instalación).  

---

### **Proceso Paso a Paso:**  
#### **1. Preparar USB Booteable**  
   a. Descargar ISO de Ubuntu Server 24.04 LTS.  
   b. Insertar USB (≥8 GB) y usar:  
      - **Rufus** (Windows):  
        - *Esquema de partición:* GPT (UEFI).  
        - *Sistema de archivos:* FAT32.  
        - Seleccionar ISO > Iniciar.  
      - **Terminal (Linux/macOS):**  
        ```bash
        sudo dd if=/ruta/ubuntu-24.04-live-server-amd64.iso of=/dev/sdX bs=4M status=progress oflag=sync
        ```  
        *(Reemplazar `/dev/sdX` con la unidad USB, e.g., `/dev/sdb`)*.  

#### **2. Configurar BIOS/UEFI del Servidor**  
   a. Reiniciar servidor y acceder a BIOS/UEFI (F2, F10, DEL, ESC).  
   b. Ajustes críticos:  
      - *Boot Order:* Priorizar USB.  
      - *Modo de arranque:* **UEFI** (recomendado).  
      - *Secure Boot:* **Deshabilitado** (compatible, pero puede causar conflictos).  
      - *Virtualization (VT-x/AMD-V):* Habilitado si se usará KVM.  
   c. Guardar cambios y reiniciar.  

#### **3. Iniciar Instalador**  
   a. Al arrancar desde USB, seleccionar idioma (ej: **Español**).  
   b. **Teclado:**  
      - Diseño: `Español` o `Latinoamericano`.  
      - Verificar distribución con prueba interactiva.  

#### **4. Configuración de Red**  
   a. El instalador detectará interfaces de red.  
   b. **Asignar IP:**  
      - *DHCP (predeterminado):* Para redes con servidor DHCP.  
      - *IP Estática:*  
        ```  
        IPv4: Manual  
        Dirección: 192.168.1.100/24  
        Gateway: 192.168.1.1  
        DNS: 8.8.8.8, 8.8.4.4  
        ```  
   c. **Nombre del servidor:** Ej: `servidor-01`.  

#### **5. Usuario y Contraseña**  
   a. **Crear usuario:**  
      - Nombre completo: `Administrador del Sistema`  
      - Nombre de usuario: `admin` (evitar `root`).  
   b. **Contraseña:**  
      - Mínimo 8 caracteres, combinación de mayúsculas, números y símbolos.  
   c. **Importar claves SSH (opcional):**  
      - Pegar clave pública SSH para acceso remoto seguro.  

#### **6. Particionamiento de Discos**  
   a. **Método recomendado:**  
      - *Guided - use entire disk:* Para instalación simple.  
      - *Guided - use entire disk with LVM:* Para flexibilidad en gestión de volúmenes.  
      - *Custom:* Para configuración avanzada.  
   b. **Ejemplo LVM (recomendado para servidores):**  
      - Seleccionar disco (ej: `/dev/sda`).  
      - Configurar:  
        ```  
        Tamaño de volumen: 100% del espacio libre  
        Volumen LVM: /dev/vgubuntu/root  
        Puntos de montaje:  
          /     → ext4 (20 GB mínimo)  
          /var  → ext4 (10 GB)  
          /home → ext4 (5 GB)  
          swap  → Tamaño igual a RAM  
        ```  
   c. Confirmar cambios (`Write changes to disk`).  

#### **7. Perfil de Instalación**  
   a. **Seleccionar servicios:**  
      - [x] OpenSSH server (imprescindible para administración remota).  
      - [ ] Docker (si se usará contenedores).  
      - [ ] LAMP stack (para servidor web).  
      - [ ] Print server (opcional).  
   b. **Actualizaciones automáticas:**  
      - *Security updates:* Recomendado para servidores.  

#### **8. Instalación del Sistema**  
   a. Confirmar configuración y comenzar instalación.  
   b. **Proceso automático:**  
      - Descarga de paquetes (requiere Internet).  
      - Instalación de GRUB (gestor de arranque).  
   c. **Reinicio:**  
      - Extraer USB al finalizar.  
      - Iniciar sesión con el usuario creado.  

---

### **Configuración Post-Instalación**  
#### **1. Actualizar Sistema**  
```bash  
sudo apt update && sudo apt full-upgrade -y  
```  

#### **2. Configurar IP Estática (si no se hizo durante instalación)**  
   a. Editar configuración Netplan:  
      ```bash  
      sudo nano /etc/netplan/00-installer-config.yaml  
      ```  
   b. Ejemplo:  
      ```yaml  
      network:
        version: 2
        ethernets:
          enp0s3:
            dhcp4: no
            addresses: [192.168.1.100/24]
            routes:
              - to: default
                via: 192.168.1.1
            nameservers:
              addresses: [8.8.8.8, 1.1.1.1]
      ```  
   c. Aplicar:  
      ```bash  
      sudo netplan apply  
      ```  

#### **3. Habilitar Acceso Root (opcional)**  
```bash  
sudo passwd root  # Establecer contraseña  
sudo nano /etc/ssh/sshd_config  # Permitir root: PermitRootLogin yes  
sudo systemctl restart sshd  
```  

#### **4. Firewall (UFW)**  
```bash  
sudo ufw allow OpenSSH  
sudo ufw allow 80/tcp  # HTTP  
sudo ufw allow 443/tcp # HTTPS  
sudo ufw enable  
```  

#### **5. Instalar Herramientas Esenciales**  
```bash  
sudo apt install -y htop tmux ncdu tree git  
```  

---

### **Configuración Avanzada**  
- **RAID Software:**  
  - Usar `mdadm` durante particionamiento (opción *Custom*).  
- **NFS/Samba:**  
  ```bash  
  sudo apt install nfs-kernel-server samba -y  
  ```  
- **Monitoreo:**  
  - Instalar Nagios o Prometheus + Grafana.  

---

### **Solución de Problemas Comunes**  
- **Error "No se detecta disco":**  
  - Requiere drivers de almacenamiento (ej: RAID). Descargar `.deb` del fabricante y copiar a USB.  
  - Durante particionamiento, usar `Ctrl+Alt+F2` para abrir consola y montar USB.  
- **Problemas de arranque (GRUB):**  
  ```bash  
  sudo grub-install /dev/sda  
  sudo update-grub  
  ```  
- **Conexión SSH rechazada:**  
  - Verificar estado del servicio: `sudo systemctl status sshd`.  

---

### **Notas Clave**  
- **Soporte LTS:** Ubuntu 24.04 tiene soporte hasta **Abril 2034**.  
- **Seguridad:**  
  - Usar siempre claves SSH en lugar de contraseñas.  
  - Configurar fail2ban: `sudo apt install fail2ban`.  
- **Rendimiento:**  
  - Para servidores, usar sistema de archivos **XFS** o **ext4** (evitar ZFS sin RAM suficiente).  

¡Ubuntu Server 24.04 LTS está listo para implementar servicios críticos!

Referencia video explica la instalación https://www.youtube.com/watch?v=D1cWCqKsN00 

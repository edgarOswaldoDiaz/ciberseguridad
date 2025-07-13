# Cheat Sheet** Docker & Docker Compose 

---

## 🔹 Docker CLI

### Gestión de imágenes

* **Listar imágenes**

  ```bash
  docker images
  ```
* **Descargar (pull)**

  ```bash
  docker pull <imagen>:<tag>
  ```
* **Construir (build)**

  ```bash
  docker build -t <nombre>:<tag> <ruta/Dockerfile>
  ```
* **Eliminar imagen**

  ```bash
  docker rmi <imagenID|nombre:tag>
  ```

### Gestión de contenedores

* **Listar contenedores**

  ```bash
  docker ps          # en ejecución
  docker ps -a       # todos
  ```
* **Ejecutar un contenedor**

  ```bash
  docker run -d \
    --name <nombre> \
    -p <host>:<contenedor> \
    -e VAR=valor \
    <imagen>:<tag>
  ```
* **Acceder/interactivo**

  ```bash
  docker run -it <imagen>:<tag> /bin/bash
  ```
* **Detener**

  ```bash
  docker stop <contenedorID|nombre>
  ```
* **Reiniciar**

  ```bash
  docker restart <contenedor>
  ```
* **Eliminar**

  ```bash
  docker rm <contenedor>
  ```

### Inspección y control

* **Ver logs**

  ```bash
  docker logs <contenedor>        # salida completa
  docker logs -f <contenedor>     # “follow”
  ```
* **Ejecutar comando en un contenedor activo**

  ```bash
  docker exec -it <contenedor> <comando>
  ```
* **Inspeccionar detalles**

  ```bash
  docker inspect <objeto>
  ```
* **Mostrar estadísticas (CPU, memoria…)**

  ```bash
  docker stats [<contenedor>...]
  ```

### Redes y volúmenes

* **Listar redes**

  ```bash
  docker network ls
  ```
* **Crear red**

  ```bash
  docker network create <nombre>
  ```
* **Conectar contenedor a red**

  ```bash
  docker network connect <red> <contenedor>
  ```
* **Listar volúmenes**

  ```bash
  docker volume ls
  ```
* **Crear volumen**

  ```bash
  docker volume create <nombre>
  ```
* **Montar volumen**

  ```bash
  docker run -v <volumen>:/path/en/contenedor …
  ```

### Limpieza (prune)

* **Eliminar recursos no usados**

  ```bash
  docker system prune       # elimina contenedores detenidos, redes, imágenes “dangling”
  docker volume prune       # elimina volúmenes no referenciados
  docker network prune      # elimina redes no usadas
  docker image prune -a     # elimina imágenes no referenciadas
  ```

---

## Docker Compose

### Ciclo de vida

* **Levantar servicios**

  ```bash
  docker-compose up
  ```
* **Levantar en segundo plano**

  ```bash
  docker-compose up -d
  ```
* **Bajar servicios**

  ```bash
  docker-compose down
  ```
* **Reconstruir imágenes**

  ```bash
  docker-compose up --build
  ```

### Inspección y control

* **Listar servicios y contenedores**

  ```bash
  docker-compose ps
  ```
* **Ver logs**

  ```bash
  docker-compose logs
  docker-compose logs -f         # seguimiento
  docker-compose logs <servicio>  
  ```
* **Ejecutar comando en un servicio**

  ```bash
  docker-compose exec <servicio> <comando>
  ```
* **Escalar réplicas (solo en modo swarm)**

  ```bash
  docker-compose up -d --scale <servicio>=<n>
  ```

### Gestión de imágenes y redes

* **Forzar pull de imágenes**

  ```bash
  docker-compose pull
  ```
* **Eliminar contenedores, redes, volúmenes y/o imágenes**

  ```bash
  docker-compose down \
    --volumes   # elimina volúmenes
    --rmi all   # elimina imágenes
  ```
* **Mostrar configuración tras “merge”**

  ```bash
  docker-compose config
  ```

---

## Tips adicionales

* **Alias útil**

  ```bash
  alias dps="docker ps -a"
  alias dclean="docker system prune -af"
  ```
* **Modo swarm (orquestación)**

  ```bash
  docker swarm init
  docker stack deploy -c docker-compose.yml <stack_name>
  ```
* **Variables de entorno**

  * `.env` en mismo directorio se carga automáticamente al usar Compose.

---

> By CISO oswaldo.diaz 

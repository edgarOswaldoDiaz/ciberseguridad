# No‑SQL


## Neo4j

| Categoría             | Comando                                                          |
| --------------------- | ---------------------------------------------------------------- |
| **Conectar**          | `neo4j console` o a través de Neo4j Browser                      |
| **Crear nodo**        | `CREATE (n:Label {prop1: val1, prop2: val2});`                   |
| **Leer nodos**        | `MATCH (n:Label) RETURN n;`                                      |
| **Leer con filtro**   | `MATCH (n:Label {prop: val}) RETURN n;`                          |
| **Crear relación**    | `MATCH (a),(b) WHERE a.id=… AND b.id=… CREATE (a)-[:TIPO]->(b);` |
| **Actualizar nodo**   | `MATCH (n:Label {id:…}) SET n.prop = nuevo_val;`                 |
| **Eliminar nodo**     | `MATCH (n:Label {id:…}) DETACH DELETE n;`                        |
| **Eliminar relación** | `MATCH ()-[r:TIPO]->() DELETE r;`                                |

---

## ** Comandos Generales**

| Comando | Descripción |
|--------|-------------|
| `RETURN` | Devuelve resultados de una consulta |
| `MATCH` | Busca patrones en el grafo |
| `WHERE` | Filtra resultados |
| `CREATE` | Crea nodos o relaciones |
| `MERGE` | Crea nodos o relaciones si no existen |
| `DELETE` | Elimina nodos o relaciones |
| `DETACH DELETE` | Elimina nodos y sus relaciones |
| `SET` | Asigna o actualiza propiedades |
| `REMOVE` | Elimina propiedades o etiquetas |
| `WITH` | Encadena partes de una consulta |
| `UNWIND` | Desenvuelve listas en filas individuales |
| `LIMIT` | Limita el número de resul tados |
| `SKIP` | Omite un número de resultados |
| `ORDER BY` | Ordena los resultados |
| `DISTINCT` | Elimina duplicados |
| `OPTIONAL MATCH` | Coincidencia opcional de patrones |

---

## ** Nodos y Relaciones**

### Crear nodos

```cypher
CREATE (n:Label {property: 'value'})
```

### Crear relaciones

```cypher
CREATE (n1)-[:RELATION_TYPE]->(n2)
```

### Combinar nodos y relaciones

```cypher
CREATE (n1:Label1 {prop: 'val1'})-[:RELATION]->(n2:Label2 {prop: 'val2'})
```

---

## ** Búsqueda (MATCH)**

### Buscar nodos

```cypher
MATCH (n:Label)
RETURN n
```

### Buscar relaciones

```cypher
MATCH (n1)-[r:RELATION_TYPE]->(n2)
RETURN n1, r, n2
```

### Buscar por propiedad

```cypher
MATCH (n:Label {property: 'value'})
RETURN n
```

---

## ** MERGE (Crear si no existe)**

```cypher
MERGE (n:Label {property: 'value'})
ON CREATE SET n.created = timestamp()
ON MATCH SET n.lastSeen = timestamp()
```

---

## ** Actualizar / Eliminar**

### Actualizar propiedades

```cypher
MATCH (n:Label {property: 'value'})
SET n.newProperty = 'newValue'
```

### Eliminar nodo

```cypher
MATCH (n:Label {property: 'value'})
DELETE n
```

### Eliminar nodo con relaciones

```cypher
MATCH (n:Label {property: 'value'})
DETACH DELETE n
```

### Eliminar propiedad

```cypher
MATCH (n:Label {property: 'value'})
REMOVE n.property
```

### Eliminar etiqueta

```cypher
MATCH (n:Label {property: 'value'})
REMOVE n:Label
```

---

## ** Relaciones**

### Crear relación

```cypher
MATCH (a:Person {name: 'Alice'}), (b:Person {name: 'Bob'})
CREATE (a)-[:KNOWS]->(b)
```

### Eliminar relación

```cypher
MATCH (a)-[r:KNOWS]->(b)
DELETE r
```

---

## ** Funciones Comunes**

| Función | Descripción |
|--------|-------------|
| `count()` | Cuenta resultados |
| `sum()` | Suma valores |
| `avg()` | Promedio |
| `max()` / `min()` | Valor máximo/mínimo |
| `collect()` | Agrupa valores en lista |
| `size()` | Tamaño de una lista o cadena |
| `exists()` | Verifica si una propiedad existe |
| `coalesce()` | Devuelve el primer valor no nulo |
| `timestamp()` | Devuelve marca de tiempo actual |
| `toUpper()` / `toLower()` | Convierte texto a mayúsculas/minúsculas |

---

## ** Patrones Comunes**

### Encontrar amigos de amigos

```cypher
MATCH (p1:Person)-[:KNOWS]->(friend)-[:KNOWS]->(foaf:Person)
WHERE p1.name = 'Alice'
RETURN foaf
```

### Caminos más cortos

```cypher
MATCH path = shortestPath((a:Person {name: 'Alice'})-[*]-(b:Person {name: 'Bob'}))
RETURN path
```

---

## ** Índices y Constraints**

### Crear índice

```cypher
CREATE INDEX FOR (n:Label) ON (n.property)
```

### Crear constraint de unicidad

```cypher
CREATE CONSTRAINT FOR (n:Label) REQUIRE n.property IS UNIQUE
```

### Eliminar índice o constraint

```cypher
DROP INDEX index_name
DROP CONSTRAINT constraint_name
```

---

## ** Perfilado y Explicación**

| Comando | Descripción |
|--------|-------------|
| `EXPLAIN` | Muestra el plan de ejecución sin correr la consulta |
| `PROFILE` | Ejecuta la consulta y muestra estadísticas |

```cypher
EXPLAIN MATCH (n:Label) RETURN n
PROFILE MATCH (n:Label) RETURN count(n)
```

---

## ** Importar Datos**

### Desde CSV

```cypher
LOAD CSV WITH HEADERS FROM 'file:///ruta/archivo.csv' AS row
CREATE (:Label {property: row.column})
```

---

## ** Comandos del Shell / Administración**

| Comando | Descripción |
|--------|-------------|
| `:help` | Muestra ayuda |
| `:clear` | Limpia la consola |
| `:server status` | Estado del servidor |
| `:play movies` | Ejemplo de base de datos de películas |
| `:schema` | Muestra esquema de índices/constraints |
| `:queries` | Muestra consultas activas |
| `:sysinfo` | Información del sistema |


---

## Redis (CLI)

| Comando               | Descripción                                  |
| --------------------- | -------------------------------------------- |
| **Conectar**          | `redis-cli`                                  |
| **SET**               | `SET clave valor`                            |
| **GET**               | `GET clave`                                  |
| **DEL**               | `DEL clave`                                  |
| **EXISTS**            | `EXISTS clave`                               |
| **EXPIRE**            | `EXPIRE clave segundos`                      |
| **TTL**               | `TTL clave`                                  |
| **KEYS**              | `KEYS patrón*`                               |
| **HSET**              | `HSET hash campo valor`                      |
| **HGET**              | `HGET hash campo`                            |
| **HGETALL**           | `HGETALL hash`                               |
| **LPUSH**             | `LPUSH lista valor`                          |
| **RPUSH**             | `RPUSH lista valor`                          |
| **LRANGE**            | `LRANGE lista inicio fin`                    |
| **SADD**              | `SADD set miembro`                           |
| **SMEMBERS**          | `SMEMBERS set`                               |
| **PUBLISH/SUBSCRIBE** | `PUBLISH canal mensaje`<br>`SUBSCRIBE canal` |


---

## Gestión de claves (Keys)

| Comando              | Descripción                                        |
| -------------------- | -------------------------------------------------- |
| `KEYS pattern`       | Lista todas las claves que coinciden con el patrón |
| `EXISTS key`         | Comprueba si existe la clave                       |
| `DEL key`            | Elimina una o varias claves                        |
| `EXPIRE key seconds` | Establece tiempo de vida (TTL)                     |
| `TTL key`            | Muestra tiempo restante de vida de la clave        |
| `RENAME key newkey`  | Cambia el nombre de una clave                      |
| `TYPE key`           | Devuelve el tipo de dato de la clave               |

---

## Strings

| Comando                  | Descripción                         |
| ------------------------ | ----------------------------------- |
| `SET key value`          | Guarda una cadena                   |
| `GET key`                | Recupera valor de cadena            |
| `SETNX key value`        | SET si no existe                    |
| `MSET key1 v1 … keyN vN` | Establece múltiples pares key–value |
| `MGET key1 … keyN`       | Obtiene múltiples valores           |
| `INCR key`               | Incrementa entero                   |
| `INCRBY key increment`   | Incrementa por valor especificado   |
| `DECR key`               | Decrementa entero                   |
| `APPEND key value`       | Añade valor al final de la cadena   |
| `STRLEN key`             | Longitud de la cadena               |

---

## Hashes

| Comando                   | Descripción                         |
| ------------------------- | ----------------------------------- |
| `HSET key field value`    | Asigna valor a un campo             |
| `HGET key field`          | Obtiene el valor de un campo        |
| `HGETALL key`             | Devuelve todos los campos y valores |
| `HMSET key f1 v1 … fn vn` | Establece múltiples campos          |
| `HMGET key f1 … fn`       | Obtiene múltiples campos            |
| `HDEL key field`          | Elimina uno o más campos            |
| `HEXISTS key field`       | Comprueba si existe el campo        |
| `HINCRBY key field incr`  | Incrementa campo entero             |
| `HKEYS key`               | Lista todos los campos              |
| `HLEN key`                | Número de campos                    |
| `HVALS key`               | Lista todos los valores             |

---

## Listas

| Comando                     | Descripción                         |
| --------------------------- | ----------------------------------- |
| `LPUSH key value [value …]` | Inserta uno o más valores al inicio |
| `RPUSH key value [value …]` | Inserta uno o más valores al final  |
| `LPOP key`                  | Elimina y devuelve primer elemento  |
| `RPOP key`                  | Elimina y devuelve último elemento  |
| `LINDEX key index`          | Obtiene elemento por índice         |
| `LRANGE key start stop`     | Obtener rango de elementos          |
| `LREM key count value`      | Elimina elementos iguales a value   |
| `LLEN key`                  | Longitud de la lista                |
| `LSET key index value`      | Asigna nuevo valor a índice         |
| `LTRIM key start stop`      | Recorta lista al rango indicado     |

---

## Conjuntos (Sets)

| Comando                      | Descripción                          |
| ---------------------------- | ------------------------------------ |
| `SADD key member [member …]` | Añade uno o más miembros             |
| `SREM key member [member …]` | Elimina uno o más miembros           |
| `SMEMBERS key`               | Obtiene todos los miembros           |
| `SISMEMBER key member`       | Comprueba si miembro existe          |
| `SCARD key`                  | Cardinalidad (número de miembros)    |
| `SPOP key [count]`           | Elimina y devuelve miembro aleatorio |
| `SRANDMEMBER key [count]`    | Devuelve miembro(s) aleatorio(s)     |
| `SINTER key1 key2 …`         | Intersección de sets                 |
| `SUNION key1 key2 …`         | Unión de sets                        |
| `SDIFF key1 key2 …`          | Diferencia de sets                   |

---

## Sorted Sets (ZSets)

| Comando                                                       | Descripción                                |                              |
| ------------------------------------------------------------- | ------------------------------------------ | ---------------------------- |
| \`ZADD key \[NX                                               | XX] \[CH] score member \[score member …]\` | Añade miembro con puntuación |
| `ZREM key member [member …]`                                  | Elimina uno o más miembros                 |                              |
| `ZRANGE key start stop [WITHSCORES]`                          | Rango ascendente (opcional scores)         |                              |
| `ZREVRANGE key start stop [WITHSCORES]`                       | Rango descendente                          |                              |
| `ZSCORE key member`                                           | Obtiene puntuación de un miembro           |                              |
| `ZCARD key`                                                   | Tamaño del zset                            |                              |
| `ZCOUNT key min max`                                          | Cuenta entre rangos de puntuación          |                              |
| `ZRANGEBYSCORE key min max [WITHSCORES] [LIMIT offset count]` | Rango por puntuación                       |                              |
| `ZREMALL key`                                                 | Elimina todos los miembros (alias de DEL)  |                              |

---

## Pub/Sub

| Comando                          | Descripción                      |
| -------------------------------- | -------------------------------- |
| `PUBLISH channel message`        | Publica mensaje en canal         |
| `SUBSCRIBE channel [channel …]`  | Se suscribe a canal(es)          |
| `UNSUBSCRIBE [channel …]`        | Cancela suscripción              |
| `PSUBSCRIBE pattern [pattern …]` | Se suscribe por patrones         |
| `PUNSUBSCRIBE [pattern …]`       | Cancela suscripción por patrones |

---

## Transacciones

| Comando             | Descripción                                  |
| ------------------- | -------------------------------------------- |
| `MULTI`             | Inicia transacción                           |
| `EXEC`              | Ejecuta transacción                          |
| `DISCARD`           | Cancela transacción                          |
| `WATCH key [key …]` | Observa cambios para abortar si se modifican |
| `UNWATCH`           | Deja de observar                             |

---

## Scripting (Lua)

| Comando                                       | Descripción                        |
| --------------------------------------------- | ---------------------------------- |
| `EVAL script numkeys key [key …] arg [arg …]` | Ejecuta script Lua                 |
| `EVALSHA sha1 numkeys …`                      | Ejecuta script por su SHA1         |
| `SCRIPT LOAD script`                          | Carga script y devuelve SHA1       |
| `SCRIPT FLUSH`                                | Elimina todos los scripts cargados |
| `SCRIPT KILL`                                 | Mata script en ejecución           |

---

## Administración del Servidor

| Comando                      | Descripción                                  |
| ---------------------------- | -------------------------------------------- |
| `INFO [section]`             | Muestra información del servidor             |
| `PING`                       | Comprueba conexión (responde “PONG”)         |
| `FLUSHDB`                    | Elimina todas las claves de la base actual   |
| `FLUSHALL`                   | Elimina todas las claves de todas las bases  |
| `CONFIG GET pattern`         | Obtiene configuración                        |
| `CONFIG SET parameter value` | Ajusta configuración                         |
| `MONITOR`                    | Muestra en tiempo real todas las operaciones |
| `CLIENT LIST`                | Lista clientes conectados                    |
| `CLIENT KILL addr`           | Cierra conexión de cliente específico        |
| `SAVE`                       | Guarda snapshot RDB                          |
| `BGSAVE`                     | Guarda snapshot RDB en segundo plano         |
| `LASTSAVE`                   | Hora del último snapshot                     |

---

## Conexión y seguridad

| Comando         | Descripción                               |
| --------------- | ----------------------------------------- |
| `AUTH password` | Autentica con contraseña                  |
| `SELECT index`  | Cambia a DB con índice (0–15 por defecto) |
| `QUIT`          | Cierra conexión                           |

---

## Geoespacial

| Comando                                                                           | Descripción                     |                 |
| --------------------------------------------------------------------------------- | ------------------------------- | --------------- |
| `GEOADD key longitude latitude member`                                            | Añade posición geográfica       |                 |
| `GEOPOS key member [member …]`                                                    | Obtiene posición                |                 |
| `GEODIST key member1 member2 [unit]`                                              | Distancia entre miembros        |                 |
| \`GEORADIUS key lon lat radius unit \[WITHDIST] \[WITHCOORD] \[COUNT count] \[ASC | DESC]\`                         | Busca por radio |
| `GEORADIUSBYMEMBER key member radius unit [opciones]`                             | Similar a GEORADIUS por miembro |                 |

---

## HyperLogLog

| Comando                                   | Descripción                         |
| ----------------------------------------- | ----------------------------------- |
| `PFADD key element [element …]`           | Añade elemento al HyperLogLog       |
| `PFCOUNT key [key …]`                     | Cuenta estimado de elementos únicos |
| `PFMERGE destkey sourcekey [sourcekey …]` | Combina estructuras HyperLogLog     |

---

## Streams

| Comando                                             | Descripción                |
| --------------------------------------------------- | -------------------------- |
| `XADD key ID field value [field value …]`           | Añade entrada al stream    |
| `XRANGE key start end [COUNT count]`                | Lee rango de entradas      |
| `XREVRANGE key end start [COUNT count]`             | Rango inverso              |
| `XLEN key`                                          | Longitud del stream        |
| `XDEL key ID [ID …]`                                | Elimina entradas           |
| `XTRIM key MAXLEN [~] count`                        | Recorta stream             |
| `XGROUP CREATE key groupname id`                    | Crea grupo de consumidores |
| `XREAD [COUNT count] [BLOCK ms] STREAMS key … ID …` | Lee streams (bloquea)      |

---

## Cluster

| Comando                | Descripción                   |
| ---------------------- | ----------------------------- |
| `CLUSTER INFO`         | Información del cluster       |
| `CLUSTER NODES`        | Lista de nodos en el cluster  |
| `CLUSTER MEET ip port` | Añade nodo al cluster         |
| `CLUSTER SLOTS`        | Muestra distribución de slots |
| `CLUSTER FAILOVER`     | Forzar failover               |

---

## Cassandra (CQL)

| Categoría           | Comando                                                                                    |
| ------------------- | ------------------------------------------------------------------------------------------ |
| **Conectar**        | `cqlsh [host] [puerto]`                                                                    |
| **Crear keyspace**  | `CREATE KEYSPACE ks WITH replication = {'class':'SimpleStrategy','replication_factor':3};` |
| **Usar keyspace**   | `USE ks;`                                                                                  |
| **Crear tabla**     | `CREATE TABLE tabla (id UUID PRIMARY KEY, campo1 tipo, …);`                                |
| **Insertar**        | `INSERT INTO tabla (id, campo1) VALUES (uuid(), valor);`                                   |
| **Seleccionar**     | `SELECT * FROM tabla;`<br>`SELECT campo FROM tabla WHERE id=…;`                            |
| **Actualizar**      | `UPDATE tabla SET campo=valor WHERE id=…;`                                                 |
| **Eliminar fila**   | `DELETE FROM tabla WHERE id=…;`                                                            |
| **Alterar tabla**   | `ALTER TABLE tabla ADD nuevo_campo tipo;`                                                  |
| **Borrar tabla**    | `DROP TABLE tabla;`                                                                        |
| **Borrar keyspace** | `DROP KEYSPACE ks;`                                                                        |

---

## Gestión de Keyspaces

| Comando                                                                 | Descripción                                     | Ejemplo   |
| ----------------------------------------------------------------------- | ----------------------------------------------- | --------- |
| `CREATE KEYSPACE`                                                       | Crea un keyspace con estrategia de replicación. | \`\`\`sql |
| CREATE KEYSPACE mi\_keyspace                                            |                                                 |           |
| WITH replication = {'class':'SimpleStrategy', 'replication\_factor':3}; |                                                 |           |

----

````|
| `DESCRIBE KEYSPACE` | Muestra la definición de un keyspace. | ```sql  
DESCRIBE KEYSPACE mi_keyspace;  
``` |
| `ALTER KEYSPACE` | Modifica la configuración de replicación. | ```sql  
ALTER KEYSPACE mi_keyspace  
WITH replication = {'class':'NetworkTopologyStrategy','DC1':3,'DC2':2};  
``` |
| `DROP KEYSPACE` | Elimina un keyspace y todo su contenido. | ```sql  
DROP KEYSPACE mi_keyspace;  
``` |

---

## Gestión de Tablas (Column Families)

````|
| Comando | Descripción | Ejemplo |
|---|---|---|
| `CREATE TABLE` | Crea una tabla con sus columnas y claves. | ```sql  
CREATE TABLE mi_keyspace.usuarios (  
  id UUID PRIMARY KEY,  
  nombre text,  
  email text,  
  creado timestamp  
);  
``` |
| `DESCRIBE TABLE` / `DESC` | Muestra la definición de una tabla. | ```sql  
DESCRIBE TABLE mi_keyspace.usuarios;  
``` |
| `ALTER TABLE ADD` | Añade una columna nueva. | ```sql  
ALTER TABLE mi_keyspace.usuarios ADD edad int;  
``` |
| `ALTER TABLE DROP` | Elimina una columna. | ```sql  
ALTER TABLE mi_keyspace.usuarios DROP email;  
``` |
| `ALTER TABLE RENAME` | Renombra columna o table. | ```sql  
ALTER TABLE mi_keyspace.usuarios RENAME creado TO fecha_creacion;  
``` |
| `DROP TABLE` | Elimina la tabla. | ```sql  
DROP TABLE mi_keyspace.usuarios;  
``` |

---

## Operaciones CRUD

| Comando | Descripción | Ejemplo |
|---|---|---|
| `INSERT INTO` | Inserta o actualiza fila. | ```sql  
INSERT INTO mi_keyspace.usuarios (id, nombre, edad)  
VALUES (uuid(), 'Ana', 29);  
``` |
| `UPDATE` | Actualiza columnas de una fila existente. | ```sql  
UPDATE mi_keyspace.usuarios  
SET edad = 30  
WHERE id = f81d4fae-7dec-11d0-a765-00a0c91e6bf6;  
``` |
| `DELETE` | Elimina columnas o filas completas. | ```sql  
-- Eliminar solo edad  
DELETE edad FROM mi_keyspace.usuarios  
WHERE id = ...;  

-- Eliminar fila entera  
DELETE FROM mi_keyspace.usuarios  
WHERE id = ...;  
``` |
| `SELECT` | Consulta datos. | ```sql  
SELECT * FROM mi_keyspace.usuarios;  

SELECT nombre, edad  
FROM mi_keyspace.usuarios  
WHERE id = ...;  
``` |

---

## Índices y Materialized Views

| Comando | Descripción | Ejemplo |
|---|---|---|
| `CREATE INDEX` | Crea un índice secundario en una columna. | ```sql  
CREATE INDEX ON mi_keyspace.usuarios (edad);  
``` |
| `DROP INDEX` | Elimina un índice. | ```sql  
DROP INDEX mi_keyspace.usuarios_edad_idx;  
``` |
| `CREATE MATERIALIZED VIEW` | Crea una vista materializada con otra clave primaria. | ```sql  
CREATE MATERIALIZED VIEW mi_keyspace.usuarios_por_edad AS  
  SELECT edad, id, nombre  
  FROM mi_keyspace.usuarios  
  WHERE edad IS NOT NULL AND id IS NOT NULL  
  PRIMARY KEY (edad, id);  
``` |
| `DROP MATERIALIZED VIEW` | Elimina la vista. | ```sql  
DROP MATERIALIZED VIEW mi_keyspace.usuarios_por_edad;  
``` |

---

## Gestión de Usuarios y Permisos

| Comando | Descripción | Ejemplo |
|---|---|---|
| `CREATE ROLE` | Crea usuario/rol. | ```sql  
CREATE ROLE analista WITH LOGIN = true AND PASSWORD = 'secret';  
``` |
| `ALTER ROLE` | Modifica rol (password, permisos). | ```sql  
ALTER ROLE analista WITH PASSWORD = 'nuevaClave';  
``` |
| `DROP ROLE` | Elimina rol. | ```sql  
DROP ROLE analista;  
``` |
| `GRANT` | Otorga permisos (ALL, SELECT, MODIFY, etc.). | ```sql  
GRANT SELECT ON KEYSPACE mi_keyspace TO analista;  
``` |
| `REVOKE` | Revoca permisos. | ```sql  
REVOKE SELECT ON KEYSPACE mi_keyspace FROM analista;  
``` |

---

## Consultas Avanzadas

| Comando | Descripción | Ejemplo |
|---|---|---|
| `BATCH` | Agrupa múltiples operaciones atómicas. | ```sql  
BEGIN BATCH  
  INSERT INTO ...;  
  UPDATE ...;  
APPLY BATCH;  
``` |
| `TTL` | Tiempo de vida en inserción. | ```sql  
INSERT INTO mi_keyspace.eventos (id, info)  
VALUES (..., 'x') USING TTL 86400;  -- 1 día  
``` |
| `CONSISTENCY` | Define nivel de consistencia en SELECT/INSERT/UPDATE. | ```sql  
CONSISTENCY QUORUM;  
SELECT * FROM ...;  
``` |
| `PAGING` | Paginación automática (con driver). | ```sql  
-- En CQLSH  
PAGING ON;  
SELECT * FROM ...;  
``` |

---

## Mantenimiento de Cluster

| Comando (cqlsh) | Descripción |
|---|---|
| `nodetool status` | Ver estado de nodos. |
| `nodetool ring` | Ver topología del anillo. |
| `nodetool repair` | Repara inconsistencias de datos. |
| `nodetool cleanup` | Limpia datos de particiones movidas. |
| `nodetool compactionstats` | Estado de compactaciones. |
| `nodetool compact` | Fuerza compactación manual. |

---

## Utilidades de cqlsh

| Comando | Descripción |
|---|---|
| `\l` o `SHOW KEYSPACES` | Lista keyspaces. |
| `\d` o `DESCRIBE` | Describe esquema general. |
| `\use` | Cambia keyspace actual. |
| `SOURCE 'archivo.cql'` | Ejecuta script CQL desde archivo. |
| `COPY` | Exporta/importa datos CSV. |  
| &nbsp;&nbsp; `COPY mi_tabla TO 'out.csv';`  
| &nbsp;&nbsp; `COPY mi_tabla FROM 'in.csv';` |


## CouchDB (HTTP API / curl)

| Operación                | Ejemplo con `curl`                                                                          |
| ------------------------ | ------------------------------------------------------------------------------------------- |
| **Listar bases**         | `curl -X GET http://host:5984/_all_dbs`                                                     |
| **Crear base**           | `curl -X PUT http://host:5984/mi_base`                                                      |
| **Eliminar base**        | `curl -X DELETE http://host:5984/mi_base`                                                   |
| **Crear/actualizar doc** | `curl -X PUT http://host:5984/mi_base/doc1 -d '{"campo":"valor"}'`                          |
| **Obtener doc**          | `curl -X GET http://host:5984/mi_base/doc1`                                                 |
| **Eliminar doc**         | `curl -X DELETE http://host:5984/mi_base/doc1?rev=<rev-id>`                                 |
| **Buscar con Mango**     | `curl -X POST http://host:5984/mi_base/_find -d '{"selector": {"campo": {"$eq":"valor"}}}'` |

---


### **Instalación y Configuración Básica**

| Comando / Acción | Descripción |
|------------------|-------------|
| `curl http://127.0.0.1:5984/` | Verificar si CouchDB está corriendo |
| `curl -X GET http://admin:password@127.0.0.1:5984/_all_dbs` | Listar todas las bases de datos |
| `curl -X PUT http://admin:password@127.0.0.1:5984/mydb` | Crear una nueva base de datos |
| `curl -X DELETE http://admin:password@127.0.0.1:5984/mydb` | Eliminar una base de datos |

---

### **Manejo de Bases de Datos**

| Comando | Descripción |
|--------|-------------|
| `GET /{db}` | Obtener información de una base de datos |
| `PUT /{db}` | Crear una base de datos |
| `DELETE /{db}` | Eliminar una base de datos |
| `GET /_all_dbs` | Listar todas las bases de datos |
| `GET /_active_tasks` | Ver tareas activas en CouchDB |

---

### **Documentos**

| Comando | Descripción |
|--------|-------------|
| `POST /{db}` | Crear un nuevo documento (CouchDB genera el `_id`) |
| `PUT /{db}/{docid}` | Crear o actualizar un documento (con `_id` específico) |
| `GET /{db}/{docid}` | Obtener un documento por ID |
| `DELETE /{db}/{docid}?rev={rev}` | Eliminar un documento |
| `COPY /{db}/{docid}?rev={rev}` | Copiar un documento |
| `GET /{db}/{docid}/{attachment}` | Obtener un archivo adjunto de un documento |

---

### **Revisiones y Conflicto de Documentos**

| Comando | Descripción |
|--------|-------------|
| `GET /{db}/{docid}?revs=true` | Mostrar historial de revisiones |
| `GET /{db}/{docid}?rev={rev}` | Obtener una versión específica de un documento |
| `POST /{db}/_purge` | Eliminar permanentemente revisiones (solo admin) |

---

### **Consultas y Vistas**

| Comando | Descripción |
|--------|-------------|
| `POST /{db}/_find` | Realizar una consulta usando Mango Query |
| `GET /{db}/_design/{ddoc}/_view/{view}` | Ejecutar una vista MapReduce |
| `PUT /{db}/_design/{ddoc}` | Crear o actualizar un documento de diseño (vista) |
| `GET /{db}/_explain` | Explicar cómo se ejecuta una consulta Mango |

---

### **Replicación**

| Comando | Descripción |
|--------|-------------|
| `POST /_replicate` | Iniciar una replicación entre bases de datos |
| `GET /_scheduler/jobs` | Ver trabajos de replicación activos |
| `GET /_scheduler/docs` | Ver documentos de replicación programados |

Ejemplo de replicación:
```json
{
  "source": "http://example.com/source_db",
  "target": "http://admin:pass@localhost:5984/target_db",
  "continuous": true
}
```

---

### **Funciones de Administración**

| Comando | Descripción |
|--------|-------------|
| `GET /_config` | Ver configuración actual de CouchDB |
| `PUT /_config/{section}/{key}` | Modificar una configuración |
| `GET /_stats` | Estadísticas del servidor |
| `GET /_log` | Ver el log del servidor |
| `POST /_restart` | Reiniciar CouchDB (requiere permisos de admin) |

---

### **Autenticación y Seguridad**

| Comando | Descripción |
|--------|-------------|
| `POST /_session` | Iniciar sesión (autenticación por cookie) |
| `GET /_session` | Verificar sesión actual |
| `DELETE /_session` | Cerrar sesión |
| `PUT /{db}/_security` | Establecer permisos de seguridad en una BD |
| `GET /{db}/_security` | Ver permisos de seguridad de una BD |

---

### **Útil para Desarrolladores**

| Comando | Descripción |
|--------|-------------|
| `GET /` | Información básica del servidor |
| `GET /_uuids` | Generar UUIDs |
| `GET /_utils` | Acceder a Fauxton (interfaz web de CouchDB) |

---

### **Ejemplo Práctico con cURL**

Crear un documento:
```bash
curl -X POST http://admin:password@127.0.0.1:5984/mydb \
     -H "Content-Type: application/json" \
     -d '{"name": "John", "age": 30}'
```

Consultar con Mango:
```bash
curl -X POST http://admin:password@127.0.0.1:5984/mydb/_find \
     -H "Content-Type: application/json" \
     -d '{"selector": {"name": "John"}}'
```

## MongoDB (Shell)

| Categoría              | Comando y descripción                                                              |         |
| ---------------------- | ---------------------------------------------------------------------------------- | ------- |
| **Conectar**           | `mongo` — lanza el shell de MongoDB                                                |         |
| **Mostrar bases**      | `show dbs`                                                                         |         |
| **Usar base**          | `use <db>`                                                                         |         |
| **Crear colección**    | `db.createCollection("<colección>")`                                               |         |
| **Insertar documento** | `db.<colección>.insertOne({ campo: valor, … })`                                    |         |
| **Insertar varios**    | `db.<colección>.insertMany([{…}, {…}, …])`                                         |         |
| **Buscar**             | `db.<colección>.find()`<br>`db.<colección>.find({ filtro })`                       |         |
| **Proyección**         | `db.<colección>.find({}, { campo1: 1, campo2: 0 })`                                |         |
| **Modificar**          | `db.<colección>.updateOne({ filtro }, { $set: { campo: valor } })`<br>`updateMany` |         |
| **Reemplazar**         | `db.<colección>.replaceOne({ filtro }, { documento completo })`                    |         |
| **Eliminar**           | `db.<colección>.deleteOne({ filtro })`<br>`deleteMany({ filtro })`                 |         |
| **Crear índice**       | \`db.\<colección>.createIndex({ campo: 1                                           | ‑1 })\` |
| **Listar índices**     | `db.<colección>.getIndexes()`                                                      |         |
| **Aggregation**        | `db.<colección>.aggregate([ { $stage1 }, { $stage2 }, … ])`                        |         |

---


### **Conexión y administración**

| Comando | Descripción |
|--------|-------------|
| `mongo` | Iniciar el shell de MongoDB |
| `mongod` | Iniciar el servidor de MongoDB |
| `mongod --config /ruta/a/mongod.conf` | Iniciar MongoDB con archivo de configuración |
| `mongostat` | Ver estadísticas en tiempo real |
| `mongodump` | Realizar copia de seguridad |
| `mongorestore` | Restaurar desde copia de seguridad |
| `mongoexport` | Exportar datos a JSON/CSV |
| `mongoimport` | Importar datos desde JSON/CSV |

---

### **Bases de datos**

| Comando | Descripción |
|--------|-------------|
| `show dbs` | Mostrar todas las bases de datos |
| `use <db_name>` | Usar o crear una base de datos |
| `db` | Mostrar la base de datos actual |
| `db.dropDatabase()` | Eliminar la base de datos actual |

---

### **Colecciones**

| Comando | Descripción |
|--------|-------------|
| `show collections` | Mostrar colecciones en la BD actual |
| `db.createCollection("nombre")` | Crear una nueva colección |
| `db.<collection>.drop()` | Eliminar una colección |

---

### **Operaciones CRUD**

#### **Insertar documentos**

| Comando | Descripción |
|--------|-------------|
| `db.<collection>.insertOne({doc})` | Insertar un documento |
| `db.<collection>.insertMany([{doc1}, {doc2}])` | Insertar varios documentos |

#### **Buscar documentos**

| Comando | Descripción |
|--------|-------------|
| `db.<collection>.find()` | Buscar todos los documentos |
| `db.<collection>.findOne()` | Buscar un documento |
| `db.<collection>.find({filtro})` | Buscar con filtro |
| `db.<collection>.find().pretty()` | Mostrar resultados formateados |
| `db.<collection>.find({}).limit(5)` | Limitar resultados |
| `db.<collection>.find().sort({campo: 1})` | Ordenar (1 = asc, -1 = desc) |

#### **Actualizar documentos**

| Comando | Descripción |
|--------|-------------|
| `db.<collection>.updateOne({filtro}, {$set: {campo: valor}})` | Actualizar un documento |
| `db.<collection>.updateMany({filtro}, {$set: {campo: valor}})` | Actualizar varios documentos |
| `db.<collection>.replaceOne({filtro}, {nuevoDoc})` | Reemplazar un documento |

#### **Eliminar documentos**

| Comando | Descripción |
|--------|-------------|
| `db.<collection>.deleteOne({filtro})` | Eliminar un documento |
| `db.<collection>.deleteMany({filtro})` | Eliminar varios documentos |

---

### **Operadores de consulta**

| Operador | Descripción |
|---------|-------------|
| `$eq` | Igual |
| `$ne` | No igual |
| `$gt`, `$gte` | Mayor que, mayor o igual |
| `$lt`, `$lte` | Menor que, menor o igual |
| `$in`, `$nin` | En lista, no en lista |
| `$and`, `$or`, `$not`, `$nor` | Lógicos |
| `$exists` | Campo existe |
| `$regex` | Expresión regular |

---

### **Operadores de actualización**

| Operador | Descripción |
|---------|-------------|
| `$set` | Establecer valor |
| `$unset` | Eliminar campo |
| `$inc` | Incrementar valor |
| `$push` | Agregar a array |
| `$pull` | Remover de array |
| `$each`, `$addToSet` | Agregar múltiples valores sin duplicados |

---

### **Agregación (Pipeline)**

| Etapa | Descripción |
|-------|-------------|
| `$match` | Filtrar documentos |
| `$group` | Agrupar por campo |
| `$sort` | Ordenar documentos |
| `$limit` | Limitar resultados |
| `$skip` | Saltar documentos |
| `$project` | Seleccionar campos |
| `$unwind` | Desglosar arrays |
| `$lookup` | Joins (equivalente) |
| `$out` | Guardar resultado en colección |

Ejemplo:
```js
db.ventas.aggregate([
  { $match: { cantidad: { $gt: 10 } } },
  { $group: { _id: "$producto", total: { $sum: "$cantidad" } } }
])
```

---

### **Usuarios y seguridad**

| Comando | Descripción |
|--------|-------------|
| `db.createUser({user: "usuario", pwd: "contraseña", roles: [...]})` | Crear usuario |
| `db.auth("usuario", "contraseña")` | Autenticar usuario |
| `show users` | Listar usuarios |
| `db.dropUser("usuario")` | Eliminar usuario |

---

### **Índices**

| Comando | Descripción |
|--------|-------------|
| `db.<collection>.createIndex({campo: 1})` | Crear índice (1: asc, -1: desc) |
| `db.<collection>.getIndexes()` | Listar índices |
| `db.<collection>.dropIndex("nombre_índice")` | Eliminar índice |

---

## Otras operaciones útiles

* **Backup/Restore**

  * MongoDB: `mongodump --db mi_db --out /ruta/`
    `mongorestore --db mi_db /ruta/mi_db/`
  * Cassandra: `nodetool snapshot ks` y `sstableloader`
* **Monitorización**

  * Redis: `redis-cli INFO`
  * Cassandra: `nodetool status`
* **Seguridad**

  * MongoDB: creación de usuarios y roles con `db.createUser()`
  * Cassandra: configurar autenticación en `cassandra.yaml`

________________________-

> By CISO oswaldo.diaz

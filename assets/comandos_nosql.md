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

## 🔧 **1. Comandos Generales**

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
| `LIMIT` | Limita el número de resultados |
| `SKIP` | Omite un número de resultados |
| `ORDER BY` | Ordena los resultados |
| `DISTINCT` | Elimina duplicados |
| `OPTIONAL MATCH` | Coincidencia opcional de patrones |

---

## 🧱 **2. Nodos y Relaciones**

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

## 🔍 **3. Búsqueda (MATCH)**

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

## 🔁 **4. MERGE (Crear si no existe)**

```cypher
MERGE (n:Label {property: 'value'})
ON CREATE SET n.created = timestamp()
ON MATCH SET n.lastSeen = timestamp()
```

---

## 🧹 **5. Actualizar / Eliminar**

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

## 🔗 **6. Relaciones**

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

## 📊 **7. Funciones Comunes**

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

## 🧠 **8. Patrones Comunes**

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

## 🛠️ **9. Índices y Constraints**

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

## 🧪 **10. Perfilado y Explicación**

| Comando | Descripción |
|--------|-------------|
| `EXPLAIN` | Muestra el plan de ejecución sin correr la consulta |
| `PROFILE` | Ejecuta la consulta y muestra estadísticas |

```cypher
EXPLAIN MATCH (n:Label) RETURN n
PROFILE MATCH (n:Label) RETURN count(n)
```

---

## 📁 **11. Importar Datos**

### Desde CSV

```cypher
LOAD CSV WITH HEADERS FROM 'file:///ruta/archivo.csv' AS row
CREATE (:Label {property: row.column})
```

---

## 🧾 **12. Comandos del Shell / Administración**

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

¿Quieres que te lo exporte en formato PDF o Markdown para imprimir? También puedo ayudarte a crear una versión visual.


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

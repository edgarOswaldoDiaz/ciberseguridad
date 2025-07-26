# No‑SQL

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

## Neo4j (Cypher)

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

# No‑SQL

---

## MongoDB (mongo / mongosh)

### Conexión y gestión de bases de datos

```shell
# Iniciar shell
mongo
mongosh

# Listar bases de datos
show dbs

# Seleccionar o crear base
use mi_base

# Mostrar colecciónes
show collections
```

### CRUD básico

```js
// Insertar documentos
db.usuarios.insertOne({ nombre: "Ana", edad: 28 });
db.usuarios.insertMany([{…}, {…}]);

// Buscar documentos
db.usuarios.find({ edad: { $gt: 25 } });
db.usuarios.findOne({ nombre: "Ana" });

// Actualizar documentos
db.usuarios.updateOne(
  { nombre: "Ana" },
  { $set: { edad: 29 } }
);
db.usuarios.updateMany(
  { edad: { $lt: 20 } },
  { $inc: { edad: 1 } }
);

// Reemplazar documento
db.usuarios.replaceOne(
  { _id: ObjectId("…") },
  { nombre: "Ana", edad: 30, ciudad: "MX" }
);

// Eliminar documentos
db.usuarios.deleteOne({ nombre: "Ana" });
db.usuarios.deleteMany({ edad: { $lt: 18 } });
```

### Índices y agregaciones

```js
// Crear índice
db.usuarios.createIndex({ email: 1 }, { unique: true });

// Explorar índices
db.usuarios.getIndexes()

// Pipeline de agregación
db.ventas.aggregate([
  { $match: { total: { $gt: 100 } } },
  { $group: { _id: "$vendedor", sumaVentas: { $sum: "$total" } } },
  { $sort: { sumaVentas: -1 } }
]);
```

### Administración

```shell
# Copia de seguridad y restauración
mongodump --db mi_base --out /respaldos/
mongorestore --db mi_base /respaldos/mi_base

# Usuarios y roles
use admin
db.createUser({
  user: "appUser",
  pwd: "secret",
  roles: [{ role: "readWrite", db: "mi_base" }]
});
```

---

## Neo4j (Cypher)

### Conexión

```shell
# Desde la CLI
cypher-shell -u neo4j -p contraseña
```

### Creación de nodos y relaciones

```cypher
// Crear un nodo
CREATE (p:Persona {nombre: "Luis", edad: 35});

// Crear etiqueta múltiple
CREATE (o:Organizacion:Cliente {nombre: "Acme Corp"});

// Crear relación
MATCH (a:Persona {nombre: "Luis"}), (b:Organizacion {nombre: "Acme Corp"})
CREATE (a)-[:TRABAJA_EN {desde: 2020}]->(b);
```

### Lectura y búsqueda

```cypher
// Buscar todos los nodos de un tipo
MATCH (p:Persona)
RETURN p LIMIT 25;

// Patron de búsqueda con relación
MATCH (p:Persona)-[r:TRABAJA_EN]->(o:Organizacion)
WHERE r.desde > 2019
RETURN p.nombre, o.nombre, r.desde;
```

### Actualización y borrado

```cypher
// Actualizar propiedad
MATCH (p:Persona {nombre: "Luis"})
SET p.edad = 36;

// Eliminar relación o nodo
MATCH (p:Persona {nombre: "Luis"})-[r:TRABAJA_EN]->(o)
DELETE r;

MATCH (p:Persona {nombre: "Luis"})
DETACH DELETE p;
```

### Índices y restricciones

```cypher
// Índice
CREATE INDEX persona_nombre IF NOT EXISTS FOR (p:Persona) ON (p.nombre);

// Restricción de unicidad
CREATE CONSTRAINT ON (p:Persona) ASSERT p.email IS UNIQUE;
```

---

## CouchDB (REST API)

> Todas las operaciones se hacen vía HTTP(S), normalmente con `curl` o herramientas como Postman.

### Gestión de bases de datos

```bash
# Listar bases
curl -X GET http://localhost:5984/_all_dbs

# Crear base
curl -X PUT http://localhost:5984/mi_base

# Eliminar base
curl -X DELETE http://localhost:5984/mi_base
```

### Documentos

```bash
# Crear documento (ID autogenerado)
curl -X POST http://localhost:5984/mi_base \
     -H "Content-Type: application/json" \
     -d '{"nombre":"Ana","edad":28}'

# Crear/Actualizar documento con ID propio
curl -X PUT http://localhost:5984/mi_base/usuario123 \
     -H "Content-Type: application/json" \
     -d '{"nombre":"Ana","edad":29,"_rev":"1-xyz"}'

# Obtener documento
curl -X GET http://localhost:5984/mi_base/usuario123

# Eliminar documento
curl -X DELETE http://localhost:5984/mi_base/usuario123?rev=1-xyz
```

### Vistas y búsquedas

```json
// Definir un diseño (_design) con vistas
{
  "_id": "_design/mi_vista",
  "views": {
    "por_edad": {
      "map": "function(doc) { emit(doc.edad, doc); }"
    }
  }
}

// Consultar vista
curl -X GET http://localhost:5984/mi_base/_design/mi_vista/_view/por_edad?key=28
```

### Replicación

```bash
# Replicar de origen a destino
curl -X POST http://localhost:5984/_replicate \
     -H "Content-Type: application/json" \
     -d '{
       "source": "mi_base",
       "target": "http://remoto:5984/mi_base_replica",
       "continuous": true
     }'
```

---

## Cassandra (cqlsh)

### Conexión y keyspaces

```shell
# Iniciar shell
cqlsh localhost 9042

# Listar keyspaces
DESCRIBE KEYSPACES;

# Crear keyspace
CREATE KEYSPACE mi_keyspace
  WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 3};

# Usar keyspace
USE mi_keyspace;
```

### Tablas y CRUD

```sql
-- Crear tabla
CREATE TABLE usuarios (
  id uuid PRIMARY KEY,
  nombre text,
  edad int
);

-- Insertar datos
INSERT INTO usuarios (id, nombre, edad)
VALUES (uuid(), 'Ana', 28);

-- Consultar datos
SELECT * FROM usuarios WHERE id = xxxx-xxxx-...;

-- Actualizar datos
UPDATE usuarios SET edad = 29 WHERE id = xxxx-xxxx-...;

-- Borrar datos
DELETE FROM usuarios WHERE id = xxxx-xxxx-...;
```

### Índices y colecciones

```sql
-- Crear índice secundario
CREATE INDEX ON usuarios (edad);

-- Tipos de datos avanzados
CREATE TABLE tienda (
  id uuid PRIMARY KEY,
  productos map<text,double>,
  etiquetas set<text>,
  visitas list<timestamp>
);
```

### Administración y utilidades

```shell
# Estado del clúster
nodetool status

# Compaction manual
nodetool compact mi_keyspace usuarios

# Backup/restauración
# (Depende de nodetool snapshot y sstableloader)
nodetool snapshot -t respaldo1 mi_keyspace
sstableloader -d nodo1,nodo2 /ruta/al/snapshot
```

________________________

> By CISO oswaldo.diaz

# SQL (Structured Query Language)

---

## Data Definition Language (DDL)

| Comando           | Descripción                                        | Ejemplo                                                                                                           |
| ----------------- | -------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `CREATE DATABASE` | Crea una nueva base de datos                       | `sql<br>CREATE DATABASE MiBaseDeDatos;`                                                                           |
| `DROP DATABASE`   | Elimina una base de datos                          | `sql<br>DROP DATABASE MiBaseDeDatos;`                                                                             |
| `CREATE TABLE`    | Crea una nueva tabla                               | `sql<br>CREATE TABLE Clientes (<br>  id INT PRIMARY KEY,<br>  nombre VARCHAR(100),<br>  email VARCHAR(255)<br>);` |
| `ALTER TABLE`     | Modifica la estructura de una tabla                | `sql<br>ALTER TABLE Clientes ADD COLUMN edad INT;`                                                                |
| `DROP TABLE`      | Elimina una tabla                                  | `sql<br>DROP TABLE Clientes;`                                                                                     |
| `TRUNCATE TABLE`  | Elimina todos los registros de una tabla (sin log) | `sql<br>TRUNCATE TABLE Clientes;`                                                                                 |
| `RENAME TABLE`    | Cambia el nombre de una tabla                      | `sql<br>ALTER TABLE Clientes RENAME TO Usuarios;`                                                                 |
| `COMMENT ON`      | Agrega comentario a tablas o columnas              | `sql<br>COMMENT ON COLUMN Clientes.email IS 'Correo electrónico del cliente';`                                    |

---

## Data Manipulation Language (DML)

| Comando              | Descripción                         | Ejemplo                                                                                                                                                                                                                                                     |
| -------------------- | ----------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `SELECT`             | Consulta datos                      | `sql<br>SELECT id, nombre FROM Clientes WHERE edad > 30 ORDER BY nombre DESC;`                                                                                                                                                                              |
| `INSERT INTO`        | Inserta uno o varios registros      | `sql<br>INSERT INTO Clientes (id, nombre, email) VALUES (1, 'Ana', 'ana@ejemplo.com');`                                                                                                                                                                     |
| `UPDATE`             | Actualiza registros existentes      | `sql<br>UPDATE Clientes SET email = 'nuevo@ejemplo.com' WHERE id = 1;`                                                                                                                                                                                      |
| `DELETE`             | Elimina registros                   | `sql<br>DELETE FROM Clientes WHERE id = 1;`                                                                                                                                                                                                                 |
| `MERGE` (o `UPSERT`) | Inserta o actualiza según condición | `sql<br>MERGE INTO Clientes AS T<br>USING (VALUES (1,'Ana','ana@ejemplo.com')) AS S(id,nombre,email)<br>ON T.id = S.id<br>WHEN MATCHED THEN UPDATE SET nombre = S.nombre<br>WHEN NOT MATCHED THEN INSERT (id,nombre,email) VALUES (S.id,S.nombre,S.email);` |

---

## Data Control Language (DCL)

| Comando  | Descripción                      | Ejemplo                                                |
| -------- | -------------------------------- | ------------------------------------------------------ |
| `GRANT`  | Otorga permisos a usuarios/roles | `sql<br>GRANT SELECT, INSERT ON Clientes TO usuario1;` |
| `REVOKE` | Revoca permisos                  | `sql<br>REVOKE INSERT ON Clientes FROM usuario1;`      |

---

## Transaction Control Language (TCL)

| Comando       | Descripción                                  | Ejemplo                   |
| ------------- | -------------------------------------------- | ------------------------- |
| `BEGIN TRAN`  | Inicia una transacción                       | `sql<br>BEGIN TRAN;`      |
| `COMMIT`      | Confirma todos los cambios de la transacción | `sql<br>COMMIT;`          |
| `ROLLBACK`    | Revierte la transacción completa             | `sql<br>ROLLBACK;`        |
| `SAVEPOINT`   | Marca un punto dentro de la transacción      | `sql<br>SAVEPOINT sp1;`   |
| `ROLLBACK TO` | Revierte a un savepoint específico           | `sql<br>ROLLBACK TO sp1;` |

---

## Claúsulas y Funcionalidades Clave

* **`WHERE`**: Filtra filas según condición

  ```sql
  SELECT * FROM Pedidos
  WHERE fecha >= '2025-01-01';
  ```
* **`GROUP BY`**: Agrupa resultados

  ```sql
  SELECT cliente_id, COUNT(*) AS total_pedidos
  FROM Pedidos
  GROUP BY cliente_id;
  ```
* **`HAVING`**: Filtra grupos generados con `GROUP BY`

  ```sql
  SELECT cliente_id, COUNT(*) AS total_pedidos
  FROM Pedidos
  GROUP BY cliente_id
  HAVING COUNT(*) > 5;
  ```
* **`ORDER BY`**: Ordena resultados

  ```sql
  SELECT * FROM Productos
  ORDER BY precio DESC;
  ```
* **`LIMIT`** / **`OFFSET`**: Paginación

  ```sql
  SELECT * FROM Empleados
  ORDER BY id
  LIMIT 10 OFFSET 20;
  ```
* **`DISTINCT`**: Elimina duplicados

  ```sql
  SELECT DISTINCT ciudad FROM Clientes;
  ```
* **`UNION` / `UNION ALL`**: Combina resultados de varias consultas

  ```sql
  SELECT nombre FROM Usuarios
  UNION
  SELECT nombre FROM Administradores;
  ```

---

## Joins (Combinación de tablas)

| Tipo              | Descripción                                                 | Ejemplo                                                                                   |
| ----------------- | ----------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `INNER JOIN`      | Solo filas con coincidencia en ambas tablas                 | `sql<br>SELECT *<br>FROM Clientes C<br>INNER JOIN Pedidos P ON C.id = P.cliente_id;`      |
| `LEFT JOIN`       | Todas las filas de la izquierda, coincidentes de la derecha | `sql<br>SELECT *<br>FROM Clientes C<br>LEFT JOIN Pedidos P ON C.id = P.cliente_id;`       |
| `RIGHT JOIN`      | Todas las filas de la derecha, coincidentes de la izquierda | `sql<br>SELECT *<br>FROM Clientes C<br>RIGHT JOIN Pedidos P ON C.id = P.cliente_id;`      |
| `FULL OUTER JOIN` | Todas las filas de ambas tablas, coincidentes donde existan | `sql<br>SELECT *<br>FROM Clientes C<br>FULL OUTER JOIN Pedidos P ON C.id = P.cliente_id;` |
| `CROSS JOIN`      | Producto cartesiano                                         | `sql<br>SELECT *<br>FROM Colores<br>CROSS JOIN Tallas;`                                   |

---

## Objetos Auxiliares

* **Vistas (`VIEW`)**

  ```sql
  CREATE VIEW VistaActivos AS
  SELECT id, nombre FROM Empleados WHERE activo = 1;
  ```

* **Índices (`INDEX`)**

  ```sql
  CREATE INDEX idx_email_clientes ON Clientes(email);
  ```

* **Funciones y Procedimientos Almacenados**

  ```sql
  CREATE FUNCTION fn_total_pedidos(cli_id INT)
  RETURNS INT
  BEGIN
    DECLARE cnt INT;
    SELECT COUNT(*) INTO cnt FROM Pedidos WHERE cliente_id = cli_id;
    RETURN cnt;
  END;
  ```

---

## Subconsultas y Expresiones Compuestas

* **Subconsulta en `SELECT`**

  ```sql
  SELECT nombre,
         (SELECT COUNT(*) FROM Pedidos WHERE cliente_id = C.id) AS total_pedidos
  FROM Clientes C;
  ```
* **Subconsulta en `WHERE`**

  ```sql
  SELECT * FROM Productos
  WHERE categoria_id IN (SELECT id FROM Categorias WHERE nombre = 'Electrónica');
  ```
* **CTE (Common Table Expression)**

  ```sql
  WITH Ventas2025 AS (
    SELECT producto_id, SUM(cantidad) AS total_vendido
    FROM Ventas
    WHERE YEAR(fecha) = 2025
    GROUP BY producto_id
  )
  SELECT P.nombre, V.total_vendido
  FROM Ventas2025 V
  JOIN Productos P ON P.id = V.producto_id;
  ```

---

> **Tip:** cada dialecto (MySQL, PostgreSQL, SQL Server, Oracle, SQLite…) puede tener extensiones propias. Revisa siempre la documentación específica de tu motor.

____________________________

> By CISO oswaldo.diaz

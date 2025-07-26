# PHP

## **Comandos Básicos de PHP CLI**

| Comando | Descripción |
|--------|-------------|
| `php -v` | Muestra la versión de PHP instalada |
| `php -m` | Lista los módulos cargados |
| `php -i` | Muestra la información de PHP (similar a `phpinfo()`) |
| `php archivo.php` | Ejecuta un archivo PHP desde la terminal |
| `php -S localhost:8000` | Inicia el servidor integrado de PHP |
| `php -l archivo.php` | Verifica la sintaxis de un archivo PHP |

---

## **Variables y Tipos de Datos**

```php
$variable = "Hola";        // String
$numero = 42;              // Integer
$decimal = 3.14;           // Float
$booleano = true;          // Boolean
$nulo = null;              // Null
$arreglo = [1,2,3];        // Array
```

---

## **Operadores**

| Operador | Descripción |
|---------|-------------|
| `+`, `-`, `*`, `/`, `%` | Aritméticos |
| `==`, `===`, `!=`, `!==` | Comparación |
| `&&`, `\|\|`, `!` | Lógicos |
| `.=` | Concatenar y asignar |
| `??` | Null coalescing (PHP 7+) |

---

## **Estructuras de Control**

### Condicionales
```php
if ($condicion) {
    // código
} elseif ($otra) {
    // código
} else {
    // código
}

switch ($variable) {
    case 'valor':
        // código
        break;
    default:
        // código
}
```

### Bucles
```php
for ($i = 0; $i < 10; $i++) {
    // código
}

foreach ($array as $item) {
    // código
}

while ($condicion) {
    // código
}

do {
    // código
} while ($condicion);
```

---

## **Funciones**

### Definir una función
```php
function nombreFuncion($parametro = 'valor') {
    return $resultado;
}
```

### Funciones comunes
| Función | Descripción |
|--------|-------------|
| `echo "texto"` | Imprime texto |
| `print_r($variable)` | Imprime información legible de una variable |
| `var_dump($variable)` | Muestra información detallada, incluyendo tipo |
| `isset($variable)` | Verifica si una variable está definida |
| `empty($variable)` | Verifica si una variable está vacía |
| `unset($variable)` | Destruye una variable |
| `strlen($cadena)` | Devuelve la longitud de una cadena |
| `strpos($cadena, "busca")` | Busca la posición de una subcadena |
| `explode(" ", $cadena)` | Divide una cadena en un array |
| `implode(" ", $array)` | Une elementos de un array en una cadena |

---

## **Arrays**

```php
$array = array(1, 2, 3); // o [1, 2, 3]
$asociativo = ["clave" => "valor"];

// Funciones útiles:
count($array);          // Tamaño del array
array_push($array, 4);  // Añadir elemento
array_pop($array);      // Eliminar último elemento
array_merge($a1, $a2);  // Unir arrays
array_keys($array);     // Obtener claves
array_values($array);   // Obtener valores
```

---

## **Manejo de Archivos**

```php
file_get_contents("archivo.txt");     // Leer archivo
file_put_contents("archivo.txt", $data); // Escribir en archivo
unlink("archivo.txt");                // Eliminar archivo
is_file("ruta");                      // Verifica si es archivo
is_dir("ruta");                       // Verifica si es directorio
mkdir("nueva_carpeta");               // Crear carpeta
```

---

## **Trabajar con Formularios y HTTP**

```php
$_GET['clave'];         // Datos de URL
$_POST['clave'];        // Datos de formulario POST
$_REQUEST['clave'];     // GET, POST o COOKIE
$_SESSION['clave'];     // Variables de sesión
$_COOKIE['clave'];      // Cookies
$_SERVER['REQUEST_METHOD']; // Método HTTP
```

---

## **Funciones de Fecha**

```php
date("Y-m-d H:i:s");       // Fecha actual
strtotime("2024-12-31");   // Convierte cadena a timestamp
time();                    // Timestamp actual
```

---

## **Manejo de Excepciones**

```php
try {
    // Código que puede fallar
} catch (Exception $e) {
    echo 'Error: ' . $e->getMessage();
} finally {
    // Siempre se ejecuta
}
```

---

## **Funciones Útiles Variadas**

| Función | Descripción |
|--------|-------------|
| `json_encode($array)` | Convierte array a JSON |
| `json_decode($json)` | Convierte JSON a array/objeto |
| `filter_var($email, FILTER_VALIDATE_EMAIL)` | Valida email |
| `password_hash($pass, PASSWORD_DEFAULT)` | Encripta contraseña |
| `password_verify($pass, $hash)` | Verifica contraseña |
| `header("Location: url")` | Redirige a otra página |
| `exit()` o `die()` | Finaliza la ejecución |

---

## **Composer (Gestor de dependencias)**

| Comando | Descripción |
|--------|-------------|
| `composer init` | Inicializa un proyecto |
| `composer require vendor/package` | Instala un paquete |
| `composer install` | Instala dependencias del `composer.json` |
| `composer update` | Actualiza dependencias |
| `composer dump-autoload` | Regenera el autoloader |

____________________

> By CISO oswaldo.diaz

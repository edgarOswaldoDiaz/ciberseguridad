# **C++ Cheat Sheet**

## Estructura básica

```cpp
#include <iostream>   // Librerías
using namespace std;  // Espacio de nombres

int main() {
    cout << "Hola, mundo" << endl; // Salida
    return 0; // Fin del programa
}
```

---

## Tipos de datos

```cpp
int x = 10;          // Entero
float y = 3.14;      // Decimal (32 bits)
double z = 2.71828;  // Decimal (64 bits)
char c = 'A';        // Carácter
string s = "Texto";  // Cadena
bool b = true;       // Booleano
```

---

## Entrada y salida

```cpp
cout << "Valor: " << x << endl;  // Salida
cin >> x;                        // Entrada
```

---

## Operadores

* **Aritméticos**: `+ - * / % ++ --`
* **Relacionales**: `== != > < >= <=`
* **Lógicos**: `&& || !`
* **Asignación**: `= += -= *= /= %=`
* **Bit a bit**: `& | ^ ~ << >>`

---

## Condicionales

```cpp
if (x > 0) {
    cout << "Positivo";
} else if (x == 0) {
    cout << "Cero";
} else {
    cout << "Negativo";
}

switch (op) {
    case 1: cout << "Uno"; break;
    case 2: cout << "Dos"; break;
    default: cout << "Otro";
}
```

---

## Bucles

```cpp
for (int i=0; i<5; i++) { cout << i; }

int i=0;
while (i<5) { cout << i; i++; }

do { cout << i; i++; } while (i<5);
```

---

## Funciones

```cpp
int suma(int a, int b) {
    return a + b;
}
```

---

## Arreglos y strings

```cpp
int arr[5] = {1,2,3,4,5};
cout << arr[0];

string texto = "Hola";
cout << texto.length();
```

---

## Punteros y referencias

```cpp
int x = 10;
int *p = &x;       // puntero
cout << *p;        // accede al valor

int &ref = x;      // referencia
ref = 20;
```

---

## Clases y objetos

```cpp
class Persona {
public:
    string nombre;
    int edad;

    void saludar() {
        cout << "Hola, soy " << nombre;
    }
};

Persona p;
p.nombre = "Ana";
p.saludar();
```

---

## Constructores y herencia

```cpp
class Animal {
public:
    Animal(string n) { nombre = n; }
    void hablar() { cout << nombre << " hace un sonido"; }
protected:
    string nombre;
};

class Perro : public Animal {
public:
    Perro(string n) : Animal(n) {}
    void hablar() { cout << nombre << " dice Guau"; }
};
```

---

## STL (Standard Template Library)

```cpp
#include <vector>
#include <map>
#include <algorithm>

vector<int> v = {1,2,3};
v.push_back(4);

map<string,int> m;
m["uno"] = 1;

sort(v.begin(), v.end());
```

---

## Excepciones

```cpp
try {
    throw runtime_error("Error!");
} catch (exception &e) {
    cout << e.what();
}
```

---

## Archivos

```cpp
#include <fstream>

ofstream out("archivo.txt");
out << "Hola archivo";
out.close();

ifstream in("archivo.txt");
string linea;
while(getline(in, linea)) cout << linea;
in.close();
```

---

## Palabras clave útiles

`auto, const, static, friend, virtual, override, this, namespace, template, typename`

______________

> By CISO oswaldo.diaz

# **Diseño de algoritmos de seguridad**

El diseño de algoritmos de seguridad es un campo estratégico y altamente especializado que impacta directamente en la protección de datos y sistemas críticos. En el contexto de un diplomado en ciberseguridad, comprender los principios, tipos y desafíos del diseño algorítmico es fundamental para formar profesionales capaces de responder a los riesgos emergentes con soluciones innovadoras, robustas y sostenibles.

**Fundamentos del diseño de algoritmos de seguridad**

El diseño de algoritmos de seguridad parte del análisis profundo de amenazas y vulnerabilidades en los sistemas informáticos. Los algoritmos deben ser capaces de resistir ataques tanto pasivos como activos, y para ello, es imprescindible que estén basados en principios sólidos de criptografía, teoría de la información y matemáticas aplicadas.

Un algoritmo de seguridad eficaz debe cumplir con tres requisitos fundamentales:

- **Solidez criptográfica**: La seguridad debe residir en la fortaleza matemática del algoritmo, no en la confidencialidad del diseño.
- **Eficiencia computacional**: Debe ser lo suficientemente rápido para integrarse en sistemas en tiempo real, sin comprometer el rendimiento.
- **Escalabilidad y adaptabilidad**: Debe poder adaptarse a distintos contextos y evolucionar frente a nuevas amenazas.

**Principios clave en el diseño**

El diseño de algoritmos de seguridad no solo requiere pericia técnica, sino también una visión estratégica. Algunos principios esenciales incluyen:

- **Principio de Kerckhoffs**: “Un sistema debe ser seguro incluso si todo lo relacionado con él, excepto la clave, es de conocimiento público”.
- **Minimización de la superficie de ataque**: Los algoritmos deben limitar la cantidad de datos expuestos a potenciales atacantes.
- **Resistencia a ataques criptográficos conocidos**: Como ataques por fuerza bruta, análisis de canal lateral, ataques de colisión o criptoanálisis diferencial.

Además, es fundamental realizar un **análisis formal de seguridad**, sometiendo el algoritmo a pruebas rigurosas, auditorías de código y revisión por la comunidad científica. El avance de la tecnología impone nuevos desafíos al diseño de algoritmos de seguridad. La aparición de la **computación cuántica** amenaza con volver obsoletos muchos algoritmos actuales, como RSA o ECC. Esto ha dado paso a un nuevo campo: la **criptografía post-cuántica**, donde se diseñan algoritmos resistentes a ataques de computadoras cuánticas. Otro reto creciente es el **equilibrio entre seguridad y usabilidad**, especialmente en entornos de dispositivos móviles, IoT y edge computing, donde los recursos son limitados y los algoritmos deben ser livianos y eficientes.

**Tipos de algoritmos de seguridad**

Los algoritmos de seguridad pueden clasificarse principalmente en tres categorías:

- **Criptografía simétrica**: Utiliza la misma clave para cifrar y descifrar la información. Ejemplos representativos son AES (Advanced Encryption Standard) y DES (Data Encryption Standard).
- **Criptografía asimétrica**: Utiliza un par de claves (pública y privada). Ejemplos: RSA, ECC (Elliptic Curve Cryptography).
- **Algoritmos de hashing**: Proveen integridad y autenticación de datos. Ejemplos: SHA-2, SHA-3, BLAKE3.

Cada tipo responde a diferentes necesidades de seguridad, y su elección depende del entorno operativo, la sensibilidad de los datos y las amenazas predominantes.

---

### Criptografía Simétrica

En criptografía simétrica, **la misma clave** se utiliza para cifrar y descifrar el mensaje:

#### Fórmulas en LaTeX:

```latex
% Cifrado simétrico
C = E_K(M)

% Descifrado simétrico
M = D_K(C)
```

#### Donde:
- \( M \): mensaje original (plaintext)
- \( C \): mensaje cifrado (ciphertext)
- \( K \): clave secreta compartida
- \( E_K \): función de cifrado usando la clave \( K \)
- \( D_K \): función de descifrado usando la clave \( K \)

Este ejemplo proporciona una introducción básica a la criptografía simétrica utilizando Python y la biblioteca `cryptography`. En aplicaciones del mundo real, se deben considerar aspectos más avanzados como la rotación de claves, el almacenamiento seguro de claves y la elección de algoritmos y modos de operación apropiados para las necesidades específicas de seguridad.

```python
from cryptography.fernet import Fernet

def generar_clave():
    """Genera una clave secreta para el cifrado simétrico."""
    clave = Fernet.generate_key()
    return clave

def cifrar_mensaje(mensaje, clave):
    """Cifra un mensaje utilizando la clave proporcionada."""
    f = Fernet(clave)
    mensaje_bytes = mensaje.encode('utf-8')  # Codificar el mensaje a bytes
    mensaje_cifrado = f.encrypt(mensaje_bytes)
    return mensaje_cifrado

def descifrar_mensaje(mensaje_cifrado, clave):
    """Descifra un mensaje cifrado utilizando la clave proporcionada."""
    f = Fernet(clave)
    mensaje_descifrado_bytes = f.decrypt(mensaje_cifrado)
    mensaje_descifrado = mensaje_descifrado_bytes.decode('utf-8')  # Decodificar los bytes a string
    return mensaje_descifrado

if __name__ == "__main__":
    # 1. Generar una clave secreta (esto se haría una sola vez y se guardaría de forma segura)
    clave_secreta = generar_clave()
    print(f"Clave secreta generada: {clave_secreta.decode()}") # ¡Importante! No mostrar la clave en un entorno real

    # 2. Mensaje que queremos cifrar
    mensaje_original = "Este es un mensaje secreto."
    print(f"\nMensaje original: {mensaje_original}")

    # 3. Cifrar el mensaje utilizando la clave secreta
    mensaje_cifrado = cifrar_mensaje(mensaje_original, clave_secreta)
    print(f"Mensaje cifrado: {mensaje_cifrado}")

    # 4. Descifrar el mensaje cifrado utilizando la misma clave secreta
    mensaje_descifrado = descifrar_mensaje(mensaje_cifrado, clave_secreta)
    print(f"Mensaje descifrado: {mensaje_descifrado}")

    # 5. Verificar que el mensaje original y el mensaje descifrado son iguales
    if mensaje_original == mensaje_descifrado:
        print("\n¡El cifrado y descifrado se realizaron correctamente!")
    else:
        print("\n¡Hubo un error en el cifrado o descifrado!")
```

**Explicación**

1.  **Importación de la biblioteca `cryptography`:**
    ```python
    from cryptography.fernet import Fernet
    ```
    * Importamos la clase `Fernet` del módulo `fernet` dentro de la biblioteca `cryptography`. `Fernet` es una implementación de cifrado simétrico autenticado. Esto significa que no solo cifra los datos, sino que también asegura su integridad (que no han sido alterados). Utiliza el algoritmo de cifrado AES (Advanced Encryption Standard) en modo CBC (Cipher Block Chaining) con un HMAC (Hash-based Message Authentication Code) para la autenticación.

2.  **Función `generar_clave()`:**
    ```python
    def generar_clave():
        """Genera una clave secreta para el cifrado simétrico."""
        clave = Fernet.generate_key()
        return clave
    ```
    * Esta función utiliza el método estático `Fernet.generate_key()` para crear una nueva clave secreta.
    * **Importante:** Esta clave debe mantenerse en secreto y compartirse de forma segura entre las partes que necesitan cifrar y descifrar mensajes. Generar una nueva clave para cada comunicación o sesión sensible es una buena práctica de seguridad.
    * La clave generada es una secuencia de bytes.

3.  **Función `cifrar_mensaje(mensaje, clave)`:**
    ```python
    def cifrar_mensaje(mensaje, clave):
        """Cifra un mensaje utilizando la clave proporcionada."""
        f = Fernet(clave)
        mensaje_bytes = mensaje.encode('utf-8')  # Codificar el mensaje a bytes
        mensaje_cifrado = f.encrypt(mensaje_bytes)
        return mensaje_cifrado
    ```
    * Creamos una instancia de la clase `Fernet` pasando la `clave` generada. Esta instancia (`f`) es la que se utilizará para las operaciones de cifrado y descifrado con esa clave específica.
    * El mensaje original (`mensaje`) es una cadena de texto (string). Para que `Fernet` pueda cifrarlo, primero debemos convertirlo a una secuencia de bytes utilizando la codificación `utf-8`.
    * El método `f.encrypt(mensaje_bytes)` realiza el cifrado del mensaje en bytes y devuelve el `mensaje_cifrado` también en formato de bytes.

4.  **Función `descifrar_mensaje(mensaje_cifrado, clave)`:**
    ```python
    def descifrar_mensaje(mensaje_cifrado, clave):
        """Descifra un mensaje cifrado utilizando la clave proporcionada."""
        f = Fernet(clave)
        mensaje_descifrado_bytes = f.decrypt(mensaje_cifrado)
        mensaje_descifrado = mensaje_descifrado_bytes.decode('utf-8')  # Decodificar los bytes a string
        return mensaje_descifrado
    ```
    * Al igual que en el cifrado, creamos una instancia de `Fernet` con la misma `clave` utilizada para cifrar. **Es crucial usar la misma clave para descifrar.**
    * El método `f.decrypt(mensaje_cifrado)` toma el mensaje cifrado en bytes y lo descifra, devolviendo el resultado también en bytes (`mensaje_descifrado_bytes`).
    * Finalmente, decodificamos la secuencia de bytes resultante a una cadena de texto utilizando `decode('utf-8')` para obtener el mensaje original.

5.  **Bloque `if __name__ == "__main__":`:**
    * Este bloque de código se ejecuta solo cuando el script se ejecuta directamente (no cuando se importa como un módulo).
    * **Generación de la clave:** Se llama a `generar_clave()` para obtener una clave secreta. En un escenario real, esta clave se generaría una vez y se almacenaría de forma segura.
    * **Definición del mensaje original:** Se define un mensaje de ejemplo que queremos cifrar.
    * **Cifrado del mensaje:** Se llama a `cifrar_mensaje()` para cifrar el mensaje original utilizando la clave generada.
    * **Descifrado del mensaje:** Se llama a `descifrar_mensaje()` para intentar descifrar el mensaje cifrado utilizando la misma clave.
    * **Verificación:** Se compara el mensaje original con el mensaje descifrado para asegurar que el proceso de cifrado y descifrado fue exitoso.

**Conceptos Clave de Criptografía Simétrica:**

* **Una única clave:** La misma clave (`clave_secreta`) se utiliza tanto para cifrar como para descifrar el mensaje. Esta es la característica fundamental de la criptografía simétrica.
* **Secreto compartido:** Para que la comunicación sea segura, la clave secreta debe ser conocida únicamente por las partes que se comunican. Si un tercero obtiene la clave, podrá cifrar y descifrar los mensajes.
* **Algoritmo de cifrado:** En este ejemplo, la biblioteca `Fernet` internamente utiliza un algoritmo de cifrado simétrico fuerte (AES) junto con mecanismos de autenticación.
* **Proceso de cifrado:** El mensaje original se transforma en un formato ilegible (el mensaje cifrado) utilizando la clave y el algoritmo.
* **Proceso de descifrado:** El mensaje cifrado se revierte a su forma original (el mensaje descifrado) utilizando la misma clave y el algoritmo inverso.

**Consideraciones Importantes en la Criptografía Simétrica:**

* **Gestión de claves:** El mayor desafío en la criptografía simétrica es la gestión segura de las claves. ¿Cómo se genera, almacena y comparte la clave de forma segura entre las partes?
* **Seguridad de la clave:** Si la clave se ve comprometida, toda la comunicación cifrada con esa clave también se verá comprometida.
* **Escalabilidad:** En sistemas con muchos participantes, gestionar una clave secreta única para cada par de comunicantes puede volverse complejo.







### Criptografía Asimétrica

En criptografía asimétrica se utiliza un **par de claves**: una clave pública \( K_{pub} \) para cifrar y una clave privada \( K_{priv} \) para descifrar:

#### Fórmulas en LaTeX:

```latex
% Cifrado asimétrico
C = E_{K_{pub}}(M)

% Descifrado asimétrico
M = D_{K_{priv}}(C)
```

#### Donde:
- \( K_{pub} \): clave pública del receptor
- \( K_{priv} \): clave privada del receptor
- \( E_{K_{pub}} \): función de cifrado con clave pública
- \( D_{K_{priv}} \): función de descifrado con clave privada
______________________________




_______________________
> Stallings, W. (2023). *Cryptography and network security: Principles and practice* (8th ed.). Pearson.  

> Paar, C., & Pelzl, J. (2010). *Understanding cryptography: A textbook for students and practitioners*. Springer.  

> Schneier, B. (2015). *Applied cryptography: Protocols, algorithms, and source code in C* (20th Anniversary ed.). Wiley.  

> National Institute of Standards and Technology (NIST). (2022). *Post-Quantum Cryptography: NIST's Approach and Evaluation Criteria*. U.S. Department of Commerce.  

> Menezes, A. J., van Oorschot, P. C., & Vanstone, S. A. (2018). *Handbook of applied cryptography*. CRC Press.  




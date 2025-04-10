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

# Criptografía Simétrica

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

- **Importación de la biblioteca `cryptography`:**
    ```python
    from cryptography.fernet import Fernet
    ```
    * Importamos la clase `Fernet` del módulo `fernet` dentro de la biblioteca `cryptography`. `Fernet` es una implementación de cifrado simétrico autenticado. Esto significa que no solo cifra los datos, sino que también asegura su integridad (que no han sido alterados). Utiliza el algoritmo de cifrado AES (Advanced Encryption Standard) en modo CBC (Cipher Block Chaining) con un HMAC (Hash-based Message Authentication Code) para la autenticación.

- **Función `generar_clave()`:**
    ```python
    def generar_clave():
        """Genera una clave secreta para el cifrado simétrico."""
        clave = Fernet.generate_key()
        return clave
    ```
    * Esta función utiliza el método estático `Fernet.generate_key()` para crear una nueva clave secreta.
    * **Importante:** Esta clave debe mantenerse en secreto y compartirse de forma segura entre las partes que necesitan cifrar y descifrar mensajes. Generar una nueva clave para cada comunicación o sesión sensible es una buena práctica de seguridad.
    * La clave generada es una secuencia de bytes.

- **Función `cifrar_mensaje(mensaje, clave)`:**
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

- **Función `descifrar_mensaje(mensaje_cifrado, clave)`:**
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

- **Bloque `if __name__ == "__main__":`:**
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

# Criptografía Asimétrica

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

En la práctica, a menudo se utiliza una combinación de criptografía simétrica y asimétrica. Por ejemplo, se puede usar la criptografía asimétrica para intercambiar de forma segura una clave de sesión simétrica, y luego usar esa clave simétrica para cifrar la mayor parte de la comunicación debido a su mayor eficiencia.

```python
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization

def generar_claves_rsa():
    """Genera un par de claves RSA (pública y privada)."""
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    public_key = private_key.public_key()
    return private_key, public_key

def cifrar_mensaje_publico(mensaje, public_key):
    """Cifra un mensaje utilizando la clave pública del receptor."""
    mensaje_bytes = mensaje.encode('utf-8')
    ciphertext = public_key.encrypt(
        mensaje_bytes,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return ciphertext

def descifrar_mensaje_privado(ciphertext, private_key):
    """Descifra un mensaje utilizando la clave privada del receptor."""
    plaintext_bytes = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    plaintext = plaintext_bytes.decode('utf-8')
    return plaintext

def serializar_clave_publica(public_key):
    """Serializa la clave pública a formato PEM para su almacenamiento o envío."""
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    return public_pem

def cargar_clave_publica_serializada(public_pem):
    """Carga una clave pública desde su representación serializada en formato PEM."""
    public_key = serialization.load_pem_public_key(
        public_pem,
    )
    return public_key

if __name__ == "__main__":
    # 1. Generar un par de claves RSA (clave privada y clave pública)
    private_key_alice, public_key_alice = generar_claves_rsa()
    print("Par de claves RSA de Alicia generado.")

    # 2. Alicia quiere enviar un mensaje secreto a Bob. Primero, Bob le envía su clave pública.
    # (Simulamos la clave pública de Bob)
    private_key_bob, public_key_bob = generar_claves_rsa()
    print("\nPar de claves RSA de Bob generado (simulado).")
    public_key_bob_serializada = serializar_clave_publica(public_key_bob)
    print("\nClave pública de Bob (serializada):\n", public_key_bob_serializada.decode())

    # 3. Alicia recibe la clave pública de Bob y la carga (si estuviera serializada)
    clave_publica_bob_cargada = cargar_clave_publica_serializada(public_key_bob_serializada)

    # 4. Alicia escribe su mensaje
    mensaje_secreto = "Hola Bob, este es un mensaje confidencial de Alicia."
    print(f"\nMensaje de Alicia: {mensaje_secreto}")

    # 5. Alicia cifra el mensaje utilizando la clave pública de Bob
    mensaje_cifrado = cifrar_mensaje_publico(mensaje_secreto, clave_publica_bob_cargada)
    print(f"\nMensaje cifrado por Alicia para Bob: {mensaje_cifrado}")

    # 6. Alicia envía el mensaje cifrado a Bob.

    # 7. Bob recibe el mensaje cifrado y lo descifra utilizando su clave privada
    mensaje_descifrado = descifrar_mensaje_privado(mensaje_cifrado, private_key_bob)
    print(f"\nMensaje descifrado por Bob: {mensaje_descifrado}")

    # 8. Verificar que el mensaje original y el mensaje descifrado son iguales
    if mensaje_secreto == mensaje_descifrado:
        print("\n¡El cifrado y descifrado asimétrico se realizaron correctamente!")
    else:
        print("\n¡Hubo un error en el cifrado o descifrado asimétrico!")

    # Ejemplo de cómo Alicia podría firmar un mensaje (esto va más allá del cifrado, pero es importante en asimétrica)
    from cryptography.hazmat.primitives.asymmetric import signature
    signer = private_key_alice.signer(
        signature.PSS(
            mgf=signature.MGF1(hashes.SHA256()),
            salt_length=signature.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    mensaje_a_firmar = "Este mensaje está firmado por Alicia."
    mensaje_a_firmar_bytes = mensaje_a_firmar.encode('utf-8')
    signer.update(mensaje_a_firmar_bytes)
    firma = signer.finalize()
    print(f"\nFirma de Alicia: {firma}")

    # Bob (o cualquier persona con la clave pública de Alicia) puede verificar la firma
    verifier = public_key_alice.verifier(
        signature.PSS(
            mgf=signature.MGF1(hashes.SHA256()),
            salt_length=signature.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    verifier.update(mensaje_a_firmar_bytes)
    try:
        verifier.verify(firma)
        print("\n¡La firma de Alicia es válida!")
    except Exception as e:
        print("\n¡La firma NO es válida!")
```

**Explicación**

- **Importación de módulos:**
    ```python
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.asymmetric import rsa, padding
    from cryptography.hazmat.primitives import serialization, asymmetric
    ```
    * Importamos los módulos necesarios de la biblioteca `cryptography` para realizar operaciones de hashing (SHA256), generación de claves RSA, esquemas de relleno (OAEP), y serialización de claves.

- **Función `generar_claves_rsa()`:**
    ```python
    def generar_claves_rsa():
        """Genera un par de claves RSA (pública y privada)."""
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
        )
        public_key = private_key.public_key()
        return private_key, public_key
    ```
    * Esta función genera un par de claves RSA.
    * `rsa.generate_private_key()` crea la clave privada. Los parámetros son:
        * `public_exponent`: Un número entero público utilizado en el algoritmo RSA (generalmente se usa 65537).
        * `key_size`: El tamaño de la clave en bits. 2048 bits es un tamaño común y considerado seguro para muchas aplicaciones. Claves más grandes son más seguras pero también más lentas.
    * `private_key.public_key()` deriva la clave pública correspondiente a la clave privada generada.
    * La función devuelve ambos objetos de clave.

- **Función `cifrar_mensaje_publico(mensaje, public_key)`:**
    ```python
    def cifrar_mensaje_publico(mensaje, public_key):
        """Cifra un mensaje utilizando la clave pública del receptor."""
        mensaje_bytes = mensaje.encode('utf-8')
        ciphertext = public_key.encrypt(
            mensaje_bytes,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return ciphertext
    ```
    * Esta función cifra un mensaje utilizando la clave pública del destinatario.
    * Primero, el mensaje se codifica a bytes.
    * `public_key.encrypt()` realiza el cifrado. Los parámetros son:
        * El mensaje en bytes.
        * Un esquema de relleno (`padding`). **Es crucial utilizar un esquema de relleno seguro en la criptografía asimétrica para prevenir ciertos tipos de ataques.** Aquí se utiliza `padding.OAEP` (Optimal Asymmetric Encryption Padding), que es un esquema recomendado.
            * `mgf`: Mask Generation Function (función de generación de máscara). `MGF1` es una función basada en un hash.
            * `algorithm`: El algoritmo hash utilizado por MGF1 y para el propio OAEP (en este caso, SHA256).
            * `label`: Un parámetro opcional que puede ser utilizado para contextos específicos. Aquí se establece en `None`.
    * La función devuelve el `ciphertext` (texto cifrado) en formato de bytes.

- **Función `descifrar_mensaje_privado(ciphertext, private_key)`:**
    ```python
    def descifrar_mensaje_privado(ciphertext, private_key):
        """Descifra un mensaje utilizando la clave privada del receptor."""
        plaintext_bytes = private_key.decrypt(
            ciphertext,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        plaintext = plaintext_bytes.decode('utf-8')
        return plaintext
    ```
    * Esta función descifra el mensaje cifrado utilizando la clave privada correspondiente.
    * `private_key.decrypt()` realiza el descifrado. **Es importante utilizar el mismo esquema de relleno (`padding.OAEP` con los mismos parámetros) que se usó durante el cifrado.**
    * El resultado es el `plaintext_bytes` (texto plano en bytes), que luego se decodifica a una cadena de texto.

- **Funciones para serializar y cargar la clave pública:**
    ```python
    def serializar_clave_publica(public_key):
        """Serializa la clave pública a formato PEM para su almacenamiento o envío."""
        public_pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        return public_pem

    def cargar_clave_publica_serializada(public_pem):
        """Carga una clave pública desde su representación serializada en formato PEM."""
        public_key = serialization.load_pem_public_key(
            public_pem,
        )
        return public_key
    ```
    * En la criptografía asimétrica, la clave pública a menudo necesita ser compartida. Para esto, se serializa a un formato estándar. El formato PEM (Privacy-Enhanced Mail) es un formato común que codifica la clave en Base64 y la envuelve con encabezados y pies de página (e.g., `-----BEGIN PUBLIC KEY-----`).
    * `public_key.public_bytes()` serializa la clave pública.
        * `encoding=serialization.Encoding.PEM`: Especifica el formato PEM.
        * `format=serialization.PublicFormat.SubjectPublicKeyInfo`: Especifica la estructura de la información de la clave pública.
    * `serialization.load_pem_public_key()` carga una clave pública desde su representación PEM.

- **Bloque `if __name__ == "__main__":`:**
    * Este bloque simula un escenario donde Alicia quiere enviar un mensaje secreto a Bob.
    * **Generación de claves:** Se genera un par de claves para Alicia y un par (simulado) para Bob. En un escenario real, cada persona generaría su propio par de claves.
    * **Intercambio de clave pública:** Se simula el envío de la clave pública de Bob a Alicia (a través de un canal que no necesita ser secreto). La clave pública puede compartirse libremente.
    * **Cifrado:** Alicia cifra su mensaje utilizando la clave pública de Bob.
    * **Envío:** El mensaje cifrado se envía a Bob (este mensaje no puede ser leído por nadie más que tenga la clave privada de Bob).
    * **Descifrado:** Bob recibe el mensaje cifrado y lo descifra utilizando su clave privada.
    * **Verificación:** Se comprueba si el mensaje original y el descifrado coinciden.

- **Ejemplo de Firma Digital (opcional pero importante en asimétrica):**
    * Se incluye un ejemplo básico de cómo Alicia podría firmar un mensaje utilizando su clave privada y cómo Bob (o cualquier persona con la clave pública de Alicia) podría verificar esa firma.
    * La firma digital proporciona autenticidad (prueba de que el mensaje proviene de Alicia) e integridad (prueba de que el mensaje no ha sido alterado).
    * Se utiliza el esquema de firma PSS (Probabilistic Signature Scheme) con SHA256.

**Conceptos Clave de Criptografía Asimétrica:**

* **Par de claves:** Se utilizan dos claves relacionadas pero diferentes: una clave pública y una clave privada.
* **Clave pública:** Se puede compartir libremente con cualquier persona. Se utiliza para cifrar mensajes destinados al propietario de la clave privada correspondiente.
* **Clave privada:** Debe mantenerse en secreto por su propietario. Se utiliza para descifrar los mensajes que fueron cifrados con su clave pública.
* **Relación matemática:** Existe una relación matemática compleja entre la clave pública y la privada, de tal manera que es computacionalmente inviable derivar la clave privada a partir de la pública.
* **Cifrado:** Para enviar un mensaje confidencial a alguien, el remitente cifra el mensaje con la *clave pública* del destinatario.
* **Descifrado:** Solo el propietario de la *clave privada* correspondiente puede descifrar el mensaje.

**Ventajas de la Criptografía Asimétrica:**

* **No se requiere un secreto compartido previo:** Las partes pueden comunicarse de forma segura sin haber intercambiado una clave secreta previamente. La clave pública se puede compartir a través de canales no seguros.
* **Habilita la firma digital:** La clave privada se puede usar para firmar digitalmente documentos, proporcionando autenticidad e integridad.

**Desventajas de la Criptografía Asimétrica:**
* **Más lenta que la criptografía simétrica:** Las operaciones de cifrado y descifrado suelen ser significativamente más lentas que las de los algoritmos simétricos.
* **Tamaño de clave más grande:** Las claves asimétricas suelen ser mucho más grandes que las claves simétricas para lograr un nivel de seguridad comparable.


# Algoritmos de hashing

Este ejemplo proporciona una comprensión fundamental de los algoritmos de hashing y cómo se pueden utilizar en Python para verificar la integridad de los datos.


```python
import hashlib

def calcular_hash(mensaje, algoritmo='sha256'):
    """Calcula el hash de un mensaje utilizando el algoritmo especificado."""
    mensaje_bytes = mensaje.encode('utf-8')  # Codificar el mensaje a bytes
    if algoritmo == 'sha256':
        hash_object = hashlib.sha256(mensaje_bytes)
    elif algoritmo == 'sha1':
        hash_object = hashlib.sha1(mensaje_bytes)
    elif algoritmo == 'md5':
        hash_object = hashlib.md5(mensaje_bytes)
    else:
        raise ValueError(f"Algoritmo de hash no soportado: {algoritmo}")
    hash_hex = hash_object.hexdigest()
    return hash_hex

def verificar_integridad(mensaje, hash_esperado, algoritmo='sha256'):
    """Calcula el hash del mensaje y lo compara con el hash esperado."""
    hash_calculado = calcular_hash(mensaje, algoritmo)
    if hash_calculado == hash_esperado:
        print("¡Integridad verificada! El mensaje no ha sido alterado.")
        return True
    else:
        print("¡Alerta! El mensaje ha sido alterado.")
        print(f"Hash calculado: {hash_calculado}")
        print(f"Hash esperado: {hash_esperado}")
        return False

if __name__ == "__main__":
    mensaje_original = "Este es un mensaje importante."

    # 1. Calcular el hash SHA-256 del mensaje original
    hash_sha256 = calcular_hash(mensaje_original, 'sha256')
    print(f"Mensaje original: {mensaje_original}")
    print(f"Hash SHA-256: {hash_sha256}")

    # 2. Calcular el hash SHA-1 del mensaje original
    hash_sha1 = calcular_hash(mensaje_original, 'sha1')
    print(f"Hash SHA-1: {hash_sha1}")

    # 3. Calcular el hash MD5 del mensaje original
    hash_md5 = calcular_hash(mensaje_original, 'md5')
    print(f"Hash MD5: {hash_md5}")

    print("\n--- Verificación de Integridad ---")

    # 4. Simular la recepción del mensaje y su hash esperado
    mensaje_recibido = "Este es un mensaje importante."
    hash_esperado_sha256 = hash_sha256

    # 5. Verificar la integridad del mensaje recibido
    verificar_integridad(mensaje_recibido, hash_esperado_sha256, 'sha256')

    # 6. Simular la alteración del mensaje
    mensaje_alterado = "Este es un mensaje importante, con un cambio."

    # 7. Verificar la integridad del mensaje alterado con el hash original
    verificar_integridad(mensaje_alterado, hash_esperado_sha256, 'sha256')
```

**Explicación:**

- **Importación de la biblioteca `hashlib`:**
    ```python
    import hashlib
    ```
    * Importamos la biblioteca `hashlib`, que proporciona acceso a varios algoritmos de hashing seguros (como SHA-256, SHA-1, MD5, etc.).

- **Función `calcular_hash(mensaje, algoritmo='sha256')`:**
    ```python
    def calcular_hash(mensaje, algoritmo='sha256'):
        """Calcula el hash de un mensaje utilizando el algoritmo especificado."""
        mensaje_bytes = mensaje.encode('utf-8')  # Codificar el mensaje a bytes
        if algoritmo == 'sha256':
            hash_object = hashlib.sha256(mensaje_bytes)
        elif algoritmo == 'sha1':
            hash_object = hashlib.sha1(mensaje_bytes)
        elif algoritmo == 'md5':
            hash_object = hashlib.md5(mensaje_bytes)
        else:
            raise ValueError(f"Algoritmo de hash no soportado: {algoritmo}")
        hash_hex = hash_object.hexdigest()
        return hash_hex
    ```
    * Esta función toma un `mensaje` (string) y un `algoritmo` de hashing (por defecto 'sha256') como entrada.
    * **Codificación a bytes:** Primero, el `mensaje` se codifica a una secuencia de bytes utilizando `mensaje.encode('utf-8')`. Los algoritmos de hashing operan sobre datos binarios.
    * **Selección del algoritmo:** Se utiliza una estructura `if-elif-else` para seleccionar el algoritmo de hashing deseado de la biblioteca `hashlib` basándose en el parámetro `algoritmo`.
        * `hashlib.sha256(mensaje_bytes)`: Crea un objeto hash utilizando el algoritmo SHA-256.
        * `hashlib.sha1(mensaje_bytes)`: Crea un objeto hash utilizando el algoritmo SHA-1.
        * `hashlib.md5(mensaje_bytes)`: Crea un objeto hash utilizando el algoritmo MD5.
        * Si se proporciona un algoritmo no soportado, se levanta una excepción `ValueError`.
    * **Cálculo del hash:** El método `hash_object.update(mensaje_bytes)` (aunque no se usa explícitamente aquí, es la forma general de procesar datos en bloques) procesa los bytes del mensaje. Luego, `hash_object.digest()` devuelve el valor hash en formato de bytes (binario).
    * **Representación hexadecimal:** El método `hash_object.hexdigest()` convierte el valor hash binario en una cadena de caracteres hexadecimal, que es una representación más común y legible de un hash.
    * La función devuelve la cadena hexadecimal del hash.

- **Función `verificar_integridad(mensaje, hash_esperado, algoritmo='sha256')`:**
    ```python
    def verificar_integridad(mensaje, hash_esperado, algoritmo='sha256'):
        """Calcula el hash del mensaje y lo compara con el hash esperado."""
        hash_calculado = calcular_hash(mensaje, algoritmo)
        if hash_calculado == hash_esperado:
            print("¡Integridad verificada! El mensaje no ha sido alterado.")
            return True
        else:
            print("¡Alerta! El mensaje ha sido alterado.")
            print(f"Hash calculado: {hash_calculado}")
            print(f"Hash esperado: {hash_esperado}")
            return False
    ```
    * Esta función se utiliza para verificar si un mensaje recibido ha sido alterado durante la transmisión o el almacenamiento.
    * Toma el `mensaje` recibido, el `hash_esperado` (calculado previamente del mensaje original), y el `algoritmo` de hashing utilizado.
    * Calcula el hash del `mensaje` recibido utilizando la misma función `calcular_hash()` y el mismo algoritmo.
    * Compara el `hash_calculado` con el `hash_esperado`.
    * Si los hashes coinciden, significa que el mensaje probablemente no ha sido modificado, y la función imprime un mensaje de verificación y devuelve `True`.
    * Si los hashes no coinciden, indica que el mensaje ha sido alterado, y la función imprime una alerta, muestra ambos hashes para comparación, y devuelve `False`.

- **Bloque `if __name__ == "__main__":`:**
    * Este bloque de código se ejecuta cuando el script se ejecuta directamente.
    * **Mensaje original:** Se define un mensaje de ejemplo.
    * **Cálculo de hashes:** Se llama a la función `calcular_hash()` para obtener los hashes del mensaje original utilizando diferentes algoritmos (SHA-256, SHA-1, MD5). Se imprimen los resultados.
    * **Verificación de integridad:**
        * Se simula la recepción del mismo mensaje original y se utiliza el hash SHA-256 calculado previamente como el `hash_esperado`. Se llama a `verificar_integridad()` para confirmar que el mensaje no ha sido alterado.
        * Se simula la recepción de un mensaje ligeramente alterado. Se utiliza el mismo `hash_esperado` (del mensaje original) para verificar la integridad. En este caso, los hashes no coincidirán, indicando la alteración.

**Conceptos Clave de Algoritmos de Hashing Ilustrados:**

* **Función unidireccional (One-way function):** Los algoritmos de hashing están diseñados para ser funciones unidireccionales. Esto significa que es fácil calcular el hash de un mensaje, pero es computacionalmente extremadamente difícil (prácticamente imposible) realizar el proceso inverso: encontrar el mensaje original a partir de su hash.
* **Tamaño fijo de salida:** Independientemente del tamaño del mensaje de entrada, el valor hash resultante siempre tendrá una longitud fija para un algoritmo específico. Por ejemplo, un hash SHA-256 siempre tendrá 256 bits (64 caracteres hexadecimales).
* **Determinismo:** Para un mismo mensaje de entrada y el mismo algoritmo de hashing, el valor hash resultante siempre será el mismo.
* **Resistencia a colisiones:** Un buen algoritmo de hashing debe ser resistente a colisiones. Una colisión ocurre cuando dos mensajes diferentes producen el mismo valor hash. Idealmente, la probabilidad de encontrar una colisión debe ser extremadamente baja.

**Algoritmos de Hashing Comunes (ejemplificados):**

* **SHA-256 (Secure Hash Algorithm 256-bit):** Es un algoritmo de hashing criptográfico ampliamente utilizado y considerado seguro para muchas aplicaciones. Produce un hash de 256 bits.
* **SHA-1 (Secure Hash Algorithm 1):** Es un algoritmo más antiguo que SHA-256. Si bien fue ampliamente utilizado, se ha demostrado que es vulnerable a ataques de colisión y ya no se recomienda para nuevas aplicaciones donde la resistencia a colisiones es crítica. Produce un hash de 160 bits.
* **MD5 (Message Digest Algorithm 5):** Es otro algoritmo de hashing más antiguo. También se ha demostrado que es vulnerable a ataques de colisión y no se recomienda para aplicaciones de seguridad donde la integridad es primordial. Produce un hash de 128 bits.

**Usos Comunes de los Algoritmos de Hashing:**

* **Verificación de integridad de datos:** Asegurar que un archivo no ha sido modificado durante la descarga, la transmisión o el almacenamiento.
* **Almacenamiento seguro de contraseñas:** En lugar de almacenar las contraseñas en texto plano, se almacenan sus hashes. Cuando un usuario intenta iniciar sesión, se calcula el hash de la contraseña ingresada y se compara con el hash almacenado.
* **Firmas digitales:** Los hashes se utilizan para crear firmas digitales eficientes. En lugar de firmar un documento completo, se firma su hash.
* **Tablas hash:** En estructuras de datos para una búsqueda eficiente.
* **Criptomonedas:** Muchos sistemas de criptomonedas utilizan algoritmos de hashing para diversas operaciones, como la creación de nuevos bloques (minería).

**Consideraciones Importantes:**

* **Elección del algoritmo:** La elección del algoritmo de hashing depende de los requisitos de seguridad de la aplicación. Para aplicaciones donde la resistencia a colisiones es crítica, se deben utilizar algoritmos más seguros como SHA-256 (o incluso SHA-3).
* **Salting (para contraseñas):** Cuando se utiliza hashing para almacenar contraseñas, es crucial utilizar "salts" (valores aleatorios únicos para cada contraseña) para dificultar los ataques de diccionario y las tablas rainbow. El salt se concatena con la contraseña antes de aplicar el hash.

_______________________
> Stallings, W. (2023). *Cryptography and network security: Principles and practice* (8th ed.). Pearson.  

> Paar, C., & Pelzl, J. (2010). *Understanding cryptography: A textbook for students and practitioners*. Springer.  

> Schneier, B. (2015). *Applied cryptography: Protocols, algorithms, and source code in C* (20th Anniversary ed.). Wiley.  

> National Institute of Standards and Technology (NIST). (2022). *Post-Quantum Cryptography: NIST's Approach and Evaluation Criteria*. U.S. Department of Commerce.  

> Menezes, A. J., van Oorschot, P. C., & Vanstone, S. A. (2018). *Handbook of applied cryptography*. CRC Press.  




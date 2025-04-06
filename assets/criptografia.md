# Conceptos básicos de criptografía

Las características y diferencias entre criptografía y encriptación:

| Característica/Aspecto        | Criptografía                                                                                                                               | Encriptación (Cifrado)                                                                                                                               |
| :----------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Naturaleza** | Ciencia y arte de proteger la información mediante códigos. Disciplina teórica y práctica.                                                  | Proceso específico dentro de la criptografía. Acción de transformar datos legibles a ilegibles.                                                    |
| **Alcance** | Amplio. Incluye el diseño y análisis de algoritmos para confidencialidad, integridad, autenticación, no repudio y más.                      | Limitado a la transformación de datos para asegurar la confidencialidad.                                                                           |
| **Objetivo Principal** | Seguridad integral de la información, abordando diversos aspectos como secreto, autenticidad, integridad y disponibilidad.                  | Ocultar el contenido de la información para que solo pueda ser comprendida por quienes poseen la clave correcta.                                  |
| **Procesos Involucrados** | Diseño de algoritmos (cifrado, hash, firma digital, etc.), análisis de seguridad, gestión de claves, protocolos criptográficos.             | Aplicación de un algoritmo de cifrado específico utilizando una clave para transformar el texto plano en texto cifrado.                               |
| **Resultados/Productos** | Algoritmos criptográficos, protocolos de seguridad (TLS/SSL, IPsec), sistemas de gestión de claves, firmas digitales, funciones hash, entre otros. | Texto cifrado (ciphertext) que resulta de la aplicación del algoritmo de cifrado al texto plano.                                                     |
| **Funciones Clave** | Confidencialidad, integridad, autenticación, no repudio, control de acceso.                                                               | Principalmente confidencialidad (ocultar la información).                                                                                             |
| **Nivel de Abstracción** | Nivel conceptual y teórico, abarcando los fundamentos matemáticos y los principios de seguridad.                                         | Nivel práctico y operativo, la implementación concreta de un algoritmo para cifrar datos.                                                             |
| **Analogía** | El campo de la "seguridad informática".                                                                                                     | Una "cerradura" o un "candado" que protege un objeto o información.                                                                                 |
| **Ejemplos de Técnicas/Áreas** | Cifrado simétrico y asimétrico, funciones hash, firmas digitales, criptografía cuántica, esteganografía (aunque relacionada, no es puramente criptografía). | AES, DES, RSA (para cifrado), cifrado de disco, cifrado de comunicaciones (HTTPS).                                                                 |
| **Dependencia** | La encriptación es una herramienta *dentro* del campo de la criptografía.                                                                 | La encriptación se basa en los principios y algoritmos desarrollados por la criptografía.                                                              |

Nota: la **criptografía** es el paraguas que engloba todas las técnicas y principios para la seguridad de la información, mientras que la **encriptación** es una técnica específica dentro de la criptografía que se enfoca en hacer que la información sea ininteligible sin la clave adecuada.

## Encriptación

La encriptación de datos es una técnica esencial en la seguridad de la información, que consiste en transformar la información de manera que solo pueda ser interpretada por aquellos que tienen la clave de desencriptación adecuada. Este proceso es crucial en la actualidad debido a la creciente cantidad de datos sensibles que se almacenan y transmiten a través de medios electrónicos. En este ensayo, exploraremos los fundamentos de la encriptación de datos, su importancia y algunos de los métodos comunes de encriptación.

La encriptación de datos tiene una historia larga y rica, que se remonta a la antigüedad. A lo largo de los siglos, diversas civilizaciones han desarrollado métodos de cifrado para proteger la confidencialidad de la información, desde el cifrado César utilizado por Julio César hasta las máquinas Enigma utilizadas durante la Segunda Guerra Mundial. Sin embargo, en la era digital, la encriptación se ha vuelto más sofisticada y se basa en algoritmos matemáticos avanzados.

La importancia de la encriptación de datos es evidente en varios contextos:

- Confidencialidad de la información: La encriptación garantiza que solo las personas autorizadas puedan acceder a la información. Esto es crucial en la protección de datos personales, como números de tarjetas de crédito, contraseñas y registros médicos.

- Integridad de los datos: La encriptación no solo protege los datos de acceso no autorizado, sino que también asegura que los datos no se hayan modificado durante la transmisión o el almacenamiento. Cualquier alteración en los datos encriptados sería evidente al intentar desencriptarlos.

- Autenticación: La encriptación también se utiliza en la autenticación de usuarios y sistemas. Las firmas digitales, que son esencialmente formas de encriptación, se utilizan para verificar la identidad de las partes involucradas en una comunicación.

Existen dos tipos principales de encriptación: encriptación simétrica y encriptación asimétrica.

- Encriptación simétrica: En este enfoque, la misma clave se utiliza para encriptar y desencriptar los datos. Aunque es eficiente y rápida, el desafío principal es la distribución segura de la clave entre las partes autorizadas.

- Encriptación asimétrica: En este caso, se utilizan dos claves diferentes: una clave pública para encriptar y una clave privada para desencriptar. La clave pública se puede compartir ampliamente, mientras que la clave privada debe mantenerse en secreto. Esto resuelve el problema de la distribución de claves, pero es más lento que la encriptación simétrica.

Un ejemplo común de encriptación en la vida cotidiana es el protocolo HTTPS utilizado para proteger las transacciones en línea. Cuando ingresas información en un sitio web seguro, los datos se encriptan antes de enviarse al servidor. El navegador y el servidor intercambian claves públicas y privadas para asegurarse de que solo el servidor pueda desencriptar los datos.

La encriptación de datos desempeña un papel fundamental en la ciberseguridad y la protección de la privacidad en la era digital. A medida que la cantidad de información sensible que circula en línea continúa creciendo, la encriptación seguirá siendo esencial para garantizar que nuestros datos estén seguros y protegidos. La evolución constante de los métodos de encriptación y la investigación en ciberseguridad son esenciales para mantenernos un paso adelante de las amenazas en constante cambio.


### Cifrado 

En su forma más básica, el cifrado es el proceso de codificación de datos sencibles, por medio de claves emisora y receptora.
 
Una clave de cifrado es una colección de algoritmos diseñados para ser totalmente únicos, estos son capaces de codificar y descifrar datos, esencialmente desbloqueando la información y volviéndola a datos legibles. Quien esté encriptando los datos poseerá la clave que bloquea los datos y hará 'copias' y las pasará a las personas relevantes que requieren acceso. Este proceso se llama criptografía de clave pública. La criptografía informática o criptográfica, que es una forma de encriptación, se volvió significativa durante la segunda guerra mundial con las fuerzas militares en toda Europa encargadas de romper el código Enigma de Alemania.

#### Métodos de encriptación: ¿Cómo funciona el cifrado?

- En la práctica, envía un mensaje usando un servicio de mensajería cifrado (por ejemplo, WhatsApp), el servicio envuelve el mensaje en código, lo codifica y crea una clave de cifrado. Solo puede ser desbloqueado por el destinatario del mensaje.

- El cifrado digital es complicado y es por eso que se considera difícil de descifrar. Para reforzar esa protección, se crea un nuevo conjunto de algoritmos de encriptación cada vez que dos teléfonos inteligentes comienzan a comunicarse entre sí. Es posible usar el cifrado de extremo a extremo, el servicio de notificación en WhatsApp ahora admite este tipo de encriptación.

- El cifrado de extremo a extremo se refiere al proceso de codificación (emisor - receptor) de cierta información para que solo el remitente y el receptor puedan verla.

- El cifrado simétrico es el proceso de utilizar la misma clave (dos claves que son idénticas) para encriptar y descifrar datos. Esto significa que dos o más partes tendrán acceso a la misma clave, lo que para algunos es un gran inconveniente, a pesar de que el algoritmo matemático para proteger los datos es prácticamente imposible de descifrar. Las preocupaciones de las personas a menudo aterrizan con los comportamientos de aquellos con acceso a la clave compartida.

Por el contrario, el cifrado asimétrico se refiere al método de utilizar un par de claves: una para encriptar los datos y la otra para descifrarla.

#### Cómo funciona la encriptación

- Los datos no encriptados, a menudo denominados texto sin formato, se encriptan usando un algoritmo de encriptación y una clave de cifrado, este proceso genera textos cifrados que solo se pueden ver en su forma original si se descifran con la clave correcta. El descifrado es simplemente el inverso del cifrado, siguiendo los mismos pasos, pero invirtiendo el orden en que se aplican las claves, los algoritmos de encriptación más utilizados actualmente se dividen en dos categorías: simétricos y asimétricos.
 
- Los cifrados de clave simétrica, también conocidos como "clave secreta", usan una sola clave, a veces denominada secreto compartido porque el sistema que realiza el cifrado debe compartirlo con cualquier entidad que intente descifrar los datos cifrados. El cifrado de clave simétrica más utilizado es el Estándar de cifrado avanzado (AES), que fue diseñado para proteger la información clasificada del gobierno.

- El cifrado de clave simétrica suele ser mucho más rápido que el cifrado asimétrico, pero el remitente debe intercambiar la clave utilizada para cifrar los datos con el destinatario antes de que el destinatario pueda realizar el descifrado en el texto cifrado. La necesidad de distribuir y gestionar de forma segura grandes cantidades de claves significa que la mayoría de los procesos criptográficos utilizan un algoritmo simétrico para cifrar de manera eficiente los datos, pero utilizan un algoritmo asimétrico para intercambiar de forma segura la clave secreta.

- La criptografía asimétrica, también conocida como criptografía de clave pública, utiliza dos claves diferentes pero vinculadas matemáticamente, una pública y otra privada. La clave pública se puede compartir con todos, mientras que la clave privada debe mantenerse en secreto. El algoritmo de encriptación RSA es el algoritmo de clave pública más utilizado, en parte porque las claves pública y privada pueden encriptar un mensaje; la tecla opuesta a la utilizada para encriptar un mensaje se usa para descifrarla. Este atributo proporciona un método para asegurar no solo la confidencialidad, sino también la integridad, autenticidad e irreprochabilidad de las comunicaciones electrónicas y los datos en reposo a través del uso de firmas digitales.

#### Beneficios del cifrado

El objetivo principal del cifrado es proteger la confidencialidad de los datos digitales almacenados en sistemas informáticos o transmitidos a través de Internet o cualquier otra red informática. 

Los algoritmos de cifrados modernos también desempeñan un papel vital en la seguridad de los sistemas de TI y las comunicaciones, ya que pueden proporcionar no solo la confidencialidad, sino también los siguientes elementos clave de seguridad:

- Autenticación: el origen de un mensaje puede ser verificado.
- Integridad: prueba de que el contenido de un mensaje no se ha modificado desde que se envió.
- No repudio: el remitente de un mensaje no puede denegar el envío del mensaje.

#### Tipos de cifrado

La criptografía de clave pública tradicional depende de las propiedades de los números primos grandes y la dificultad computacional de factorizar esos primos. La criptografía de curva elíptica (ECC) permite otro tipo de criptografía de clave pública que depende de las propiedades de la ecuación de curva elíptica; los algoritmos criptográficos resultantes pueden ser más rápidos y eficientes y pueden producir niveles comparables de seguridad con claves criptográficas más cortas. Como resultado, los algoritmos ECC a menudo se implementan en IoT y otros productos con recursos informáticos limitados.

Algunas aplicaciones pregonan el uso del cifrado de extremo a extremo (E2EE) para garantizar que los datos enviados entre dos partes no puedan ser vistos por un atacante que intercepte el canal de comunicación. El uso de un circuito de comunicación encriptado, como lo proporciona Transport Layer Security (TLS) entre el cliente web y el software del servidor web, no siempre es suficiente para asegurar E2EE; típicamente, el contenido real que se está transmitiendo se cifra mediante el software del cliente antes de pasarlo a un cliente web, y el destinatario descifra únicamente.
 
Las aplicaciones de mensajería que proporcionan E2EE incluyen WhatsApp de Facebook y la señal de Open Whisper Systems. Los usuarios de Facebook Messenger también pueden recibir mensajes E2EE con la opción "Conversaciones secretas".

#### Funciones hash criptográficas

El cifrado suele ser una función bidireccional, lo que significa que el mismo algoritmo puede utilizarse para cifrar texto plano y descifrar texto cifrado. Una función hash criptográfica se puede ver como un tipo de función unidireccional para el cifrado, lo que significa que la salida de la función no se puede invertir fácilmente para recuperar la entrada original. Las funciones hash se usan comúnmente en aspectos de la seguridad para generar firmas digitales y verificaciones de integridad de datos. Toman un archivo electrónico, un mensaje o un bloque de datos y generan una huella digital breve del contenido llamado resumen del mensaje o valor hash. Las propiedades clave de una función de hash criptográfica segura son:

- La longitud de salida es pequeña en comparación con la entrada
- La computación es rápida y eficiente para cualquier entrada
- Cualquier cambio en la entrada afecta a los bits de salida
- Valor unidireccional: la entrada no puede determinarse a partir de la salida
- Fuerte resistencia a la colisión: dos entradas diferentes no pueden crear la misma salida

Los cifrados en las funciones hash están optimizados para el hash, usan claves y bloques grandes, pueden cambiar las claves de manera eficiente en cada bloque y han sido diseñados y analizados para resistir ataques relacionados. 
Los sistemas de cifrado de uso general utilizados para el cifrado tienden a tener diferentes objetivos de diseño. 
Por ejemplo, el cifrado AES de bloque de clave simétrica también podría usarse para generar valores hash, pero sus tamaños de clave y bloque lo hacen no trivial e ineficiente.

#### Algoritmos criptográficos 

- RC4: Es un algoritmo de cifrado de flujo simétrico que se utiliza en protocolos de seguridad como TLS. Fue diseñado por Ron Rivest en 1987.

- RCS: No es un algoritmo de cifrado conocido. Podría ser un error tipográfico o referirse a otro concepto.

- RC6 (128 bits): Es un cifrador de bloque simétrico que utiliza claves de 128 bits. Fue diseñado por RSA Security y es una extensión de RC5.

- RSA (Rivets Shamir Adelman) internet encryption:RSA es un algoritmo de cifrado asimétrico que utiliza un par de claves: una pública y una privada. Fue inventado por Ron Rivest, Adi Shamir y Leonard Adleman en 1977. Se utiliza para encriptar y firmar digitalmente la información en internet.

- Secure Hashing Algorithms (SHA):Los algoritmos de hash seguro son funciones criptográficas que toman un conjunto de datos y devuelven un valor de longitud fija, conocido como resumen o hash. Estos son cruciales para garantizar la integridad de los datos.

- SHA1 160 bits digest MDS:SHA-1 es un algoritmo de hash con un resumen de 160 bits. "Digest" se refiere al valor de hash resultante. MDS significa "Message Digest Secure", y SHA-1 utiliza el método Merkle-Damgard para generar el resumen.

- SHA2 256 32-bit words and SHA5S12 use 64-bits:SHA-2 es una familia de algoritmos de hash seguro. SHA-256 utiliza palabras de 32 bits para procesar los datos. "SHA5S12" no parece ser un algoritmo conocido; podría ser un error tipográfico o referirse a otro concepto.

- SHA3 XO red: SHA-3 es otra familia de algoritmos de hash seguro. "XO red" no es un término reconocido en este contexto. Puede ser un error tipográfico o requerir más contexto.

- SSH (secure shell):SSH es un protocolo de red que proporciona un entorno seguro para la comunicación en una red no segura. Se utiliza para acceder a sistemas remotos de forma segura.

- Public Key Infrastructure (PKI):PKI es un conjunto de políticas, procesos y tecnologías que aseguran la comunicación electrónica segura mediante el uso de claves públicas y privadas.

- Certificate management system:Un sistema de gestión de certificados es una infraestructura que emite, gestiona y revoca certificados digitales utilizados en la autenticación y cifrado.

- Digital certificates:Certificados digitales son documentos electrónicos que autentican la identidad de una entidad en línea y facilitan la comunicación segura mediante el uso de claves públicas y privadas.

- Validation Authority (VA):Una Autoridad de Validación es una entidad que verifica la autenticidad de la información presentada para la emisión de certificados digitales.

- Certificate Authority (CA):Una Autoridad de Certificación emite y gestiona certificados digitales, confirmando la autenticidad de la entidad asociada a la clave pública contenida en el certificado.

- End user:El usuario final es la persona que utiliza un sistema o servicio después de que todos los componentes se hayan implementado y configurado.

- Registration Authority (RA):Una Autoridad de Registro es responsable de verificar la identidad de individuos o entidades antes de que se emitan certificados digitales por parte de una Autoridad de Certificación.

- SSL (secure socket layer):SSL fue el precursor de TLS y es un protocolo de seguridad que garantiza la privacidad y la integridad de los datos transmitidos a través de internet.

- RSA Asymmetric (public key) encryption: RSA, como se mencionó anteriormente, es un algoritmo de cifrado asimétrico que utiliza un par de claves, una pública y otra privada.

- TLS (transport layer security) secure connections:TLS es el sucesor de SSL y es un protocolo criptográfico que garantiza la seguridad de las comunicaciones en una red, como internet. Se utiliza para establecer conexiones seguras.

#### Validación de algoritmos criptográficos

NIST mantiene un registro de las validaciones realizadas en todos los programas de estándar criptográficos anteriores y actuales. A medida que las nuevas implementaciones de algoritmo son validadas por NIST y CSEC, se agregan a la lista de validación de algoritmo apropiada, tomando en cuenta lo siguiente:

- [ ] AES Advanced Encryption Standard
- [ ] CCM Certificación Certified in Congress Management
- [ ] Component 
- [ ] DRBG Deterministic Random Bit Generator
- [ ] DSA Digital Signature Algorithm
- [ ] ECDSA Elliptic Curve Digital Signature Algorithm
- [ ] HMAC Hash-based Message Authentication Code
- [ ] KAS KAFIRIM CIA
- [ ] KDF Certificado de electrodomésticos 
- [ ] RSA Rivest, Shamir y Adleman
- [ ] SHA-3 Secure Hash Algorithm - Agencia de seguridad de la NASA
- [ ] SHS Siemens Health Service
- [ ] Skipjack Algoritmo privado de National Security Agency (NSA)
- [ ] TDES Algortmo de IBM

Lista de algoritmos retirados.

- [ ] DES (1977 - April 1996) 
- [ ] DES 
- [ ] FIPS 171 (ANSI X9.17 Key Management) 
- [ ] MAC 
- [ ] RNG 

______________________________

La criptografía es un campo amplio y complejo, y su implementación en un lenguaje de programación como C++ puede variar según el algoritmo que desees utilizar. Aquí te proporcionaré un ejemplo simple de cifrado y descifrado utilizando el algoritmo AES (Advanced Encryption Standard) mediante la biblioteca Crypto++.

Crear un archivo .cpp con el siguiente contenido. 

```
#include <iostream>
#include <iomanip>
#include <cryptopp/aes.h>
#include <cryptopp/modes.h>
#include <cryptopp/filters.h>

using namespace CryptoPP;

// Función para cifrar utilizando AES
std::string EncryptAES(const std::string& plainText, const byte key[ AES::DEFAULT_KEYLENGTH ], const byte iv[ AES::BLOCKSIZE ]) {
    std::string cipherText;

    try {
        CBC_Mode< AES >::Encryption encryption;
        encryption.SetKeyWithIV(key, AES::DEFAULT_KEYLENGTH, iv);

        StringSource(plainText, true,
            new StreamTransformationFilter(encryption,
                new StringSink(cipherText)
            )
        );
    }
    catch(const CryptoPP::Exception& e) {
        std::cerr << "Error en cifrado: " << e.what() << std::endl;
        exit(1);
    }

    return cipherText;
}

// Función para descifrar utilizando AES
std::string DecryptAES(const std::string& cipherText, const byte key[ AES::DEFAULT_KEYLENGTH ], const byte iv[ AES::BLOCKSIZE ]) {
    std::string decryptedText;

    try {
        CBC_Mode< AES >::Decryption decryption;
        decryption.SetKeyWithIV(key, AES::DEFAULT_KEYLENGTH, iv);

        StringSource(cipherText, true,
            new StreamTransformationFilter(decryption,
                new StringSink(decryptedText)
            )
        );
    }
    catch(const CryptoPP::Exception& e) {
        std::cerr << "Error en descifrado: " << e.what() << std::endl;
        exit(1);
    }

    return decryptedText;
}

int main() {
    // Clave y IV (Vector de Inicialización) predefinidos (¡NO usar estos en producción!)
    byte key[ AES::DEFAULT_KEYLENGTH ] = {'1','2','3','4','5','6','7','8','9','0','1','2','3','4','5','6'};
    byte iv[ AES::BLOCKSIZE ] = {'1','2','3','4','5','6','7','8','9','0','1','2','3','4','5','6','7','8','9','0','1','2','3','4','5','6','7','8','9','0','1'};

    std::string mensajeOriginal = "Hola, mundo. Este es un ejemplo de cifrado AES con Crypto++.";
    std::cout << "Mensaje original: " << mensajeOriginal << std::endl;

    // Cifrar el mensaje
    std::string mensajeCifrado = EncryptAES(mensajeOriginal, key, iv);
    std::cout << "Mensaje cifrado: " << mensajeCifrado << std::endl;

    // Descifrar el mensaje
    std::string mensajeDescifrado = DecryptAES(mensajeCifrado, key, iv);
    std::cout << "Mensaje descifrado: " << mensajeDescifrado << std::endl;

    return 0;
}
```

Este ejemplo proporciona una introducción básica al concepto de hashing y su aplicación en la seguridad de contraseñas. En un curso de ciberseguridad, se profundizaría en diferentes algoritmos hash, sus fortalezas y debilidades, ataques comunes (como ataques de diccionario y rainbow tables), y técnicas para fortalecer la seguridad de las contraseñas (como el uso de "salt").


```python
import hashlib

def generar_hash(texto):
  """
  Genera un hash SHA-256 para el texto proporcionado.

  Args:
    texto: La cadena de texto para la que se generará el hash.

  Returns:
    Una cadena hexadecimal que representa el hash del texto.
    Devuelve None si el texto no es una cadena.
  """
  if not isinstance(texto, str):
    print("Error: El input debe ser una cadena de texto.")
    return None

  # Codificamos el texto a bytes, ya que las funciones hash trabajan con bytes.
  texto_bytes = texto.encode('utf-8')

  # Creamos un objeto hash utilizando el algoritmo SHA-256.
  hasher = hashlib.sha256()

  # Actualizamos el objeto hash con los bytes del texto.
  hasher.update(texto_bytes)

  # Obtenemos el hash resultante en formato hexadecimal.
  hash_hexadecimal = hasher.hexdigest()

  return hash_hexadecimal

def verificar_password(password_ingresada, hash_almacenado):
  """
  Verifica si el hash de la contraseña ingresada coincide con el hash almacenado.

  Args:
    password_ingresada: La contraseña que el usuario ha ingresado.
    hash_almacenado: El hash previamente calculado y almacenado de la contraseña correcta.

  Returns:
    True si los hashes coinciden, False en caso contrario.
  """
  hash_ingresado = generar_hash(password_ingresada)
  if hash_ingresado is None:
    return False  # Indica un error al generar el hash

  return hash_ingresado == hash_almacenado

# Ejemplo de uso:
password_secreta = "MiPasswordSeguro123"

# Generamos el hash de la contraseña secreta y lo almacenamos (simuladamente).
hash_almacenado = generar_hash(password_secreta)
print(f"El hash de la contraseña '{password_secreta}' es: {hash_almacenado}")
print("-" * 30)

# Simulación de un intento de inicio de sesión:
password_intento1 = "MiPasswordSeguro123"
if verificar_password(password_intento1, hash_almacenado):
  print(f"La contraseña '{password_intento1}' es correcta.")
else:
  print(f"La contraseña '{password_intento1}' es incorrecta.")

password_intento2 = "MiPasswordFalsa"
if verificar_password(password_intento2, hash_almacenado):
  print(f"La contraseña '{password_intento2}' es correcta.")
else:
  print(f"La contraseña '{password_intento2}' es incorrecta.")
```

**Explicación:**

1.  **`import hashlib`:**
    * Esta línea importa el módulo `hashlib` de Python. Este módulo proporciona varias funciones para realizar operaciones de hashing seguro (funciones resumen).

2.  **`def generar_hash(texto):`:**
    * Define una función llamada `generar_hash` que toma un argumento `texto` (la cadena de la cual queremos obtener el hash).
    * **`if not isinstance(texto, str):`**: Realiza una verificación de tipo para asegurarse de que la entrada sea una cadena de texto. Si no lo es, imprime un mensaje de error y devuelve `None`. Esto es importante para la robustez del código.
    * **`texto_bytes = texto.encode('utf-8')`:**
        * Las funciones hash en `hashlib` trabajan con datos binarios (bytes), no directamente con cadenas de texto.
        * `texto.encode('utf-8')` convierte la cadena de texto `texto` a una secuencia de bytes utilizando la codificación UTF-8, que es una codificación de caracteres ampliamente utilizada y compatible.
    * **`hasher = hashlib.sha256()`:**
        * Crea un objeto hash utilizando el algoritmo SHA-256. SHA-256 es una función hash criptográfica que produce un hash de 256 bits (64 caracteres hexadecimales). Es considerada segura para muchas aplicaciones.
        * Existen otros algoritmos hash disponibles en `hashlib` como `md5`, `sha1`, `sha512`, etc., pero SHA-256 es una buena opción por su equilibrio entre seguridad y rendimiento.
    * **`hasher.update(texto_bytes)`:**
        * Alimenta los datos (en forma de bytes) al objeto hash. Puedes llamar a `update()` varias veces para procesar grandes cantidades de datos en bloques.
    * **`hash_hexadecimal = hasher.hexdigest()`:**
        * `hasher.hexdigest()` calcula el hash final de los datos proporcionados y lo devuelve como una cadena de caracteres hexadecimales. Esta representación hexadecimal es común para mostrar y almacenar hashes.
    * **`return hash_hexadecimal`:**
        * La función devuelve la cadena hexadecimal que representa el hash del texto de entrada.

3.  **`def verificar_password(password_ingresada, hash_almacenado):`:**
    * Define una función llamada `verificar_password` que toma dos argumentos:
        * `password_ingresada`: La contraseña que el usuario está intentando ingresar.
        * `hash_almacenado`: El hash de la contraseña correcta que se ha guardado previamente (por ejemplo, en una base de datos).
    * **`hash_ingresado = generar_hash(password_ingresada)`:**
        * Llama a la función `generar_hash` para calcular el hash de la contraseña que el usuario ha ingresado.
    * **`if hash_ingresado is None:`**: Verifica si hubo un error al generar el hash (por ejemplo, si la `password_ingresada` no era una cadena). Si hay un error, devuelve `False`.
    * **`return hash_ingresado == hash_almacenado`:**
        * Compara el `hash_ingresado` (el hash de la contraseña que el usuario proporcionó) con el `hash_almacenado`.
        * Si los dos hashes son idénticos, significa que la contraseña ingresada coincide con la contraseña original (o al menos produce el mismo hash), y la función devuelve `True`.
        * Si los hashes no coinciden, la función devuelve `False`.

4.  **Ejemplo de Uso:**
    * **`password_secreta = "MiPasswordSeguro123"`:** Define una variable que representa una contraseña secreta.
    * **`hash_almacenado = generar_hash(password_secreta)`:** Genera el hash de esta contraseña secreta y lo guarda en la variable `hash_almacenado`. En un sistema real, este `hash_almacenado` se guardaría en una base de datos, no la contraseña en texto plano.
    * **`print(...)`:** Imprime el hash generado para mostrarlo.
    * **`print("-" * 30)`:** Imprime una línea separadora para mejorar la legibilidad.
    * **Simulación de intentos de inicio de sesión:**
        * Se definen dos intentos de contraseña (`password_intento1` y `password_intento2`).
        * Se llama a la función `verificar_password` para cada intento, comparando el hash del intento con el `hash_almacenado`.
        * Se imprime un mensaje indicando si la contraseña es correcta o incorrecta basándose en el resultado de la comparación de hashes.

* **Almacenamiento Seguro de Contraseñas:** En lugar de almacenar las contraseñas de los usuarios en texto plano (lo cual sería extremadamente peligroso), los sistemas seguros almacenan los hashes de las contraseñas. Cuando un usuario intenta iniciar sesión, el sistema calcula el hash de la contraseña ingresada y lo compara con el hash almacenado. Si coinciden, la contraseña es considerada correcta sin que el sistema nunca haya necesitado conocer la contraseña en texto plano.
* **Integridad de Datos:** Las funciones hash también se utilizan para verificar la integridad de los datos. Si se calcula el hash de un archivo y luego se modifica el archivo, al volver a calcular el hash, el valor será diferente. Esto permite detectar si un archivo ha sido alterado.
* **Firmas Digitales:** Las funciones hash son un componente clave en las firmas digitales, donde se utiliza el hash de un documento para crear una firma única que puede ser verificada.

**Conceptos Clave en Hashing Criptográfico:**

* **Unidireccionalidad:** Es computacionalmente inviable (prácticamente imposible) obtener el texto original (la "preimagen") a partir de su hash.
* **Resistencia a Colisiones:** Es difícil encontrar dos entradas diferentes que produzcan el mismo valor hash. Aunque las colisiones teóricamente existen para todas las funciones hash, para las funciones hash criptográficas fuertes, encontrarlas es extremadamente difícil.
* **Determinismo:** Para una misma entrada, la función hash siempre producirá la misma salida.


______________________________

> Susilo Yuda Irawan, Agung & Pratama, Adi & Antono, Ryan. (2021). RC4 Cryptography Implementation Analysis on Text Data. JURNAL SISFOTEK GLOBAL. 11. 115. 10.38101/sisfotek.v11i2.408. 

> Okyere, Rufus. (2022). Efficient Data Hiding Scheme Using Steganography and Cryptography Technique. Advances in Multidisciplinary and scientific Research Journal Publication. 10. 25-32. 10.22624/AIMS/DIGITAL/V10N4P4. 

> Khan, Razib & Haque, Rakib Ul & Syeed, Mahbubul & Uddin, Faisal. (2023). Towards Convergence of Data Federation and Cryptography based Solution for Ensuring Secure Interoperability in Mobile Financial Services. 

> Rodrigues, Gustavo & Braga, Alexandre & Dahab, Ricardo. (2023). Detecting Cryptography Misuses With Machine Learning: Graph Embeddings, Transfer Learning and Data Augmentation in Source Code Related Tasks. IEEE Transactions on Reliability. PP. 1-12. 10.1109/TR.2023.3237849. 

> Hossain, Md Al Amin. (2022). ENHANCING PERFORMANCE OF DATA PRIVACY ON THE CLOUD USING CRYPTOGRAPHY WITH STEGANOGRAPHY IN PYTHON. 

> Hegde, Nagaratna & Deepthi, P.. (2023). Securing Data in Internet of Things (IoT) Using Elliptic Curve Cryptography. 10.1007/978-981-19-8086-2_95. 

> Surendiran, R. & Raja, K. (2023). A Fog Computing Approach for Securing IoT Devices Data using DNA-ECC Cryptography. 1. 10-16. 

> Varghese, Fredy & Sasikala, P.. (2023). A Detailed Review Based on Secure Data Transmission Using Cryptography and Steganography. Wireless Personal Communications. 129. 1-28. 10.1007/s11277-023-10183-z. 

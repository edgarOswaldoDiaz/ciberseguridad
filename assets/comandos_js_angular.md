# Angular.JS

Angular CLI Cheat Sheet
Instalación de Angular CLI
Instala Angular CLI globalmente para usar los comandos en cualquier directorio.
npm install -g @angular/cli

Creación de un nuevo proyecto
Crea una nueva aplicación Angular con la estructura básica.
ng new nombre-proyecto

Opciones comunes:

--style=scss : Usa SCSS como preprocesador de estilos.
--routing : Incluye un módulo de enrutamiento.
--minimal : Crea un proyecto con configuración mínima.

Estructura de comandos básicos
Ejecuta comandos dentro del directorio del proyecto.
Iniciar el servidor de desarrollo
Inicia un servidor local con recarga automática.
ng serve

Opciones:

--open o -o : Abre el navegador automáticamente.
--port=4200 : Especifica el puerto del servidor.
--host=0.0.0.0 : Permite acceso desde otras máquinas en la red.

Generar componentes, servicios, módulos, etc.
Genera archivos para diferentes elementos de Angular.
ng generate <tipo> <nombre>

Alias corto: ng g <tipo> <nombre>
Tipos comunes:

Componente: ng g component nombre-componente
Servicio: ng g service nombre-servicio
Módulo: ng g module nombre-modulo
Directiva: ng g directive nombre-directiva
Pipe: ng g pipe nombre-pipe
Guard: ng g guard nombre-guard
Interface: ng g interface nombre-interfaz
Clase: ng g class nombre-clase

Opciones:

--module=nombre-modulo : Especifica el módulo donde se registra el componente.
--skip-tests : Omite la generación de archivos de prueba.
--flat : Genera el archivo sin crear un directorio adicional.

Compilar el proyecto
Compila el proyecto para producción.
ng build

Opciones:

--prod : Compila en modo producción (optimizado).
--base-href=/ruta/ : Especifica la URL base para la aplicación.
--output-path=dist/ : Define la carpeta de salida.

Ejecutar pruebas
Corre las pruebas unitarias con Karma.
ng test

Opciones:

--code-coverage : Genera un informe de cobertura de código.
--watch=false : Ejecuta las pruebas una sola vez sin recarga automática.

Corre las pruebas de extremo a extremo (E2E) con Cypress o Protractor (dependiendo de la versión).
ng e2e

Actualizar Angular
Actualiza las dependencias de Angular y el CLI.
ng update

Opciones:

@angular/cli : Actualiza el CLI.
@angular/core : Actualiza el framework Angular.
--all : Actualiza todas las dependencias.

Gestión de dependencias
Instala una librería o paquete.
npm install nombre-paquete

O agrega un paquete específico a Angular.
ng add nombre-paquete

Ejemplo: ng add @angular/material para instalar Angular Material.
Generar documentación
Genera documentación para el proyecto con Compodoc.
ng doc

Nota: Requiere instalar @compodoc/compodoc previamente.
Internacionalización (i18n)
Extrae cadenas para traducción.
ng extract-i18n

Opciones:

--out-file=nombre-archivo : Especifica el archivo de salida para las traducciones.

Configuración del proyecto
Edita el archivo de configuración angular.json para personalizar opciones de compilación, pruebas, etc.
Comandos de linting
Verifica el código en busca de errores y problemas de estilo.
ng lint

Opciones:

--fix : Corrige automáticamente los errores detectados.

Generar biblioteca
Crea una biblioteca reutilizable.
ng generate library nombre-libreria

Ejecutar comandos personalizados
Ejecuta scripts definidos en package.json.
npm run nombre-script

Estructura de un proyecto Angular

src/app/: Contiene los componentes, servicios, módulos y otros elementos principales.
angular.json: Configuración del proyecto.
package.json: Dependencias y scripts.
tsconfig.json: Configuración de TypeScript.
src/index.html: Archivo HTML principal.
src/main.ts: Punto de entrada de la aplicación.

Buenas prácticas

Usa nombres descriptivos para componentes, servicios, etc.
Organiza los módulos por funcionalidad.
Mantén los componentes pequeños y reutilizables.
Usa ng generate para mantener la consistencia en la estructura del proyecto.
Ejecuta ng lint regularmente para mantener el código limpio.

_______________________

> By CISO oswaldo.diaz

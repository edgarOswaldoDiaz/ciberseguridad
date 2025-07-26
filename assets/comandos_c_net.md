# C# .NET 
---

## Gestión del SDK y herramientas

| Comando                           | Descripción                                       | Ejemplo                              |
| --------------------------------- | ------------------------------------------------- | ------------------------------------ |
| `dotnet --info`                   | Muestra información del SDK y runtimes instalados | `dotnet --info`                      |
| `dotnet --list-sdks`              | Lista los SDKs instalados                         | `dotnet --list-sdks`                 |
| `dotnet --list-runtimes`          | Lista los runtimes instalados                     | `dotnet --list-runtimes`             |
| `dotnet tool install -g <tool>`   | Instala globalmente una herramienta .NET          | `dotnet tool install -g dotnet-ef`   |
| `dotnet tool update -g <tool>`    | Actualiza una herramienta global                  | `dotnet tool update -g dotnet-ef`    |
| `dotnet tool uninstall -g <tool>` | Desinstala una herramienta global                 | `dotnet tool uninstall -g dotnet-ef` |

---

## Creación y configuración de proyectos

| Comando                               | Descripción                                  | Ejemplo                                    |
| ------------------------------------- | -------------------------------------------- | ------------------------------------------ |
| `dotnet new <plantilla>`              | Crea un nuevo proyecto a partir de plantilla | `dotnet new console -n MiApp`              |
| `dotnet new sln -n MiSolucion`        | Crea una solución vacía                      | `dotnet new sln -n MiSolucion`             |
| `dotnet sln add <proyecto.csproj>`    | Agrega un proyecto a la solución             | `dotnet sln add src/MiApp/MiApp.csproj`    |
| `dotnet sln remove <proyecto.csproj>` | Elimina un proyecto de la solución           | `dotnet sln remove src/MiApp/MiApp.csproj` |

---

## Compilar, ejecutar y limpiar

| Comando          | Descripción                       | Ejemplo                          |
| ---------------- | --------------------------------- | -------------------------------- |
| `dotnet restore` | Restaura paquetes NuGet faltantes | `dotnet restore`                 |
| `dotnet build`   | Compila el proyecto/solución      | `dotnet build MiSolucion.sln`    |
| `dotnet run`     | Ejecuta la aplicación (solo SDK)  | `dotnet run --project src/MiApp` |
| `dotnet clean`   | Elimina binarios y artefactos     | `dotnet clean`                   |

---

## Testing

| Comando                | Descripción                        | Ejemplo                                |
| ---------------------- | ---------------------------------- | -------------------------------------- |
| `dotnet test`          | Ejecuta pruebas en el proyecto     | `dotnet test tests/MiApp.Tests`        |
| `dotnet test --filter` | Ejecuta pruebas que cumplan filtro | `dotnet test --filter "Category=Unit"` |

---

## Publicación y empaquetado

| Comando                               | Descripción                      | Ejemplo                                 |
| ------------------------------------- | -------------------------------- | --------------------------------------- |
| `dotnet publish -c Release -o <ruta>` | Publica la aplicación (Release)  | `dotnet publish -c Release -o publish/` |
| `dotnet pack -c Release`              | Genera un paquete NuGet (.nupkg) | `dotnet pack -c Release`                |

---

## Gestión de paquetes NuGet

| Comando                           | Descripción                                | Ejemplo                                 |
| --------------------------------- | ------------------------------------------ | --------------------------------------- |
| `dotnet add package <paquete>`    | Agrega paquete NuGet al proyecto           | `dotnet add package Newtonsoft.Json`    |
| `dotnet remove package <paquete>` | Elimina paquete NuGet del proyecto         | `dotnet remove package Newtonsoft.Json` |
| `dotnet restore`                  | Restaura paquetes definidos en el proyecto | `dotnet restore`                        |

---

## Entity Framework Core

> **Requisito**: tener instalado el tool `dotnet-ef` (ver sección 1)

| Comando                                             | Descripción                                            | Ejemplo                                                                      |
| --------------------------------------------------- | ------------------------------------------------------ | ---------------------------------------------------------------------------- |
| `dotnet ef migrations add <NombreMigracion>`        | Crea una nueva migración                               | `dotnet ef migrations add InitialCreate`                                     |
| `dotnet ef migrations remove`                       | Elimina la última migración                            | `dotnet ef migrations remove`                                                |
| `dotnet ef database update [<NombreMigracion>]`     | Aplica migraciones pendientes o hasta una específica   | `dotnet ef database update`<br>`dotnet ef database update v1`                |
| `dotnet ef dbcontext scaffold <cadena> <proveedor>` | Genera modelos desde DB existing (reverse engineering) | `dotnet ef dbcontext scaffold "..." Microsoft.EntityFrameworkCore.SqlServer` |

---

## Compilador C# y MSBuild

| Comando                           | Descripción                                  | Ejemplo                                           |
| --------------------------------- | -------------------------------------------- | ------------------------------------------------- |
| `csc <archivos>.cs -out:<exe>`    | Compila archivos C# sin usar el SDK .NET     | `csc Program.cs -out:MiApp.exe`                   |
| `msbuild <solucion.sln> /t:Build` | Construye solución o proyecto con MSBuild    | `msbuild MiSolucion.sln /p:Configuration=Release` |
| `msbuild <.csproj> /t:Clean`      | Limpia artefactos de un proyecto con MSBuild | `msbuild MiApp.csproj /t:Clean`                   |

______________________

> By CISO oswaldo.diaz 

# Spring Framework

## **Spring Boot CLI Comandos**

```bash
# Crear proyecto Spring Boot
spring init --dependencies=web,data-jpa,h2 my-project

# Crear proyecto con estructura específica
spring init --dependencies=web --build=gradle --java-version=11 my-app

# Ejecutar aplicación
spring run Application.java
```

## **Maven Comandos**

```bash
# Crear proyecto Spring Boot
mvn archetype:generate -DgroupId=com.example -DartifactId=my-app

# Compilar proyecto
mvn compile

# Ejecutar tests
mvn test

# Empaquetar aplicación
mvn package

# Ejecutar aplicación
mvn spring-boot:run

# Limpiar proyecto
mvn clean

# Instalar dependencias
mvn install
```

## **Gradle Comandos**

```bash
# Compilar proyecto
./gradlew build

# Ejecutar aplicación
./gradlew bootRun

# Ejecutar tests
./gradlew test

# Limpiar proyecto
./gradlew clean

# Generar wrapper
gradle wrapper
```

## **Anotaciones Core**

### Componentes
```java
@Component          // Componente genérico
@Service            // Capa de servicio
@Repository         // Capa de acceso a datos
@Controller         // Capa de presentación (MVC)
@RestController     // Controlador REST
@Configuration      // Clase de configuración
```

### Inyección de Dependencias
```java
@Autowired          // Inyección automática
@Qualifier("beanName") // Especificar bean
@Primary            // Bean primario
@Lazy               // Inicialización perezosa
@Value("${property}") // Inyectar valor de properties
```

### Configuración de Beans
```java
@Bean               // Declarar bean
@Scope("singleton") // Alcance del bean
@PostConstruct      // Método después de inicialización
@PreDestroy         // Método antes de destrucción
```

## **Web - Controladores**

### Mapeo de URLs
```java
@RequestMapping("/api")           // Mapeo general
@GetMapping("/users")             // GET
@PostMapping("/users")            // POST
@PutMapping("/users/{id}")        // PUT
@DeleteMapping("/users/{id}")     // DELETE
@PatchMapping("/users/{id}")      // PATCH
```

### Parámetros
```java
@RequestParam("name") String name     // Parámetro query
@PathVariable("id") Long id           // Parámetro path
@RequestBody User user                // Cuerpo de la petición
@RequestHeader("Authorization") String auth // Header
@CookieValue("JSESSIONID") String cookie    // Cookie
```

### Respuestas
```java
@ResponseBody       // Devolver cuerpo en respuesta
@ResponseStatus(HttpStatus.CREATED) // Código HTTP
@CrossOrigin        // CORS
```

## **Data Access - JPA/Hibernate**

### Entidades
```java
@Entity             // Entidad JPA
@Table(name = "users") // Tabla
@Id                 // Clave primaria
@GeneratedValue(strategy = GenerationType.IDENTITY) // Auto-generado
@Column(name = "username") // Columna
@Transient          // No persistente
@Temporal(TemporalType.TIMESTAMP) // Fecha
```

### Relaciones
```java
@OneToOne
@OneToMany
@ManyToOne
@ManyToMany
@JoinColumn(name = "user_id") // Clave foránea
@JoinTable( // Tabla intermedia
    name = "user_roles",
    joinColumns = @JoinColumn(name = "user_id"),
    inverseJoinColumns = @JoinColumn(name = "role_id")
)
```

### Repositorios
```java
@Repository
public interface UserRepository extends JpaRepository<User, Long> {
    // Métodos personalizados
    List<User> findByUsername(String username);
    User findByEmail(String email);
    
    @Query("SELECT u FROM User u WHERE u.age > ?1")
    List<User> findUsersOlderThan(int age);
}
```

## **Validación**

```java
@Valid              // Validar objeto
@NotNull            // No nulo
@NotEmpty           // No vacío
@NotBlank           // No blanco
@Size(min=2, max=50) // Tamaño
@Email              // Email válido
@Min(18) @Max(100)  // Rango numérico
@Pattern(regexp="...") // Expresión regular
```

## **Seguridad - Spring Security**

```java
@EnableWebSecurity  // Habilitar seguridad
@PreAuthorize("hasRole('ADMIN')") // Autorización método
@Secured("ROLE_ADMIN") // Rol requerido
```

## **Transacciones**

```java
@Transactional      // Transacción
@Transactional(readOnly = true) // Solo lectura
@Transactional(rollbackFor = Exception.class) // Rollback
```

## **REST Client**

```java
@FeignClient(name = "user-service", url = "http://localhost:8080")
public interface UserServiceClient {
    @GetMapping("/api/users/{id}")
    User getUser(@PathVariable("id") Long id);
}
```

## ⚙**Configuración**

### Properties
```properties
# application.properties
server.port=8080
spring.datasource.url=jdbc:mysql://localhost:3306/mydb
spring.jpa.hibernate.ddl-auto=update
logging.level.com.example=DEBUG
```

### YAML
```yaml
# application.yml
server:
  port: 8080
spring:
  datasource:
    url: jdbc:mysql://localhost:3306/mydb
  jpa:
    hibernate:
      ddl-auto: update
logging:
  level:
    com.example: DEBUG
```

## **Testing**

```java
@SpringBootTest      // Test de integración
@WebMvcTest         // Test de controlador
@DataJpaTest        // Test de repositorio
@MockBean           // Mock de bean
@Test               // Método de test
@BeforeEach         // Antes de cada test
@AfterEach          // Después de cada test
```

## **Actuator Endpoints**

```properties
# application.properties
management.endpoints.web.exposure.include=*
management.endpoint.health.show-details=always
```

```bash
# Endpoints comunes
/actuator/health     # Estado de la aplicación
/actuator/info       # Información de la app
/actuator/metrics    # Métricas
/actuator/env        # Variables de entorno
/actuator/loggers    # Configuración de logs
/actuator/beans      # Beans registrados
```

## **Docker**

```dockerfile
# Dockerfile
FROM openjdk:11-jre-slim
COPY target/app.jar app.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "/app.jar"]
```

```bash
# Construir imagen
docker build -t my-app .

# Ejecutar contenedor
docker run -p 8080:8080 my-app
```

## **Comandos Útiles de Desarrollo**

```bash
# Generar proyecto con Spring Boot CLI
spring init --dependencies=web,jpa,mysql --build=maven my-spring-app

# Ejecutar con perfil específico
mvn spring-boot:run -Dspring-boot.run.profiles=dev

# Crear ejecutable JAR
mvn clean package

# Ejecutar JAR
java -jar target/my-app.jar --spring.profiles.active=prod
```

## **Dependencias Comunes Maven**

```xml
<!-- Web -->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
</dependency>

<!-- JPA -->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-jpa</artifactId>
</dependency>

<!-- MySQL -->
<dependency>
    <groupId>mysql</groupId>
    <artifactId>mysql-connector-java</artifactId>
</dependency>

<!-- Security -->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-security</artifactId>
</dependency>

<!-- Test -->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-test</artifactId>
    <scope>test</scope>
</dependency>
```

## **Perfiles de Ejecución**

```bash
# Activar perfil
java -jar app.jar --spring.profiles.active=prod

# Variables de entorno
export SPRING_PROFILES_ACTIVE=dev
export SERVER_PORT=9090
```

---

**💡 Tips Rápidos:**
- Usa `@SpringBootApplication` para combinar `@Configuration`, `@EnableAutoConfiguration`, y `@ComponentScan`
- `application-{profile}.properties` para configuraciones por perfil
- `@ConditionalOnProperty` para beans condicionales
- `@Scheduled` para tareas programadas
- `@Async` para métodos asíncronos

___________________________

> By CISO oswaldo.diaz 

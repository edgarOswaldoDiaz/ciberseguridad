# HTML (HyperText Markup Language)

## Estructura básica del documento

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Título de la página</title>
  <!-- Enlaces a estilos, iconos, meta adicionales… -->
</head>
<body>
  <!-- Contenido visible -->
</body>
</html>
```

* `<!DOCTYPE html>`: declara HTML5.
* `<html lang="…">`: elemento raíz; `lang` indica idioma.
* `<head>`: metadatos (charset, título, viewport…).
* `<body>`: contenido de la página.

---

## Metadatos y enlaces

* `<meta charset="UTF-8">`: codificación de caracteres.
* `<meta name="viewport" content="…">`: responsive.
* `<link rel="stylesheet" href="…">`: hoja de estilos CSS.
* `<link rel="icon" href="icono.png">`: icono de la pestaña.
* `<script src="…" defer>`: enlaza un script externo.
* `<style>`: estilos internos.

---

## Elementos de secciones y agrupación

* `<header>…</header>`: encabezado de página o sección.
* `<nav>…</nav>`: navegación principal o secundaria.
* `<main>…</main>`: contenido principal (único por documento).
* `<section>…</section>`: sección genérica con tema propio.
* `<article>…</article>`: contenido autónomo (artículo, entrada).
* `<aside>…</aside>`: contenido complementario (barras laterales).
* `<footer>…</footer>`: pie de página o de sección.

---

## Texto y formatos

| Etiqueta         | Descripción                                     |
| ---------------- | ----------------------------------------------- |
| `<h1>`–`<h6>`    | Encabezados de niveles 1 a 6                    |
| `<p>`            | Párrafo                                         |
| `<blockquote>`   | Cita en bloque                                  |
| `<q>`            | Cita corta                                      |
| `<ul>`           | Lista desordenada                               |
| `<ol>`           | Lista ordenada                                  |
| `<li>`           | Ítem de lista                                   |
| `<dl>`           | Lista de definiciones                           |
| `<dt>`           | Término de definición                           |
| `<dd>`           | Descripción de término                          |
| `<strong>`       | Texto con fuerte énfasis (\~negrita)            |
| `<em>`           | Texto enfatizado (\~cursiva)                    |
| `<small>`        | Texto de menor importancia                      |
| `<mark>`         | Texto resaltado                                 |
| `<del>`          | Texto eliminado                                 |
| `<ins>`          | Texto insertado                                 |
| `<sub>`, `<sup>` | Subíndice / Superíndice                         |
| `<code>`         | Fragmento de código                             |
| `<pre>`          | Texto preformateado (respeta espacios y saltos) |
| `<span>`         | Contenedor en línea genérico                    |
| `<div>`          | Contenedor en bloque genérico                   |

---

## Enlaces e imágenes

```html
<a href="https://ejemplo.com" target="_blank" rel="noopener">Visitar sitio</a>
<img src="imagen.jpg" alt="Descripción" width="300" height="200">
<picture>
  <source srcset="img.webp" type="image/webp">
  <img src="img.jpg" alt="…">
</picture>
<figure>
  <img src="…">
  <figcaption>Pie de figura</figcaption>
</figure>
```

* `<a>`: enlace; atributos `href`, `target`, `rel`.
* `<img>`: imagen; atributos `src`, `alt`, `width`, `height`.
* `<picture>`/`<source>`: imágenes adaptativas.
* `<figure>` + `<figcaption>`: imagen con pie.

---

## Multimedia y elementos embebidos

```html
<video src="video.mp4" controls autoplay muted loop width="640"></video>
<audio src="audio.mp3" controls></audio>
<iframe src="https://www.youtube.com/embed/…" width="560" height="315"></iframe>
<embed src="archivo.pdf" width="600" height="400">
<object data="archivo.svg" type="image/svg+xml"></object>
<canvas id="miCanvas" width="200" height="200"></canvas>
```

* `<video>`/`<audio>`: reproductores nativos; atributos `controls`, `autoplay`, `loop`, `muted`.
* `<iframe>`: incrusta otro documento.
* `<embed>`/`<object>`: contenido external (PDF, Flash, etc.).
* `<canvas>`: lienzo para dibujo dinámico.

---

## Tablas de datos

```html
<table>
  <caption>Encabezado de la tabla</caption>
  <thead>
    <tr><th>Columna 1</th><th>Columna 2</th></tr>
  </thead>
  <tbody>
    <tr><td>Dato A</td><td>Dato B</td></tr>
  </tbody>
  <tfoot>
    <tr><td>Total</td><td>…</td></tr>
  </tfoot>
</table>
```

* `<table>`: tabla principal.
* `<thead>`, `<tbody>`, `<tfoot>`: secciones.
* `<tr>`: fila.
* `<th>`: celda de cabecera.
* `<td>`: celda de datos.
* `<caption>`: título de la tabla.

---

## Formularios y controles

```html
<form action="/enviar" method="post" enctype="multipart/form-data">
  <label for="texto">Texto:</label>
  <input type="text" id="texto" name="texto" placeholder="Escribe aquí" required>
  
  <label>
    <input type="checkbox" name="opcion" value="1"> Opción 1
  </label>
  
  <label for="seleccion">Selecciona:</label>
  <select id="seleccion" name="seleccion">
    <option value="a">A</option>
    <option value="b" selected>B</option>
  </select>
  
  <label for="archivo">Subir archivo:</label>
  <input type="file" id="archivo" name="archivo" accept=".png, .jpg">
  
  <button type="submit">Enviar</button>
</form>
```

* `<form>`: formulario; atributos `action`, `method`, `enctype`.
* `<label>`: etiqueta asociada a un control (`for`).
* `<input>`: múltiples `type`:

  * `text`, `password`, `email`, `url`, `tel`, `number`
  * `checkbox`, `radio`, `file`, `date`, `color`, `range`, `search`, `hidden`, `submit`, `reset`, `button`
* `<textarea>`: área de texto multilínea.
* `<select>` + `<option>`: lista desplegable.
* `<button>`: botón; `type="submit"`/`reset`/`button`.

---

## Elementos interactivos y API

* `<details>` + `<summary>`: contenido desplegable.
* `<dialog>`: cuadro de diálogo modal.
* `data-*`: atributos personalizados para datos.
* `hidden`: atributo booleano para ocultar elementos.
* `contenteditable="true"`: texto editable por el usuario.

---

## Scripts y programación

```html
<script>
  // JS inline
  document.addEventListener('DOMContentLoaded', () => {
    console.log('¡Página cargada!');
  });
</script>
<script src="app.js" defer></script>
```

* `<script>`: código JavaScript.
* Atributos: `src`, `async`, `defer`, `type="module"`.
* `<noscript>`: contenido alternativo si JS está deshabilitado.

---

## Accesibilidad y SEO

* `alt` en `<img>`: texto alternativo.
* `aria-label`, `aria-hidden`, `role`: atributos ARIA.
* Encabezados jerárquicos (`<h1>`→`<h6>`).
* Textos descriptivos en enlaces y botones.
* Uso adecuado de `label` en formularios.

___________________________

> By CISO oswaldo.diaz

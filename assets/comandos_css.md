# CSS (Cascading Style Sheets)

## 1. Selectores básicos

```css
/* Etiqueta */
p { ... }

/* Clase */
.btn { ... }

/* ID */
#header { ... }

/* Universal */
* { ... }

/* Descendiente */
nav ul li { ... }

/* Hijo directo */
article > p { ... }

/* Hermano adyacente */
h2 + p { ... }

/* Hermano general */
h2 ~ p { ... }
```

## 2. Pseudo‑clases y pseudo‑elementos

```css
/* Pseudo‑clases */
a:hover      { ... }
input:focus  { ... }
li:nth-child(odd) { ... }

/* Pseudo‑elementos */
p::first-line    { ... }
img::after       { content: ""; display: block; }
```

## 3. At‑rules

```css
@import url("estilos.css");
@charset "UTF-8";
@media (max-width: 768px) { … }
@supports (display: grid) { … }
@font-face {
  font-family: "MiFuente";
  src: url("MiFuente.woff2") format("woff2");
}
```

## 4. Modelo de caja (Box Model)

```css
/* Dimensiones */
width: 200px;    height: 100px;

/* Márgenes y relleno */
margin: 10px 5px;       /* top/bottom 10, left/right 5 */
padding: 8px 12px 8px;  /* top, right, bottom */

/* Border */
border: 1px solid #000;
border-radius: 4px;

/* Box-sizing */
box-sizing: content-box; /* default */
box-sizing: border-box;
```

## 5. Tipografía y texto

```css
font-family: Arial, sans-serif;
font-size: 16px;
font-weight: bold;
line-height: 1.5;
text-align: center;
text-decoration: underline;
text-transform: uppercase;
letter-spacing: 0.05em;
word-spacing: 0.1em;
```

## 6. Colores y fondos

```css
/* Colores */
color: #333;
background-color: rgba(255,255,255,0.8);

/* Gradientes */
background: linear-gradient(to right, #f06, #4a90e2);
background: radial-gradient(circle, #fff, #000);

/* Imágenes de fondo */
background-image: url("fondo.jpg");
background-repeat: no-repeat;
background-size: cover;
background-position: center;
```

## 7. Layout (Flexbox y Grid)

### Flexbox

```css
.container {
  display: flex;
  flex-direction: row;      /* row, column, row-reverse, column-reverse */
  justify-content: center;  /* start, end, center, space-between… */
  align-items: flex-start;  /* start, end, center, stretch… */
  flex-wrap: wrap;
}
.item {
  flex: 1 1 200px; /* grow, shrink, basis */
}
```

### Grid

```css
.grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: auto 200px;
  grid-gap: 16px;
}
.child {
  grid-column: 1 / span 2;
  grid-row: 2;
}
```

## 8. Posicionamiento

```css
position: static; /* default */
position: relative;
position: absolute;
position: fixed;
position: sticky;

top: 10px;  left: 0;
right: 1rem; bottom: 5%;
z-index: 100;
```

## 9. Transformaciones, transiciones y animaciones

```css
/* Transform */
transform: translate(10px,20px) scale(1.2) rotate(45deg) ;

/* Transition */
transition: all 0.3s ease-in-out;
transition-property: opacity, transform;
transition-duration: 250ms;

/* Animation */
@keyframes salto {
  0%   { transform: translateY(0); }
  50%  { transform: translateY(-20px); }
  100% { transform: translateY(0); }
}
.elemento {
  animation: salto 1s infinite alternate;
}
```

## 10. Filtros y efectos

```css
filter: blur(4px) brightness(0.8) contrast(120%);
mix-blend-mode: multiply; 
opacity: 0.6;
```

## 11. Variables CSS (Custom Properties)

```css
:root {
  --color-principal: #4a90e2;
  --espaciado: 1rem;
}
.elemento {
  color: var(--color-principal);
  margin: var(--espaciado) 0;
}
```

## 12. Unidades y funciones comunes

```css
/* Unidades */
px, em, rem, %, vh, vw, ch, ex

/* Funciones */
calc(100% - 2rem);
min(), max(), clamp();
url(), rgb(), hsl(), attr(), var()
```

## 13. Media Queries

```css
@media (min-width: 320px) and (max-width: 767px) {
  .menu { display: none; }
}
@media print {
  body { font-size: 12pt; }
}
```

___________________

> By CISO oswaldo.diaz

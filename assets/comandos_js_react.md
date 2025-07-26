# React.JS
---

## CLI / Proyecto

| Comando                                      | Descripción                                                           |
| -------------------------------------------- | --------------------------------------------------------------------- |
| `npx create-react-app my-app`                | Crea un nuevo proyecto React (“CRA”)                                  |
| `cd my-app`                                  | Entra en el directorio del proyecto                                   |
| `npm start` / `yarn start`                   | Inicia servidor de desarrollo (hot‑reload en `http://localhost:3000`) |
| `npm run build` / `yarn build`               | Genera versión de producción optimizada en `build/`                   |
| `npm test` / `yarn test`                     | Ejecuta tests (Jest + React Testing Library)                          |
| `npm run eject`                              | Expone configuración interna de CRA (no reversible)                   |
| `npm install <pkg>` / `yarn add <pkg>`       | Instala paquete y añade a `package.json`                              |
| `npm install -D <pkg>` / `yarn add -D <pkg>` | Instala paquete como devDependency                                    |

---

## Estructura Básica de Archivos

```
my-app/
├─ public/            # index.html, favicon, assets estáticos
└─ src/
   ├─ index.js        # Entrada, ReactDOM.render(...)
   ├─ App.js          # Componente raíz
   ├─ components/     # Componentes reutilizables
   ├─ hooks/          # Custom hooks
   ├─ context/        # Context API
   ├─ services/       # Llamadas a APIs
   └─ styles/         # Archivos CSS/SCSS
```

---

## Renderizado Inicial

```js
// src/index.js
import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);
```

---

## Componentes Funcionales & JSX

```js
// Funcional
function MiComponente({ prop1, prop2 }) {
  return (
    <>
      <h1>Hola, {prop1}!</h1>
      {prop2 && <p>Prop2 existe</p>}
    </>
  );
}

// Flecha
const Otro = ({ texto }) => <span>{texto}</span>;

// Import / Export
export default MiComponente;
import MiComponente from './MiComponente';
```

---

## Hooks Básicos

| Hook              | Uso principal                                           |
| ----------------- | ------------------------------------------------------- |
| `useState`        | Estado local: `[estado, setEstado] = useState(init)]`   |
| `useEffect`       | Efectos secundarios: `useEffect(() => { ... }, [deps])` |
| `useContext`      | Consumo de Context API: `useContext(MiContexto)`        |
| `useRef`          | Referencias mutables / accesos DOM                      |
| `useMemo`         | Memorización de valores costosos                        |
| `useCallback`     | Memorización de funciones                               |
| `useReducer`      | Estado complejo con reducer                             |
| `useLayoutEffect` | Similar a useEffect pero síncrono antes del paint       |

```js
import { useState, useEffect } from 'react';

function Contador() {
  const [cnt, setCnt] = useState(0);

  useEffect(() => {
    document.title = `Has hecho clic ${cnt} veces`;
  }, [cnt]);

  return <button onClick={() => setCnt(cnt + 1)}>Clic ({cnt})</button>;
}
```

---

## Ciclo de Vida (Componentes de Clase)

```js
class MiClase extends React.Component {
  constructor(props) {
    super(props);
    this.state = { dato: null };
  }

  componentDidMount() {
    // Montado
  }

  shouldComponentUpdate(nextProps, nextState) {
    return true; // Control de re-render
  }

  componentDidUpdate(prevProps, prevState) {
    // Actualizado
  }

  componentWillUnmount() {
    // Desmontado
  }

  render() {
    return <div>{this.state.dato}</div>;
  }
}
```

---

## Manejo de Eventos

```js
<button onClick={handleClick}>Click me</button>

function handleClick(e) {
  e.preventDefault();
  console.log('¡click!', e);
}
```

---

## Renderizado Condicional y Listas

```js
// Condicional
{isLoading ? <Spinner /> : <Contenido />}

// Listas
const items = [1,2,3];
<ul>
  {items.map(x => <li key={x}>{x}</li>)}
</ul>
```

---

## Context API

```js
// context/MyContext.js
import { createContext } from 'react';
export const MyContext = createContext(defaultValue);

// Proveedor
<MyContext.Provider value={valor}>
  <App />
</MyContext.Provider>

// Consumidor (funcional)
const valor = useContext(MyContext);
```

---

## Portals, Fragments & Error Boundaries

* **Portals:** Renderizar fuera del DOM padre

  ```js
  ReactDOM.createPortal(<Modal />, document.body);
  ```
* **Fragments:** Agrupar sin elemento extra

  ```js
  <></>  {/* o <React.Fragment> */}
  ```
* **Error Boundary (clase):** Capturar errores en descendientes

  ```js
  class ErrorBoundary extends React.Component {
    state = { hasError: false };
    static getDerivedStateFromError() { return { hasError: true }; }
    componentDidCatch(err, info) { /* log */ }
    render() { return this.state.hasError ? <h1>Oops</h1> : this.props.children; }
  }
  ```

---

## Code Splitting & Lazy Loading

```js
import { Suspense, lazy } from 'react';
const LazyComp = lazy(() => import('./Heavy'));

function App() {
  return (
    <Suspense fallback={<div>Cargando...</div>}>
      <LazyComp />
    </Suspense>
  );
}
```

---

## PropTypes & DefaultProps

```js
import PropTypes from 'prop-types';

MiComponente.propTypes = {
  texto: PropTypes.string.isRequired,
  onClick: PropTypes.func,
};

MiComponente.defaultProps = {
  onClick: () => {},
};
```

---

## Testing Básico (Jest + RTL)

```js
import { render, screen, fireEvent } from '@testing-library/react';
import MiComponente from './MiComponente';

test('muestra texto y responde clic', () => {
  render(<MiComponente texto="Hola" />);
  expect(screen.getByText(/Hola/)).toBeInTheDocument();
  fireEvent.click(screen.getByText(/Hola/));
});
```

---

## Rutas (React Router v6)

```js
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';

<BrowserRouter>
  <nav>
    <Link to="/">Home</Link>
    <Link to="/about">About</Link>
  </nav>
  <Routes>
    <Route path="/" element={<Home />} />
    <Route path="/about" element={<About />} />
  </Routes>
</BrowserRouter>
```
________________________

> By CISO oswaldo.diaz 

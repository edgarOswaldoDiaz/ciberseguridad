# GIT


## **Configuración Inicial**

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu.email@example.com"
git config --global core.editor "nano"  # Editor por defecto
git config --list  # Ver configuración actual
```

---

## **Inicializar y Clonar Repositorios**

```bash
git init                    # Inicializar un repositorio local
git clone <url>             # Clonar un repositorio remoto
```

---

## **Estado y Diferencias**

```bash
git status                  # Ver estado de los archivos
git diff                    # Ver cambios en archivos no añadidos
git diff --staged           # Ver cambios en archivos añadidos (staged)
git diff HEAD               # Comparar con el último commit
```

---

## **Agregar y Confirmar Cambios**

```bash
git add <archivo>           # Añadir archivo específico al área de preparación
git add .                   # Añadir todos los archivos modificados
git commit -m "Mensaje"     # Confirmar cambios con mensaje
git commit -a -m "Mensaje"  # Añadir y confirmar todos los archivos ya rastreados
```

---

## **Historial de Commits**

```bash
git log                     # Ver historial de commits
git log --oneline           # Historial en una línea
git log --graph             # Historial con gráfico de ramas
git log --author="Nombre"   # Filtrar por autor
git show <commit>           # Ver detalles de un commit específico
```

---

## **Ramas (Branches)**

```bash
git branch                  # Listar ramas
git branch <nombre>         # Crear una nueva rama
git checkout <rama>         # Cambiar a una rama
git checkout -b <nombre>    # Crear y cambiar a una nueva rama
git merge <rama>            # Fusionar una rama con la actual
git branch -d <nombre>      # Eliminar una rama
git branch -D <nombre>      # Forzar eliminación de rama
```

---

## **Rebase**

```bash
git rebase <rama>           # Rebasar la rama actual sobre otra
git rebase -i HEAD~n        # Rebase interactivo de los últimos n commits
```

---

## **Deshacer Cambios**

```bash
git checkout -- <archivo>   # Deshacer cambios en archivo no añadido
git reset HEAD <archivo>    # Sacar archivo del área de preparación
git reset --soft HEAD~1     # Deshacer último commit, mantener cambios
git reset --hard HEAD~1     # Deshacer último commit y cambios
git revert <commit>         # Revertir un commit específico
```

---

## **Stash (Guardado Temporal)**

```bash
git stash                   # Guardar cambios temporalmente
git stash list              # Ver lista de stashes
git stash apply             # Aplicar último stash
git stash drop              # Eliminar último stash
git stash pop               # Aplicar y eliminar stash
```

---

## **Trabajo con Repositorios Remotos**

```bash
git remote -v               # Ver repositorios remotos
git remote add origin <url> # Añadir origen remoto
git push origin <rama>      # Enviar cambios a rama remota
git push -u origin <rama>   # Enviar y establecer rama por defecto
git push --force            # Forzar push (usar con cuidado)
git pull origin <rama>      # Obtener y fusionar cambios
git fetch                   # Obtener cambios sin fusionar
```

---

## **Etiquetas (Tags)**

```bash
git tag                     # Listar etiquetas
git tag <nombre>            # Crear etiqueta ligera
git tag -a <nombre> -m "Mensaje"  # Crear etiqueta anotada
git push origin <tagname>   # Enviar etiqueta al remoto
git push origin --tags      # Enviar todas las etiquetas
```

---

## **Limpieza y Mantenimiento**

```bash
git clean -f                # Eliminar archivos no rastreados
git gc                      # Optimizar el repositorio
git fsck                    # Verificar integridad del repositorio
```

---

## **Alias Útiles**

```bash
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.unstage 'reset HEAD --'
git config --global alias.last 'log -1 HEAD'
```
_______________________

> By CISO oswaldo.diaz

# Laboratorio de Fundamentos de Procesamiento Digital de Imágenes, Visión por Computadora, VLMs y Agentic AI

**Hacia una Visión Técnico-Humanista: Procesamiento, Algoritmos y Sociedad**

**IFTS Nº 24 — Ciencia de Datos e Inteligencia Artificial**  
**3er año — 1er cuatrimestre 2026**

---

## 🧠 Qué es este repositorio

Este repositorio contiene el material de laboratorio de la materia.  
Las carpetas (`001/`, `002/`, etc.) representan unidades temáticas con notebooks (`.ipynb`) y scripts (`.py`).

---

## ⚙️ Setup inicial (una sola vez)

### 1. Clonar el repositorio

```bash
git clone https://github.com/mattbarreto/ifts24-lab-pdi-2026.git
cd ifts24-lab-pdi-2026
```

---

## 🐍 Entorno virtual (.venv)

### Crear entorno virtual

```bash
python -m venv .venv
```

### Activar entorno

**Windows (PowerShell):**
```powershell
.venv\Scripts\Activate.ps1
```

**Windows (CMD / Git Bash):**
```bash
.venv\Scripts\activate
```

### Desactivar entorno

```bash y Powershell
deactivate
```

---

## 📦 Dependencias

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Actualizar pip:

```bash
python -m pip install --upgrade pip
```

Guardar nuevas dependencias:

```bash
pip freeze > requirements.txt
```

---

## 🧪 Comandos de Python

Ejecutar script:

```bash
python archivo.py
```

Abrir Jupyter Notebook:

```bash
jupyter notebook
```

Abrir Jupyter Lab:

```bash
jupyter lab
```

Crear kernel del entorno:

```bash
python -m ipykernel install --user --name=venv-pdi
```

Ver versión de Python:

```bash
python --version
```

---

## 🔧 Comandos de Git (uso diario)

### Estado del repo

```bash
git status
```

### Ver cambios

```bash
git diff
```

### Agregar cambios

```bash
git add .
```

Agregar archivo específico:

```bash
git add archivo.py
```

### Commit

```bash
git commit -m "mensaje claro del cambio"
```

### Subir cambios

```bash
git push origin master
```

---

## 🔄 Actualizar repo

```bash
git pull origin master
```

---

## 🌿 Trabajo con ramas

Crear rama:

```bash
git checkout -b feature/nombre
```

Cambiar de rama:

```bash
git checkout master
```

Merge:

```bash
git merge feature/nombre
```

Eliminar rama:

```bash
git branch -d feature/nombre
```

---

## 🚨 Buenas prácticas

- Activar siempre el `.venv` antes de trabajar
- No subir `.venv/` al repo (agregarlo al `.gitignore`)
- Hacer commits chicos y claros
- Usar ramas para cambios grandes
- Mantener actualizado el `requirements.txt`

---

## 🧠 Librerías principales

- OpenCV (`cv2`)
- NumPy
- Matplotlib
- Pillow
- scikit-image
- py5

---

## ⚠️ Notas importantes

- `py5` requiere Java → https://py5coding.org/content/install.html
- `google.colab.patches` es solo para Google Colab
- Se recomienda usar VS Code + extensiones Python y Jupyter

---

## 🚀 Flujo de trabajo recomendado

```bash
# 1. Actualizar repo
git pull origin master

# 2. Activar entorno
.venv\Scripts\activate

# 3. Instalar dependencias (si cambian)
pip install -r requirements.txt

# 4. Trabajar en código

# 5. Guardar cambios
git add .
git commit -m "descripcion"
git push origin master
```

---


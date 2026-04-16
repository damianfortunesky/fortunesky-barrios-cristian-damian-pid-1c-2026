# 📘 Clase 2 — Py5 y Fundamentos de Procesamiento de Imágenes

---

## 🧠 1. Repaso

- Imagen = función f(x, y)
- Imagen digital = datos discretos
- Píxel = unidad básica
- Concepto clave: imágenes operativas

---

## 🖼️ 2. Procesamiento Digital de Imágenes (PDI)

El PDI consiste en aplicar algoritmos sobre imágenes para:

- Mejorarlas (enhancement)
- Analizarlas
- Extraer información

---

## 🔧 3. Técnicas principales

- Image Enhancement → mejora de imagen
- Filtering → filtrado
- Edge Detection → detección de bordes
- Transformaciones geométricas
- Procesamiento en frecuencia
- Operaciones morfológicas
- Transformaciones de color fileciteturn3file0

---

## 🤖 4. Librerías importantes

- OpenCV
- scikit-image
- Pillow (PIL)
- Py5 (la que usamos en clase)
- YOLO / Supervision (visión avanzada)

---

## 🎨 5. ¿Qué es Py5?

- Librería basada en Processing
- Permite trabajar con gráficos e imágenes
- Ideal para aprendizaje visual

Requiere:
- Python
- Java (JDK)

---

## ⚙️ 6. Estructura de un programa Py5

### setup()

Se ejecuta una sola vez:
- Tamaño del canvas
- Configuración inicial

```python
def setup():
    py5.size(500, 500)
    py5.background(255)
```

---

### draw()

Se ejecuta en loop:

```python
def draw():
    py5.circle(250, 250, 100)
```

---

## 🎨 7. Colores

- RGB:
  - R: 0–255
  - G: 0–255
  - B: 0–255

```python
py5.fill(255, 0, 0)  # rojo
py5.stroke(0, 0, 0) # borde
```

---

## 🔷 8. Formas básicas

```python
py5.point(x, y)
py5.line(x1, y1, x2, y2)
py5.rect(x, y, w, h)
py5.circle(x, y, d)
py5.ellipse(x, y, w, h)
```

---

## 🖼️ 9. Manejo de imágenes

```python
img = py5.load_image("imagen.png")
py5.image(img, x, y)
py5.image(img, x, y, w, h)
```

---

## 🎛️ 10. Filtros (MUY IMPORTANTE)

```python
py5.apply_filter(py5.GRAY)
py5.apply_filter(py5.INVERT)
py5.apply_filter(py5.THRESHOLD)
py5.apply_filter(py5.BLUR)
```

Tipos:
- GRAY → escala de grises
- INVERT → negativo
- THRESHOLD → binarización
- BLUR → desenfoque
- POSTERIZE → reduce colores
- ERODE / DILATE → morfología fileciteturn3file0

---

## 🖱️ 11. Interacción

### Mouse

```python
py5.mouse_x
py5.mouse_y
py5.is_mouse_pressed
```

Eventos:
```python
py5.mouse_pressed()
py5.mouse_dragged()
```

---

### Teclado

```python
py5.key
py5.is_key_pressed
```

Eventos:
```python
py5.key_pressed()
```

---

## 🔢 12. Píxeles (CLAVE PARA PARCIAL)

- Una imagen = array lineal de píxeles

Fórmula:

index = x + y * width

```python
py5.load_pixels()
py5.pixels[index] = color
py5.update_pixels()
```

---

## ⚡ 13. Resumen rápido

- Py5 = entorno gráfico para imágenes
- setup() → inicializa
- draw() → loop
- filtros → transformación de imagen
- píxeles → nivel bajo de manipulación
- interacción → mouse + teclado

---

## 💡 Nota personal

Esto es base para:
- Visión por computadora
- Machine Learning con imágenes
- Procesamiento de datos visuales


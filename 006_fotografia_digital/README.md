# README.md

# Parte 1 — Cámara oscura y procesamiento digital

## Objetivo de la actividad

El objetivo de esta actividad fue:

* construir una cámara oscura artesanal,
* capturar una imagen real utilizando el dispositivo,
* aplicar procesamiento digital básico,
* analizar el comportamiento de la imagen y sus limitaciones físicas.

---

# 1. Cámara oscura

## Principio óptico

La cámara oscura funciona mediante la propagación rectilínea de la luz.

La luz atraviesa un pequeño orificio y proyecta una imagen invertida sobre una superficie interna.

---

## Conceptos observados

### Propagación rectilínea

La luz viaja en línea recta desde la escena hasta el plano de proyección.

### Imagen invertida

La proyección aparece invertida vertical y horizontalmente debido a la geometría del sistema óptico.

### Plano de imagen

La superficie interna donde se proyecta la escena actúa como plano de imagen.

### Apertura y nitidez

El tamaño del orificio afecta directamente la nitidez:

* agujero grande → más luz pero menos definición,
* agujero pequeño → mayor nitidez pero menos luminosidad.

---

# 2. Captura de imagen

## Resultado obtenido

La imagen capturada presenta:

* bajo contraste,
* desenfoque óptico,
* ruido,
* iluminación irregular,
* pérdida de detalle fino.

Estas características son típicas de una cámara oscura artesanal.

---

# 3. Procesamiento digital

## Objetivo del procesamiento

Mejorar la percepción visual de la imagen sin alterar excesivamente la información original.

---

# 4. Conversión a HSV

## ¿Por qué usar HSV?

La imagen fue convertida desde RGB hacia HSV.

HSV separa la información en:

* H → tono/color,
* S → saturación,
* V → brillo/luminancia.

Esto permite modificar únicamente el brillo sin alterar directamente los colores.

---

# 5. Separación de canales

Se separaron los canales:

* H (Hue),
* S (Saturation),
* V (Value).

El procesamiento se realizó únicamente sobre el canal V.

---

# 6. Ecualización del canal V

## ¿Qué se hizo?

Se aplicó ecualización de histograma únicamente sobre el canal V.

---

## ¿Por qué sobre V y no RGB?

Ecualizar directamente RGB puede:

* alterar colores,
* producir artefactos cromáticos,
* deformar el balance visual.

En cambio, ecualizar V:

* mejora contraste,
* aumenta visibilidad,
* conserva mejor los colores originales.

---

# 7. Recomposición de la imagen

Luego de ecualizar el canal V:

* los canales HSV fueron recombinados,
* la imagen fue convertida nuevamente a RGB/BGR.

---

# 8. Histogramas

## Histograma original

La imagen original presenta:

* rango dinámico reducido,
* predominio de tonos medios,
* pocos negros profundos,
* pocas altas luces reales.

---

## Histograma ecualizado

Luego de la ecualización:

* el rango tonal se expande,
* mejora la distribución de intensidades,
* aumenta el contraste visual.

---

# 9. Resultados obtenidos

## Mejoras observadas

### Mejora de contraste

Las zonas oscuras y claras se diferencian mejor.

### Recuperación visual

Aparecen estructuras antes poco visibles.

### Mejor percepción de profundidad

La imagen adquiere mayor separación tonal.

### Conservación de color

Los colores originales se mantienen relativamente estables.

---

# 10. Limitaciones observadas

## Limitaciones físicas de la cámara oscura

### Desenfoque óptico

La ausencia de lentes genera baja nitidez.

### Ruido

La poca iluminación obliga a exposiciones más complejas.

### Sobreexposición

Algunas zonas brillantes se saturan fácilmente.

### Difracción

El pequeño orificio introduce pérdida de detalle.

### Bajo detalle fino

La imagen conserva una apariencia suave y difusa.

---

# 11. Análisis final

El procesamiento aplicado mejora claramente:

* contraste,
* percepción visual,
* distribución tonal.

Sin embargo:

* no puede recuperar detalle perdido físicamente,
* no elimina completamente el blur óptico,
* ni corrige limitaciones estructurales de la cámara oscura.

El principal límite de calidad proviene de la captura física y no del procesamiento digital.

---

# 12. Conclusión

La actividad permitió comprender:

* fundamentos ópticos de la cámara oscura,
* comportamiento de imágenes con bajo contraste,
* uso del espacio HSV,
* aplicación práctica de ecualización de histograma,
* interpretación de histogramas,
* relación entre captura física y procesamiento digital.

La ecualización sobre el canal V permitió mejorar la imagen respetando el objetivo pedagógico de la actividad y manteniendo coherencia con los fundamentos del procesamiento digital de imágenes.

# -------------------------------------------------------------------------------------------------------------------------------------------------------- #

# Parte 2 — Composición y lenguaje visual

---

# 4. Fotografía de simplicidad visual

## Objetivo

Construir una imagen donde el sujeto principal sea claramente identificable.

## Estrategias utilizadas

- acercamiento
- reducción de ruido visual
- separación sujeto/fondo
- conversión a escala de grises

## Explicación compositiva

La imagen original contenía múltiples elementos distractores:
- silla
- mesa
- texturas secundarias
- espacio vacío excesivo

Se realizó un reencuadre para centrar la atención en el gato y eliminar elementos innecesarios.

La conversión a escala de grises reduce la información cromática y enfatiza:
- forma
- contraste
- textura
- volumen

## Preguntas guía

### ¿Qué elementos distraían?

La silla, el piso, la mesa y los objetos del fondo.

### ¿Qué se eliminó?

Se eliminó gran parte del entorno mediante crop.

### ¿Cómo cambia la lectura en escala de grises?

La imagen se vuelve más gráfica y centrada en formas y contraste.

---

# 5. Reencuadre y reinterpretación

## Objetivo

Demostrar que cambiar el encuadre modifica el significado de la imagen.

## Explicación

Se partió de una imagen amplia del ambiente.

Se realizaron dos recortes:

### Crop A

Mantiene parte del entorno.
El sujeto continúa relacionado con el espacio.

### Crop B

Aísla al gato.
La imagen se vuelve más abstracta y psicológica.

## Preguntas guía

### ¿Qué se vuelve importante después del crop?

El rostro y la postura del sujeto.

### ¿Qué información desaparece?

Contexto espacial y objetos secundarios.

### ¿El sujeto cambia?

Sí.
Pasa de ser parte de una escena a convertirse en el foco absoluto.

### ¿La imagen se vuelve más narrativa o más abstracta?

El crop cerrado genera una imagen más abstracta e íntima.

---

# 6. Punto de vista y construcción narrativa

## Objetivo

Explorar cómo la posición de la cámara modifica:
- escala
- contexto
- relación emocional

## Explicación

Se fotografió el mismo sujeto desde dos ángulos:
- frontal
- cenital

La vista frontal genera cercanía emocional.

La vista cenital genera distancia y vulnerabilidad.

## Preguntas guía

### ¿Qué información aparece desde el nuevo ángulo?

La forma del cuerpo y la relación espacial con el sillón.

### ¿Cómo cambia la percepción del sujeto?

El sujeto parece más pequeño y aislado.

### ¿Qué relación genera la cámara con la escena?

La cámara frontal genera igualdad visual.
La cenital genera observación externa.

---

# 7. Fotografía basada en la luz

## Objetivo

Usar la luz como elemento estructural de la imagen.

## Estrategia utilizada

- luz lateral
- alto contraste
- sombras marcadas

## Explicación

La luz lateral genera:
- volumen
- textura
- dramatismo

Las sombras permiten separar al sujeto del fondo oscuro.

## Preguntas guía

### ¿La luz revela o esconde?

Hace ambas cosas:
revela volumen y esconde parte del entorno.

### ¿Genera textura?

Sí.
La manta y el pelaje se vuelven más táctiles.

### ¿Construye atmósfera?

Sí.
La escena adquiere un tono introspectivo.

### ¿Cómo cambia el volumen?

El contraste lateral aumenta la percepción tridimensional.

---

# Parte 3 — Reflexión y selección

---

# 8. Selección crítica

## Imagen elegida

actividad7_luz_final.jpg

## Explicación

La imagen elegida funciona mejor porque:
- posee intención visual clara
- tiene contraste fuerte
- separa correctamente sujeto y fondo
- utiliza la luz como elemento compositivo

## Imágenes descartadas

Las imágenes descartadas presentaban:
- exceso de espacio vacío
- menor impacto visual
- iluminación menos controlada
- menor claridad narrativa

## Decisiones que mejoraron la imagen final

- reencuadre
- control de luz
- simplificación compositiva
- selección crítica

---

# 9. Reflexión final

## ¿Qué aprendiste sobre mirar?

Aprendí que fotografiar implica observar relaciones entre:
- luz
- forma
- encuadre
- intención

## ¿Qué diferencia hay entre registrar y construir una imagen?

Registrar es capturar una escena.
Construir implica tomar decisiones visuales conscientes.

## ¿Qué relación encontrás entre óptica, percepción y composición?

La óptica condiciona la luz.
La percepción organiza visualmente la escena.
La composición dirige la atención.

## ¿Cómo modifica el postproceso la lectura de una fotografía?

El postproceso puede:
- enfatizar contraste
- dirigir la mirada
- cambiar atmósferas
- simplificar información visual

---

# 10. Anexo técnico

## Operaciones realizadas

- conversión RGB → HSV
- ecualización del canal V
- transformación a escala de grises
- recorte digital
- análisis de histograma

## Objetivo técnico

Mejorar:
- contraste
- separación visual
- lectura tonal

## Código utilizado

El procesamiento fue realizado en Python utilizando:
- OpenCV
- NumPy
- Matplotlib

## Procesos incluidos

### Conversión RGB ↔ HSV

Separación de:
- tono
- saturación
- brillo

### Ecualización del canal V

Mejora del contraste lumínico.

### Escala de grises

Simplificación visual basada en luminancia.

### Histogramas

Análisis de distribución tonal de la imagen.
# TFI 1: Mejora y restauracion de imagenes

**Modalidad:** trabajo en parejas con defensa oral breve e individual.

**Entrega:** notebook completo + carpeta de imagenes originales + carpeta de resultados procesados.

## Proposito

Este Trabajo Final Integrador 1 te pide pasar de los cuadernos guiados a una resolucion mas autonoma y argumentada. Ya no alcanza con aplicar funciones de OpenCV de manera aislada: tenes que diagnosticar un problema visual, comparar estrategias y sostener una decision tecnica con evidencia.

El eje del trabajo es construir **tres pipelines de mejora y restauracion**, uno por cada tipo de caso:

1. **Imagen obtenida mediante camara oscura**
2. **Imagen de medio grafico color**
3. **Imagen de medio grafico blanco/negro**

## Restricciones obligatorias

- El trabajo debe incluir los **tres casos obligatorios**.
- Cada caso debe partir de una **imagen original propia o seleccionada con criterio**.
- En cada caso tenes que mostrar al menos:
  - un **diagnostico inicial**;
  - **dos estrategias comparables**;
  - una **eleccion final justificada**.
- No se acepta repetir exactamente el mismo pipeline en los tres casos salvo que argumentes por que el problema visual es efectivamente equivalente.
- Cada pipeline debe tener una **cantidad acotada de operaciones**. Si agregas muchos pasos, tenes que justificar por que cada uno aporta algo distinto.
- No vale escribir solo que una salida "queda mejor". Tenes que explicar **que problema resolvio**, **que mejora produjo** y **que limite mantiene**.

## Recomendacion de alcance

Conviene que cada pipeline tenga entre **2 y 4 operaciones principales**. El objetivo no es acumular tecnicas, sino elegir con criterio.

## Notebook de soporte recomendado

Para el caso de medio grafico blanco/negro, antes o durante este trabajo conviene revisar:

- `004 - computer_vision_parte_1/006b - filtros de suavizado y reduccion de ruido.ipynb`
- `004 - computer_vision_parte_1/006b2 - umbralizacion global, Otsu y adaptive threshold.ipynb`
- `004 - computer_vision_parte_1/006c - morfologia matematica para limpieza de mascaras.ipynb`

## Que tienen que hacer

En el notebook deben:

1. presentar el trabajo y explicar brevemente el objetivo general;
2. cargar las tres imagenes de partida;
3. diagnosticar el problema visual principal en cada caso;
4. probar al menos dos estrategias por caso;
5. comparar resultados intermedios y justificar parametros;
6. elegir una version final para cada pipeline;
7. guardar las tres imagenes finales procesadas;
8. cerrar con una comparacion transversal entre los tres casos.

## Sugerencias tecnicas por caso

### 1. Camara oscura

Problemas frecuentes:

- bajo contraste;
- imagen oscura;
- ruido;
- zona importante poco visible;
- exceso de fondo inutil.

Operaciones posibles:

- recorte;
- ajuste de brillo y contraste;
- `CLAHE`;
- suavizado gaussiano o mediana.

### 2. Medio grafico color

Problemas frecuentes:

- perspectiva deformada;
- colores apagados;
- dominante de iluminacion;
- manchas o danos localizados.

Operaciones posibles:

- rectificacion de perspectiva;
- ecualizacion o `CLAHE` segun el caso;
- mejora sobre HSV o LAB;
- `inpainting` si hubiera dano localizado.

### 3. Medio grafico blanco/negro

Problemas frecuentes:

- iluminacion desigual;
- ruido;
- texto o trazos cortados;
- fondo gris o sucio;
- perdida de legibilidad.

Operaciones posibles:

- conversion a grises;
- suavizado;
- umbral global, `Otsu` o `adaptiveThreshold`;
- apertura o clausura morfologica.

## Trabajo con IA

Podes usar IA como apoyo para:

- discutir alternativas de pipeline;
- auditar errores de codigo;
- pedir explicaciones comparativas entre tecnicas.

Pero no vale usarla como reemplazo de tu criterio. Toda decision final, toda justificacion y toda seleccion de parametros tienen que quedar bajo responsabilidad del equipo.

## Registro breve del uso de IA

Dentro del notebook debe aparecer un registro breve con estas columnas:

- caso;
- objetivo de la consulta;
- pedido a la IA;
- que conservaste;
- que descartaste;
- que aprendiste.

## Entregables

- `TFI_1 - mejora y restauracion de imagenes.ipynb` completo;
- carpeta con las imagenes originales usadas;
- carpeta con las tres salidas finales;
- comparaciones visuales incluidas dentro del notebook;
- reflexion final con limites del metodo.

## Rubrica de evaluacion

| Criterio | Peso | Que se espera |
|---|---:|---|
| Diagnostico del problema visual | 20% | Lectura clara del defecto principal y del objetivo de mejora |
| Coherencia tecnica del pipeline | 25% | Operaciones pertinentes para el problema observado |
| Comparacion de estrategias | 20% | Dos pruebas reales por caso y justificacion de la eleccion |
| Claridad del notebook y comunicacion tecnica | 20% | Notebook ordenado, reproducible, con lenguaje tecnico claro |
| Reflexion critica y limites | 15% | Conciencia de que mejora la imagen y que no puede recuperar |

## Condiciones minimas para aprobar

La entrega no alcanza el minimo si:

- falta alguno de los tres casos obligatorios;
- no hay comparacion entre dos estrategias por caso;
- no se explica por que se eligio la version final;
- no aparecen imagenes de antes y despues;
- el notebook no se puede seguir o no se puede ejecutar de manera razonable;
- la reflexion final se reduce a describir filtros aplicados sin criterio.

## Defensa oral breve

En la defensa cada integrante debe poder responder, con sus palabras:

- cual fue el problema principal de cada caso;
- por que una estrategia funciono mejor que otra;
- que haria distinto si tuviera mas tiempo;
- donde aparecen los limites del metodo.

## Recomendacion final

Vale mas un pipeline breve, coherente y bien argumentado que una cadena larga de operaciones aplicada sin criterio. En este trabajo se evalua sobre todo **como decidis**, no solo **que funcion usas**.

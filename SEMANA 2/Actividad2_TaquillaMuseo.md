# ACTIVIDAD EVALUABLE 2 — LA TAQUILLA DEL MUSEO

**Curso:** Fundamentos de programación
**Semana:** 2 · Decisiones, ciclos y detective de bugs
**Ponderación:** 6% de la calificación total del curso
**Modalidad:** Individual
**Fecha límite:** viernes 23 de octubre de 2026, 23:59 h (sin prórroga)
**Evidencia de entrega:** liga pública de **tu mismo repositorio del curso**, ahora con la carpeta `semana2/`

---

## 1. El reto

El **Museo de Antropología e Historia** necesita un programa para su taquilla. Hoy el cajero calcula todo a mano y se equivoca con los descuentos: a veces aplica dos al mismo tiempo, a veces ninguno. Tu misión es construir el programa que cobre a cada visitante el precio correcto **y solo un descuento**, que funcione para cualquier cantidad de visitantes y que al cerrar la taquilla entregue el corte de caja.

Como en la semana 1, **primero se piensa y después se programa**:

1. **Parte A (a mano):** diseñas la lógica en papel.
2. **Parte B (notebook):** la conviertes en un programa.
3. **Parte C (notebook):** demuestras que funciona con casos de prueba.
4. **Parte D (GitHub):** lo entregas como profesional.

---

## 2. Las reglas del museo

**Precio base según la edad:**

| Edad | Precio base |
| :--- | :---: |
| Menos de 3 años | Gratis ($0) |
| De 3 a 17 años | $30 |
| 18 años o más | $45 |

**Descuentos (solo para personas de 18 años o más):**

| Tipo de visitante | Cómo se identifica | Descuento |
| :--- | :--- | :---: |
| Adulto mayor | **Automático** si tiene 60 años o más | 12% |
| Estudiante | Lo elige en el menú (opción 1) | 10% |
| Profesor | Lo elige en el menú (opción 2) | 10% |
| Ninguno | Lo elige en el menú (opción 3) | 0% |

**Reglas que no se rompen:**
- **Un solo descuento por boleto.** Si alguien tiene 60 años o más **y** además es profesor o estudiante, recibe **solo el de adulto mayor** (el más alto).
- Los menores de 18 años **no tienen descuento** y **no se les pregunta el tipo de visitante**.
- Una edad negativa o mayor de 110 **no es válida**: se avisa, no se cobra y se pide el siguiente visitante.
- La taquilla se cierra cuando el cajero escribe `fin`.

---

## 3. Partes de la actividad

### Parte A — Diseño a mano (25 pts)

Hecha **a mano en tu libreta**, escaneada en un solo PDF.

**A1. Tabla de decisión.** Completa la tabla con **todos** los casos posibles de un visitante válido. Son 6 filas. Agrega una columna con un **ejemplo** de edad y tipo, y calcula cuánto paga.

| # | Edad | Tipo | Precio base | Descuento | Paga | Ejemplo |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | Menos de 3 | (no se pregunta) | $0 | — | $0.00 | 2 años |
| 2 | … | … | … | … | … | … |

> 💡 Pista: piensa en qué pasa con un profesor de 65 años.

**A2. Diagrama de flujo.** Dibuja el diagrama de flujo de **toda la taquilla**. Debe incluir:
- El **ciclo**: una flecha que regresa para atender al siguiente visitante.
- El **rombo** de `fin` que cierra la taquilla.
- El **rombo** de edad no válida.
- Los **rombos** de la tabla de decisión.
- El **resumen final**.

Cada bloque del diagrama debe poder señalarse en tu código.

### Parte B — El programa (45 pts)

En `semana2/taquilla_museo.ipynb`. Tu programa debe:

1. Usar **constantes** al inicio para los precios y los descuentos. Por ejemplo: `PRECIO_ADULTO = 45`.
2. Usar un ciclo **`while`** que atienda visitantes hasta que se escriba `fin`.
3. Usar **`break`** para cerrar la taquilla al recibir `fin`.
4. Usar **`continue`** para saltar una edad no válida sin cobrarla.
5. Calcular el precio y el descuento con **`if / elif / else`** siguiendo tu tabla de la Parte A.
6. Preguntar el tipo de visitante **solo** a los mayores de 18, con este menú: `1) Estudiante  2) Profesor  3) Ninguno`.
7. Mostrar el **detalle de cada visitante** en una línea: número, edad, tipo, precio base, descuento y cuánto paga.
8. Al cerrar, mostrar el **corte de caja**: visitantes cobrados, total en descuentos y total a pagar. Necesitas **acumuladores** y un **contador**.
9. Mostrar todos los montos con 2 decimales.

**Ejemplo de cómo debe verse** (los textos pueden variar; los números no):
```
=== TAQUILLA DEL MUSEO ===
Edad del visitante (o 'fin' para cerrar la taquilla): 25
Tipo: 1) Estudiante  2) Profesor  3) Ninguno: 2
Visitante 1 | Edad: 25 | Profesor | Base: $45.00 | Descuento: $4.50 | A pagar: $40.50
Edad del visitante (o 'fin' para cerrar la taquilla): fin
=== CORTE DE CAJA ===
Visitantes cobrados: 1
Total en descuentos: $4.50
TOTAL A PAGAR: $40.50
```

**Estructura sugerida del notebook:**

| Celda | Tipo | Contenido |
| :---: | :--- | :--- |
| 1 | Markdown | Título, tu nombre y matrícula, y en 2–3 líneas qué hace el programa |
| 2 | Código | Constantes y acumuladores en 0 |
| 3 | Código | El ciclo de la taquilla y el corte de caja |
| 4 | Markdown | Parte C: tus casos de prueba |

> 🔍 **Atajo de detective:** antes de que el ciclo funcione, prueba solo la parte de las decisiones con **una** edad fija (por ejemplo `edad = 65`). Cuando eso salga bien, envuélvelo en el `while`.

### Parte C — Casos de prueba (15 pts)

Ejecuta tu programa con **estos 3 casos**, uno por uno. Para cada caso, en una celda Markdown escribe el total que **esperabas** (calculado con tu tabla de la Parte A) y el que **obtuviste**, y di si coinciden.

| Caso | Entradas, en orden | Total esperado |
| :---: | :--- | :---: |
| 1 | `25` (tipo `2`), `2`, `15`, `67` (tipo `1`), `fin` | *calcúlalo tú* |
| 2 | `-5`, `30` (tipo `3`), `fin` | *calcúlalo tú* |
| 3 | `fin` | *calcúlalo tú* |

Después agrega **un caso propio**, con al menos 4 visitantes, que ponga a prueba la regla de "un solo descuento".

> 💡 Si un caso no coincide, **no lo escondas**: usa la técnica del detective, encuentra el bug y explica en 2 líneas qué era. Un bug bien documentado vale más que un resultado maquillado.

### Parte D — Entrega profesional en GitHub (15 pts)

**D1. Estructura.** En **el mismo repositorio** de la semana 1:
```
tu-repositorio/
├── README.md                 (actualizado: menciona la semana 2)
├── semana1/
│   └── ...
└── semana2/
    ├── ParteA_TablaDiagrama.pdf
    └── taquilla_museo.ipynb  (ejecutado: con salidas visibles)
```

**D2. Historial.** Haz al menos **3 commits** conforme avanzas, con mensajes descriptivos. Por ejemplo:
```
docs: agregar tabla de decisión y diagrama de la taquilla
feat: taquilla del museo con precios y descuentos
test: agregar casos de prueba de la actividad 2
```

---

## 4. Entregables

| Entregable | Archivo | Dónde |
| :--- | :--- | :--- |
| Tabla de decisión y diagrama, a mano y escaneados | `ParteA_TablaDiagrama.pdf` | `semana2/` |
| Programa y casos de prueba | `taquilla_museo.ipynb` | `semana2/` |
| **Evidencia** | **Liga pública de tu repositorio** | Plataforma del curso |

**Reglas de entrega:**
- **Fecha límite sin prórroga.** Si algo no funciona, entrega lo que tengas y documenta el error.
- Solo se reciben entregas en **tu repositorio único del curso**. No se aceptan repositorios nuevos ni archivos enviados por fuera de GitHub.
- El notebook debe estar **ejecutado**: si en GitHub no se ven las salidas, la Parte C vale 0.
- Las entregas idénticas o sustancialmente iguales entre alumnos valen 0.
- Puedo pedirte que expliques tu código en clase. Si no puedes explicarlo, no se considera tuyo.

---

## 5. Rúbrica de evaluación (100 pts)

| Parte | Criterio | Pts | Excelente (100%) | Bueno (75%) | Regular (50%) | Insuficiente (0%) |
| :---: | :--- | :---: | :--- | :--- | :--- | :--- |
| A | **Tabla de decisión** | 12 | Las 6 combinaciones correctas, con ejemplo y monto; resuelve bien el caso del adulto mayor que también es profesor o estudiante. | 1 caso faltante o con un monto erróneo. | 2 o 3 casos faltantes o erróneos. | No la incluye o no está hecha a mano. |
| A | **Diagrama de flujo** | 13 | Símbolos correctos; incluye ciclo, rombo de `fin`, rombo de edad no válida, decisiones y resumen; coherente con el código. | Completo, con 1 o 2 símbolos mal usados o una flecha faltante. | Le falta el ciclo o las decisiones, o no coincide con el código. | No lo incluye o es ilegible. |
| B | **Precios por edad** | 10 | $0, $30 y $45 correctos en todos los rangos, incluyendo los límites (2, 3, 17 y 18 años). | Un límite mal resuelto (por ejemplo, 18 años cobra $30). | Una categoría de precio incorrecta. | No calcula precios por edad. |
| B | **Un solo descuento** | 12 | 12% automático a partir de 60 años, 10% para estudiante o profesor, nunca dos descuentos y sin descuento a menores. Usa constantes. | Correcto, pero sin constantes o con el tipo preguntado a menores. | Aplica descuento a menores o algún caso con descuento incorrecto. | No aplica descuentos. |
| B | **Ciclo, `break` y `continue`** | 13 | `while` que atiende visitantes hasta `fin`; `break` cierra la taquilla; `continue` salta la edad no válida sin cobrarla. | Funciona, pero `break` o `continue` están mal ubicados (por ejemplo, la edad no válida se cuenta como visitante). | Usa solo uno de los dos, o el ciclo no termina correctamente. | Sin ciclo. |
| B | **Detalle y corte de caja** | 10 | Línea de detalle por visitante y corte de caja con contador y dos acumuladores correctos, todo con 2 decimales. | Corte de caja correcto con el detalle incompleto. | Acumuladores con errores (por ejemplo, reiniciados dentro del ciclo). | Sin detalle ni corte de caja. |
| C | **Casos de prueba** | 15 | Los 3 casos ejecutados, con total esperado y obtenido; caso propio que prueba el descuento único; bugs encontrados documentados. | 3 casos sin el caso propio, o comparación incompleta. | Solo 1 o 2 casos. | No los incluye o el notebook no está ejecutado. |
| D | **Estructura y README** | 7 | Mismo repositorio del curso, carpeta `semana2/` con ambos archivos y README actualizado. | Fallas menores de estructura o README sin actualizar. | Archivos fuera de `semana2/`. | Repositorio nuevo o privado, o sin liga. |
| D | **Historial de commits** | 8 | 3 o más commits progresivos con mensajes descriptivos. | 3 commits con mensajes poco descriptivos. | 1 o 2 commits. | Sin commits de la semana 2. |
| | **TOTAL** | **100** | | | | |

---

## 6. Checklist antes de entregar

- [ ] Mi tabla de decisión tiene 6 casos y resuelve al profesor de 65 años.
- [ ] Mi diagrama tiene una flecha de regreso (el ciclo) y el rombo de `fin`.
- [ ] Probé las edades límite: 2, 3, 17, 18, 59 y 60.
- [ ] Escribí `-5` y el programa lo rechazó **sin contarlo** como visitante.
- [ ] Escribí `fin` al inicio y el corte de caja salió en $0.00 sin errores.
- [ ] Mi notebook está ejecutado y se ven las salidas en GitHub.
- [ ] Tengo 3 commits o más de la semana 2, en el mismo repositorio del curso.

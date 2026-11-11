# 25 EJERCICIOS DE PRÁCTICA EN CLASE — SEMANA 5

**Curso:** Fundamentos de programación
**Alcance:** tuplas, diccionarios, excepciones y strings.

Se resuelven **en clase**, en `semana5/practica.ipynb`. **No son evaluables**, pero cada bloque entrena una sección de la Actividad 4.

**Nivel:** 🟢 calentamiento · 🟡 en forma · 🔴 modo experto

---

## BLOQUE T · TUPLAS (lunes)

### T1 🟢 La fecha del concierto
Crea `fecha = (13, 11, 2026)`. Muestra el día, el año y cuántos elementos tiene.
**Salida:**
```
13
2026
3
```

### T2 🟢 Coordenadas de la rodada
Desempaqueta `punto = (20.59, -100.39)` en las variables `lat` y `lon` en una sola línea y muéstralas.
**Salida:** `Latitud: 20.59 · Longitud: -100.39`

### T3 🟡 ¿Lista o tupla?
Para cada dato, decide si usarías **lista** o **tupla** y explica por qué en una celda Markdown:
1. Los días de la semana.
2. El carrito de compras de una tienda en línea.
3. Las coordenadas de un punto en el mapa.
4. Tu playlist favorita.
5. Tu fecha de nacimiento.

### T4 🟡 El disco ya grabado
Dada `disco = ("Intro", "Riff")`, intenta agregar `"Solo"` con `append()` y observa el error. Después crea una **tupla nueva** que sí lo incluya.
**Salida:**
```
AttributeError: 'tuple' object has no attribute 'append'
('Intro', 'Riff', 'Solo')
```

### T5 🟡 El podio
Dada `puntajes = (7, 10, 6, 9)`, conviértela en lista, ordénala de mayor a menor y muestra solo los 3 primeros.
**Salida:** `[10, 9, 7]`
💡 Pista: `lista[:3]` toma los 3 primeros elementos.

### T6 🔴 La gira
Dada `gira = (("Qro", 15), ("Mty", 22), ("Gdl", 29))`, recórrela con un `for` desempaquetando cada pareja.
**Salida:**
```
15 nov: Qro
22 nov: Mty
29 nov: Gdl
```

---

## BLOQUE D · DICCIONARIOS (martes)

### D1 🟢 Precios del merch
Crea `precios = {"playera": 350, "gorra": 220, "parche": 80}`. Muestra el precio de la gorra, agrega `"sudadera"` a $650 y muestra cuántos productos hay.
**Salida:**
```
220
4
```

### D2 🟢 Inventario
Dado `stock = {"playera": 10}`, se venden 3 playeras. Actualiza el valor y muestra el diccionario.
**Salida:** `{'playera': 7}`

### D3 🟡 La lista de precios
Con el diccionario de D1, recórrelo con `items()` y muestra cada producto con su precio.
**Salida:**
```
playera: $350
gorra: $220
parche: $80
sudadera: $650
```

### D4 🟡 ¿Qué género domina?
Dada `generos = ["metal", "rock", "metal", "punk", "metal"]`, cuenta cuántas veces aparece cada uno usando un diccionario que **empieza vacío**.
**Salida:** `{'metal': 3, 'rock': 1, 'punk': 1}`
💡 Pista: si el género ya está en el diccionario, súmale 1; si no, créalo con 1.

### D5 🟡 Mini traductor
Con `traducciones = {"hello": "hola", "bye": "adiós"}`, usa `get()` para traducir `"thanks"` sin que truene.
**Salida:** `No conozco esa palabra`

### D6 🔴 El ticket del merch
Con `precios` (de D1) y `carrito = {"playera": 2, "parche": 3}`, calcula el total del carrito recorriéndolo con `items()`.
**Salida:** `Total: $940`

---

## BLOQUE E · EXCEPCIONES (miércoles)

### E1 🟢 Ponle casco
Convierte `"dos"` a entero dentro de un `try` y atrapa el error con un mensaje amable.
**Salida:** `Eso no es un número`

### E2 🟢 Identifica la excepción
Sin ejecutarlas, predice qué excepción lanza cada línea. Después compruébalo con un `try` / `except Exception as e` que muestre `type(e).__name__`.
```python
int("")
10 / 0
[1, 2][5]
{"a": 1}["b"]
"a" + 1
```
**Salida:** `ValueError`, `ZeroDivisionError`, `IndexError`, `KeyError`, `TypeError`

### E3 🟡 Promedio seguro
Calcula el promedio de `notas = []` (lista vacía) con `sum(notas) / len(notas)`. Atrapa el error específico con un mensaje claro.
**Salida:** `No hay calificaciones registradas`

### E4 🟡 Taquilla con validación
Pide cuántos boletos quiere el usuario. Repite la pregunta mientras escriba algo que no sea número **o** un número fuera del rango 1 a 6.
**Entrada:** `dos`, `8`, `4`
**Salida:**
```
Escribe un número
Máximo 6 boletos por persona
Compraste 4 boletos
```

### E5 🔴 Tienda a prueba de errores
Con el diccionario `precios`, pide un producto y muestra su precio. Si el producto no existe, atrapa el `KeyError`.
**Entrada:** `gorra` → **Salida:** `La gorra cuesta $220`
**Entrada:** `taza` → **Salida:** `No vendemos eso`

---

## BLOQUE S · STRINGS (jueves)

### S1 🟢 El cartel
Con `banda = "iron maiden"`, muéstrala en mayúsculas, con formato de título y su longitud.
**Salida:**
```
IRON MAIDEN
Iron Maiden
11
```

### S2 🟢 Cambio de sede
Reemplaza `"Monterrey"` por `"Querétaro"` en `"La gira inicia en Monterrey"`.
**Salida:** `La gira inicia en Querétaro`

### S3 🟡 Palabras y letras
Para `frase = "el metal nunca muere"`, muestra cuántas palabras tiene, cuántos caracteres en total y cuántas letras sin contar espacios.
**Salida:**
```
Palabras: 4
Caracteres: 20
Letras: 17
```

### S4 🟡 Limpia la entrada
El usuario escribe `"  METALLICA "`. Límpialo con `strip()` y `title()` y compruébalo contra `"Metallica"`.
**Salida:**
```
Metallica
True
```

### S5 🟡 ¿Lo menciona?
Para `texto = "me gusta el rock"`, comprueba con `in` si contiene `"rock"` y con `find()` en qué posición empieza. Haz lo mismo con `"jazz"`.
**Salida:**
```
True 12
False -1
```

### S6 🔴 Iniciales
Con `split()`, obtén las iniciales de `"Bruce Dickinson"`.
**Salida:** `B.D.`

---

## BLOQUE B · DETECTIVE DE BUGS (viernes)

### B1 🟡 La clave fantasma
```python
contactos = {"Ana": "555-01", "Luis": "555-02"}
print(contactos["Pedro"])
```
¿Qué error aparece y por qué? Corrígelo de **dos formas distintas**: con `in` y con `get()`.

### B2 🔴 El casco que tapa los ojos
El usuario escribe `20` y el programa responde "Escribe un número". ¡Pero 20 sí es un número!
```python
try:
    edad = int(input("Edad: "))
    print(f"Tienes {edda} años")
except:
    print("Escribe un número")
```
Encuentra el verdadero error, explica por qué el `except:` sin tipo lo escondió y corrígelo.
💡 Pista: cambia `except:` por `except ValueError:` y vuelve a ejecutar.

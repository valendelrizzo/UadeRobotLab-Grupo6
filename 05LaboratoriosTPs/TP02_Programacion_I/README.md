# Informe Técnico: Controlador de Misiones (`mi_tp02.py`)

**Universidad Argentina de la Empresa (UADE)**  
**Materia:** Programación I — Trabajo Práctico N.° 2  
**Equipo:** Grupo 6 (`UadeRobotLab-Grupo6`)

---

## 1. Objetivo del Desarrollo

El trabajo realizado por el grupo consistió en programar el controlador de misiones del robot dentro del archivo principal del proyecto. El objetivo de este desarrollo es contar con un programa que reciba una lista de órdenes, verifique que cada instrucción sea segura y esté bien armada antes de enviarla al robot, ejecute únicamente los movimientos válidos y guarde un registro de todo lo ocurrido durante la misión.

---

## 2. Validación de Comandos (Parte 1)

Para evitar que el robot reciba órdenes inexistentes o valores fuera de límite, el programa define desde el inicio cuáles son las únicas cuatro acciones permitidas (**avanzar**, **girar**, **detenerse** y **saludar**) y cuántos datos necesita cada una para funcionar.

Cada vez que el controlador analiza una orden, la pasa por cuatro controles consecutivos:

1. **Existencia del comando:** Verifica que la instrucción no esté vacía y que su nombre coincida con alguna de las cuatro acciones permitidas. Si no existe, la rechaza con un código de error específico.
2. **Cantidad de datos:** Comprueba que la orden tenga la cantidad exacta de elementos que requiere esa acción (las órdenes de movimiento necesitan ir acompañadas de velocidad y tiempo, mientras que detenerse y saludar no llevan datos adicionales).
3. **Tipo de dato:** En los comandos que llevan velocidad y tiempo, revisa que esos valores sean efectivamente números y no texto u otro tipo de dato inválido.
4. **Límites de seguridad:** Controla que ni la velocidad ni el tiempo superen los topes máximos permitidos para avanzar y girar, y que la duración no sea un número negativo.

Si la instrucción falla en alguno de estos pasos, la validación devuelve un número negativo distinto según el tipo de error encontrado. Si supera todas las revisiones sin problemas, devuelve un valor positivo indicando que el comando está aprobado.

---

## 3. Ejecución y Recorrido de la Misión (Partes 2 y 3)

Una vez resuelta la validación, el programa divide el manejo de las órdenes en dos etapas:

* **Ejecución individual:** Antes de mover el robot, esta etapa consulta el resultado de la validación. Si el comando fue rechazado, lo descarta de inmediato y no hace nada. Si fue aprobado, identifica cuál de las cuatro acciones se pidió y le envía la orden correspondiente al robot con sus respectivos valores.
* **Recorrido de la misión completa:** El controlador recorre la lista de comandos de la misión uno por uno de principio a fin. Por cada elemento, evalúa si es válido y, solo en caso afirmativo, lo manda a ejecutar. De esta manera, si en el medio de la lista aparece un comando con errores, el programa simplemente lo saltea sin frenar el resto de la misión. Al mismo tiempo, guarda en una lista de historial cada comando junto con el código que arrojó su validación, tanto si se ejecutó como si fue rechazado.

---

## 4. Reporte y Flujo Principal (Parte 4 y Cierre)

En la última parte, el programa toma el historial acumulado durante todo el recorrido y lo muestra por pantalla para dejar constancia de qué ocurrió con cada orden de la misión.

Finalmente, el bloque principal se encarga de conectar al robot al iniciar el programa, poner en marcha la misión elegida y generar el reporte. Toda esta secuencia se ejecuta dentro de una estructura protegida que garantiza que, al terminar la misión o ante cualquier interrupción inesperada, el robot reciba siempre la orden de detenerse por completo y desconectarse de forma segura.
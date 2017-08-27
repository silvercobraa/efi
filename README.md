# EmojiFuck Interpreter

Presentando EmojiFuck, una variante del lenguaje de programación Brainfuck y su intérprete, efi (EmojiFuck Interpreter).
EmojiFuck funciona moviendo un puntero sobre una cinta de 30000 celdas, todas incicialmente en cero.
Consta de 8 instrucciones:
😂: Mueve el puntero una celda hacia la derecha.
👌: Mueve el puntero una celda hacia la izquierda.
💦: Incrementa el valor de la celda actual en una unidad.
💯: Decrementa el valor de la celda actual en una unidad.
🔥: Lee un caracter por entrada estándar y almacena su valor en la celda actual.
😭: Imprime en la salida estándar el caracter cuyo valor es el de la celda actual.
🍆: Inicia un ciclo iterativo, siempre y cuando el valor de la celda actual sea distinto de cero.
✔: Marca el fin del bloque de un ciclo iterativo.

Para ejecutar un programa EmojiFuck existente, utilizar el comando:
$ python efi.py nombre_programa.ef

Programa de ejemplo (Hello World!):
💦💦💦💦💦💦💦💦🍆😂💦💦💦💦🍆😂💦💦😂💦💦💦😂💦💦💦😂💦👌👌👌👌💯✔😂💦😂💦😂💯😂😂💦🍆👌✔👌💯✔😂😂😭😂💯💯💯😭💦💦💦💦💦💦💦😭😭💦💦💦😭😂😂😭👌💯😭👌😭💦💦💦😭💯💯💯💯💯💯😭💯💯💯💯💯💯💯💯😭😂😂💦😭😂💦💦😭

Existe un mapeo uno a uno entre los programas escritos en EmojiFuck y Brainfuck. Para convertir un programa Brainfuck, utilizar la herramienta bftoef.py
Ejemplo:
$ python btoef.py programa_brainfuck.b > programa_emojifuck.ef
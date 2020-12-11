// Esto es un comentario

/*
Esto es un comentario
de varias líneas.
*/

// A continuación se muestra un mensaje
alert("mensaje de prueba");

// Ejemplo de If
function factorial(n) {
    if ((n == 0) || (n == 1))
      return 1;
    else
      return (n * factorial(n - 1));
  }

// Ejemplo de for
for (var i = 0; i < 9; i++) {
    n += i;
    mifuncion(n);
 }

 // Ejemplo de While
num1 = 0;
num2 = 0;
while (num1 < 3) {
  num1 ++;
  num2 += num1;
}

// Ejemplo de Switch Case
switch (diaSemana){
  case 1:
      alert('Hoy es lunes');
      break;
  case 2:
      alert('Hoy es martes');
      break;
  case 3:
      alert('Hoy es miercoles');
      break;
  case 4:
      alert('Hoy es jueves');
      break;
  case 5:
      alert('Hoy es viernes');
      break;
  case 6:
  case 7:
      alert('Es fin de semana');
      break;
  default:
      alert('Ese dia no existe');
      break;
}
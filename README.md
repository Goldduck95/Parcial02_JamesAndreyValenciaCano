# Parcial02_JamesAndreyValenciaCano
**Respuesta del parcial**
Para que el servicio se comunica con otro a través de solicitudes HTTP, cambiaría el diseño. Luego de calcular el factorial, mandaría los datos (número, resultado y paridad) al servicio de historial mediante una solicitud POST. Así, cada servicio conserva su responsabilidad de manera independiente: uno se encarga del cálculo y el otro guarda los datos en la base de datos, lo que garantiza un diseño escalable y desacoplado.

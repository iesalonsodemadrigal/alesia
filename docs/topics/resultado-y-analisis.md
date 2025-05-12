# Resultado y Análisis

A lo largo de esta investigación se han llevado a cabo cuatro fases experimentales claramente definidas. En cada una de
ellas se ha validado una parte imporante de la hipótesis principal del estudio: que es posible traducir entre la lengua
oral y la Lengua de Signos Española (LSE), y viceversa, mediante el uso de tecnologías basadas en inteligencia
artificial. A continuación, se detallan los resultados obtenidos por fase:

## Fase I: Conversión voz-texto y texto-voz

- Se ha implementado un sistema de reconocimiento de voz con modelos de IA que permite convertir en tiempo real mensajes
  orales en texto con una precisión media superior al 90% en pruebas controladas.
- La conversión de texto a voz también ha sido satisfactoria, generando un tono natural y comprensible en menos de un
  segundo de latencia.
- Este rendimiento permite mantener interacciones fluidas, lo cual era uno de los requisitos clave del sistema.

## Fase II: Conversión de la gramática española a la gramática LSE

- Se ha logrado desarrollar un módulo de reestructuración gramatical capaz de transformar frases en español a una
  estructura adecuada para su interpretación en LSE.
- La transformación incluye la eliminación de artículos, reordenamiento sintáctico y simplificación de frases, lo que
  facilita la traducción posterior a signos.
- El proceso inverso (de LSE a español oral estructurado) también ha sido posible, mediante reglas inversas
  implementadas en pruebas experimentales.
- La validez de estas transformaciones ha sido confirmada por intérpretes profesionales de LSE, quienes han calificado
  el resultado como coherente y comprensible.

## Fase III: Interpretación LSE en modelo 2D

- Se ha realizado un análisis de más de 600 signos en LSE mediante la herramienta MediaPipe, extrayendo con éxito las
  coordenadas de las manos y el cuerpo.
- Estas coordenadas se han estructurado en una base de datos indexada que permite la recuperación rápida de cada signo.
- Al reconstruir frases completas combinando signos, se ha conseguido mostrar oraciones completas en un modelo 2D, a
  partir de mensajes orales convertidos a texto.
- La precisión de los movimientos es suficiente para que el mensaje sea identificable por usuarios sordos e intérpretes
  consultados.

## Fase IV: Interpretación LSE con avatar 3D

- Se ha desarrollado un avatar 3D en Unity capaz de interpretar las coordenadas obtenidas en MediaPipe y reproducirlas
  como animaciones fluidas.
- El resultado es un entorno tridimensional donde el avatar ejecuta en tiempo real los signos correspondientes a las
  frases reconocidas.
- El modelo tridimensional permite mayor expresividad y comprensión visual, acercando la experiencia a una
  interpretación humana.
- Esta fase sigue progresando.

Los resultados obtenidos permiten confirmar que:

- La tecnología actual permite automatizar la traducción entre lengua oral y LSE, de manera funcional y comprensible.
- La fluidez, precisión y velocidad del sistema son suficientes para mantener una conversación básica entre una persona
  oyente y una persona con problemas auditivos.
- La combinación de herramientas libres o accesibles (MediaPipe, Unity, motores de IA) demuestra que es viable
  desarrollar soluciones accesibles sin requerir grandes inversiones.
- El enfoque modular del sistema (voz ↔ texto, gramática, signos, animación) facilita su escalabilidad y mejora
  continua.
- Además, el desarrollo ha permitido a los alumnos implicarse activamente en un proyecto con impacto social, integrando
  conocimientos de programación, inteligencia artificial, lenguaje de signos, visión artificial y desarrollo 3D.

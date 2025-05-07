# Slide 1: Presentación
---

# Slide 2: Problema (Ian)

Te despiertas, desayunas y vas a clase...

Intentas comunicarte con tu profesor, realizar actividades en equipo, pedir ayuda a un compañero... pero nadie te
entiende.

Esta es la realidad diaria de miles de personas con discapacidad auditiva que utilizan la Lengua de Signos como medio de
comunicación.

Personas que se enfrentan a barreras de comunicación constantes que limitan su acceso a la educación, la salud o el
empleo.

# Slide 3: Alesia (Ian)

Frente al silencio, nace la innovación.

Alesia es nuestro proyecto de investigación aplicada: una aplicación capaz de escuchar una conversación, entenderla y
traducirla automáticamente a Lengua de Signos Española.

# Slide 4: Estructura app (Ian)

El proyecto es multiplataforma, se puede usar en un móvil, un reloj e incluso en unas gafas inteligentes.

Utilizamos Inteligencia Artificial para convertir voz en texto, reorganizar el mensaje con la gramática de la lengua de
signos y representar la interpretación en un avatar 3D llamada Alesia.

Vamos ahora a explicar las cuatro fases que forman el desarrollo experimental.

# Slide 5 (David)

Para que Alesia pueda interpretar, lo primero es escuchar y entender lo que se dice.

Analizamos diferentes herramientas de transcripción automática y seleccionamos la más adecuada, equilibrando velocidad y
precisión, para asegurar una experiencia fluida y en tiempo real.

# Slide 6 (David)

Ya tenemos el mensaje en texto… pero no basta con traducir palabra por palabra.

La Lengua de Signos no es una traducción literal del español. Tiene su propio orden, sus propias reglas. Por ejemplo, no
se dice 'Hola, ¿cómo estáis hoy? espero que te encuentres bien.', sino algo como 'Hola. Tu como hoy yo esperar tu
bien.'.

Para resolver esto, entrenamos un modelo de Inteligencia Artificial capaz de transformar la frase original al formato
correcto para que pueda ser entendida en lengua de signos.

# Slide 7 (Ales)

Aquí empieza la magia. Esta es probablemente la parte más compleja del proyecto: transformar los
movimientos humanos en datos que la máquina pueda entender.

Hemos desarrollado un algoritmo capaz de analizar vídeos del diccionario de lengua de signos y extraer las coordenadas
en 3D de cada parte del cuerpo.

Con esta información, creamos una base de datos que nos permite buscar una palabra y obtener su traducción en
coordenadas.

# Slide 8 (Ales)

-------- Relacionada con Slide 7: Se ve un vídeo con las coordenadas

# Slide 9 (David)

Esta es la parte final del proceso. Obtenemos las coordenadas de nuestra base de datos y pasamos esta información a
nuestro avatar 3D: Alesia.

El resultado es una representación visual del mensaje de voz ahora accesible en Lengua de Signos.

La validación de estas fases representan la parte cuantitativa de nuestro enfoque mixto de investigación.

# Slide 10 (David)

El camino hasta aquí no ha sido fácil. Hemos pasado muchas horas estudiando la lengua de signos, analizando vídeos,
desarrollando algoritmos para transformar coordenadas.

Comenzamos con algo sencillo: una figura en 2D. Pero sabíamos que eso no era suficiente.

Así que seguimos mejorando, iterando, y finalmente dimos el salto a un entorno en 3D donde cada signo cobra vida con
mayor realismo y claridad.

Un vídeo de apenas 10 segundos pero que a nosotros nos ha llevado un curso.

# Slide 11 (David)

Aquí podéis ver la precisión y el realismo de Alesia.
A la izquierda, una persona interpretando la palabra 'hola' en Lengua de Signos.
A la derecha, Alesia reproduciendo ese mismo signo a partir de las coordenadas generadas.

# Slide 12 (Ian)

Para evaluar nuestro MVP, diseñamos un cuestionario propio.
Nos basamos en cuestionarios ya validadas, pero adaptadas a las características específicas de nuestro proyecto.

Estamos muy orgullosos de los resultados. La valoración media ha sido positiva.
Como mejora destacada, señalan la falta de expresión facial, algo fundamental en lengua de signos.
Una mejora que vemos viable desarrollar ya que la falta de expresión de Alesia se debe a que los vídeos que usamos como
base eran solo de palabras, sin expresión.

Este cuestionario representa el enfoque cualitativo de nuestra investigación. (: recoger opiniones directas de
intérpretes
en lengua de signos) (tras ver a Alesia interpretar frases).

# Slide 13 (Ales)

Nuestra investigación demuestra que sí es posible desarrollar una aplicación capaz de traducir la lengua hablada a la
Lengua de Signos en tiempo real.

Hemos visto que la expresión facial es una parte clave que aún debemos incorporar, pero ya sabemos como hacerlo.

La Inteligencia Artificial ha sido fundamental en cada fase del proyecto: sin ella, esto no sería posible.

Y lo más importante: Alesia no es solo una herramienta tecnológica.
Es una herramienta para la igualdad de oportunidades (inclusión social).

# Slide 14 (Ales)

Queremos terminar compartiendo algo que nos hace especial ilusión.

En febrero de 2025, NVIDIA presentó un proyecto muy similar al nuestro: una herramienta para traducir la lengua hablada
a la lengua de signos.

Nosotros empezamos en octubre de 2024, con menos recursos pero con la misma visión.

Ver que una gran empresa apuesta por lo mismo que nosotros nos confirma algo: vamos por el buen camino.

Y eso nos anima a seguir investigando. Hoy como alumnos, pero mañana como desarrolladores, creemos firmemente que la
tecnología debe estar al servicio de la inclusión de todas las personas.

# Slide 15:

Muchas gracias (representación signo 'gracias')

# Otras ideas:

- Usamos unity por ser menos costoso que la generación de vídeos con IA.
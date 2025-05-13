# Fase III: Interpretación LSE en modelo 2D

## Objetivo

El objetivo de este módulo del proyecto consiste en el paso de texto, ya sea introducido por el usuario o el generado
por el módulo voz-texto, a imagen ya sea como una sucesión de imágenes estáticas o como un video.

Para lograr esto en un primer momento consideramos el uso de inteligencia artificial generativa debido a los avances que
se han hecho a lo largo del último año en este campo. Sin embargo, planteaba distintos desafíos que elaboraremos más
adelante. Para solventarlos y continuar con el desarrollo del proyecto llegamos a una conclusión que se convertiría en
un punto de inflexión haciendo uso de las distintas librerías de visión computacional de la suite de aprendizaje
automático conocida como MediaPipe.

Durante todo el proyecto debemos tener en cuenta que para poder llevar esto a cabo necesitamos tener una cantidad de
datos lo suficientemente grande para poder generar al menos entre 600-800 conceptos del LSE. Esto es crucial ya que para
poder llevar a cabo una implementación con cualquiera de las herramientas debemos tener en cuenta la facilidad con la
cual podemos llevar esto a cabo.

## Análisis y evaluación de las herramientas existentes

### Inteligencia Artificial Generativa

Nuestro primer acercamiento al planteamiento del proyecto. Brevemente, la inteligencia artificial generativa o conocida
también como GenAI es un tipo de inteligencia artificial capa de crear contenido original e ideas como conversaciones,
historias, imágenes, videos y música en respuesta a instrucciones del usuario. Para lograr esto se utilizan modelos que
han sido previamente entrenados con datos ya existentes, los codifican y con ello consiguen enlazar datos relacionados
en cantidades masivas.

Debido a los avances en el campo de la GenAI de imágenes y video a lo largo del último año se valoró utilizar esta
herramienta debido a la posibilidad de crear con ella imágenes realistas y adaptables a distintas instrucciones que
muestren los distintos patrones dentro de la lengua de signos española.

Se investigó acerca de Sora, el modelo creado por Open AI para la creación de videos, pero siendo descartado rápidamente
debido al alto coste económico que podría suponer para un proyecto de estas dimensiones que necesitaría de una creación
constante de videos en corto tiempo además de un problema de precisión para mantener una estética homogénea y
comprensible a lo largo de todos los videos generados. También cabe destacar que un problema al que se enfrentan los
modelos de generación de video consiste en la falta de consistencia con la física del mundo real y aunque para nuestro
caso de uso no sería un gran problema debido a la naturaleza de los videos (una persona gesticulando sobre un fondo de
un color concreto) es algo para tener en cuenta en caso de tener que generar secuencias más largas

Esto nos dejaría con generación de imágenes que tienen una base más estable sobre la que trabajar ya que han tenido más
tiempo para desarrollarse. Se valoran algunas opciones principales después de una rápida investigación. DALLE,
proporcionada con el plan gratuito de ChatGPT(OpenAI), Midjourney y algunas implementaciones disponibles en la
plataforma Huggin Face de Stable Diffusion concretamente de una que permite modificar parámetros sobre la postura,
crucial para que los gestos del lenguaje de signos sea legible.

Descartamos Midjourney y derivados por su alto coste. Y por otro lado comparamos las características de los otros dos:

![Tabla 16: Características de aplicaciones](tabla_ia_generativa.jpeg)

Llegados a este punto queda analizar Stabble Diffusion + Control Net Al ser la herramienta utilizada. Evaluar y reseñar
el uso que pudimos darle.

Primero de todo la información disponible acerca de este enfoque es prometedora, un vistazo rápido a la web y a las
distintas documentaciones mantenidas por la comunidad asi como la alojada en Huggin Face nos deja ver el potencial de
esta herramienta sin embargo nos enfrentamos a distintos desafíos:

- Precisión: incluso en un modelo preciso como este nos damos con que necesitamos una generación de una secuencia grande
  de imágenes para poder reproducir los distintos gestos para poder llevar a cabo una palabra, un concepto, una frase.
  Mantener la consistencia a lo largo de las distintas imágenes puede considerarse un desafío lo suficientemente serio
  para valorar el uso de esta herramienta.
- Complejidad: si bien la complejidad es manejable hacen falta herramientas externas como OpenPose, una librería con la
  cual controlnet crea imágenes de control, un paso intermedio entre la instrucción del usuario y el acabado final. Sin
  embargo, OpenPose a fecha de realizar esta investigación no se encontraba optimizado para tarjetas gráficas del
  fabricante AMD el conocimiento técnico para llevar a cabo la implementación sugerida por la documentación se escapaba
  de nuestros límites en aquel momento.

Para añadir a esto debemos tener en cuenta la integración de este modelo en él marco general de lo que nuestra
aplicación plantea conseguir.

Las pruebas que hicimos al respecto con esta herramienta en concreto no tuvieron el resultado esperado. De este modo y
valorando el aumento repentino de complejidad, la falta de algunos conocimientos técnicos, la posible falta de precisión
y otras limitaciones de tiempo, así como la integración en el proyecto general de esta herramienta decidimos dejarla de
lado pero no descartamos que junto a los futuros avances de este campo de la inteligencia artificial equipos con mayores
recursos que los nuestros puedan desarrollar un proyecto similar con esta herramienta.

### MediaPipe

Segunda herramienta planteada para llevar a cabo la implementación del proyecto. Originalmente se valora como
complemento mejorar la precisión de las poses generadas por modelos de IA generativa.

MediaPipe es un framework desarrollado por Google ,de código abierto que cuenta con distintas soluciones optimizadas
para nuestro problema a resolver ya que incluye reconocimiento facial, detección de manos y segmentación de la pose.

Se considera como una herramienta válida para el proyecto después de extraer la pose de varios videos de bibliotecas de
datos sobre lenguaje de signos extrayendo los landamarks de las manos y el cuerpo en un formato JSON. La facilidad para
integrarlo con Python lenguaje usado para este tipo de trabajos relacionados con inteligencia artificial y machine
learning, y su mayor eficiencia en términos de rendimiento frente a las opciones de IA. En las primeras pruebas se
analizaron videos de 1,5,30,60 y 120 segundos sin superar los segundos de tiempo de procesado y sin prácticamente
consumir recursos de la maquina donde ejecutábamos el programa. También fue probado en dispositivos de menor rendimiento
obteniendo resultados similares.

Lo que consolidó la elección de Mediapipe fue la idea de que si con un pequeño script éramos capaces de extraer la pose
de todos los frames de un video, podríamos utilizar esas mismas coordenadas para reproducir un modelo 2D a partir del
fichero generado. Esta premisa se convirtió en la base del desarrollo posterior del proyecto.
Ventajas de Mediapipe:

- Eficiencia y rapidez: Procesa imágenes en tiempo real sin necesidad de hardware especializado.
- Bajo consumo de recursos: Puede ejecutarse en CPU sin afectar significativamente el rendimiento del sistema.
- Fácil integración con Python: Dispone de una API sencilla y bien documentada.
- Precisión más que aceptable para detección de manos y poses: Genera coordenadas en 3D que pueden utilizarse para
  representar movimientos.
- No requiere entrenamiento adicional: A diferencia de modelos generativos, Mediapipe ya viene preentrenado y listo para
  su uso.
  Limitaciones de Mediapipe
- Dependencia de la calidad del video: Factores como iluminación, resolución y ángulo de la cámara pueden afectar la
  precisión de la detección.
- Falta de coherencia temporal en ciertos casos: En algunos movimientos rápidos, los landmarks pueden sufrir pequeñas
  variaciones, lo que genera inconsistencias en la secuencia de poses.

Comparación con IA Generativa: Aunque Mediapipe es más rápido y fácil de usar, quizá no ofrece la flexibilidad
creativa de modelos generativos, que pueden generar imágenes más detalladas y estilizadas, pero como hemos analizado
previamente las ventajas de esta herramienta superan con creces dicha limitación
Lo que consolidó la elección de Mediapipe fue la idea de que si con un pequeño script éramos capaces de extraer la
pose de todos los frames de un video, podríamos utilizar esas mismas coordenadas para reproducir un modelo 2D a partir
del
fichero generado. Esta premisa se convirtió en la base del desarrollo posterior del proyecto.

**Ventajas de Mediapipe:**

- Eficiencia y rapidez: Procesa imágenes en tiempo real sin necesidad de hardware especializado.
- Bajo consumo de recursos: Puede ejecutarse en CPU sin afectar significativamente el rendimiento del sistema.
- Fácil integración con Python: Dispone de una API sencilla y bien documentada.
- Precisión más que aceptable para detección de manos y poses: Genera coordenadas en 3D que pueden utilizarse para
  representar movimientos.
- No requiere entrenamiento adicional: A diferencia de modelos generativos, Mediapipe ya viene preentrenado y listo
  para su uso.

**Limitaciones de Mediapipe:**

- Dependencia de la calidad del video: Factores como iluminación, resolución y ángulo de la cámara pueden afectar la
  precisión de la detección.
- Falta de coherencia temporal en ciertos casos: En algunos movimientos rápidos, los landmarks pueden sufrir pequeñas
  variaciones, lo que genera inconsistencias en la secuencia de poses.
- Comparación con IA Generativa: Aunque Mediapipe es más rápido y fácil de usar, quizá no ofrece la flexibilidad
  creativa de modelos generativos, que pueden generar imágenes más detalladas y estilizadas, pero como hemos analizado
  previamente las ventajas de esta herramienta superan con creces dicha limitación.

## Implementación Técnica

La implementación de Mediapipe en el proyecto se basó en la extracción de landmarks a partir de videos de referencia. Se
desarrolló un script en Python utilizando OpenCV y Mediapipe para procesar cada frame del video y guardar los datos en
formato JSON.

El flujo de trabajo del script es el siguiente:

1. Se carga el video de entrada y se inicializan los modelos de Mediapipe (detección de pose y manos).
2. Se extraen frames a intervalos regulares para su procesamiento.
3. Se aplican los modelos de Mediapipe para detectar los landmarks de pose y manos.
4. Se almacenan las coordenadas de los landmarks en un archivo JSON.
5. Se optimiza el procesamiento para garantizar tiempos de ejecución rápidos sin comprometer la precisión.

Podemos comprobar el resultado de esta herramienta:

Análisis de un vídeo para obtener las coordenadas que intervienen en la interpretación de una palabra:
![Ejemplo del análisis de las coordenadas de un vídeo](mediapipe_1.jpg)

Coordendas obtenidas tras el análisis de un vídeo:
![Coordenadas obtenidas tras el análisis de los vídeos](ejemplo_mediapipe_2.jpeg)

Con este análisis y la implementación técnica, Mediapipe se consolidó como la mejor opción para nuestro enfoque,
permitiéndonos centrar los esfuerzos en procesar grandes volúmenes de datos para construir un diccionario visual de
lenguaje de señas.

## Implementacion del enfoque final

Para poder comprobar el funcionamiento de la herramienta escogida procedimos a programar una pequeña demostración.
Para la minidemo del proyecto, desarrollamos una pequeña aplicación dividida en tres módulos principales:

- landmarks_loader.py: Esta clase se encarga de cargar los landmarks almacenados en archivos .json. Al instanciarse,
  recibe como parámetro la ruta de la carpeta donde se encuentran estos archivos. Su función principal es organizar los
  datos en dos listas separadas: una para los landmarks del cuerpo y otra para los de la mano, devolviendo una
  estructura que contiene ambas.
- frame_renderer.py: Este módulo utiliza la librería Pygame para visualizar los landmarks extraídos. Al instanciarse,
  recibe como parámetros el tamaño de la pantalla donde se dibujarán los landmarks y los datos generados por
  landmarks_loader.py. En su constructor, también se definen las conexiones entre los puntos clave del esqueleto y las
  manos, que servirán para representar la estructura de la pose.

Para la visualización, se dibujan primero los puntos individuales en rojo, representando cada landmark, y luego se
conectan entre sí siguiendo la estructura del esqueleto y las manos.

La clase también incluye el método render_frame(), que gestiona el bucle principal de renderizado. Utiliza funciones de
Pygame como time.Clock() para controlar la velocidad de actualización, display.flip() para refrescar la pantalla y
quit() para cerrar la aplicación.

**Funcionamiento General de la Minidemo:**

Los landmarks previamente extraídos de los videos se almacenan en archivos .json, cada uno con el nombre del concepto
que representa. Para permitir la interacción del usuario con la demo, implementamos un sistema que convierte el input en
el nombre del archivo correspondiente.

Este proceso está controlado por un bucle while, que toma la frase introducida por el usuario y la descompone en
palabras individuales. Luego, busca un archivo que coincida con cada palabra. En caso de no encontrar una coincidencia
exacta, el sistema intenta combinar dos palabras y verifica nuevamente la existencia del archivo correspondiente.
Resultados y conclusiones iniciales.

Podemos comprobar el resultado de la representación del concepto “me llamo”:

![Ejemplo de una interpretación de una palabra en LSE](mediapipe_3.jpeg)

Después de obtener este resultado prometedor y con margen de mejora y tras evaluar las diferentes herramientas y
enfoques disponibles para la representación del lenguaje de signos mediante inteligencia artificial, llegamos a la
conclusión de que el uso de MediaPipe en combinación con un modelo 2D basado en landmarks es la opción más viable para
nuestro caso de uso. Este método destaca por su rapidez, bajo coste computacional y facilidad de integración,
permitiéndonos centrarnos en la recopilación y estructuración de datos.

A lo largo del proyecto, descartamos soluciones basadas en generación de imágenes mediante modelos de IA debido a
problemas de coste, precisión y consistencia. También encontramos limitaciones en el uso de técnicas avanzadas como
ControlNet, cuya implementación y ajustes requerían un nivel técnico que escapaba de nuestros recursos actuales.

Gracias a este enfoque, conseguimos una representación visual coherente del lenguaje de signos, con la posibilidad de
expandir el modelo para abarcar una mayor cantidad de conceptos. En futuras iteraciones del proyecto, se podrían
explorar mejoras como:

- Optimización del procesamiento de landmarks para aumentar la fluidez de la animación.
- Uso de redes neuronales para predecir y suavizar los movimientos entre frames.
- Integración de un sistema de traducción automática de español escrito a LSE mediante IA generativa.
- Un modelo animado en tiempo real usando las coordenadas tridimensionales de Mediapipe

La realización de este módulo sienta una base sólida para futuras investigaciones en el ámbito de la accesibilidad y la
comunicación mediante inteligencia artificial, con el objetivo de mejorar la representación y comprensión de la Lengua
de Signos Española en entornos digitales.





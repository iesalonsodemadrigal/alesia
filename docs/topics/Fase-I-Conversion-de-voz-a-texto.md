# Fase I: Conversion de voz a texto

Se busca encontrar una herramienta o modelo de transcripción a el idioma español que se adapte a las necesidades de
nuestro proyecto, teniendo en cuenta características como el tipo de entrada de audio, tiempo total de realización,
precisión (WER), si necesita de conexión a internet, cuenta con un servicio gratuito o de pago…

Se ha investigado los distintos modelos existentes que se puedan utilizar en una aplicación móvil y se han probado todos
los que estaban a nuestro alcance comparando las características antes mencionadas, descartando los que no eran
compatibles con nuestra idea de proyecto.

Además, Se ha enfatizado la importancia de minimizar el tiempo de transcripción, procurando que, en la medida de lo
posible no requiera conexión a internet y que el porcentaje de error se mantenga dentro de un margen aceptable.
Asimismo, se ha evaluado la compatibilidad de estos modelos con herramientas destinadas a la detección de sentimientos a
través del análisis del tono de voz y las expresiones faciales.

Estos modelos han sido evaluados mediante pruebas con los mismos audios, verificando las características previamente
mencionadas. Para la realización de las pruebas, se han utilizado audios de Common Voice (Mozilla), una amplia colección
de datos en español con diversidad de acentos; CHiME Dataset, un conjunto de datos diseñado para evaluar el rendimiento
en entornos con ruido; y audios propios, grabaciones experimentales realizadas en condiciones reales.

A continuación, se presentará una tabla con las características teóricas de cada modelo que paso la fase de selección
para después realizar pruebas.

![Tabla 1: Características técnicas de aplicaciones](tabla_analisis_voz.png)

![Figura 0.1: Comparativa de la tasa de error de palabras](grafica_error_apps_voz.png)

## Análisis y comparativa

El objetivo de este análisis es comparar los diferentes modelos y herramientas de transcripción de voz a texto evaluadas
en este proyecto, considerando factores clave como precisión (WER), velocidad de transcripción, requerimientos de
hardware, modo de operación (offline o en la nube), costos y compatibilidad con dispositivos móviles (Android).
La finalidad es identificar cual de estos modelos se adapta mejor a las necesidades del proyecto, optimizando la
transcripción en español sin depender de conexión a internet y asegurando un tiempo de respuesta óptimo.
Se han analizado múltiples opciones de transcripción, las cuales se pueden dividir en tres grandes categorías:

1. Modelos de IA open-source para dispositivos locales (ejecución en CPU/GPU):
    * Whisper-Tiny (Whisper.cpp)
    * Whisper-Base (Whisper.cpp)
    * DeepSpeech-Polyglot
2. Servicios de transcripción basados en la nube (requieren conexión a internet):
    * Speechmatics
    * Whisper API (OpenAI)
    * Google Speech-to-Text API
    * VEED.IO / Descript
3. Herramientas integradas en Android
    * SpeechRecognizer (nativo en Android)

Cada modelo ha sido probado en el mismo dispositivo para garantizar una comparación justa en términos de
rendimiento.

![Comparativa de modelos testeados](Comparativa de modelos testeados.png)

## Conclusión de la comparación

Tras analizar los distintos modelos de transcripción, se ha determinado que los modelos más precisos son los de Google y
OpenAI (Whisper API). Sin embargo, su implementación requiere pago por uso y conexión a internet, lo que los hace
inviables para este proyecto.

Por otro lado, Whisper-Tiny y Whisper-Base (Whisper.cpp) representan las mejores opciones gratuitas, pero presentan
demoras en la transcripción, lo que afecta su uso en aplicaciones que requieren procesamiento en tiempo real.
Finalmente, SpeechRecognizer de Android se posiciona como la mejor alternativa para este proyecto debido a su rapidez,
precisión y facilidad de integración, cumpliendo con los requisitos establecidos sin necesidad de conexión a internet ni
costos adicionales.

## Problemas encontrados en las pruebas

Durante la evaluación de cada modelo, se identificó diversas limitaciones que afectaron su viabilidad dentro del
proyecto. Uno de los principales inconvenientes fue el tiempo de transcripción. Se observo que Whisper-Tiny y
Whisper-Base presentan tiempo de procesamiento significativamente elevados en comparación con SpeechRecognizer de
Android, lo que dificulta su uso en aplicaciones que requieren una respuesta en tiempo real.

Otro aspecto critico fue el consumo de recursos. Modelos como Whisper (OpenAI) y DeepSpeech-Polyglot requieren una CPU o
GPU potente, lo que implica un alto uso de RAM y podría ralentizar el rendimiento del dispositivo. Por otro lado, los
servicios basados en la nube, como Google Speech-to-Text o Whisper API, requieren una conexión constante a internet, lo
que limita su usabilidad en entornos sin acceso estable a la red.

La compatibilidad con Android también presento un desafío. SpeechRecognizer resulto ser la única opción nativa y
altamente optimizada para este sistema operativo, facilitando su integración. En contraste, Whisper-Base y Whisper-Tiny
requieren el uso de Whisper.cpp, lo que complica su implementación en dispositivos móviles y aumenta la carga de trabajo
en términos de desarrollo.

Finalmente, el costo fue un factor determinante en la selección del modelo. Aunque Whisper API y Google Speech-to-Text
las opciones con mayor precisión, su uso implica costos elevados a largo plazo, lo que los hace inviable para este
proyecto. Del mismo modo, servicios como Speechmatics y VEED.IO requieren suscripciones o pagos por uso, lo que los
descarta como alternativas viables dentro de un presupuesto limitado.

### Resultado de las Pruebas

Se realizaron pruebas con audios de diferentes duraciones para evaluar el tiempo de transcripción y la tasa de error en
la transcripción (WER, Word Error Rate). A continuación, se presenta un resumen de los tiempos de transcripción y
precisión obtenidos con los modelos más relevantes.

![Datos sobre la transcripción probada](Datos sobre la transcripción probada.png)

## Selección de la Herramienta para la implementación del proyecto

La principal ventaja de SpeechRecognizer es su capacidad para realizar transcripciones en tiempo real sin generar
tiempos de espera prolongados, lo que resulta fundamental para garantizar una experiencia fluida en el uso de la
aplicación. A diferencia de otros modelos evaluados, su procesamiento es inmediato, lo que permite una respuesta rápida
y eficiente.

Otro factor determinante en su selección es que no requiere conexión a internet, lo que permite su funcionamiento en
cualquier entorno, sin depender de servidores externos o servicios en la nube. Esto representa una ventaja significativa
en términos de accesibilidad y privacidad, especialmente en escenarios donde la conectividad des limitada o inexistente.

Por último, su implementación en Android es gratuita y sencilla, ya que forma parte de las herramientas nativas del
sistema operativo. No es necesario instalar bibliotecas externas ni realizar configuraciones complejas, lo que facilita
su integración en el desarrollo de la aplicación y reduce la carga de trabajo en términos de implementación.

## Implementación técnica

La implementación de SpeechRecognizer en el proyecto se basó en la propia documentación de Android. Se creo una clase
que permitía utilizar la herramienta de forma sencilla, su flujo de trabajo es el siguiente:

1. Se piden permisos al usuario para utilizar el micrófono.
2. Inicializa el reconocimiento de voz.
3. Escucha al usuario cuando se presiona un botón (Start Recording)
4. Muestra la transcripción en tiempo real en la pantalla.
5. Se detiene el reconocimiento automáticamente o al presionar otro botón (Stop Recording).

## Conclusión

Aunque modelos como Whisper-Base (Whisper.cpp) y Whisper-Tiny ofrecían soluciones offline, sus tiempos de transcripción
eran excesivamente largos, lo que los hace inviables para el propósito del proyecto. En contraste, SpeechRecognizer de
Android se posiciona como la mejor opción, gracias a su rapidez y precisión, sin necesidad de hardware avanzado ni
conexión a la nube. 








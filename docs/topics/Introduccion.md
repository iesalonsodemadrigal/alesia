# Introducción

La comunicación es una necesidad fundamental del ser humano, y su ausencia genera importantes barreras en la inclusión
social, educativa y profesional de las personas con discapacidad auditiva. En España, la Lengua de Signos Española (LSE)
constituye un sistema lingüístico completo utilizado por miles de personas con problemas auditivos como medio principal
de comunicación. No obstante, la falta de herramientas accesibles que permitan la traducción automática entre la lengua
oral y la LSE sigue siendo una limitación significativa, especialmente en contextos cotidianos donde no siempre se
dispone de intérpretes.

El presente trabajo surge como una propuesta innovadora desde el ámbito educativo, en el marco de un Ciclo Formativo de
Grado Superior en Desarrollo de Aplicaciones Multiplataforma. El objetivo principal es explorar la viabilidad técnica de
desarrollar un sistema de traducción automática entre la lengua oral y la LSE mediante el uso de tecnologías basadas en
inteligencia artificial (IA).

El estudio se enmarca dentro de la investigación aplicada con enfoque mixto y carácter experimental. Se ha
desarrollado un prototipo funcional denominado ALESIA (Asistente para la interpretación a Lenguaje de Signos con
Inteligencia Artificial), que integra módulos de reconocimiento y síntesis de voz, adaptación gramatical al lenguaje de
signos, análisis visual con visión artificial y representación gráfica 2D y 3D.

## Marco teórico

La investigación se apoya en un conjunto de disciplinas interrelacionadas que conforman el núcleo tecnológico del
sistema ALESIA: la inteligencia artificial, el procesamiento del lenguaje natural (PLN), la lingüística aplicada a la
LSE, la visión artificial y el modelado gráfico tridimensional.

### Inteligencia Artificial y Procesamiento del Lenguaje Natural

La inteligencia artificial ha experimentado un desarrollo vertiginoso en los últimos años, especialmente gracias al uso
de modelos de aprendizaje profundo. Dentro de este campo, el procesamiento del lenguaje natural (PLN) permite a las
máquinas comprender y generar lenguaje humano.

### Lengua de Signos Española (LSE)

La LSE es una lengua visoespacial que presenta una estructura gramatical distinta al español oral. Se caracteriza por el
uso de parámetros como la configuración y orientación de las manos, el punto de articulación, el movimiento y la
expresión facial. La correcta traducción a LSE requiere no solo una transcripción textual, sino una adaptación
morfosintáctica que respete las convenciones gramaticales de esta lengua.

### Visión Artificial

La visión por computador permite a las máquinas interpretar imágenes del entorno. En este proyecto, se utiliza
MediaPipe, una biblioteca de Google capaz de identificar puntos clave del cuerpo, rostro y manos en tiempo real. Esta
herramienta posibilita el registro preciso de los movimientos corporales necesarios para representar signos en LSE.

### Modelado Gráfico y Representación 3D

Para lograr una representación visual comprensible, se ha empleado el motor gráfico Unity, ampliamente utilizado en
desarrollo de videojuegos y simulaciones. Unity permite construir avatares animados que reproducen las coordenadas
obtenidas por MediaPipe, ofreciendo una experiencia comunicativa visual realista y accesible.

### Estado del Arte

Existen iniciativas previas orientadas a la traducción entre lengua oral y lengua de signos, particularmente en ASL (
American Sign Language), como SignAll o HandTalk. Sin embargo, en el caso del español y la LSE, las investigaciones y
soluciones prácticas son escasas. El proyecto ALESIA contribuye a llenar ese vacío, al integrar tecnologías accesibles y
validadas por profesionales de la LSE, presentando un enfoque modular, escalable y replicable.


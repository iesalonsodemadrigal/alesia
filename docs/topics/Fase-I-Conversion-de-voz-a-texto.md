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



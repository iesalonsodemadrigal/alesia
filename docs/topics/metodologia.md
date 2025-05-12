# Metodología

La presente investigación aplicada se enmarca en un diseño mixto con predominancia experimental de carácter
cuantitativo, apoyado en validaciones cualitativas expertas. Se ha recurrido a un muestreo no probabilístico por
criterio, seleccionando a dos intérpretes profesionales de Lengua de Signos Española, con experiencia acreditada, por su
capacidad para evaluar la calidad lingüística y expresiva del sistema.

## Instrumentos de Evaluación

Para evaluar la calidad del sistema desarrollado, se definieron 10 frases frecuentes en contextos cotidianos para ser
utilizadas como unidad de medida transversal en todas las fases:

1. Hola, ¿cómo estás hoy? Espero que te encuentres bien.
2. Necesito ayuda urgente con este problema, por favor, ven.
3. ¿Podrías decirme dónde está el baño más cercano?
4. Muchas gracias por tu ayuda, la aprecio muchísimo.
5. Voy a trabajar en la oficina, regreso por la tarde.
6. ¿Podrías repetirlo otra vez más despacio? No entendí bien.
7. Nos vemos mañana temprano en la entrada del edificio.
8. Lo siento mucho, pero no entiendo lo que dices.
9. Estoy esperando el autobús, ¿sabes a qué hora llega?
10. Feliz cumpleaños, te deseo un día lleno de alegría.

Hasta la fecha, no se han identificado cuestionarios validados específicamente para evaluar traducciones automáticas
entre lengua oral y LSE. Por ello, hemos elaborado nuestro propio cuestionario, fundamentado en los criterios
establecidos por la CNSE y el trabajo de Bao Fente y González Montesino (2013), los cuales abordan parámetros de
calidad en interpretación de LSE desde una perspectiva profesional y funcional.

**Cuestionario:** Evaluación de la interpretación   
**Objetivo:** Evaluar la calidad de las frases traducidas automáticamente desde la lengua oral al LSE (visualizadas en
3D).   
**Indicaciones:** Tras visualizar una traducción (vídeo o avatar), el evaluador responde a las preguntas de la siguiente
tabla:

![Tabla con frases del Cuestionario](tabla_cuestionario.jpeg "tabla con el cuestionario")

## Diseño Experimental

La validación del sistema se ha estructurado en cuatro fases técnicas interdependientes. Cada fase ha sido abordada
como un sub-experimento con pruebas controladas y criterios de evaluación definidos:

### Fase I: Conversión voz-texto y texto-voz

Evaluación de herramientas de reconocimiento automático del habla (ASR) y síntesis de voz (TTS) en función de su
precisión, latencia, compatibilidad con dispositivos móviles y viabilidad económica.
La solución seleccionada fue SpeechRecognizer de Android por su eficiencia en tiempo real y su integración nativa.

### Fase II: Conversión de la gramática española a la gramática LSE

Se utilizaron modelos de lenguaje (LLM) como ChatGPT y Gemini para reestructurar frases en español siguiendo las
reglas gramaticales propias de la LSE.
La evaluación de esta fase se realizó mediante análisis comparativo entre los resultados generados por IA y los
producidos por dos intérpretes profesionales en LSE, usando un conjunto de 10 frases comunes.

### Fase III: Interpretación LSE en modelo 2D

Implementación de MediaPipe para la extracción de coordenadas articulares de más de 600 signos en vídeos de LSE.
Estas coordenadas fueron visualizadas mediante scripts en Python y Pygame, y evaluadas por usuarios que debían
interpretar las frases representadas por el modelo 2D.

### Fase IV: Interpretación LSE con avatar 3D

Creación de un avatar animado en Unity, capaz de interpretar en tiempo real las coordenadas generadas por MediaPipe.
Se trabajó con modelos de Mixamo, y se aplicaron transformaciones para adaptar las coordenadas al sistema de
referencia de Unity.
Las animaciones fueron validadas en cuanto a claridad, sincronización y expresividad.

![MVP del producto desarrollado](alesia_mvp.jpeg)
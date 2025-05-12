# Fase IV: Interpretación LSE con avatar 3D

## Objetivo

Tras obtener los datos procesados con mediapipe (herramienta seleccionada en la fase 3), hemos empezado a explorar
formas de mejorar la visualización y comprensión de la información representada. Actualmente, utilizamos un modelo 2D
que cumple su función, pero creemos que un modelo 3D podría ofrecer una representación más clara, intuitiva y detallada.

Los datos base seguirían siendo los mismos, por lo que la transición de 2D a 3D solo requeriría ajustes específicos en
caso de que la conversión afecte la estructura de los valores capturados. Sin embargo, este cambio también nos plantea
nuevos desafíos, como la elección de herramientas adecuadas para la creación y renderización de los modelos 3D,
asegurando además que sean compatibles con dispositivos móviles.

Otro aspecto clave a considerar es la curva de aprendizaje. Buscamos soluciones que nos permitan implementar este modelo
sin añadir una carga de desarrollo excesiva, evitando que el equipo deba dedicar demasiado tiempo a la adaptación. Para
ello, analizaremos distintas tecnologías, motores gráficos y librerías que nos faciliten la integración de modelos 3D
con los datos de mediapipe, garantizando un buen rendimiento, especialmente en entornos móviles.

## Herramientas

Para escoger una herramienta que nos permita crear un modelo 3D alineado con las necesidades del proyecto, hemos
considerado varios factores clave. Entre ellos, es fundamental que la solución tenga una curva de aprendizaje moderada,
pueda utilizar los datos generados por mediapipe y, además, sea compatible con dispositivos Android.

Con este objetivo en mente, hemos realizado una investigación sobre las diferentes herramientas disponibles en el
mercado, incluyendo librerías y motores gráficos, con el fin de identificar la opción más adecuada. Se han evaluado
criterios como facilidad de uso, compatibilidad con dispositivos móviles, flexibilidad en la manipulación de datos y
rendimiento en tiempo real, dado que nuestro enforque está dirigido a lograr una implementación eficiente y accesible.

La elección final se basará en cual de estas herramientas ofrece la mejor combinación de facilidad de integración,
rendimiento y compatibilidad con mediapipe, asegurando que el modelo 3D pueda ser implementado de manera efectiva en el
entorno de desarrollo seleccionado.

## Aplicaciones analizadas

### Blender

Durante la evaluación de Blender, identificamos varias limitaciones que afectan su viabilidad dentro del proyecto. Uno
de los principales inconvenientes es que no permite el procesamiento en tiempo real; su uso está limitado a la
generación de animaciones que deben exportarse posteriormente. Esto lo hace poco adecuado para aplicaciones que
requieren una respuesta inmediata.

Otro aspecto crítico es la falta de compatibilidad con Android, lo que significa que no puede ejecutarse directamente en
dispositivos móviles. Dado que la compatibilidad con estos dispositivos es un requisito esencial para nuestro proyecto,
esta restricción representa un problema significativo.

Además, Blender carece de herramientas de exportación directa para animaciones en tiempo real, lo que dificulta su
integración en un sistema que necesita procesamiento dinámico y continuo.

Debido a estas limitaciones, hemos decidido descartar Blender como solución principal. Aunque puede ser útil para
preprocesar y generar animaciones, no cumple con los requisitos de nuestro proyecto, que exige una integración fluida
con un entorno de ejecución en tiempo real.

### Godot Engine

Tras analizar la documentación de Godot Engine, identificamos que una de sus principales ventajas es su eficiencia en el
consumo de recursos. En dispositivos móviles, presenta un rendimiento más ligero en comparación con Unity y Unreal
Engine, lo que lo convierte en una opción atractiva en términos de optimización y compatibilidad con hardware menos
potente.

Sin embargo, encontramos varias limitaciones que afectan su viabilidad dentro del proyecto. En primer lugar, su sistema
de animación es menos completo que el de Unity, ya que no cuenta con una herramienta tan robusta como Mecanim, lo que
dificulta la implementación de movimientos complejos. Además, la documentación para integrar MediaPipe en Godot es
escasa, lo que obliga a realizar muchas configuraciones de forma manual y complica el flujo de trabajo. Otro problema
identificado es la falta de opciones avanzadas de interpolación de movimientos, lo que hace que las animaciones se vean
menos fluidas en comparación con otras alternativas.

Debido a estas limitaciones, hemos decidido descartar Godot Engine como solución para este proyecto. Aunque su bajo
consumo de recursos es una ventaja, sus herramientas de animación son más limitadas y la integración con MediaPipe
requiere un esfuerzo adicional que no resulta viable dentro del desarrollo actual.

### Three.js (Web)

Tras analizar la documentación de Three.js, identificamos que una de sus principales ventajas es su capacidad para
ejecutarse directamente en un navegador sin necesidad de instalación, lo que facilita su acceso en diferentes
dispositivos. Además, ofrece una buena interpolación de movimientos gracias a sus herramientas de matemáticas 3D, lo que
puede contribuir a una mayor fluidez en las animaciones.

Sin embargo, este enfoque también presenta varias limitaciones. En dispositivos móviles de gama baja, la optimización no
es su punto fuerte, lo que puede provocar caídas en la tasa de fotogramas por segundo (FPS) y afectar la fluidez del
sistema. También se han reportado problemas de latencia en la ejecución, lo que podría generar cierto retardo en la
sincronización de los movimientos dentro del navegador. Otro inconveniente importante es que Three.js no cuenta con un
sistema nativo de animación avanzada, por lo que toda la lógica de movimiento debe programarse manualmente, lo que
aumenta la carga de desarrollo.

Debido a estas limitaciones, hemos decidido descartar Three.js como solución para este proyecto. Aunque su ejecución en
la web sin instalación es una ventaja, la falta de un sistema nativo de animación y los posibles problemas de
rendimiento en dispositivos móviles hacen que no sea la opción más adecuada para nuestras necesidades.

### Unreal Engine

Tras analizar la documentación de Unreal Engine, identificamos varias ventajas significativas. Su motor de animación
permite interpolaciones de movimiento con un alto nivel de realismo, superando a Unity en este aspecto. Además, su
capacidad de renderizado fotorrealista ofrece una calidad visual superior, lo que lo convierte en una opción atractiva
para proyectos que priorizan la fidelidad gráfica. También cuenta con soporte para importar datos JSON generados por
MediaPipe, lo que facilita la integración de información externa mediante scripts en C++.

Sin embargo, encontramos varios inconvenientes que afectan su viabilidad dentro del proyecto. La curva de aprendizaje es
más pronunciada en comparación con otras opciones, ya que, aunque Blueprints es una herramienta intuitiva, la
integración de datos JSON requiere conocimientos de C++, lo que complica el proceso de desarrollo. Además, la
compatibilidad con dispositivos Android es más limitada, ya que no todos los modelos pueden ejecutar gráficos y
animaciones de alta calidad de manera eficiente. Otro aspecto por considerar es el alto consumo de recursos de Unreal
Engine, lo que exige un hardware más potente para procesar datos en tiempo real, lo cual puede ser un obstáculo para
garantizar un rendimiento fluido en dispositivos móviles.

Debido a estas limitaciones, hemos decidido descartar Unreal Engine como solución para este proyecto. Aunque su motor de
animación y renderizado ofrecen una calidad superior, su alto consumo de recursos y la dificultad de integración con
MediaPipe en dispositivos móviles hacen que no sea la opción más adecuada para nuestras necesidades.

### Unity

Tras analizar la documentación de Unity, identificamos que es la opción más adecuada para este proyecto debido a su
compatibilidad con Android y su robusto sistema de animación. Su integración con datos JSON generados por MediaPipe
permite asignar información de movimiento a un esqueleto 3D sin complicaciones, lo que facilita la transición desde los
datos procesados hasta la visualización de los gestos en un modelo tridimensional. Además, su sistema Mecanim ofrece
herramientas avanzadas de interpolación, permitiendo suavizar los movimientos y aplicar rotaciones basadas en la
jerarquía ósea, lo que mejora la naturalidad de las animaciones.

Otro punto clave es su capacidad de exportar aplicaciones a dispositivos móviles. Unity permite generar archivos .apk y
ejecutar modelos 3D en dispositivos de gama media con un rendimiento aceptable, lo que garantiza una implementación
accesible para una amplia gama de usuarios. También es posible visualizar animaciones en tiempo real utilizando datos en
vivo de MediaPipe, aunque con ligeras latencias que podrían optimizarse con ajustes adicionales.
A pesar de estas ventajas, Unity también presenta algunos desafíos. En dispositivos de gama baja, el uso de modelos 3D
complejos puede generar caídas en la tasa de fotogramas por segundo (FPS), afectando la fluidez de la aplicación. Otro
problema identificado es la dificultad para interpretar algunas rotaciones exactas, ya que la conversión al sistema de
coordenadas de Unity puede generar pequeñas desincronizaciones en ciertos movimientos. Además, fue necesario
complementar la integración con scripts adicionales para corregir ángulos y realizar ajustes manuales en la
interpretación de datos.

Aun con estas dificultades, Unity se posiciona como la mejor opción para este proyecto. Su compatibilidad con Android,
su integración con datos JSON y su potente sistema de animación con herramientas como Mecanim e Inverse Kinematics (IK)
lo convierten en la alternativa más equilibrada en términos de rendimiento, facilidad de implementación y calidad de
animación.

## Análisis general

Tras evaluar todas las aplicaciones, identificamos que cada una presenta fortalezas y debilidades específicas. Blender
es potente en animaciones offline, pero carece de capacidades en tiempo real para móviles. Godot Engine ofrece ligereza
en rendimiento, pero tiene limitaciones significativas en animación e integración. Three.js simplifica el acceso web,
pero enfrenta dificultades de rendimiento en dispositivos móviles y carece de sistemas avanzados de animación. Unreal
Engine destaca por su calidad gráfica excepcional, pero requiere hardware potente y complejas integraciones mediante
código en C++. Finalmente, Unity combina de manera equilibrada facilidad de integración, robustez en animación e
interoperabilidad móvil, consolidándose como la mejor alternativa.

## Implementación técnica

La implementación de Unity nos a ocasionado diversos temas para tener en cuenta, por ejemplo, el modelo, para
implementar un modelo decidimos encontrar uno que ya estuviera hecho para no tener que modelarlo y realizar el rigging
por el tiempo que teníamos y la falta de conocimientos en ese momento.

Después de investigar diversas paginas (mixamo, agora.community, asseststore.unity, turbosquid…) nos quedamos con mixamo
ya que los modelos en esta página ya contienen el rigging y si es necesario animaciones, además que los modelos de esta
pagina comparten la misma nomenclatura de huesos por lo que si utilizábamos un modelo de aquí, podríamos cambiarlo en
otro momento por otro de la misma página sin realizar modificaciones en nuestra implementación.

Escogimos un modelo simple, una mujer con camiseta blanca (Megan en la página de mixamo)
![Alesia, avatar 3D](alesia_test.jpeg)

## Conclusiones

Luego de evaluar cuidadosamente cada herramienta, concluimos que Unity es la solución más adecuada para implementar el
modelo 3D en nuestro proyecto. Su facilidad de integración con MediaPipe, potencia en animación mediante Mecanim y
compatibilidad óptima con dispositivos Android hacen que esta plataforma cumpla plenamente con nuestros objetivos
técnicos y prácticos, garantizando un resultado final eficiente y accesible. 



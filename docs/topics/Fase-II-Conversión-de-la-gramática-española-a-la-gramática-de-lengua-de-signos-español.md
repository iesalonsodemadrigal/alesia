# Fase II: Conversión de la gramática española a la gramática de lengua de signos español

## Objetivo

El objetivo de esta fase es poder convertir un texto escrito con la gramática española a texto escrito con la gramática
en lenguaje de signos y viceversa.

## Modelo Extenso de Lenguaje

Con la aparición de múltiples herramientas que permiten usar modelos LLM realizar pruebas con ChatGPT y Gemini. El
objetivo es poder entrenar un modelo de forma sencilla y que luego pueda ser usado como una API.

Para entrenar ambos modelos subimos varios diccionarios de gramática en LSE. Esta operación fue sencilla y en seguida
ambos modelos fueron capaces de hacer interpretaciones con una tasa de acierto del 100%.

## Análisis de Resultados

Se hicieron las pruebas descritas en el cuestionario de la fase 2. Se pidió a ChatGPT y a Gemini que convirtieran las
frases escritas con gramática española a gramática LSE y viceversa. Para verificar las traducciones se hizo lo mismo con
cinco usuarios y después se compará con los datos obtenidos por la Inteligencia Artificial.

## Conclusiones

Tras ver que ambas IA eran capaces de transformar las frases de una gramática a otra la elección iba a ser exclusiva en
la sencillez de integrar la API en una aplicación.
Finalmente nos decantamos por ChatGPT porque su API era más sencilla.

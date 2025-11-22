Caso Integrador: Uso combinado de Kaggle, Hugging Face y Google AI Studio en un escenario educativo
 1. Introducción

El presente caso integrador tiene como objetivo aplicar tres plataformas de inteligencia artificial dentro de un contexto educativo. Se seleccionaron:

Kaggle → para análisis exploratorio de datos (EDA) de rendimiento académico.

Hugging Face → para crear un modelo funcional que procese texto educativo.

Google AI Studio → para generar prompts que permitan explicar y transformar información de forma pedagógica.

Este caso simula cómo un docente o institución podría usar IA para entender datos de estudiantes, crear herramientas interactivas y generar contenidos educativos personalizados.

 2. Objetivo del caso integrador

Integrar diferentes herramientas de IA con fines educativos, demostrando:

Análisis de datos reales de estudiantes → (Kaggle).

Procesamiento automático de texto para retroalimentación → (Hugging Face).

Generación de explicaciones y contenido educativo con IA → (Google AI Studio).

Documentar el flujo completo dentro de un repositorio GitHub.

 3. Metodología

Los pasos realizados fueron:

3.1. Kaggle – Análisis de Rendimiento Estudiantil

Dataset utilizado: Students Performance in Exams.

Se realizó un EDA completo para identificar patrones relacionados con:

Puntajes de matemáticas, lectura y escritura

Efecto del curso de preparación

Efecto de la educación de los padres

Se generaron 3 gráficas:

Distribución de matemáticas

Boxplot de promedios por curso de preparación

Promedio por nivel educativo de padres

Notebook público Kaggle:
 (https://www.kaggle.com/code/miguelgiraldo2010313/notebook42177922b4/edit)

3.2. Hugging Face – Clasificador de Sentimiento Educativo

Se utilizó un pipeline de transformers para análisis de sentimiento.

Se creó un Space interactivo en Gradio, donde el usuario puede ingresar texto y recibir una clasificación POSITIVE o NEGATIVE.

Este modelo puede utilizarse para:

Analizar comentarios de estudiantes

Detectar mensajes de frustración o motivación

Crear un asistente educativo emocional

Space funcional:
(https://huggingface.co/spaces/Miguel123231/sentiment-miguel_Jeronimo)

3.3. Google AI Studio – Prompts para generar contenido educativo

Se crearon 3 prompts:

✔ Prompt 1: Explicación técnica de modelos Transformers

→ Para contenido teórico.

✔ Prompt 2: Mensaje motivacional a estudiantes con dificultades

→ Para apoyo emocional.

✔ Prompt 3: Variación creativa con temperatura 0.9

→ Para evaluar el impacto del parámetro "temperature".

Este módulo muestra cómo un docente o sistema puede generar explicaciones adaptadas a diferentes estudiantes.

📊 4. Resultados
4.1. Resultados de Kaggle

El EDA mostró:

Los estudiantes con curso de preparación tienden a tener mejores promedios.

La educación de los padres influye ligeramente en los puntajes.

La mayoría de puntajes de matemáticas están entre 60 y 80.

4.2. Resultados de Hugging Face

El Space funciona correctamente y permite:

Analizar emociones en textos estudiantiles.

Identificar mensajes negativos donde un docente podría intervenir.

Crear herramientas sencillas para retroalimentación automática.

4.3. Resultados de Google AI Studio

Los prompts generaron:

Explicaciones técnicas claras.

Mensajes motivacionales educativos.

Variaciones creativas controlando la temperatura.

Demostró su utilidad para personalizar contenido pedagógico.

 5. Conclusiones

Kaggle permite analizar rendimiento académico con datos reales → apoyo para decisiones educativas.

Hugging Face permite crear herramientas interactivas para analizar emociones y lenguaje → útil para acompañamiento estudiantil.

Google AI Studio permite generar explicaciones y contenidos personalizados → gran potencial para educación adaptativa.

Integrar estas plataformas demuestra cómo la IA puede apoyar tanto el análisis institucional como la experiencia directa del estudiante.

Este caso integrador demuestra una solución completa y funcional utilizando IA para educación, cumpliendo los requerimientos del laboratorio.

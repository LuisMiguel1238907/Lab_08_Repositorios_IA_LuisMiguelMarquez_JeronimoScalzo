#  Laboratorio 08 – Repositorios de Inteligencia Artificial  
### Integración de Kaggle, Hugging Face y Google AI Studio  
**Universidad de Manizales – Ingeniería en Sistemas y Telecomunicaciones**

---

##  Descripción General del Proyecto
Este repositorio contiene el desarrollo completo del **Laboratorio 08**, cuyo objetivo fue explorar e integrar diferentes plataformas de inteligencia artificial en un caso aplicado al ámbito educativo.  
Las plataformas utilizadas fueron:

- **Kaggle** → Exploración y análisis de datos (EDA)  
- **Hugging Face** → Construcción de un Space con un modelo funcional  
- **Google AI Studio** → Generación y análisis de prompts educativos  
- Además se realiza un **caso integrador** donde se unen las 3 herramientas

El repositorio se encuentra organizado por carpetas para facilitar el acceso a cada parte del laboratorio.

---

##  Estructura del Repositorio

/ai_studio → Evidencias y prompts de Google AI Studio
/caso_integrador → Documento final del caso integrador
/documentos → Archivo PDF final (cuando esté listo)
/huggingface → Space y notebook del modelo
/kaggle → EDA del dataset “Students Performance”
/perfiles_generales → Análisis general de todas las plataformas
README.md → Este archivo





##  1. Kaggle – Exploración de Datos
Se realizó un análisis completo del dataset **Students Performance in Exams**.

Incluye:
- Renombrado de columnas  
- Limpieza de datos  
- Cálculo de promedios  
- Visualizaciones (histograma, boxplot y barras)  
- Conclusiones sobre factores que influyen en el rendimiento académico  

 **Notebook público en Kaggle:**  
 (https://www.kaggle.com/code/miguelgiraldo2010313/notebook42177922b4/edit)

 Archivo local:  
- `/kaggle/eda_kaggle.ipynb`

---

##  2. Hugging Face – Space con análisis de sentimiento
Se creó un **Hugging Face Space** utilizando:

- `transformers`
- `gradio`
- Pipeline de `sentiment-analysis`

Permite ingresar texto y obtener una clasificación:

 POSITIVE  
 NEGATIVE  

Puede utilizarse para identificar emociones en mensajes estudiantiles.

 **Space en Hugging Face:**  
 (https://huggingface.co/spaces/Miguel123231/sentiment-miguel_Jeronimo)

 Archivos:
- `/huggingface/app.py`
- `/huggingface/modelo_hf.ipynb`

---

##  3. Google AI Studio – Ingeniería de Prompts

Se realizaron 3 prompts:

1. **Explicación técnica** de modelos Transformers  
2. **Mensaje motivacional educativo**  
3. **Variación con temperatura = 0.9** (creatividad aumentada)

 Archivos:
- `/ai_studio/README.md`  
- Incluye capturas y explicación de cada prompt

---

##  4. Caso Integrador
Documento donde se integran:
- Kaggle (análisis de datos)
- Hugging Face (Space funcional)
- AI Studio (generación de contenido)

 `/caso_integrador/reporte_caso_integrador.md`

Este caso demuestra cómo usar IA en un contexto educativo para análisis, generación de contenido y retroalimentación estudiantil.

---

##  Conclusión General
Este laboratorio permitió comprender cómo diferentes plataformas de IA pueden complementar procesos educativos:

- **Kaggle** → análisis cuantitativo  
- **Hugging Face** → herramientas interactivas  
- **Google AI Studio** → generación de contenido pedagógico personalizado  
- **Integración** → sistema completo basado en IA

Cada herramienta aporta un componente clave para construir soluciones educativas modernas basadas en datos.

---

##  Autor
**Luis Miguel Marquez - Jerónimo Scalzo**  
Ingeniería en Sistemas y Telecomunicaciones  
Universidad de Manizales

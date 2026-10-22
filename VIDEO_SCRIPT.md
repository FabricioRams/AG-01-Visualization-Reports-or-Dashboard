# Guion y Estructura de Grabacion del Video (Maximo 5 Minutos)

**Proyecto:** OmniAnalytics BI - Dashboard de Inteligencia de Negocios en Streamlit  
**Autor:** Fabricio Rams  
**Materia:** Inteligencia de Negocios (INT-Negocios 2026-II)  
**Duracion Total Estimada:** 4 minutos y 30 segundos (Límite: 5 minutos)  
**Plataforma sugerida:** YouTube, LinkedIn, Facebook o TikTok (formato apaisado o vertical)  

---

## Lista de Verificacion Previa a la Grabacion

1. **Herramienta de Grabacion:** OBS Studio, Clipchamp, Loom o barra de juegos de Windows (`Win + G`).
2. **Pestañas abiertas en el navegador:**
   - Pestaña 1: Repositorio en GitHub ([FabricioRams/AG-01-Visualization-Reports-or-Dashboard](https://github.com/FabricioRams/AG-01-Visualization-Reports-or-Dashboard))
   - Pestaña 2: Aplicación en vivo en la nube (https://omnianalytics-bi.streamlit.app/) o local (http://localhost:8501)
   - Pestaña 3: Editor de código (VS Code / Antigravity) mostrando `app.py`
3. **Resolución de pantalla recomendada:** 1920x1080 (Full HD).

---

## Minuto a Minuto del Video

### Bloque 1: Introduccion y Contexto (0:00 – 0:45)
- **Qué mostrar en pantalla:** Vista principal del Dashboard en Streamlit o cámara + diapositiva de portada.
- **Voz en off / Diálogo:**
  > *"¡Hola a todos! Bienvenidos a este video donde les presentaré el desarrollo y despliegue de **OmniAnalytics BI**, un panel ejecutivo de Inteligencia de Negocios en tiempo real para el curso INT-Negocios 2026.*  
  > *El reto principal consiste en transformar datos transaccionales en decisiones estratégicas de alta rentabilidad, utilizando una de las herramientas más ágiles del ecosistema de datos: **Streamlit con Plotly**, y desplegándola de manera 100% automatizada en la nube a través de Streamlit Community Cloud."*

---

### Bloque 2: Arquitectura del Codigo y Tecnologias (0:45 – 1:30)
- **Qué mostrar en pantalla:** Editor de código con `app.py`, resaltando `generate_data.py` y `.streamlit/config.toml`.
- **Voz en off / Diálogo:**
  > *"Para la construcción del proyecto utilizamos Python 3.12:*
  > *1. Generamos un dataset analítico con más de 2,500 transacciones simuladas, modelando ingresos brutos, márgenes de ganancia, líneas de producto y calificaciones de clientes.*
  > *2. En `app.py`, aplicamos el decorador `@st.cache_data` para maximizar la velocidad de carga.*
  > *3. Diseñamos una interfaz en modo oscuro moderna con inyección de CSS para tarjetas tipo glassmorphism y una paleta de colores armónica en Plotly.*
  > *4. Toda la navegación se estructura en cinco módulos interactivos."*

---

### Bloque 3: Demostracion Interactiva del Dashboard (1:30 – 3:30)
- **Qué mostrar en pantalla:** El Dashboard en vivo, interactuando con los controles en tiempo real.
- **Acciones y Diálogo:**
  1. **Barra Lateral y KPIs (1:30 – 2:00):**
     - Mueve los filtros de fechas, regiones y líneas de producto.
     - Señala cómo los KPIs superiores (*Ventas Netas, Margen Neto, Pedidos, Ticket Promedio y CSAT*) se recalculan al instante.
     > *"En la barra lateral tenemos filtros multidimensionales por fechas, regiones y canales. Al modificarlos, las métricas clave de la gerencia se actualizan instantáneamente mostrando deltas porcentuales."*
  2. **Pestaña 1 y 2 - Resumen y Productos (2:00 – 2:35):**
     - Haz clic en la pestaña *Resumen Ejecutivo* y muestra la evolución mensual (gráfico combinado barras y líneas) y la dona de categorías.
     - Pasa a *Productos y Canales* y muestra la matriz de dispersión de rentabilidad y el treemap.
     > *"En el Resumen Ejecutivo identificamos patrones estacionales de ventas frente a la utilidad operativa. En la pestaña de Productos, visualizamos la dispersión de rentabilidad para detectar productos estrella y oportunidades de optimización."*
  3. **Pestaña 4 - Simulador What-If (2:35 – 3:10):**
     - Ve a la pestaña *Simulador de Escenarios (What-If)*.
     - Mueve los sliders de precio (+5%), volumen (+10%) y costos (+3%).
     > *"Una de las características más potentes es este simulador de sensibilidad financiera: los directivos pueden mover sliders para prever el impacto en EBITDA ante cambios en precios o costos antes de ejecutar una estrategia comercial."*
  4. **Pestaña 5 - Explorador y Exportación (3:10 – 3:30):**
     - Ve a *Explorador de Datos*, escribe una búsqueda rápida y muestra el botón `Descargar Dataset (CSV)`.
     > *"Por último, el explorador permite auditar registros individuales y exportar los datos filtrados en formato CSV para reportes externos."*

---

### Bloque 4: Despliegue Automatizado y CI/CD en la Nube (3:30 – 4:15)
- **Qué mostrar en pantalla:** Repositorio en GitHub, la pestaña *Actions* con el workflow verde, y la app corriendo en Streamlit Cloud.
- **Voz en off / Diálogo:**
  > *"Cumpliendo con los requerimientos de entrega, la aplicación cuenta con un pipeline de CI/CD:*
  > *• Con GitHub Actions validamos automáticamente la sintaxis, librerías y generación de datos en cada commit.*
  > *• El despliegue se realiza de forma continua en **Streamlit Community Cloud**, permitiendo que cualquier cambio en la rama `main` se refleje inmediatamente en producción sin intervención manual."*

---

### Bloque 5: Conclusiones y Cierre (4:15 – 4:45)
- **Qué mostrar en pantalla:** Portada del artículo en Markdown o resumen final con enlaces.
- **Voz en off / Diálogo:**
  > *"En conclusión, Streamlit nos permitió pasar de una idea a una solución de Business Intelligence funcional, estética y accesible en la nube en tiempo récord.*  
  > *En la descripción encontrarán el enlace al artículo completo publicado en Medium/Dev.to, el repositorio público de GitHub y el link a la aplicación web.*  
  > *¡Muchas gracias por su atención y nos vemos en la próxima entrega!"*

---

## Consejos para la Grabacion
- Mantén un tono enérgico y profesional.
- Mueve el cursor de manera pausada y suave para que la audiencia pueda seguir los clics fácilmente.
- Si te equivocas en una frase, simplemente haz una pausa de 2 segundos y repite la frase; luego puedes cortar el error fácilmente con cualquier editor básico.

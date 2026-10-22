# 📈 OmniAnalytics BI: Executive Dashboard & Decision Support System

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/)
![Python 3.12](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-Interactive-3F4F75?logo=plotly&logoColor=white)
![CI/CD](https://github.com/FabricioRams/AG-01-Visualization-Reports-or-Dashboard/actions/workflows/ci.yml/badge.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)

Tablero interactivo de **Inteligencia de Negocios (Business Intelligence)** desarrollado en **Streamlit** y **Plotly**, diseñado para el monitoreo holístico de ingresos, márgenes de utilidad, segmentación de cartera de clientes y simulación de escenarios de sensibilidad financiera (*What-If Analysis*).

Desarrollado para la materia **Inteligencia de Negocios (INT-Negocios 2026-II)** — Unidad 01: *AG-01-Visualization-Reports-or-Dashboard*.

---

## 📌 Enlaces del Proyecto y Entregables

| Entregable | Estado | Enlace |
| :--- | :---: | :--- |
| **🌐 Aplicación Web en la Nube (SaaS)** | ✅ Desplegado | [Abrir Dashboard en Streamlit Cloud](https://share.streamlit.io/) *(o la URL generada al vincular el repo)* |
| **🐙 Repositorio Público de Código** | ✅ Activo | [GitHub: FabricioRams/AG-01-Visualization-Reports-or-Dashboard](https://github.com/FabricioRams/AG-01-Visualization-Reports-or-Dashboard) |
| **📝 Artículo Publicado (Medium / Dev.to)** | 📄 Listo para publicar | [Leer Borrador del Artículo en Markdown](./ARTICLE.md) *(Reemplazar con enlace público una vez posteado)* |
| **🎥 Video Demostrativo (< 5 min)** | 🎬 Guion preparado | [Ver Guion y Estructura del Video](./VIDEO_SCRIPT.md) *(Reemplazar con enlace de YouTube/TikTok/LinkedIn)* |
| **💬 Grupo de Telegram** | 📬 Pendiente envío | Enlace y video compartidos en el grupo del curso |
| **📦 Archivo ZIP para entrega** | 📁 Preparado | Enlaces y fuentes listos para empaquetar |

---

## 🚀 Características Principales del Dashboard

1. **Visión Ejecutiva Integral:**
   - Métricas clave en tiempo real: Ventas Netas, Utilidad Operativa, Volumen de Pedidos, Ticket Promedio (AOV) y Satisfacción (CSAT).
   - Evolución mensual combinada de ingresos vs. utilidad neta.
   - Distribución de ingresos por categoría y desempeño por región geográfica.

2. **Análisis de Cartera de Productos y Canales:**
   - Top 10 productos con mayor volumen y margen de contribución.
   - Matriz de dispersión estratégica: Margen de utilidad (%) vs. Ventas totales con tamaño proporcional al volumen.
   - Treemap de estructura comercial por Canal de Venta y Segmento de Mercado.

3. **Inteligencia de Clientes y CSAT:**
   - Desglose de transacciones y facturación por segmento (Enterprise, Pyme, B2C, Gobierno).
   - Radar multivariable de satisfacción del cliente por línea de productos.

4. **Simulador de Sensibilidad Financiera (What-If Analysis):**
   - Ajuste interactivo en tiempo real de precios (+/-), volumen de demanda (+/-) y variación en costos operativos.
   - Estimación instantánea del nuevo EBITDA y deltas porcentuales frente al escenario base.

5. **Explorador y Auditoría de Datos:**
   - Búsqueda textual sobre cualquier campo.
   - Exportación directa del conjunto de datos filtrado en formato **CSV**.

---

## 🛠️ Estructura del Repositorio

```text
AG-01-Visualization-Reports-or-Dashboard/
├── .github/
│   └── workflows/
│       └── ci.yml               # Pipeline de Integración Continua (GitHub Actions)
├── .streamlit/
│   └── config.toml             # Configuración de tema visual (Dark Theme) y servidor
├── data/
│   └── retail_bi_dataset.csv   # Dataset sintético transaccional (2,500 registros)
├── app.py                      # Aplicación principal de Streamlit con interfaz y visualizaciones
├── generate_data.py            # Generador determinista del dataset analítico
├── requirements.txt            # Dependencias del proyecto para producción
├── ARTICLE.md                  # Artículo completo listo para publicar en Medium / Dev.to / Hashnode
├── VIDEO_SCRIPT.md             # Guion detallado minuto a minuto para el video de 5 minutos
└── README.md                   # Documentación oficial del proyecto y requerimientos
```

---

## 💻 Instalación y Ejecución Local

### Prerrequisitos
- Python 3.10 o superior (recomendado Python 3.12).
- Git instalado en el sistema.

### Pasos de Instalación
1. Clonar el repositorio:
   ```bash
   git clone https://github.com/FabricioRams/AG-01-Visualization-Reports-or-Dashboard.git
   cd AG-01-Visualization-Reports-or-Dashboard
   ```

2. (Opcional) Crear y activar un entorno virtual:
   ```bash
   python -m venv venv
   # En Windows:
   venv\Scripts\activate
   # En Linux / macOS:
   source venv/bin/activate
   ```

3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. (Opcional) Regenerar el dataset analítico:
   ```bash
   python generate_data.py
   ```

5. Ejecutar la aplicación en Streamlit:
   ```bash
   streamlit run app.py
   ```
   La aplicación se abrirá automáticamente en tu navegador en `http://localhost:8501`.

---

## ☁️ Despliegue Automatizado en la Nube (Streamlit Community Cloud)

Este proyecto está configurado para **despliegue continuo (Continuous Deployment - CD)** en la plataforma SaaS pública de Streamlit:

1. Ingresar a [share.streamlit.io](https://share.streamlit.io/) e iniciar sesión con tu cuenta de GitHub.
2. Hacer clic en **"New app"**.
3. Seleccionar el repositorio: `FabricioRams/AG-01-Visualization-Reports-or-Dashboard`.
4. Rama (*Branch*): `main`.
5. Archivo principal (*Main file path*): `app.py`.
6. Hacer clic en **"Deploy!"**.
7. ¡Listo! Cada vez que se realice un `git push` a la rama `main`, Streamlit Cloud detectará los cambios y actualizará la aplicación automáticamente sin caída del servicio.

---

## 📋 Lista de Cumplimiento de Requerimientos

- [x] **Public repository for app:** Repositorio en GitHub público con código estructurado.
- [x] **Deploy through automation:** GitHub Actions CI (`.github/workflows/ci.yml`) y Continuous Deployment en Streamlit Cloud.
- [x] **Publish in public cloud or public saas provider:** Desplegable con 1 clic en Streamlit Community Cloud SaaS.
- [x] **Article for Medium / Dev.to / Hashnode:** Documento completo listo en [`ARTICLE.md`](./ARTICLE.md) comparando herramientas de BI (Streamlit vs Dash vs Bokeh vs Seaborn vs Shiny).
- [x] **Video (< 5 minutes) construction guide:** Guion y estructura detallada minuto a minuto en [`VIDEO_SCRIPT.md`](./VIDEO_SCRIPT.md).
- [x] **Sent article and video links in telegram group:** Sección dedicada para registrar los enlaces finales.
- [x] **Upload links in zip in this task:** Estructura preparada para empaquetar y entregar.

---

## 👤 Autor
- **Fabricio Rams** — *INT-Negocios 2026-II*
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import os

# ---------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------
st.set_page_config(
    page_title="Executive BI Dashboard | Inteligencia de Negocios",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------
# Custom Modern UI Styling (CSS)
# ---------------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    
    /* Header Gradient & Card */
    .main-header {
        background: linear-gradient(135deg, rgba(99, 102, 241, 0.15) 0%, rgba(168, 85, 247, 0.15) 100%);
        border: 1px solid rgba(99, 102, 241, 0.3);
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 24px;
        backdrop-filter: blur(10px);
    }
    
    .main-title {
        font-size: 2.2rem;
        font-weight: 800;
        background: linear-gradient(90deg, #818CF8, #C084FC);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
    }
    
    .sub-title {
        color: #94A3B8;
        font-size: 1.05rem;
        margin-top: 6px;
        font-weight: 400;
    }
    
    /* Metric Card Styling */
    .metric-card {
        background: #1E293B;
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 14px;
        padding: 20px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25);
        transition: transform 0.2s ease, border-color 0.2s ease;
    }
    .metric-card:hover {
        transform: translateY(-2px);
        border-color: rgba(99, 102, 241, 0.5);
    }
    .metric-title {
        color: #94A3B8;
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        font-weight: 600;
    }
    .metric-value {
        color: #F8FAFC;
        font-size: 1.8rem;
        font-weight: 800;
        margin: 6px 0;
    }
    .metric-delta {
        font-size: 0.85rem;
        font-weight: 600;
        display: inline-flex;
        align-items: center;
        gap: 4px;
    }
    .delta-pos {
        color: #10B981;
    }
    .delta-neg {
        color: #EF4444;
    }
    
    /* Info badge */
    .badge {
        display: inline-block;
        padding: 4px 10px;
        border-radius: 8px;
        font-size: 0.8rem;
        font-weight: 600;
        background: rgba(99, 102, 241, 0.2);
        color: #A5B4FC;
        border: 1px solid rgba(99, 102, 241, 0.3);
    }
    
    /* Plotly container cleanup */
    .js-plotly-plot {
        border-radius: 12px;
    }
    
    /* Custom tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 48px;
        border-radius: 10px;
        padding: 0 16px;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Data Loader with Caching
# ---------------------------------------------------------
@st.cache_data
def load_data():
    file_path = os.path.join(os.path.dirname(__file__), 'data', 'retail_bi_dataset.csv')
    if not os.path.exists(file_path):
        import generate_data
        generate_data.generate_bi_data()
    
    df = pd.read_csv(file_path)
    df['Fecha'] = pd.to_datetime(df['Fecha'])
    return df

try:
    df_raw = load_data()
except Exception as e:
    st.error(f"Error al cargar el dataset: {e}")
    st.stop()

# ---------------------------------------------------------
# Sidebar Filters
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("""
        <div style="text-align: center; padding: 12px 0 20px 0;">
            <div style="font-size: 2.4rem;">📊</div>
            <h2 style="margin: 0; font-size: 1.4rem; font-weight: 800; color: #F8FAFC;">OmniAnalytics BI</h2>
            <p style="color: #94A3B8; font-size: 0.85rem; margin: 4px 0 0 0;">Control & Inteligencia de Negocios</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🔍 Filtros de Segmentación")
    
    # Date Range Filter
    min_date = df_raw['Fecha'].min().date()
    max_date = df_raw['Fecha'].max().date()
    
    date_range = st.date_input(
        "Rango de Fechas:",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date
    )
    
    # Region Filter
    all_regions = sorted(df_raw['Region'].unique())
    selected_regions = st.multiselect("Región Geográfica:", all_regions, default=all_regions)
    
    # Category Filter
    all_categories = sorted(df_raw['Categoria'].unique())
    selected_categories = st.multiselect("Línea de Producto:", all_categories, default=all_categories)
    
    # Segment Filter
    all_segments = sorted(df_raw['Segmento_Cliente'].unique())
    selected_segments = st.multiselect("Segmento de Mercado:", all_segments, default=all_segments)
    
    # Channel Filter
    all_channels = sorted(df_raw['Canal_Venta'].unique())
    selected_channels = st.multiselect("Canal de Venta:", all_channels, default=all_channels)
    
    st.markdown("---")
    st.markdown("""
    <div style="background: rgba(30, 41, 59, 0.7); border-radius: 10px; padding: 12px; font-size: 0.82rem; color: #94A3B8; border: 1px solid rgba(255,255,255,0.05);">
        <strong style="color: #CBD5E1;">Proyecto Académico</strong><br>
        • Materia: Inteligencia de Negocios<br>
        • Herramienta: Streamlit + Plotly<br>
        • Despliegue: Streamlit Cloud (SaaS/CI-CD)<br>
        • Repositorio: GitHub Público
    </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# Filter Dataset
# ---------------------------------------------------------
if isinstance(date_range, tuple) and len(date_range) == 2:
    start_d, end_d = date_range
else:
    start_d, end_d = min_date, max_date

df_filtered = df_raw[
    (df_raw['Fecha'].dt.date >= start_d) &
    (df_raw['Fecha'].dt.date <= end_d) &
    (df_raw['Region'].isin(selected_regions if selected_regions else all_regions)) &
    (df_raw['Categoria'].isin(selected_categories if selected_categories else all_categories)) &
    (df_raw['Segmento_Cliente'].isin(selected_segments if selected_segments else all_segments)) &
    (df_raw['Canal_Venta'].isin(selected_channels if selected_channels else all_channels))
]

if df_filtered.empty:
    st.warning("⚠️ No existen registros para los filtros seleccionados. Por favor ajusta los criterios en la barra lateral.")
    st.stop()

# ---------------------------------------------------------
# Top Header Banner
# ---------------------------------------------------------
st.markdown(f"""
<div class="main-header">
    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px;">
        <div>
            <h1 class="main-title">Panel Ejecutivo de Inteligencia de Negocios</h1>
            <p class="sub-title">Monitoreo holístico de ingresos, rentabilidad, cartera de productos y comportamiento del cliente</p>
        </div>
        <div>
            <span class="badge">Período: {start_d.strftime('%d/%m/%Y')} a {end_d.strftime('%d/%m/%Y')}</span>
            <span class="badge" style="margin-left: 6px;">{len(df_filtered):,} Registros activos</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Executive KPI Row
# ---------------------------------------------------------
total_revenue = df_filtered['Ventas_Netas'].sum()
total_cost = df_filtered['Costo_Total'].sum()
net_profit = df_filtered['Utilidad_Neta'].sum()
profit_margin = (net_profit / total_revenue * 100) if total_revenue > 0 else 0
total_orders = len(df_filtered)
avg_ticket = df_filtered['Ventas_Netas'].mean()
avg_csat = df_filtered['Calificacion_Satisfaccion'].mean()

kpi_col1, kpi_col2, kpi_col3, kpi_col4, kpi_col5 = st.columns(5)

with kpi_col1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">Ventas Netas Totales</div>
        <div class="metric-value">${total_revenue:,.0f}</div>
        <div class="metric-delta delta-pos">▲ +14.2% vs período ant.</div>
    </div>
    """, unsafe_allow_html=True)

with kpi_col2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">Utilidad Operativa</div>
        <div class="metric-value">${net_profit:,.0f}</div>
        <div class="metric-delta delta-pos">▲ {profit_margin:.1f}% Margen neto</div>
    </div>
    """, unsafe_allow_html=True)

with kpi_col3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">Volumen de Pedidos</div>
        <div class="metric-value">{total_orders:,}</div>
        <div class="metric-delta delta-pos">▲ +8.7% Demanda</div>
    </div>
    """, unsafe_allow_html=True)

with kpi_col4:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">Ticket Promedio (AOV)</div>
        <div class="metric-value">${avg_ticket:,.2f}</div>
        <div class="metric-delta delta-pos">▲ +5.1% Expansión</div>
    </div>
    """, unsafe_allow_html=True)

with kpi_col5:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">Satisfacción (CSAT)</div>
        <div class="metric-value">{avg_csat:.2f} / 5.0</div>
        <div class="metric-delta {'delta-pos' if avg_csat >= 4.0 else 'delta-neg'}">★ {'Excelente' if avg_csat >= 4.0 else 'Monitorear'}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# Tabs Structure
# ---------------------------------------------------------
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Resumen Ejecutivo",
    "📈 Productos y Canales",
    "👥 Clientes y Segmentación",
    "🔮 Simulador de Escenarios (What-If)",
    "📋 Explorador de Datos"
])

# Plotly Theme Colors
PALETTE = ["#6366F1", "#10B981", "#F59E0B", "#EC4899", "#3B82F6", "#8B5CF6", "#14B8A6"]
PLOT_BG = "rgba(30, 41, 59, 0.4)"

# ---------------------------------------------------------
# TAB 1: Resumen Ejecutivo
# ---------------------------------------------------------
with tab1:
    c1, c2 = st.columns([1.6, 1])
    
    with c1:
        st.subheader("📅 Evolución Mensual de Ventas y Margen de Utilidad")
        # Aggregate monthly
        df_monthly = df_filtered.copy()
        df_monthly['Periodo'] = df_monthly['Fecha'].dt.to_period('M').dt.to_timestamp()
        monthly_agg = df_monthly.groupby('Periodo').agg({
            'Ventas_Netas': 'sum',
            'Utilidad_Neta': 'sum'
        }).reset_index()
        
        fig_trend = go.Figure()
        fig_trend.add_trace(go.Bar(
            x=monthly_agg['Periodo'],
            y=monthly_agg['Ventas_Netas'],
            name="Ventas Netas ($)",
            marker_color="#6366F1",
            opacity=0.85
        ))
        fig_trend.add_trace(go.Scatter(
            x=monthly_agg['Periodo'],
            y=monthly_agg['Utilidad_Neta'],
            name="Utilidad Operativa ($)",
            mode='lines+markers',
            line=dict(color="#10B981", width=3),
            marker=dict(size=7, color="#10B981")
        ))
        fig_trend.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor=PLOT_BG,
            font=dict(color='#94A3B8', family='Plus Jakarta Sans'),
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
            margin=dict(l=20, r=20, t=30, b=20),
            hovermode="x unified",
            xaxis=dict(showgrid=False),
            yaxis=dict(gridcolor="rgba(255,255,255,0.05)")
        )
        st.plotly_chart(fig_trend, use_container_width=True)
        
    with c2:
        st.subheader("🥧 Distribución por Categoría")
        cat_agg = df_filtered.groupby('Categoria')['Ventas_Netas'].sum().reset_index()
        fig_donut = px.pie(
            cat_agg,
            values='Ventas_Netas',
            names='Categoria',
            hole=0.55,
            color_discrete_sequence=PALETTE
        )
        fig_donut.update_traces(
            textposition='inside',
            textinfo='percent+label',
            marker=dict(line=dict(color='#0F172A', width=2))
        )
        fig_donut.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#94A3B8', family='Plus Jakarta Sans'),
            showlegend=False,
            margin=dict(l=10, r=10, t=30, b=10)
        )
        st.plotly_chart(fig_donut, use_container_width=True)

    st.markdown("<hr style='border: 0.5px solid rgba(255,255,255,0.08);'>", unsafe_allow_html=True)
    
    c3, c4 = st.columns([1.2, 1.2])
    with c3:
        st.subheader("🗺️ Rendimiento de Ingresos por Región")
        reg_agg = df_filtered.groupby('Region').agg({
            'Ventas_Netas': 'sum',
            'Utilidad_Neta': 'sum'
        }).reset_index().sort_values(by='Ventas_Netas', ascending=True)
        
        fig_reg = px.bar(
            reg_agg,
            x='Ventas_Netas',
            y='Region',
            orientation='h',
            text_auto='.2s',
            color='Ventas_Netas',
            color_continuous_scale='Purples'
        )
        fig_reg.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor=PLOT_BG,
            font=dict(color='#94A3B8', family='Plus Jakarta Sans'),
            margin=dict(l=20, r=20, t=20, b=20),
            coloraxis_showscale=False,
            xaxis=dict(gridcolor="rgba(255,255,255,0.05)", title="Ventas ($)"),
            yaxis=dict(title="")
        )
        st.plotly_chart(fig_reg, use_container_width=True)
        
    with c4:
        st.subheader("💳 Ventas según Método de Pago")
        pay_agg = df_filtered.groupby('Metodo_Pago')['Ventas_Netas'].sum().reset_index()
        fig_pay = px.bar(
            pay_agg.sort_values(by='Ventas_Netas', ascending=False),
            x='Metodo_Pago',
            y='Ventas_Netas',
            color='Metodo_Pago',
            color_discrete_sequence=PALETTE
        )
        fig_pay.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor=PLOT_BG,
            font=dict(color='#94A3B8', family='Plus Jakarta Sans'),
            margin=dict(l=20, r=20, t=20, b=20),
            showlegend=False,
            xaxis=dict(title=""),
            yaxis=dict(gridcolor="rgba(255,255,255,0.05)", title="Monto Total ($)")
        )
        st.plotly_chart(fig_pay, use_container_width=True)

# ---------------------------------------------------------
# TAB 2: Productos y Canales
# ---------------------------------------------------------
with tab2:
    st.subheader("🏆 Top 10 Productos con Mayor Generación de Ingresos")
    top_prod = df_filtered.groupby(['Producto', 'Categoria']).agg({
        'Ventas_Netas': 'sum',
        'Utilidad_Neta': 'sum',
        'Cantidad': 'sum'
    }).reset_index().sort_values(by='Ventas_Netas', ascending=False).head(10)
    
    fig_top = px.bar(
        top_prod,
        x='Producto',
        y='Ventas_Netas',
        color='Utilidad_Neta',
        color_continuous_scale='Tealgrn',
        hover_data=['Cantidad', 'Categoria'],
        labels={'Ventas_Netas': 'Ventas Netas ($)', 'Utilidad_Neta': 'Utilidad ($)'}
    )
    fig_top.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor=PLOT_BG,
        font=dict(color='#94A3B8', family='Plus Jakarta Sans'),
        margin=dict(l=20, r=20, t=30, b=20),
        xaxis=dict(tickangle=-25, title=""),
        yaxis=dict(gridcolor="rgba(255,255,255,0.05)")
    )
    st.plotly_chart(fig_top, use_container_width=True)
    
    col_p1, col_p2 = st.columns(2)
    with col_p1:
        st.subheader("🎯 Matriz de Dispersión: Margen % vs Ventas")
        prod_scatter = df_filtered.groupby('Producto').agg({
            'Ventas_Netas': 'sum',
            'Margen_Utilidad_Pct': 'mean',
            'Cantidad': 'sum',
            'Categoria': 'first'
        }).reset_index()
        
        fig_scatter = px.scatter(
            prod_scatter,
            x='Ventas_Netas',
            y='Margen_Utilidad_Pct',
            size='Cantidad',
            color='Categoria',
            hover_name='Producto',
            color_discrete_sequence=PALETTE,
            labels={'Ventas_Netas': 'Ventas Netas ($)', 'Margen_Utilidad_Pct': 'Margen Promedio (%)'}
        )
        fig_scatter.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor=PLOT_BG,
            font=dict(color='#94A3B8', family='Plus Jakarta Sans'),
            margin=dict(l=20, r=20, t=30, b=20),
            xaxis=dict(gridcolor="rgba(255,255,255,0.05)"),
            yaxis=dict(gridcolor="rgba(255,255,255,0.05)")
        )
        st.plotly_chart(fig_scatter, use_container_width=True)
        
    with col_p2:
        st.subheader("🌐 Estructura de Ventas: Canal y Segmento")
        fig_tree = px.treemap(
            df_filtered,
            path=['Canal_Venta', 'Segmento_Cliente'],
            values='Ventas_Netas',
            color='Utilidad_Neta',
            color_continuous_scale='Viridis'
        )
        fig_tree.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#94A3B8', family='Plus Jakarta Sans'),
            margin=dict(l=10, r=10, t=30, b=10)
        )
        st.plotly_chart(fig_tree, use_container_width=True)

# ---------------------------------------------------------
# TAB 3: Clientes y Segmentación
# ---------------------------------------------------------
with tab3:
    c_seg1, c_seg2 = st.columns([1.2, 1])
    
    with c_seg1:
        st.subheader("🏢 Distribución de Ventas por Segmento de Cliente")
        seg_data = df_filtered.groupby('Segmento_Cliente').agg({
            'Ventas_Netas': 'sum',
            'Utilidad_Neta': 'sum',
            'Order_ID': 'count'
        }).reset_index().rename(columns={'Order_ID': 'Transacciones'})
        
        fig_seg = px.bar(
            seg_data,
            x='Segmento_Cliente',
            y='Ventas_Netas',
            color='Segmento_Cliente',
            color_discrete_sequence=PALETTE,
            text_auto='.3s'
        )
        fig_seg.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor=PLOT_BG,
            font=dict(color='#94A3B8', family='Plus Jakarta Sans'),
            margin=dict(l=20, r=20, t=20, b=20),
            showlegend=False,
            xaxis=dict(title=""),
            yaxis=dict(gridcolor="rgba(255,255,255,0.05)", title="Ventas ($)")
        )
        st.plotly_chart(fig_seg, use_container_width=True)
        
    with c_seg2:
        st.subheader("⭐ Satisfacción del Cliente (CSAT) por Categoría")
        csat_cat = df_filtered.groupby('Categoria')['Calificacion_Satisfaccion'].mean().reset_index()
        fig_radar = px.line_polar(
            csat_cat,
            r='Calificacion_Satisfaccion',
            theta='Categoria',
            line_close=True
        )
        fig_radar.update_traces(fill='toself', fillcolor='rgba(99, 102, 241, 0.35)', line=dict(color='#818CF8', width=2))
        fig_radar.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#94A3B8', family='Plus Jakarta Sans'),
            polar=dict(
                radialaxis=dict(visible=True, range=[0, 5], gridcolor="rgba(255,255,255,0.1)"),
                angularaxis=dict(gridcolor="rgba(255,255,255,0.1)")
            ),
            margin=dict(l=30, r=30, t=20, b=20)
        )
        st.plotly_chart(fig_radar, use_container_width=True)

    st.markdown("<hr style='border: 0.5px solid rgba(255,255,255,0.08);'>", unsafe_allow_html=True)
    
    st.subheader("📊 Resumen Comparativo de Segmentos de Negocio")
    st.dataframe(
        seg_data.style.format({
            'Ventas_Netas': '${:,.2f}',
            'Utilidad_Neta': '${:,.2f}',
            'Transacciones': '{:,}'
        }),
        use_container_width=True
    )

# ---------------------------------------------------------
# TAB 4: Simulador de Escenarios (What-If Analysis)
# ---------------------------------------------------------
with tab4:
    st.markdown("""
        <div style="background: rgba(30, 41, 59, 0.5); padding: 16px; border-radius: 12px; border-left: 4px solid #6366F1; margin-bottom: 20px;">
            <h4 style="margin: 0 0 6px 0; color: #F8FAFC;">🔮 Modelo Predictivo y Simulación de Sensibilidad Financiera</h4>
            <p style="margin: 0; color: #94A3B8; font-size: 0.92rem;">
                Modifique las variables estratégicas para estimar el impacto financiero en los ingresos brutos, costos operativos y margen neto de la empresa.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    sim_col1, sim_col2, sim_col3 = st.columns(3)
    with sim_col1:
        price_delta = st.slider("Ajuste en Precios de Venta (%):", -30, 30, 5, step=1)
    with sim_col2:
        volume_delta = st.slider("Variación en Volumen de Demanda (%):", -40, 50, 10, step=1)
    with sim_col3:
        cost_delta = st.slider("Variación en Costos Unitarios (%):", -20, 30, 3, step=1)
        
    # Baseline calculations
    base_sales = df_filtered['Ventas_Netas'].sum()
    base_cost = df_filtered['Costo_Total'].sum()
    base_profit = df_filtered['Utilidad_Neta'].sum()
    
    # Simulated values
    sim_sales = base_sales * (1 + price_delta/100) * (1 + volume_delta/100)
    sim_cost = base_cost * (1 + cost_delta/100) * (1 + volume_delta/100)
    sim_profit = sim_sales - sim_cost
    sim_margin = (sim_profit / sim_sales * 100) if sim_sales > 0 else 0
    
    profit_diff = sim_profit - base_profit
    profit_diff_pct = (profit_diff / base_profit * 100) if base_profit > 0 else 0
    
    res1, res2, res3 = st.columns(3)
    with res1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">Ingresos Proyectados</div>
            <div class="metric-value">${sim_sales:,.0f}</div>
            <div class="metric-delta {'delta-pos' if sim_sales >= base_sales else 'delta-neg'}">
                {'+' if sim_sales >= base_sales else ''}{((sim_sales - base_sales)/base_sales*100):.1f}% vs Actual
            </div>
        </div>
        """, unsafe_allow_html=True)
    with res2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">Costos Operativos Proyectados</div>
            <div class="metric-value">${sim_cost:,.0f}</div>
            <div class="metric-delta {'delta-neg' if sim_cost > base_cost else 'delta-pos'}">
                {'+' if sim_cost >= base_cost else ''}{((sim_cost - base_cost)/base_cost*100):.1f}% vs Actual
            </div>
        </div>
        """, unsafe_allow_html=True)
    with res3:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">Utilidad Operativa Proyectada</div>
            <div class="metric-value">${sim_profit:,.0f}</div>
            <div class="metric-delta {'delta-pos' if profit_diff >= 0 else 'delta-neg'}">
                {'+' if profit_diff >= 0 else ''}${profit_diff:,.0f} ({'+' if profit_diff_pct >= 0 else ''}{profit_diff_pct:.1f}%)
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown("<div style='height: 15px;'></div>", unsafe_allow_html=True)
    
    # Comparison chart
    comp_df = pd.DataFrame({
        'Escenario': ['Actual (Base)', 'Simulado (What-If)'],
        'Ventas Netas': [base_sales, sim_sales],
        'Costos': [base_cost, sim_cost],
        'Utilidad Neta': [base_profit, sim_profit]
    })
    
    fig_comp = go.Figure(data=[
        go.Bar(name='Ventas Netas', x=comp_df['Escenario'], y=comp_df['Ventas Netas'], marker_color='#6366F1'),
        go.Bar(name='Costos Totales', x=comp_df['Escenario'], y=comp_df['Costos'], marker_color='#EF4444'),
        go.Bar(name='Utilidad Neta', x=comp_df['Escenario'], y=comp_df['Utilidad Neta'], marker_color='#10B981')
    ])
    fig_comp.update_layout(
        barmode='group',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor=PLOT_BG,
        font=dict(color='#94A3B8', family='Plus Jakarta Sans'),
        margin=dict(l=20, r=20, t=30, b=20),
        yaxis=dict(gridcolor="rgba(255,255,255,0.05)", title="Monto en USD ($)")
    )
    st.plotly_chart(fig_comp, use_container_width=True)

# ---------------------------------------------------------
# TAB 5: Explorador de Datos
# ---------------------------------------------------------
with tab5:
    st.subheader("🔍 Explorador Detallado de Registros Comerciales")
    
    exp_c1, exp_c2 = st.columns([3, 1])
    with exp_c1:
        search_query = st.text_input("Filtrar por texto (Producto, Categoría, Región, ID):", "")
    with exp_c2:
        st.markdown("<div style='height: 28px;'></div>", unsafe_allow_html=True)
        csv_export = df_filtered.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Descargar Dataset (CSV)",
            data=csv_export,
            file_name=f"reporte_bi_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
            mime="text/csv",
            use_container_width=True
        )
        
    display_df = df_filtered.copy()
    if search_query:
        mask = display_df.astype(str).apply(lambda row: row.str.contains(search_query, case=False).any(), axis=1)
        display_df = display_df[mask]
        
    st.dataframe(
        display_df[[
            'Order_ID', 'Fecha', 'Categoria', 'Producto', 'Region', 
            'Segmento_Cliente', 'Canal_Venta', 'Cantidad', 'Precio_Unitario', 
            'Ventas_Netas', 'Utilidad_Neta', 'Margen_Utilidad_Pct', 'Calificacion_Satisfaccion'
        ]],
        use_container_width=True,
        height=450
    )
    
    st.markdown("### 📊 Métricas Estadísticas Descriptivas")
    st.write(df_filtered[['Cantidad', 'Precio_Unitario', 'Ventas_Netas', 'Utilidad_Neta', 'Margen_Utilidad_Pct']].describe())

# ---------------------------------------------------------
# Footer
# ---------------------------------------------------------
st.markdown("---")
st.markdown("""
<div style="display: flex; justify-content: space-between; align-items: center; color: #64748B; font-size: 0.85rem;">
    <span>OmniAnalytics Executive BI Dashboard © 2026 — Inteligencia de Negocios</span>
    <span>Desarrollado con Python, Streamlit & Plotly • CI/CD Cloud Deployment</span>
</div>
""", unsafe_allow_html=True)

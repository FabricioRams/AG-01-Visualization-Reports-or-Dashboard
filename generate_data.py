import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_bi_data():
    np.random.seed(42)
    n_records = 2500
    
    start_date = datetime(2025, 1, 1)
    end_date = datetime(2026, 9, 30)
    days_range = (end_date - start_date).days
    
    categories = {
        'Tecnología y Gadgets': ['Laptops Pro', 'Monitores UltraWide', 'Smartphones Enterprise', 'Accesorios Wireless', 'Servidores Cloud Edge'],
        'Electrohogar & Smart Home': ['Aspiradoras Robot', 'Sistemas IoT', 'Purificadores de Aire', 'Iluminación Inteligente'],
        'Moda & Wearables': ['Relojes Inteligentes', 'Prendas Térmicas Tech', 'Calzado Ergonómico', 'Mochilas Smart'],
        'Servicios B2B': ['Consultoría en Cloud', 'Soporte 24/7 Premium', 'Licenciamiento SaaS BI', 'Auditoría de Datos'],
        'Salud & Bienestar': ['Monitores Biométricos', 'Ergonomía de Oficina', 'Nutrición Funcional', 'Purificación de Agua']
    }
    
    regions = ['Norte (Monterrey / Chihuahua)', 'Centro (CDMX / Bajío)', 'Sur (Puebla / Mérida)', 'Occidente (Guadalajara)', 'Internacional (LATAM)']
    segments = ['Corporativo / Enterprise', 'Pequeña y Mediana Empresa (Pyme)', 'Consumidor Final (B2C)', 'Gobierno / Educativo']
    channels = ['Portal Web Directo', 'Fuerza de Ventas Directa', 'Marketplace Aliado', 'App Móvil']
    payment_methods = ['Transferencia Bancaria', 'Tarjeta de Crédito Corporativa', 'Pasarela Online (Stripe/PayPal)', 'Crédito a 30 días']
    
    data = []
    
    for i in range(1, n_records + 1):
        order_id = f"ORD-2025-{10000 + i}"
        random_days = np.random.randint(0, days_range)
        date = start_date + timedelta(days=random_days)
        
        category = np.random.choice(list(categories.keys()), p=[0.35, 0.20, 0.15, 0.20, 0.10])
        product = np.random.choice(categories[category])
        region = np.random.choice(regions, p=[0.25, 0.35, 0.15, 0.15, 0.10])
        segment = np.random.choice(segments, p=[0.35, 0.30, 0.25, 0.10])
        channel = np.random.choice(channels, p=[0.40, 0.25, 0.20, 0.15])
        payment = np.random.choice(payment_methods, p=[0.30, 0.35, 0.25, 0.10])
        
        quantity = np.random.choice([1, 2, 3, 5, 8, 10, 15, 20], p=[0.35, 0.25, 0.15, 0.10, 0.05, 0.05, 0.03, 0.02])
        
        # Base unit prices depending on category
        if category == 'Tecnología y Gadgets':
            unit_price = np.random.uniform(250.0, 1850.0)
            cost_factor = np.random.uniform(0.60, 0.75)
        elif category == 'Servicios B2B':
            unit_price = np.random.uniform(500.0, 3500.0)
            cost_factor = np.random.uniform(0.35, 0.50)
        elif category == 'Electrohogar & Smart Home':
            unit_price = np.random.uniform(120.0, 850.0)
            cost_factor = np.random.uniform(0.55, 0.70)
        elif category == 'Moda & Wearables':
            unit_price = np.random.uniform(45.0, 320.0)
            cost_factor = np.random.uniform(0.40, 0.60)
        else:
            unit_price = np.random.uniform(80.0, 600.0)
            cost_factor = np.random.uniform(0.45, 0.65)
            
        unit_price = round(unit_price, 2)
        unit_cost = round(unit_price * cost_factor, 2)
        
        # Discount (0% to 15%)
        discount_rate = np.random.choice([0.0, 0.05, 0.10, 0.15], p=[0.5, 0.25, 0.15, 0.10])
        total_gross = round(unit_price * quantity, 2)
        discount_amount = round(total_gross * discount_rate, 2)
        total_net_sales = round(total_gross - discount_amount, 2)
        total_cost = round(unit_cost * quantity, 2)
        profit = round(total_net_sales - total_cost, 2)
        margin_pct = round((profit / total_net_sales) * 100, 2) if total_net_sales > 0 else 0
        
        # Customer rating 1 to 5
        csat = np.random.choice([3, 4, 5, 2, 1], p=[0.15, 0.45, 0.30, 0.07, 0.03])
        
        data.append({
            'Order_ID': order_id,
            'Fecha': date.strftime('%Y-%m-%d'),
            'Año': date.year,
            'Mes': date.strftime('%B'),
            'Mes_Num': date.month,
            'Trimestre': f"Q{(date.month - 1) // 3 + 1}",
            'Categoria': category,
            'Producto': product,
            'Region': region,
            'Segmento_Cliente': segment,
            'Canal_Venta': channel,
            'Metodo_Pago': payment,
            'Cantidad': quantity,
            'Precio_Unitario': unit_price,
            'Costo_Unitario': unit_cost,
            'Ventas_Brutas': total_gross,
            'Descuento_Aplicado': discount_amount,
            'Ventas_Netas': total_net_sales,
            'Costo_Total': total_cost,
            'Utilidad_Neta': profit,
            'Margen_Utilidad_Pct': margin_pct,
            'Calificacion_Satisfaccion': csat
        })
        
    df = pd.DataFrame(data)
    df.sort_values(by='Fecha', inplace=True)
    df.to_csv('data/retail_bi_dataset.csv', index=False, encoding='utf-8')
    print(f"Dataset generated successfully with {len(df)} rows.")

if __name__ == '__main__':
    import os
    os.makedirs('data', exist_ok=True)
    generate_bi_data()

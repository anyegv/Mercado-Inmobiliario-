# Mercado-Inmobiliario-
# Análisis del Mercado Inmobiliario en Cuba

> Estado: 🚧 En desarrollo — Fase de análisis y recopilación de datos

## 🎯 Objetivo del proyecto
Analizar el comportamiento del mercado inmobiliario en Cuba (venta y alquiler)
a partir de datos obtenidos de portales web, redes sociales y fuentes oficiales,
para identificar patrones de precios, oferta y demanda según ubicación geográfica.

## 📊 Análisis planteado

### Preguntas a responder
- ¿Por qué en los municipios más poblados hay más apartamentos en venta que en los menos poblados?
- ¿Por qué en los últimos tiempos se ofertan más casas amuebladas que sin amueblar?
- ¿Cómo se comportan los precios de alquiler por noche en zonas céntricas y turísticas
  (Vedado en La Habana, Varadero en Matanzas)?
- ¿Qué influencia tienen los servicios adicionales al momento de comprar una casa?
- ¿Cuántas casas se venden por año o por mes en cada provincia?

### Visualizaciones previstas
- 🥧 **Gráfica circular**: proporción de casas amuebladas vs. sin amueblar en venta.
- 📊 **Gráfica de barras agrupadas**: comparación de precios de alquiler por noche
  entre zonas (Vedado, Varadero y otras).
- 📈 **Series temporales**: cantidad de casas vendidas por año/mes por provincia.

### Hipótesis iniciales
- La oferta se concentra en municipios con mayor población y actividad económica.
- El aumento de casas amuebladas en venta puede responder a migración o urgencia de venta.
- Los precios de alquiler en zonas turísticas superan ampliamente a los céntricos no turísticos.

## 🗺️ Metodología (cómo lo voy a hacer)

### Fuentes de datos
- **Scraping web**:
  - Cubisima
  - Revolico
- **Redes sociales**:
  - Grupos de Facebook
  - Grupos de WhatsApp
  - Cuentas especializadas en Instagram
- **Fuentes oficiales**:
  - Datos estadísticos oficiales (ONEI u otras)

### Fases del proyecto
1. **Fase 1 – Análisis y definición** ✅ (en curso)
   - Planteamiento de preguntas
   - Definición de fuentes
2. **Fase 2 – Recopilación de datos**
   - Scraping de portales
   - Búsqueda manual en redes sociales
   - Consulta de fuentes oficiales
3. **Fase 3 – Procesamiento y limpieza**
4. **Fase 4 – Visualización y conclusiones**

### Pasos concretos
- [ ] Definir variables a extraer (precio, ubicación, metros, amueblado, etc.)
- [ ] Diseñar scraper para Cubisima
- [ ] Diseñar scraper para Revolico
- [ ] Recopilar datos de redes sociales manualmente
- [ ] Obtener datos oficiales por provincia
- [ ] Limpiar y unificar los datos
- [ ] Generar gráficas
- [ ] Redactar conclusiones

## 📅 Progreso
| Fecha | Avance |
|-------|--------|
| 10/10 | Planteamiento de preguntas y fuentes de datos |

## 📝 Notas y dudas abiertas
- Aún por definir: qué variables exactas extraer de cada fuente.
- Verificar disponibilidad y actualización de datos oficiales por provincia.
- Evaluar si los datos de redes sociales son comparables con los de los portales.
- Pendiente: definir herramientas para scraping (Python + BeautifulSoup/Scrapy).
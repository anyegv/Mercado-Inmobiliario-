# Mercado Inmobiliario en Cuba

**Reporte Técnico**

3 de noviembre de 2026

---

## 1. Resumen

Este proyecto presenta un análisis exploratorio del mercado inmobiliario cubano, con énfasis en La Habana. A partir de datos recolectados de Casa Oasis y de fuentes digitales informales (Revolico, Facebook y grupos de WhatsApp), se analiza cómo los servicios básicos, la ubicación geográfica, la cantidad de cuartos y el tipo de vivienda se relacionan con el precio. El trabajo combina análisis visual, descriptivo y cuantitativo, y se materializa en un conjunto de módulos en Python que cargan los datos, los transforman y generan las visualizaciones. La recolección de datos comenzó el 3 de octubre. El proyecto es de carácter individual y los objetivos planteados fueron cumplidos, con ajustes surgidos durante el proceso de desarrollo.

---

## 2. Contexto y planteamiento

Durante el desarrollo surgieron varias preguntas de investigación; sin embargo, las limitaciones de los datos obligaron a descartar algunas (cantidad de casas vendidas por año en el país, accesible solo vía MINJUS; comparación histórica de precios, sin fuente oficial) y a concentrar el trabajo en los análisis que relacionan precio con atributos de la vivienda.

---

## 3. Datos y fuentes

**Fuentes:**

1. **Casa Oasis**, portal inmobiliario líder en Cuba, orientado a comprar, vender, permutar y rentar propiedades.
2. **Fuentes digitales informales:** Revolico, Facebook y grupos de WhatsApp, que funcionan como mercados paralelos de referencia para la población.

**Limitaciones:**

- Muchas fuentes son informales y presentan sesgos de información.
- No existe una fuente oficial histórica que permita comparar precios entre años.
- El volumen de datos de ventas por año solo es accesible a través del MINJUS, por lo que ese análisis fue descartado.

---

## 4. Arquitectura del proyecto

El proyecto se organiza en módulos independientes:

- **`Funciones.py`**: carga y transformación de datos. Extrae precios de alquileres, identifica servicios asociados a cada vivienda, agrupa precios por cantidad de cuartos y consolida precios por zona.
- **`Graficas.py`**: visualizaciones estáticas. Genera el scatter de servicios vs. precio, las barras horizontales por tipo de vivienda, el gráfico de líneas de comparación internacional, las barras por cantidad de cuartos y las curvas de densidad.
- **`Proyecto.ipynb`**: notebook que orquesta el flujo, carga los módulos y contiene el contexto narrativo del análisis.

Los datos se almacenan en archivos JSON (`Alquileres`, `Casas x Cuarto`, `Alquileres x Zona`).

---

## 5. Análisis y resultados

### 5.1 Servicios básicos y precio de alquiler

Se extraen 30 alquileres, cada uno evaluado frente a ocho servicios básicos: Respaldo Energético, Tanque de Agua, Teléfono Fijo, Wifi, Climatización, Gas de la Calle, Calentador y Lavadora. La visualización es una nube de puntos donde cada punto representa una casa que posee un servicio, ordenada por precio. La mayoría de los puntos se concentran en los servicios de mayor impacto (Wifi, Climatización y Respaldo Energético), y los precios más altos tienden a concentrar una mayor cantidad de servicios.

### 5.2 Cantidad de cuartos

El gráfico de barras muestra un crecimiento escalonado muy marcado según la cantidad de cuartos. El precio promedio se incrementa de forma pronunciada al pasar de una a dos y de dos a tres habitaciones.

### 5.3 Tipo de vivienda

El gráfico de barras horizontales ordena los tipos de vivienda de menor a mayor precio mediano. Se observa un gradiente claro entre las categorías, con las viviendas independientes en el extremo superior.

### 5.4 Distribución de precios por zona

Se comparan las distribuciones de precios de alquiler de tres zonas de La Habana: Plaza de la Revolución, Centro Habana y Playa, mediante curvas de densidad (KDE). La forma de cada curva revela la concentración de precios en cada zona y permite contrastar sus perfiles de dispersión.

### 5.5 Comparación internacional

El gráfico de líneas compara los años de salario íntegro necesarios para comprar una vivienda en Brasil, El Salvador, México y Cuba. Los resultados son dramáticamente desiguales: Cuba se sitúa en el extremo más desfavorable del grupo, muy por encima del resto de los países analizados.

---

## 6. Conclusiones

Los análisis realizados permiten sostener las siguientes conclusiones:

- Los servicios básicos, y en particular Wifi, Climatización y Respaldo Energético, se asocian a los precios de alquiler más altos. Las viviendas con más servicios tienden a ubicarse en los tramos superiores de precio.
- La cantidad de cuartos no incrementa el precio de forma lineal, sino escalonada y marcada.
- El tipo de vivienda establece un gradiente de precio mediano claro, con las viviendas independientes a la cabeza.
- Las distribuciones de precios por zona difieren entre sí, lo que confirma que la ubicación no opera como un factor neutro.
- La comparación internacional ubica a Cuba en una situación de desigualdad extrema frente a los otros países analizados, en términos de años de salario necesarios para acceder a una vivienda.

En conjunto, los resultados confirman la hipótesis de partida: en el mercado inmobiliario habanero, los atributos de la vivienda no suman, multiplican. Los objetivos planteados fueron cumplidos, considerando los ajustes realizados durante el proceso de desarrollo y las restricciones impuestas por la disponibilidad y calidad de los datos.

---

**Documentación relacionada:** `journal.md`, `hands-off.md`
**Repositorio:** `/docs/`
**Código fuente:** `Funciones.py`, `Graficas.py`, `Proyecto.ipynb`
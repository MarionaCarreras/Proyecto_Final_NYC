# Proyecto_Final_NYC
# Análisis Exploratorio de Datos (EDA) - Incidencias 311 y Condiciones Meteorológicas en NYC

Este proyecto tiene como objetivo realizar un análisis exploratorio de datos (EDA) sobre incidencias reportadas en el servicio **NYC 311** y su relación con variables meteorológicas. Se han combinado dos fuentes de datos simuladas: reportes de incidencias ciudadanas y registros diarios de clima. El análisis permite observar patrones de quejas, tiempos de respuesta, distribución geográfica y posibles relaciones con la climatología.  

El periodo de datos abarca **enero a diciembre de 2023**.

---

## Herramientas Utilizadas

- **Python**: Lenguaje de programación principal para el procesamiento y análisis.
- **Pandas**: Librería para manipulación de datos.
- **Matplotlib**: Librería de visualización para generación de gráficos.
- **Visual Studio Code**: Editor de código utilizado.
- **Excel**: Herramienta BI utilizada para generar el dashboard.

---

## Datos

Se han utilizado **dos conjuntos de datos principales**:

### Dataset: `nyc_311_sample.csv`  
Contiene registros de incidencias reportadas a NYC 311:  

- `unique_key`: Identificador único de la incidencia.  
- `created_date`: Fecha y hora de creación de la incidencia.  
- `closed_date`: Fecha de cierre.  
- `complaint_type`: Tipo de queja (ruido, aparcamiento ilegal, alcantarillado, etc.).  
- `borough`: Distrito de Nueva York (Manhattan, Brooklyn, Bronx, Queens, Staten Island).  
- `agency`: Agencia responsable.  
- `status`: Estado de la incidencia (Cerrada, Abierta, Pendiente).  
- `latitude` / `longitude`: Localización geográfica.  
- `descriptor`: Descripción de la queja.  

### Dataset: `nyc_weather_sample.csv`  
Contiene registros diarios del clima en NYC:  

- `date`: Fecha del registro.  
- `tmin`: Temperatura mínima.  
- `tmax`: Temperatura máxima.  
- `precipitation`: Precipitación (mm).  
- `wind`: Velocidad del viento (km/h).  

Tras la limpieza, se generó un **dataset final** `nyc_311_weather_final.csv` que combina ambos, incluyendo nuevas variables:  

- `time_to_close_days`: Tiempo en días hasta el cierre de la incidencia.  
- `temp_avg`: Temperatura promedio diaria.  
- `rainy_day`: Indicador de si llovió ese día (precipitación > 0.2 mm).  

---

## Archivos del Repositorio

- `README.md`: Descripción y pasos del proyecto.  
- Carpeta `data/`:  
  - `raw/`: datasets en bruto.  
  - `interim/`: datasets limpios intermedios.  
  - `final/`: dataset final combinado.  
- Carpeta `src/`: scripts de soporte (`cleaning.py`, `data_load.py`, `eda_plots.py`).  
- Archivo `eda_python_.py`: ejecución del pipeline completo.  
- Carpeta `notebooks/`: contiene el notebook `01_exploratory_data_analysis.ipynb` con el análisis interactivo.  
- Carpeta `reports/`: informe final en PDF y gráficas generadas.  
- Carpeta `dashboard/`: contiene el archivo `NYC311_Dashboard_PRO.xlsx` con el dashboard en Excel.  

---

## Pasos del Proyecto

1. **Transformación y limpieza de datos**
   - Normalización de nombres de columnas.
   - Conversión de tipos de datos (fechas, categorías).
   - Creación de nuevas variables (`time_to_close_days`, `temp_avg`, `rainy_day`).
   - Eliminación de duplicados y registros inconsistentes.

2. **Análisis descriptivo**
   - Conteo de incidencias por distrito, tipo de queja y agencia.
   - Tiempo medio de respuesta.
   - Relación entre clima y volumen de incidencias.

3. **Visualización**
   - Incidencias diarias (serie temporal).
   - Top 10 tipos de queja.
   - Distribución de quejas por distrito.
   - Relación entre precipitación y número de incidencias.

4. **Archivos limpios**
   - Se guardaron los datasets transformados en `data/interim/` y `data/final/`.

5. **Dashboard en Excel**
   - **Hoja Data**: dataset completo como tabla.  
   - **Hoja Lists**: listas desplegables para selectores.  
   - **Hoja Calculos**: métricas y agregaciones filtradas.  
   - **Hoja Dashboard**: interfaz principal con:  
     - KPIs (Incidencias totales, Tiempo medio de cierre, % cerradas ≤7 días).  
     - Gráfico de incidencias diarias filtradas.  
     - Top 10 quejas filtrado.  
     - Selectores interactivos para filtrar por *Borough* y *Complaint*.  

---

## Resultados

- **Incidencias**: Se detectan picos estacionales de incidencias, con mayor concentración en meses fríos.  
- **Tipos de queja**: Las más frecuentes son **Noise** y **Illegal Parking**.  
- **Tiempos de cierre**: En promedio, ~3 días, con un 70% cerradas en menos de una semana.  
- **Relación con clima**: Se observa un ligero aumento de incidencias en días lluviosos.  

---

## Conclusión Final

El análisis exploratorio muestra que:  
- El **ruido** es la queja más recurrente en la ciudad.  
- Los **tiempos de resolución** son en general rápidos, aunque variables entre agencias y distritos.  
- El **clima** parece influir en ciertos tipos de incidencias (como problemas de alcantarillado en días lluviosos).  

  

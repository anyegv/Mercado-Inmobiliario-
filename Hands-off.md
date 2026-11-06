# Hands-Off: Mercado Inmobiliario en Cuba

## 1. Estado actual
El proyecto se encuentra **100% funcional en local** y listo para revisión. No requiere configuración especial ni variables de entorno para ejecutarse. 

Todos los códigos funcionan juntos. Si falta uno de los módulos, el código final se rompe. El proyecto está diseñado para ejecutarse de principio a fin desde el entorno local (Jupyter Notebook).

## 2. Cómo ejecutar el proyecto
1. Asegurarse de tener instaladas las dependencias (principalmente `matplotlib`, `numpy` y `statistics`).
2. Abrir el archivo `Proyecto.ipynb` en Jupyter Notebook o Jupyter Lab.
3. Ejecutar las celdas en orden secuencial.

No se requiere ninguna configuración adicional.

## 3. Estructura del código
El flujo de ejecución y la dependencia entre archivos es la siguiente:

*   **`Funciones.py`**: Módulo de carga y procesamiento. Contiene la lógica para abrir los JSON y transformar los datos.
*   **`Graficas.py`**: **El archivo principal.** Aquí se confeccionan todas las gráficas y se genera el resultado final del proyecto. Importa y utiliza las funciones de los otros módulos. Si alguien quiere ver los resultados directos, debe ejecutar o revisar este archivo.
*   **`Proyecto.ipynb`**: Notebook que orquesta todo, llama a las funciones y contiene el contexto narrativo.

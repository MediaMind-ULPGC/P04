## Ejercicio 2

Construir una pequeña aplicación que permita operar con diferentes filtros (con un selector) y trabajar con varios umbrales. (uno para los filtros pasa-bajo y pasa-alto y dos para los filtros pasa-banda y rechaza-banda). Demuestre su funcionalidad con señales ruidosas. Muestre en cada filtrado la señal original y filtrada en el dominio temporal y en el dominio de la frecuencia. 

**Flujo del programa**

Para poder comprender el funcionamiento de la aplicación, primero deberémos desglosar la función `apply_filter` ya que es la pieza fundamental de esta.

```python
def apply_filter(data, filter_type, cutoff, fs, order=5, band=None):
    nyquist = 0.5 * fs
    if filter_type == 'low':
        normal_cutoff = cutoff / nyquist
        b, a = butter(order, normal_cutoff, btype='low', analog=False)
    elif filter_type == 'high':
        normal_cutoff = cutoff / nyquist
        b, a = butter(order, normal_cutoff, btype='high', analog=False)
    elif filter_type == 'band':
        low, high = band
        low /= nyquist
        high /= nyquist
        b, a = butter(order, [low, high], btype='band', analog=False)
    elif filter_type == 'notch':
        low, high = band
        low /= nyquist
        high /= nyquist
        b, a = butter(order, [low, high], btype='bandstop', analog=False)
    y = lfilter(b, a, data)
    return y
```

Como su nombre indica, la función `apply_filter` es la encargada de aplicar los diferentes filtos al audio que empleará la aplicación:
* `data`: corresponde con la señal de entrada a filtrar.
* `filter_type`: es el tipo de filtro que quieres aplicar a la señal de entrada (paso-bajo, paso-alto, pasa-banda, banda-rechazada).
* `cutoff`: es la frecuencia de corte en Hz para los filtros pasa-bajo y pasa-alto.
* `fs`: es la frecuencia de muestreo de la señal en Hz.
* `order`: es el orden del filtro `Butterworth`. Por defecto es 5, donde un valor más alto crea un filtro más pronunciado.
* `band`: un rango de frecuencias altas y bajas en Hz, requerido solo para los filtros pasa-banda y banda-rechazada.

Definición del límite Nyquist

La frecuencia de Nyquist se calcula como la mitad de la frecuencia de muestreo. Es el límite máximo en el que se pueden definir las frecuencias de corte.
```python
nyquist = 0.5 * fs
```
Tipos de filtros

1. Filtro paso-bajo
   
Permite que solo pasen las frecuencias por debajo de `cutoff`.
```python
normal_cutoff = cutoff / nyquist
b, a = butter(order, normal_cutoff, btype='low', analog=False)
```
2. Filtro paso-alto

Permite que solo pasen las frecuencias por encima de `cutoff`.
```python
normal_cutoff = cutoff / nyquist
b, a = butter(order, normal_cutoff, btype='high', analog=False)
```
3. Filtro paso-banda

Permite el paso de frecuencias en un rango especificado por `band`.
```python
low, high = band
low /= nyquist
high /= nyquist
b, a = butter(order, [low, high], btype='band', analog=False)
```
4. Filtro banda-rechazada

Elimina las frecuencias en un rango especificado por `band`.
```python
low, high = band
low /= nyquist
high /= nyquist
b, a = butter(order, [low, high], btype='bandstop', analog=False)
```

### AudioFilterApp

Esta aplicación permite a los usuarios aplicar diferentes tipos de filtros a archivos de audio y visualizar tanto la señal original como la filtrada en dominios de tiempo y frecuencia, mediante el uso de la función `apply_filter`.

*Funciones principales*

* `select_file`: Permite al usuario seleccionar un archivo de audio tipo `.wav` desde su dispositivo para su procesamiento.
* `plot_original_and_filtered_audio`: Muestra la señal original y la señal filtrada (si se ha aplicado un filtro) en dominios del tiempo y la frecuencia.
* `update_filter`: Actualiza la señal de audio cuando el usuario cambia el filtro o los parámetros de frecuencia de corte, y aplica el filtro seleccionado.

*Caso de uso*

1. Ejecuta el programa para abrir la interfaz gráfica de la aplicación.
2. Haz clic en el botón "Seleccionar Archivo" para elegir un archivo de audio de tu dispositivo.
3. Selecciona el filtro que deseas aplicar a la señal de audio.
4. Ajusta las frecuencias de corte según el filtro seleccionado.
5. Visualiza las gráficas de la señal de audio original y la señal filtrada en una nueva ventana.

### AudioPlayer

Esta aplicación permite al usuario seleccionar, reproducir, modificar y guardar archivos de audio con diferentes filtros de frecuencia, al igual que la aplicación anterior, `AudioPlayer` emplea la función `apply_filter` y para la reproducción del audio original o filtrado empleamos la API de VLC, ya que nos aporta una calidad del audio que otras librerías o APIs de python no nos aportaban.

*Requisitos*

Asegúrate de tener VLC instalado en tu sistema.
En sistemas basados en Linux, puedes instalar VLC con:
```bash
sudo apt-get install vlc
```
En sistemas Windows o Mac, descarga VLC desde su sito [web oficial](https://www.videolan.org/vlc/index.es.html).

*Funciones principales*

* `select_file`: Permite seleccionar un archivo de audio desde el dispositivo.
* `apply_selected_filter`: Aplica el filtro seleccionado y actualiza la vista de la señal.
* `toggle_play`: Controla la reproducción y pausa del audio.
* `set_volume`: Ajusta el volumen del reproductor VLC.
* `save_file`: Guarda el archivo de audio filtrado en la ubicación especificada.
* `update_waveform`: Actualiza la gráfica de la señal de audio en la interfaz.

*Caso de uso*

1. Ejecuta la aplicación para abrir la interfaz gráfica.
2. Selecciona un archivo de audio.
3. Selecciona el filtro deseado y ajusta sus parámetros de frecuencia.
4. Haz clic en el botón "Reproducir" para escuchar el audio filtrado.
5. Ajusta el volumen según prefieras.
6. Guarda el archivo filtrado haciendo clic en "Guardar Archivo Filtrado".









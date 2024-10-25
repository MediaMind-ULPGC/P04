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







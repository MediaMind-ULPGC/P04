# Práctica 4: Procesamiento de audio.

Integrantes:
- Gerardo León Quintana
- Susana Suárez Mendoza

## Ejercicio 1:

Construir un identificador de notas musicales. Es decir; en su versión más sencilla (y suficiente) la entrada es un sonido con una sola nota musical y debe identificar cuál es. Por simplicidad elija un único instrumento para la identificación. 

Este ejercicio tiene como objetivo desarrollar un sistema de programación que simule las notas musicales de diversos instrumentos. Los instrumentos considerados son los siguientes: piano, trompeta, guitarra, violín y xilófono.

### 1. Implementación de intrumentos y acordes

 La implementación se ha realizado a través de módulos y clases, los cuales se describen en detalle a continuación.
 
- `/musical_notes`: Este módulo contiene las clases correspondientes a cada instrumento, en las que se definen las frecuencias de las notas musicales y sus respectivas octavas. En la Figura 1 se presenta el diagrama de clases para el instrumento piano, como ejemplo representativo. Las notas sostenidas han sido omitidas en el diagrama para mejorar la legibilidad. Sin embargo, la estructura para los demás instrumentos sigue el mismo esquema, variando únicamente en las frecuencias específicas de cada nota, acorde al instrumento y a la octava correspondiente.


  <div align="center">
    <img src="images/piano_notes_uml.png" alt="Diagrama Piano Notas" />
      <p><strong>Figura 1.</strong> Diagrama de clases para las notas musicales del piano.</p> 
  </div>

- `/identifiers`: Este módulo agrupa los submódulos diseñados para identificar diversos aspectos de una señal de audio, como notas individuales, acordes, y secuencias de notas a lo largo del tiempo con el fin de aproximar la partitura del sonido.
  - `/single_notes`: Este submódulo implementa la identificación de una nota musical en función del instrumento. Contiene una clase principal que sigue el patrón de diseño creacional *Factory Method*. Este patrón define una interfaz para la creación de objetos en una superclase, pero permite que las subclases definan el tipo específico de objeto que será creado. En este contexto, el patrón facilita la creación de un identificador de nota basado en el instrumento, proporcionando simplemente el nombre del mismo. Para obtener más detalles sobre los parámetros y las devoluciones de los métodos, se debe consultar el código fuente.

  <div align="center">
      <img src="images/ident_single_note.png" alt="Diagrama Identificar 1 Nota" />
        <p><strong>Figura 2.</strong> Diagrama de clases para la identificación de una nota.</p> 
  </div>

  - `/chords`: Este submódulo contiene las clases necesarias para identificar o aproximar los acordes de un archivo de audio que contiene un único acorde. Al igual que el submódulo anterior, utiliza una clase que implementa el patrón *Factory Method*. Además, cuenta con una clase que define todos los acordes y sus notas correspondientes, de la cual heredan los identificadores de acordes para cada instrumento. Esto facilita la expansión del sistema con nuevos instrumentos sin necesidad de modificar el código existente.
 
    <div align="center">
      <img src="images/chords_uml_diagram.png" alt="Diagrama Acordes" width = 900 />
        <p><strong>Figura 2.</strong> Diagrama de clases para la identificación de acordes. </p> 
    </div>

  - `/scales`: Este submódulo se encarga de identificar notas a lo largo de un intervalo de tiempo $t$, específicamente para instrumentos como el piano y la guitarra, debido a la simplicidad de su estructura. El objetivo es extraer y analizar secuencias de notas a lo largo del tiempo para aproximar la escala o partitura del audio analizado.
 
    <div align="center">
      <img src="images/uml_scale.png" alt="Diagrama Escalas" width = 700 />
        <p><strong>Figura 3.</strong> Diagrama de clases para la identificación de notas musicales a lo largo del tiempo. </p> 
    </div>

- `dominant_frequency.py`: Esta clase es la pieza central del proyecto, ya que es responsable de realizar las Transformadas de Fourier necesarias para extraer las frecuencias dominantes de la señal de audio. Sus principales métodos se describen a continuación: 

```python
# Calcula la Transformada de Fuorier y devuelve las frecuencias fundamentales
def _get_frequencies(sr, data):
  ...
  return fourier,freqs

# Devuelve la frecuencia de mayor magnitud
def get_dominant_frequency(audio_file):
  ...
  return freqs[np.argmax(fourier)]

# Identifica las n frecuencias dominantes en un archivo de audio
get_dominant_frequencies(audio_file, num_frequencies=3, min_distance=5):
  ...
  return dominant_frequencies
```

### 2. Notebook de presentación

El notebook cuyo nombre es `Ejercicio_1.ipynb` se utiliza para presentar los resultados en base a los audios de prueba descargados que se encuentran en la carpeta `/audios`. Dichos audios se han descargado de la página web [freesound](https://freesound.org/) la cual contiene audios de libre disposición.

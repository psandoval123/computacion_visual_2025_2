💾 Repositorio desarrollado en: Python, React Three Fiber, OpenCV, NumPy, Vite y MediaPipe
📅 Autor: Pablo Felipe Sandoval Menjura
🏫 Universidad Nacional de Colombia — Ingeniería de Sistemas y Computación
1️⃣ 🧪 Jerarquías y Transformaciones: El Árbol del Movimiento

🧩 Ejercicio Realizado
Breve explicación (qué hice y por qué):
En este ejercicio implementé una escena 3D interactiva usando React Three Fiber y Vite, enfocándome en comprender cómo funcionan las transformaciones jerárquicas en un entorno tridimensional.

Construí una estructura con tres niveles (padre, hijo y nieto) para observar cómo las transformaciones —traslación, rotación y escala— se propagan en cascada a los objetos hijos. Incorporé controles con Leva para manipular el nodo padre y añadí ayudas visuales como ejes y grillas.

El objetivo fue visualizar cómo los cambios en el objeto padre afectan toda la jerarquía, principio esencial en los sistemas gráficos 3D.

2️⃣ 👁️ Visión Artificial con OpenCV

🧩 Ejercicio Realizado
Breve explicación (qué hice y por qué):
En este ejercicio exploré los fundamentos de la visión artificial utilizando la biblioteca OpenCV en Python. Apliqué filtros convolucionales (desenfoque, enfoque y detección de bordes) mediante operadores Sobel, Laplaciano y Canny.

El objetivo fue comprender cómo los computadores procesan imágenes digitales a través de operaciones matemáticas sobre píxeles, observando las diferencias en cada método y su utilidad en segmentación y reconocimiento de objetos.

3️⃣ 🎨 Rasterización desde Cero (Línea, Círculo, Triángulo)

🧩 Ejercicio Realizado
Breve explicación (qué hice y por qué):
Implementé desde cero los algoritmos clásicos de rasterización para generar primitivas gráficas básicas —líneas, círculos y triángulos— sin usar librerías de alto nivel.

Desarrollé el algoritmo de Bresenham para líneas, el de punto medio para círculos y el método scanline para triángulos, apoyándome solo en Pillow, NumPy y Matplotlib.
El objetivo fue comprender cómo los gráficos vectoriales se transforman en píxeles y cómo la precisión y eficiencia afectan el resultado visual.

4️⃣ 📐 Análisis Geométrico (Centroide, Área, Perímetro)

🧩 Ejercicio Realizado
Breve explicación (qué hice y por qué):
Apliqué técnicas de análisis geométrico sobre imágenes binarizadas con OpenCV para extraer métricas descriptivas como área, perímetro y centroide.

Utilicé funciones como findContours, contourArea, arcLength y los momentos geométricos. Luego etiqueté cada objeto con sus métricas y generé un GIF animado con los resultados.
Este ejercicio permitió entender cómo los contornos pueden convertirse en datos cuantitativos útiles para reconocimiento de formas.

5️⃣ 💠 Importando el Mundo (OBJ/STL/GLTF)

🧩 Ejercicio Realizado
Breve explicación (qué hice y por qué):
Trabajé con distintos formatos de modelos 3D —OBJ, STL y GLTF— usando Trimesh en Python. Analicé diferencias en el almacenamiento de vértices, caras, normales y materiales, además de realizar conversiones entre formatos.

El objetivo fue comprender la interoperabilidad entre entornos 3D y la pérdida de información que puede producirse al convertir.
Elegí este ejercicio porque muestra la importancia de los estándares 3D para diseño, simulación y desarrollo interactivo.

6️⃣ 🌐 Escenas Paramétricas (Objetos desde Datos)

🧩 Ejercicio Realizado
Breve explicación (qué hice y por qué):
Generé una escena 3D a partir de datos estructurados (CSV) usando Open3D en Python. Cada fila representaba un objeto con coordenadas y propiedades como color y escala.

Programé la creación de primitivas de manera automática a partir de los datos, lo que me permitió comprender cómo los modelos paramétricos conectan la geometría con la información.
Este enfoque demuestra cómo se pueden crear visualizaciones tridimensionales desde datasets.

7️⃣ 🔲 Filtro Visual (Convoluciones Personalizadas)

🧩 Ejercicio Realizado
Breve explicación (qué hice y por qué):
Implementé convoluciones 2D manuales con NumPy, aplicando kernels personalizados para desenfoque, realce de bordes y detección de esquinas.

Comparé los resultados con cv2.filter2D y analicé las diferencias en eficiencia y precisión.
Este ejercicio me permitió entender la base matemática detrás del procesamiento de imágenes y de las redes convolucionales modernas.

8️⃣ 🌈 Explorando el Color (RGB, HSV, CIE Lab)

🧩 Ejercicio Realizado
Breve explicación (qué hice y por qué):
Convertí imágenes entre los modelos RGB, HSV y CIE Lab usando OpenCV para observar cómo cada uno representa el color.

Además, simulé daltonismo (protanopía y deuteranopía) mediante matrices y experimenté con filtros de brillo, contraste y temperatura.
El objetivo fue comprender los efectos perceptuales y técnicos de cada modelo y cómo se aplican en visión computacional.

9️⃣ 🎥 Proyecciones 3D (Perspectiva vs Ortográfica)

🧩 Ejercicio Realizado
Breve explicación (qué hice y por qué):
Construí una escena en React Three Fiber con dos cámaras: una perspectiva y otra ortográfica. Implementé controles con Leva para modificar el FOV y el tamaño ortográfico en tiempo real.

Esto me permitió visualizar cómo las proyecciones afectan la sensación de profundidad y composición espacial.
El ejercicio fue clave para comprender el papel de las cámaras en entornos tridimensionales.

🔟 ✋ Gestos con Webcam (MediaPipe Hands)

🧩 Ejercicio Realizado
Breve explicación (qué hice y por qué):
Desarrollé un sistema de detección de manos con MediaPipe y OpenCV. Implementé el conteo de dedos y el reconocimiento de gestos para controlar elementos visuales (cambio de color, movimiento, etc.).

El objetivo fue explorar interfaces naturales de interacción basadas en visión por computador.
Elegí este ejercicio porque combina IA ligera con control gestual, útil para aplicaciones educativas o accesibles.

1️⃣1️⃣ 🧩 Imagen = Matriz (Canales, Slicing, Histogramas)

🧩 Ejercicio Realizado
Breve explicación (qué hice y por qué):
Manipulé imágenes como matrices de datos numéricos usando OpenCV y NumPy. Separé canales RGB, realicé operaciones de recorte (slicing), edité brillo y contraste y generé histogramas de intensidad.

El ejercicio me permitió comprender cómo los valores de los píxeles determinan las características visuales y cómo modificarlos de manera controlada.
Este enfoque es fundamental para entender el procesamiento digital de imágenes.

1️⃣2️⃣ 🚀 Segmentando el Mundo (Binarización y Contornos)

🧩 Ejercicio Realizado
Breve explicación (qué hice y por qué):
Implementé distintos métodos de binarización —fija y adaptativa— con OpenCV, seguidos de detección y dibujo de contornos usando findContours.

Calculé áreas, perímetros y centroides, además de clasificar figuras según sus vértices con approxPolyDP.
Este ejercicio me ayudó a entender cómo segmentar objetos dentro de una imagen y extraer información estructural útil para reconocimiento de formas.


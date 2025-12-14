# Examen Final – Computación Visual

## 📊 Resumen del Proyecto

Este proyecto demuestra competencias en procesamiento de imágenes y desarrollo 3D interactivo, implementando dos componentes principales:
1. **Procesamiento de imágenes con Python/OpenCV** para análisis y transformación de imágenes
2. **Escena 3D interactiva con Three.js** para visualización y animación de formas geométricas

---

## 🐍 Punto 1 – Procesamiento de Imágenes en Python

### 🔬 Funcionalidades Implementadas

#### 1. **Carga y Preprocesamiento**
- **Formato**: Imagen RGB de un tigre (especie en peligro de extinción)
- **Conversión**: Transformación de BGR (OpenCV) a RGB (Matplotlib)
- **Validación**: Verificación de carga exitosa con manejo de errores

#### 2. **Filtrado Espacial**
- **Suavizado Gaussiano** (`GaussianBlur`):
  - Kernel: 11×11 píxeles
  - Sigma: 5
  - Efecto: Reducción de ruido y detalles finos
  
- **Detección de Bordes** (`Canny`):
  - Umbral bajo: 80
  - Umbral alto: 150
  - Efecto: Preservación de estructuras significativas

#### 3. **Análisis de Canales de Color**
- **Separación RGB**: Descomposición en componentes individuales
- **Visualización**: Cada canal en escala de grises
- **Análisis**: Identificación de características predominantes por canal

#### 4. **Procesamiento Morfológico**
- **Binarización**:
  - Umbral fijo (127)
  - Umbral adaptativo (Gaussiano)
  
- **Operaciones básicas**:
  - **Erosión**: Reducción de objetos, separación de elementos conectados
  - **Dilatación**: Expansión de objetos, unión de componentes
  
- **Operaciones compuestas**:
  - **Apertura**: Erosión seguida de dilatación (elimina ruido pequeño)
  - **Cierre**: Dilatación seguida de erosión (rellena huecos pequeños)

#### 5. **Generación de Animación**
- **Secuencia**: 8 transformaciones progresivas
- **Formato**: GIF animado
- **Duración**: 700ms por frame
- **Ubicación**: `python/gifs/resultado_filtros_morfologia.gif`

### 🎯 Resultados Técnicos

#### **Efectos Visuales Observados:**
1. **Filtro Gaussiano**:
   - Atenuación significativa de textura del pelaje
   - Preservación de contornos generales
   - Reducción de artefactos de compresión

2. **Detección de Bordes (Canny)**:
   - Contornos definidos de estructuras principales
   - Detección de patrones de pelaje
   - Eliminación de áreas homogéneas

3. **Canales de Color**:
   - **Canal Rojo**: Mayor contraste en zonas claras
   - **Canal Verde**: Mejor preservación de texturas
   - **Canal Azul**: Mayor ruido, útil para detección de sombras

4. **Operaciones Morfológicas**:
   - **Binarización adaptativa**: Mejor manejo de iluminación irregular
   - **Erosión/Dilatación**: Control preciso de formas binarias
   - **Apertura/Cierre**: Limpieza efectiva de artefactos

### 📈 Análisis Cuantitativo
```python
# Métricas clave obtenidas
- Resolución original: [ancho] × [alto] píxeles
- Tiempo de procesamiento: ~X segundos
- Tamaño GIF generado: ~Y MB
- Eficiencia algorítmica: O(n) para operaciones por píxel

# Celda 1 — importaciones y configuraciones
import os
import cv2
import numpy as np
import sys
import matplotlib.pyplot as plt
from PIL import Image
import imageio

# Configuraciones de matplotlib (sin %matplotlib inline)
plt.rcParams['figure.dpi'] = 120

# Rutas
DATA_DIR = "data"
GIF_DIR = "gifs"
IMG_NAME = "rino.jpg"  

# Crear carpetas
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(GIF_DIR, exist_ok=True)

print("Listo: librerías cargadas y carpetas disponibles.")
print(f"Python ejecutándose desde: {sys.executable}")

# Para mostrar imágenes si es necesario, usa plt.show()
# plt.imshow(imagen)
# plt.show()

# Celda 2 — cargar y mostrar imagen RGB
img_path = os.path.join(DATA_DIR, IMG_NAME)
img_bgr = cv2.imread(img_path)   # OpenCV carga en BGR
if img_bgr is None:
    raise FileNotFoundError(f"No se encontró la imagen en: {img_path}\nAsegúrate de que 'animal.jpg' esté en la carpeta data/")

# Convertir a RGB para mostrar con matplotlib
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(6,6))
plt.imshow(img_rgb)
plt.title("Imagen original (RGB)")
plt.axis("off")


# Celda 3 — Suavizado (GaussianBlur)
blur = cv2.GaussianBlur(img_rgb, (11, 11), 5)

fig, axs = plt.subplots(1,2, figsize=(12,6))
axs[0].imshow(img_rgb)
axs[0].set_title("Original")
axs[0].axis("off")

axs[1].imshow(blur)
axs[1].set_title("Suavizado (GaussianBlur)")
axs[1].axis("off")


# Celda 4 — Realce de bordes con Canny
gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
edges = cv2.Canny(gray, threshold1=80, threshold2=150)

plt.figure(figsize=(10,6))
plt.subplot(1,2,1)
plt.imshow(gray, cmap='gray')
plt.title("Escala de grises (base para Canny)")
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(edges, cmap='gray')
plt.title("Bordes (Canny)")
plt.axis("off")

# Celda 5 — separar canales R, G, B y mostrarlos en gris
R = img_rgb[:,:,0]
G = img_rgb[:,:,1]
B = img_rgb[:,:,2]

fig, axs = plt.subplots(1,3, figsize=(15,5))
axs[0].imshow(R, cmap='gray'); axs[0].set_title('Canal Rojo (R)'); axs[0].axis('off')
axs[1].imshow(G, cmap='gray'); axs[1].set_title('Canal Verde (G)'); axs[1].axis('off')
axs[2].imshow(B, cmap='gray'); axs[2].set_title('Canal Azul (B)'); axs[2].axis('off')

print("xdd")

# Celda 6 — binarizar (opciones fija y adaptativa)
_, binary_fixed = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
binary_adaptive = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                        cv2.THRESH_BINARY, 11, 2)

fig, axs = plt.subplots(1,3, figsize=(15,5))
axs[0].imshow(gray, cmap='gray'); axs[0].set_title('Gris original'); axs[0].axis('off')
axs[1].imshow(binary_fixed, cmap='gray'); axs[1].set_title('Binarización (fija)'); axs[1].axis('off')
axs[2].imshow(binary_adaptive, cmap='gray'); axs[2].set_title('Binarización (adaptativa)'); axs[2].axis('off')


# Celda 7 — definir kernel y aplicar erosión y dilatación
kernel = np.ones((5,5), np.uint8)

erosion = cv2.erode(binary_adaptive, kernel, iterations=1)
dilation = cv2.dilate(binary_adaptive, kernel, iterations=1)

fig, axs = plt.subplots(1,3, figsize=(15,5))
axs[0].imshow(binary_adaptive, cmap='gray'); axs[0].set_title('Binarizada (base)'); axs[0].axis('off')
axs[1].imshow(erosion, cmap='gray'); axs[1].set_title('Erosión'); axs[1].axis('off')
axs[2].imshow(dilation, cmap='gray'); axs[2].set_title('Dilatación'); axs[2].axis('off')


# Celda 8 — apertura y cierre
opening = cv2.morphologyEx(binary_adaptive, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(binary_adaptive, cv2.MORPH_CLOSE, kernel)

fig, axs = plt.subplots(1,3, figsize=(15,5))
axs[0].imshow(binary_adaptive, cmap='gray'); axs[0].set_title('Original binaria'); axs[0].axis('off')
axs[1].imshow(opening, cmap='gray'); axs[1].set_title('Apertura (open)'); axs[1].axis('off')
axs[2].imshow(closing, cmap='gray'); axs[2].set_title('Cierre (close)'); axs[2].axis('off')


# Celda 9 — preparar frames y guardar como GIF
frames = []

# 1) Original
frames.append(Image.fromarray(img_rgb))

# 2) Suavizado
frames.append(Image.fromarray(blur.astype(np.uint8)))

# 3) Bordes (convertir a RGB)
edges_rgb = np.stack([edges]*3, axis=-1)
frames.append(Image.fromarray(edges_rgb.astype(np.uint8)))

# 4) Binarizada adaptativa -> RGB
bin_rgb = np.stack([binary_adaptive]*3, axis=-1)
frames.append(Image.fromarray(bin_rgb.astype(np.uint8)))

# 5) Erosión -> RGB
erosion_rgb = np.stack([erosion]*3, axis=-1)
frames.append(Image.fromarray(erosion_rgb.astype(np.uint8)))

# 6) Dilatación -> RGB
dilation_rgb = np.stack([dilation]*3, axis=-1)
frames.append(Image.fromarray(dilation_rgb.astype(np.uint8)))

# 7) Apertura -> RGB
opening_rgb = np.stack([opening]*3, axis=-1)
frames.append(Image.fromarray(opening_rgb.astype(np.uint8)))

# Guardar GIF (ajusta duration en ms si quieres)
gif_path = os.path.join(GIF_DIR, "resultado_filtros_morfologia.gif")
frames[0].save(gif_path, save_all=True, append_images=frames[1:], duration=700, loop=0)

print("GIF guardado en:", gif_path)

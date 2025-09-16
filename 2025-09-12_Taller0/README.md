Taller de Transformaciones – Python, Three.js y Processing

Repositorio: psandoval123/computacion_visual_2025_2

🔷 Ejercicio en Python

Descripción

Este cuaderno en Jupyter Notebook demuestra transformaciones geométricas aplicadas a un triángulo:

Desplazamiento (traslación)

Giro (rotación)

Cambio de tamaño (escala)

Se implementa mediante multiplicación de matrices con numpy y se ilustra con matplotlib.

Funcionalidades

Uso de matrices de transformación.

Generación de una animación exportada como GIF.

Ajuste de parámetros de manera sencilla.

Cómo ejecutarlo

Instala las dependencias:

pip install numpy matplotlib pillow


Abre el notebook:

jupyter notebook transformaciones.ipynb

Parámetros editables

Dentro del archivo puedes modificar valores como:

tx, ty = 3, 2          # movimiento horizontal y vertical
angulo = 60             # ángulo de rotación (grados)
escala_inicial = 0.5    # tamaño inicial
escala_final = 1.5      # tamaño final

🟩 Proyecto con Three.js y React Three Fiber

Descripción

Aplicación creada con Vite y React Three Fiber. Un cubo:

Gira sobre su propio eje.

Se desplaza siguiendo una curva senoidal.

Cambia de escala con respecto al tiempo.

Incluye controles interactivos para rotar, acercar o alejar la cámara.

Características

Proyecto basado en el starter de Vite + React.

Hot Module Replacement (HMR) listo.

Configuración de ESLint y estructura organizada.

Creación inicial con:

npm create vite@latest nombre-proyecto --template react


Controles de navegación:

Clic izquierdo: girar la vista.

Clic derecho: mover la cámara.

Rueda del mouse: zoom.

Ejecución

Instala las librerías necesarias:

npm install three @react-three/fiber @react-three/drei


Levanta el servidor:

npm run dev


Abre el navegador en: http://localhost:5173

(Verifica estar en la carpeta correcta del cubo).

Personalización

En Box.jsx puedes ajustar el comportamiento del cubo:

useFrame((state) => {
  const t = state.clock.elapsedTime;
  boxRef.current.rotation.y += 0.01;      // rotación
  boxRef.current.position.x = Math.sin(t) * 2;  // movimiento senoidal
  const s = Math.sin(t) * 0.3 + 1;
  boxRef.current.scale.set(s, s, s);      // variación de escala
});


Y su apariencia:

<mesh ref={boxRef}>
  <boxGeometry args={[1, 1, 1]} />
  <meshStandardMaterial color="hotpink" />
</mesh>

🟥 Experimento en Processing

Descripción

Sketch desarrollado en Processing que anima un cubo 3D:

Rotación continua.

Desplazamiento en forma de onda.

Escalado dinámico dependiente del tiempo.

Pasos para ejecutar

Instala Processing.

Abre el archivo .pde.

Presiona “Run”.

Ajustes personalizables

Movimiento:

translate(AMP * sin(millis()/VEL), 0);
rotateY(frameCount * ROT);
scale(1 + sin(millis()/FREQ) * INTENS);


Aspecto:

box(TAM);
fill(R, G, B);
stroke(colorBorde);


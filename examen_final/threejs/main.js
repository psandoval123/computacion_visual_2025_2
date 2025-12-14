import * as THREE from "https://unpkg.com/three@0.164.0/build/three.module.js";
import { OrbitControls } from "https://unpkg.com/three@0.164.0/examples/jsm/controls/OrbitControls.js";

// -----------------------
// 1. ESCENA, RENDER Y CÁMARAS
// -----------------------
const scene = new THREE.Scene();

// Cámara 1 (vista general)
const camera1 = new THREE.PerspectiveCamera(
    75,
    window.innerWidth / window.innerHeight,
    0.1,
    1000
);
camera1.position.set(4, 4, 7);

// Cámara 2 (más cercana, otra perspectiva)
const camera2 = new THREE.PerspectiveCamera(
    75,
    window.innerWidth / window.innerHeight,
    0.1,
    1000
);
camera2.position.set(0, 8, 0);

let activeCamera = camera1;

const renderer = new THREE.WebGLRenderer({
    antialias: true
});
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

// OrbitControls
const controls = new OrbitControls(activeCamera, renderer.domElement);
controls.enableDamping = true;

// -----------------------
// 2. TEXTURAS
// -----------------------
const textureLoader = new THREE.TextureLoader();
const texturaMadera = textureLoader.load("./textures/madera.jpg");
const texturaMaderaBlanca = textureLoader.load("./textures/madera-blanca.jpg");

// -----------------------
// 3. FORMAS GEOMÉTRICAS
// -----------------------

// Piso
const planeGeo = new THREE.PlaneGeometry(20, 20);
const planeMat = new THREE.MeshStandardMaterial({ map: texturaMadera });
const piso = new THREE.Mesh(planeGeo, planeMat);
piso.rotation.x = -Math.PI / 2;
scene.add(piso);

// Cubo con textura
const cubeGeo = new THREE.BoxGeometry(1, 1, 1);
const cubeMat = new THREE.MeshStandardMaterial({ map: texturaMaderaBlanca });
const cubo = new THREE.Mesh(cubeGeo, cubeMat);
cubo.position.set(-2, 0.5, 0);
scene.add(cubo);

// Esfera
const sphereGeo = new THREE.SphereGeometry(0.7, 32, 32);
const sphereMat = new THREE.MeshStandardMaterial({ color: "orange" });
const esfera = new THREE.Mesh(sphereGeo, sphereMat);
esfera.position.set(2, 0.7, 0);
scene.add(esfera);

// Cono
const coneGeo = new THREE.ConeGeometry(0.6, 1.2, 32);
const coneMat = new THREE.MeshStandardMaterial({ color: "lightblue" });
const cono = new THREE.Mesh(coneGeo, coneMat);
cono.position.set(0, 0.6, 2);
scene.add(cono);

// -----------------------
// 4. ILUMINACIÓN
// -----------------------
const luzAmbiente = new THREE.AmbientLight(0xffffff, 0.4);
scene.add(luzAmbiente);

const luzDireccional = new THREE.DirectionalLight(0xffffff, 1);
luzDireccional.position.set(3, 10, 5);
scene.add(luzDireccional);

// -----------------------
// 5. CAMBIO DE CÁMARA
// -----------------------
document.getElementById("btnCamara").addEventListener("click", () => {
    activeCamera = activeCamera === camera1 ? camera2 : camera1;
    controls.object = activeCamera;
});

// -----------------------
// 6. ANIMACIÓN
// -----------------------
function animate() {
    requestAnimationFrame(animate);

    // Animaciones
    cubo.rotation.y += 0.01;
    esfera.rotation.x += 0.02;
    cono.rotation.z += 0.015;

    controls.update();
    renderer.render(scene, activeCamera);
}

animate();

// -----------------------
// 7. AJUSTE AL REDIMENSIONAR
// -----------------------
window.addEventListener("resize", () => {
    camera1.aspect = window.innerWidth / window.innerHeight;
    camera1.updateProjectionMatrix();

    camera2.aspect = window.innerWidth / window.innerHeight;
    camera2.updateProjectionMatrix();

    renderer.setSize(window.innerWidth, window.innerHeight);
});

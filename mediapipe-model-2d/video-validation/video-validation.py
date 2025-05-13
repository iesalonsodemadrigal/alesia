import cv2
import json
import os

# --- Parámetros de Visualización ---
json_path = os.path.join("output", "28.json")
video_path = "..\assets\hola.mov"

# Definir tamaño de la ventana
WINDOW_WIDTH = 1200  # Ancho de la ventana
WINDOW_HEIGHT = 1000  # Alto de la ventana

# Cargar el JSON de animación
with open(json_path, "r") as f:
    data = json.load(f)

frames_data = data.get("frames", [])
if not frames_data:
    print("El JSON no contiene frames.")
    exit()

# --- Mapeo Completo de Puntos Faciales ---
FACE_CONNECTIONS = {
    "mixamorig2:Jaw": list(range(0, 17)),  # Mandíbula completa
    "mixamorig2:Nose": list(range(1, 5)),  # Nariz puente
    "mixamorig2:Nostrils": list(range(6, 8)),  # Orificios nasales
    "mixamorig2:LeftEye": list(range(33, 42)),  # Ojo izquierdo
    "mixamorig2:RightEye": list(range(263, 272)),  # Ojo derecho
    "mixamorig2:LeftEyebrow": list(range(55, 65)),  # Ceja izquierda
    "mixamorig2:RightEyebrow": list(range(285, 295)),  # Ceja derecha
    "mixamorig2:MouthOuter": list(range(61, 68)),  # Boca externa
    "mixamorig2:MouthInner": list(range(78, 88)),  # Boca interna
}

# Definir conexiones del esqueleto
BONE_CONNECTIONS = {
    'mixamorig2:Spine': ('mixamorig2:Hips', 'mixamorig2:Spine'),
    'mixamorig2:Spine1': ('mixamorig2:Spine', 'mixamorig2:Spine1'),
    'mixamorig2:Spine2': ('mixamorig2:Spine1', 'mixamorig2:Spine2'),
    'mixamorig2:Neck': ('mixamorig2:Spine2', 'mixamorig2:Neck'),
    'mixamorig2:LeftArm': ('mixamorig2:LeftShoulder', 'mixamorig2:LeftArm'),
    'mixamorig2:LeftForeArm': ('mixamorig2:LeftArm', 'mixamorig2:LeftForeArm'),
    'mixamorig2:RightArm': ('mixamorig2:RightShoulder', 'mixamorig2:RightArm'),
    'mixamorig2:RightForeArm': ('mixamorig2:RightArm', 'mixamorig2:RightForeArm'),
}

# Conexiones de las manos y dedos en azul
HAND_CONNECTIONS = [
    ("mixamorig2:LeftHand", "mixamorig2:LeftHandThumb1"),
    ("mixamorig2:LeftHand", "mixamorig2:LeftHandIndex1"),
    ("mixamorig2:LeftHand", "mixamorig2:LeftHandMiddle1"),
    ("mixamorig2:LeftHand", "mixamorig2:LeftHandRing1"),
    ("mixamorig2:LeftHand", "mixamorig2:LeftHandPinky1"),
    ("mixamorig2:RightHand", "mixamorig2:RightHandThumb1"),
    ("mixamorig2:RightHand", "mixamorig2:RightHandIndex1"),
    ("mixamorig2:RightHand", "mixamorig2:RightHandMiddle1"),
    ("mixamorig2:RightHand", "mixamorig2:RightHandRing1"),
    ("mixamorig2:RightHand", "mixamorig2:RightHandPinky1"),
]

def get_bone_positions(frame_data, frame_width, frame_height):
    bone_positions = {}
    for bone in frame_data.get("bones", []):
        name = bone.get("name")
        pos = bone.get("position", {})
        x = pos.get("x", 0) * frame_width
        y = (-pos.get("y", 0)) * frame_height
        bone_positions[name] = (int(x), int(y))
    return bone_positions

cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print(f"No se pudo abrir el video: {video_path}")
    exit()

cv2.namedWindow("Visualization", cv2.WINDOW_NORMAL)  # Hacer que la ventana sea redimensionable
cv2.resizeWindow("Visualization", WINDOW_WIDTH, WINDOW_HEIGHT)  # Ajustar el tamaño de la ventana

frame_index = 0
total_frames = len(frames_data)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    h, w, _ = frame.shape

    if frame_index < total_frames:
        frame_data = frames_data[frame_index]
        bone_positions = get_bone_positions(frame_data, w, h)

        # Dibujar cada punto del esqueleto
        for name, (x, y) in bone_positions.items():
            color = (0, 255, 0)  # Verde para el cuerpo
            if "Hand" in name or "Thumb" in name or "Index" in name or "Middle" in name or "Ring" in name or "Pinky" in name:
                color = (255, 0, 0)  # Azul para las manos y dedos
            elif "Jaw" in name or "Nose" in name or "Eye" in name or "Mouth" in name or "Eyebrow" in name:
                color = (255, 105, 180)  # Rosa para la cara
            cv2.circle(frame, (x, y), 4, color, -1)
            cv2.putText(frame, name, (x + 5, y - 5),
            cv2.FONT_HERSHEY_SIMPLEX, 0.4, color, 1)

        # Dibujar conexiones del cuerpo en rojo
        for conn in BONE_CONNECTIONS.values():
            if conn[0] in bone_positions and conn[1] in bone_positions:
                cv2.line(frame, bone_positions[conn[0]], bone_positions[conn[1]], (0, 0, 255), 2)

        # Dibujar conexiones de la cara
        for conn in FACE_CONNECTIONS:
            if conn[0] in bone_positions and conn[1] in bone_positions:
                cv2.line(frame, bone_positions[conn[0]], bone_positions[conn[1]], (255, 105, 180), 2)

        # Dibujar conexiones de las manos y dedos en azul
        for conn in HAND_CONNECTIONS:
            if conn[0] in bone_positions and conn[1] in bone_positions:
                cv2.line(frame, bone_positions[conn[0]], bone_positions[conn[1]], (255, 0, 0), 2)

    cv2.imshow("Visualization", frame)
    key = cv2.waitKey(30)
    if key == 27:  # ESC para salir
        break

    frame_index += 1

cap.release()
cv2.destroyAllWindows()

import mediapipe as mp
import cv2
import json
import numpy as np
import os

# Inicializar modelos individuales
mp_pose = mp.solutions.pose
mp_hands = mp.solutions.hands

pose = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5)
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2)

# --- Conversión de Coordenadas ---
def convert_to_unity_coords(landmark):
    """Convierte las coordenadas MediaPipe a sistema left-handed de Unity."""
    return {
        'x': landmark.x,
        'y': landmark.y,  # No Invertimos eje Y
        'z': landmark.z    # Z se mantiene
    }

# --- Mapeo de Huesos de Unity ---
UNITY_BONES = {
    'mixamorig2:Hips': (23, 24),
    #'mixamorig2:Spine': (23, 24, 11, 12),
    #'mixamorig2:Spine1': (11, 12),
    #'mixamorig2:Spine2': (11, 12),
    #'mixamorig2:Neck': (11, 12),
    #'mixamorig2:Head': 0,
    'mixamorig2:LeftShoulder': 11,
    'mixamorig2:LeftArm': 13,
    'mixamorig2:LeftForeArm': 15,
    #'mixamorig2:LeftHand': 15,
    'mixamorig2:RightShoulder': 12,
    'mixamorig2:RightArm': 14,
    'mixamorig2:RightForeArm': 16,
    #'mixamorig2:RightHand': 16,
    #'mixamorig2:LeftUpLeg': 23,
    #'mixamorig2:LeftLeg': 25,
    #'mixamorig2:LeftFoot': 27,
    #'mixamorig2:LeftToeBase': 29,
    #'mixamorig2:RightUpLeg': 24,
    #'mixamorig2:RightLeg': 26,
    #'mixamorig2:RightFoot': 28,
    #'mixamorig2:RightToeBase': 30
}

# --- Mapeo de Huesos de Manos ---
LEFT_HAND_BONES = {
    'mixamorig2:LeftHand': 0,
    "mixamorig2:LeftHandThumb1": 2,
    "mixamorig2:LeftHandThumb2": 3,
    "mixamorig2:LeftHandThumb3": 4,
    "mixamorig2:LeftHandIndex1": 5,
    "mixamorig2:LeftHandIndex2": 6,
    "mixamorig2:LeftHandIndex3": 7,
    "mixamorig2:LeftHandMiddle1": 9,
    "mixamorig2:LeftHandMiddle2": 10,
    "mixamorig2:LeftHandMiddle3": 11,
    "mixamorig2:LeftHandRing1": 13,
    "mixamorig2:LeftHandRing2": 14,
    "mixamorig2:LeftHandRing3": 15,
    "mixamorig2:LeftHandPinky1": 17,
    "mixamorig2:LeftHandPinky2": 18,
    "mixamorig2:LeftHandPinky3": 19,
}

RIGHT_HAND_BONES = {
    'mixamorig2:RightHand': 0,
    "mixamorig2:RightHandThumb1": 2,
    "mixamorig2:RightHandThumb2": 3,
    "mixamorig2:RightHandThumb3": 4,
    "mixamorig2:RightHandIndex1": 5,
    "mixamorig2:RightHandIndex2": 6,
    "mixamorig2:RightHandIndex3": 7,
    "mixamorig2:RightHandMiddle1": 9,
    "mixamorig2:RightHandMiddle2": 10,
    "mixamorig2:RightHandMiddle3": 11,
    "mixamorig2:RightHandRing1": 13,
    "mixamorig2:RightHandRing2": 14,
    "mixamorig2:RightHandRing3": 15,
    "mixamorig2:RightHandPinky1": 17,
    "mixamorig2:RightHandPinky2": 18,
    "mixamorig2:RightHandPinky3": 19,
}

def process_frame(frame, frame_index):
    # Procesar cuerpo
    pose_results = pose.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    # Procesar manos
    hands_results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    data = {'frame': frame_index, 'bones': []}

    # --- Procesar Cuerpo ---
    if pose_results.pose_landmarks:
        for bone, mapping in UNITY_BONES.items():
            try:
                if isinstance(mapping, (list, tuple)):
                    valid_landmarks = [convert_to_unity_coords(pose_results.pose_landmarks.landmark[i]) for i in mapping]
                    avg_x = sum(p['x'] for p in valid_landmarks) / len(valid_landmarks)
                    avg_y = sum(p['y'] for p in valid_landmarks) / len(valid_landmarks)
                    avg_z = sum(p['z'] for p in valid_landmarks) / len(valid_landmarks)
                    position = {'x': avg_x, 'y': avg_y, 'z': avg_z}
                else:
                    pos = convert_to_unity_coords(pose_results.pose_landmarks.landmark[mapping])
                    position = {'x': pos['x'], 'y': pos['y'], 'z': pos['z']}

                rotation = {'x': 0.0, 'y': 0.0, 'z': 0.0, 'w': 1.0}
                data['bones'].append({'name': bone, 'position': position, 'rotation': rotation})

            except Exception as e:
                print(f"Error processing {bone}: {str(e)}")
                continue

    # --- Procesar Manos ---
    left_hand = None
    right_hand = None

    if hands_results.multi_hand_landmarks and hands_results.multi_handedness:
        for i, handedness in enumerate(hands_results.multi_handedness):
            label = handedness.classification[0].label  # "Left" o "Right"
            
            if label == "Left":
                left_hand = hands_results.multi_hand_landmarks[i]
            elif label == "Right":
                right_hand = hands_results.multi_hand_landmarks[i]

    # Obtener posición de las muñecas desde el cuerpo
    left_wrist_pos = convert_to_unity_coords(pose_results.pose_landmarks.landmark[15]) if pose_results.pose_landmarks else None
    right_wrist_pos = convert_to_unity_coords(pose_results.pose_landmarks.landmark[16]) if pose_results.pose_landmarks else None

    # Procesar la mano izquierda
    if left_hand is not None:
        for bone_name, mp_index in LEFT_HAND_BONES.items():
            pos = convert_to_unity_coords(left_hand.landmark[mp_index])
            rotation = {'x': 0.0, 'y': 0.0, 'z': 0.0, 'w': 1.0}
            data['bones'].append({'name': bone_name, 'position': pos, 'rotation': rotation})
    else:
        if left_wrist_pos:  # Si no hay mano, al menos colocar la muñeca
            data['bones'].append({'name': "mixamorig2:LeftHand", 'position': left_wrist_pos, 'rotation': {'x': 0.0, 'y': 0.0, 'z': 0.0, 'w': 1.0}})

    # Procesar la mano derecha
    if right_hand is not None:
        for bone_name, mp_index in RIGHT_HAND_BONES.items():
            pos = convert_to_unity_coords(right_hand.landmark[mp_index])
            rotation = {'x': 0.0, 'y': 0.0, 'z': 0.0, 'w': 1.0}
            data['bones'].append({'name': bone_name, 'position': pos, 'rotation': rotation})
    else:
        if right_wrist_pos:  # Si no hay mano, al menos colocar la muñeca
            data['bones'].append({'name': "mixamorig2:RightHand", 'position': right_wrist_pos, 'rotation': {'x': 0.0, 'y': 0.0, 'z': 0.0, 'w': 1.0}})

    return data

# --- Captura de Video ---
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

data_frames = []
video_path = "assets/alguno.mov"
cap = cv2.VideoCapture(video_path)
frame_index = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame_data = process_frame(frame, frame_index)
    if frame_data:
        data_frames.append(frame_data)

    frame_index += 1

cap.release()
cv2.destroyAllWindows()

# --- Guardar JSON ---
output_json_path = os.path.join(output_dir, "alguna.json")
with open(output_json_path, "w") as f:
    json.dump({"frames": data_frames}, f, indent=4)

print(f"JSON guardado en {output_json_path}")
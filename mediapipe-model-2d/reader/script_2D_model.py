import mediapipe as mp
import cv2
import json
import numpy as np
import os

# Inicializar modelos individuales
mp_pose = mp.solutions.pose
mp_face = mp.solutions.face_mesh
mp_hands = mp.solutions.hands

pose = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5)
face = mp_face.FaceMesh(static_image_mode=False, max_num_faces=1)
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2)

# --- Conversión de Coordenadas ---
def convert_to_unity_coords(landmark):
    """Convierte las coordenadas MediaPipe a sistema left-handed de Unity."""
    return {
        'x': landmark.x,
        'y': -landmark.y,  # Invertimos eje Y
        'z': landmark.z    # Z se mantiene
    }

# --- Mapeo Completo de Puntos Faciales ---
FACIAL_POINTS = {
    # Contorno completo de la cara (Face Contour)
    "mixamorig2:FaceContour_0": 234,
    "mixamorig2:FaceContour_1": 93,
    "mixamorig2:FaceContour_2": 132,
    "mixamorig2:FaceContour_3": 58,
    "mixamorig2:FaceContour_4": 172,
    "mixamorig2:FaceContour_5": 136,
    "mixamorig2:FaceContour_6": 150,
    "mixamorig2:FaceContour_7": 149,
    "mixamorig2:FaceContour_8": 176,
    "mixamorig2:FaceContour_9": 148,
    "mixamorig2:FaceContour_10": 152,
    "mixamorig2:FaceContour_11": 377,
    "mixamorig2:FaceContour_12": 400,
    "mixamorig2:FaceContour_13": 378,
    "mixamorig2:FaceContour_14": 379,
    "mixamorig2:FaceContour_15": 365,
    "mixamorig2:FaceContour_16": 397,
    "mixamorig2:FaceContour_17": 288,
    "mixamorig2:FaceContour_18": 361,
    "mixamorig2:FaceContour_19": 323,
    "mixamorig2:FaceContour_20": 454,
    "mixamorig2:FaceContour_21": 356,
    "mixamorig2:FaceContour_22": 389,
    "mixamorig2:FaceContour_23": 251,
    "mixamorig2:FaceContour_24": 284,
    "mixamorig2:FaceContour_25": 332,
    "mixamorig2:FaceContour_26": 297,
    "mixamorig2:FaceContour_27": 338,
    "mixamorig2:FaceContour_28": 10,
    "mixamorig2:FaceContour_29": 109,
    "mixamorig2:FaceContour_30": 67,
    "mixamorig2:FaceContour_31": 103,
    "mixamorig2:FaceContour_32": 54,
    "mixamorig2:FaceContour_33": 21,
    "mixamorig2:FaceContour_34": 162,
    "mixamorig2:FaceContour_35": 127,

    # Nariz
    "mixamorig2:Nose_0": 1,
    "mixamorig2:Nose_1": 2,
    "mixamorig2:Nose_2": 98,
    "mixamorig2:Nose_3": 327,
    "mixamorig2:Nose_4": 326,
    "mixamorig2:Nose_5": 97,
    "mixamorig2:Nose_6": 2,
    "mixamorig2:Nose_7": 5,
    "mixamorig2:Nose_8": 4,

    # Ojo izquierdo
    "mixamorig2:LeftEye_0": 33,
    "mixamorig2:LeftEye_1": 7,
    "mixamorig2:LeftEye_2": 163,
    "mixamorig2:LeftEye_3": 144,
    "mixamorig2:LeftEye_4": 145,
    "mixamorig2:LeftEye_5": 153,
    "mixamorig2:LeftEye_6": 154,
    "mixamorig2:LeftEye_7": 155,
    "mixamorig2:LeftEye_8": 133,
    "mixamorig2:LeftEye_9": 173,
    "mixamorig2:LeftEye_10": 157,
    "mixamorig2:LeftEye_11": 158,
    "mixamorig2:LeftEye_12": 159,
    "mixamorig2:LeftEye_13": 160,
    "mixamorig2:LeftEye_14": 161,
    "mixamorig2:LeftEye_15": 246,

    # Ojo derecho
    "mixamorig2:RightEye_0": 362,
    "mixamorig2:RightEye_1": 382,
    "mixamorig2:RightEye_2": 381,
    "mixamorig2:RightEye_3": 380,
    "mixamorig2:RightEye_4": 374,
    "mixamorig2:RightEye_5": 373,
    "mixamorig2:RightEye_6": 390,
    "mixamorig2:RightEye_7": 249,
    "mixamorig2:RightEye_8": 263,
    "mixamorig2:RightEye_9": 466,
    "mixamorig2:RightEye_10": 388,
    "mixamorig2:RightEye_11": 387,
    "mixamorig2:RightEye_12": 386,
    "mixamorig2:RightEye_13": 385,
    "mixamorig2:RightEye_14": 384,
    "mixamorig2:RightEye_15": 398,

    # Ceja izquierda
    "mixamorig2:LeftEyebrow_0": 46,
    "mixamorig2:LeftEyebrow_1": 53,
    "mixamorig2:LeftEyebrow_2": 52,
    "mixamorig2:LeftEyebrow_3": 65,
    "mixamorig2:LeftEyebrow_4": 55,
    #"mixamorig2:LeftEyebrow_9": 107,
    "mixamorig2:LeftEyebrow_5": 66,
    "mixamorig2:LeftEyebrow_6": 105,
    "mixamorig2:LeftEyebrow_7": 63,
    #"mixamorig2:LeftEyebrow_8": 70,

    # Ceja derecha
    "mixamorig2:RightEyebrow_0": 285,
    "mixamorig2:RightEyebrow_1": 295,
    "mixamorig2:RightEyebrow_2": 282,
    "mixamorig2:RightEyebrow_3": 283,
    "mixamorig2:RightEyebrow_4": 276,
    #"mixamorig2:RightEyebrow_9": 300,
    "mixamorig2:RightEyebrow_5": 293,
    "mixamorig2:RightEyebrow_6": 334,
    "mixamorig2:RightEyebrow_7": 296,
    #"mixamorig2:RightEyebrow_8": 336,

    # Boca externa
     "mixamorig2:MouthOuter_0": 61,   # Lado izquierdo
    "mixamorig2:MouthOuter_1": 146,
    "mixamorig2:MouthOuter_2": 91,
    "mixamorig2:MouthOuter_3": 181,
    "mixamorig2:MouthOuter_4": 84,
    "mixamorig2:MouthOuter_5": 17,
    "mixamorig2:MouthOuter_6": 314,
    "mixamorig2:MouthOuter_7": 405,
    "mixamorig2:MouthOuter_8": 321,
    "mixamorig2:MouthOuter_9": 375,
    "mixamorig2:MouthOuter_10": 291,
    "mixamorig2:MouthOuter_11": 409,  # Lado derecho

    # Labio superior exterior
    "mixamorig2:MouthOuter_12": 270,
    "mixamorig2:MouthOuter_13": 269,
    "mixamorig2:MouthOuter_14": 267,
    "mixamorig2:MouthOuter_15": 0,
    "mixamorig2:MouthOuter_16": 37,
    "mixamorig2:MouthOuter_17": 39,
    "mixamorig2:MouthOuter_18": 40,
    "mixamorig2:MouthOuter_19": 185,

     # Boca interna
    "mixamorig2:MouthInner_0": 78,   # Lado izquierdo
    "mixamorig2:MouthInner_1": 191,
    "mixamorig2:MouthInner_2": 80,
    "mixamorig2:MouthInner_3": 81,
    "mixamorig2:MouthInner_4": 82,
    "mixamorig2:MouthInner_5": 13,   # Centro inferior
    "mixamorig2:MouthInner_6": 312,
    "mixamorig2:MouthInner_7": 311,
    "mixamorig2:MouthInner_8": 310,
    "mixamorig2:MouthInner_9": 415,  # Lado derecho

    # Labio superior interno
    "mixamorig2:MouthInner_10": 308,
    "mixamorig2:MouthInner_11": 324,
    "mixamorig2:MouthInner_12": 318,
    "mixamorig2:MouthInner_13": 402,
    "mixamorig2:MouthInner_14": 317,
    "mixamorig2:MouthInner_15": 14,
    "mixamorig2:MouthInner_16": 87,
    "mixamorig2:MouthInner_17": 178,
    "mixamorig2:MouthInner_18": 88,
    "mixamorig2:MouthInner_19": 95,
}

# --- Mapeo de Huesos de Unity ---
UNITY_BONES = {
    'mixamorig2:Hips': (23, 24),
    'mixamorig2:Spine': (23, 24, 11, 12),
    'mixamorig2:Spine1': (11, 12),
    'mixamorig2:Spine2': (11, 12),
    'mixamorig2:Neck': (11, 12),
    'mixamorig2:Head': 0,
    'mixamorig2:LeftShoulder': 11,
    'mixamorig2:LeftArm': 13,
    'mixamorig2:LeftForeArm': 15,
    #'mixamorig2:LeftHand': 15,
    'mixamorig2:RightShoulder': 12,
    'mixamorig2:RightArm': 14,
    'mixamorig2:RightForeArm': 16,
    #'mixamorig2:RightHand': 16,
    'mixamorig2:LeftUpLeg': 23,
    'mixamorig2:LeftLeg': 25,
    'mixamorig2:LeftFoot': 27,
    'mixamorig2:LeftToeBase': 29,
    'mixamorig2:RightUpLeg': 24,
    'mixamorig2:RightLeg': 26,
    'mixamorig2:RightFoot': 28,
    'mixamorig2:RightToeBase': 30
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
    # Procesar cara
    face_results = face.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
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

    # --- Procesar Cara ---
    if face_results.multi_face_landmarks:
        face_lms = face_results.multi_face_landmarks[0].landmark  # Acceder al primer rostro
        for bone_name, mp_index in FACIAL_POINTS.items():
            try:
                pos = convert_to_unity_coords(face_lms[mp_index])
                rotation = {'x': 0.0, 'y': 0.0, 'z': 0.0, 'w': 1.0}
                data['bones'].append({'name': bone_name, 'position': pos, 'rotation': rotation})
            except Exception as e:
                print(f"Error processing {bone_name}: {str(e)}")
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
video_path = "assets/sentir.mov"
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
output_json_path = os.path.join(output_dir, "sentir3.9.3.json")
with open(output_json_path, "w") as f:
    json.dump({"frames": data_frames}, f, indent=4)

print(f"JSON guardado en {output_json_path}")
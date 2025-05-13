import pygame

class FrameRenderer:
    def __init__(self, screen, width, height, zoom_factor=1.0):
        self.screen = screen
        self.width = width
        self.height = height
        self.zoom_factor = zoom_factor  # Aplicamos zoom a la visualización

        # Colores de la mano y los dedos
        self.palm_color = (232, 190, 172)  # Color piel claro para la palma
        self.finger_colors = {
            1: (218, 165, 140),  # Color más oscuro para la base de los dedos
            2: (244, 187, 160),  # Color medio para la parte media
            3: (255, 228, 196)   # Color más claro para la punta de los dedos
        }

        # Colores para el torso
        self.torso_line_color = (0, 0, 0)  # Negro para las líneas del torso
        self.torso_fill_color = (50, 50, 50)  # Gris oscuro para el relleno del torso

        # Conexiones del torso con relleno
        self.torso_connections = [
            ("mixamorig2:LeftShoulder", "mixamorig2:RightShoulder"),
            ("mixamorig2:LeftShoulder", "mixamorig2:LeftUpLeg"),
            ("mixamorig2:RightShoulder", "mixamorig2:RightUpLeg"),
            ("mixamorig2:LeftUpLeg", "mixamorig2:RightUpLeg"),
        ]

        # Conexiones del cuerpo
        self.bone_connections = [
            # Torso
            #("mixamorig2:Hips", "mixamorig2:Spine"),
            #("mixamorig2:Spine", "mixamorig2:Spine1"),
            #("mixamorig2:Spine1", "mixamorig2:Spine2"),
            #("mixamorig2:Spine2", "mixamorig2:Neck"),
            ("mixamorig2:Neck", "mixamorig2:FaceContour_10"),

            # Brazo izquierdo
            #("mixamorig2:Neck", "mixamorig2:LeftShoulder"),
            ("mixamorig2:LeftShoulder", "mixamorig2:LeftArm"),
            ("mixamorig2:LeftArm", "mixamorig2:LeftForeArm"),
            #("mixamorig2:LeftForeArm", "mixamorig2:LeftHand"),

            # Brazo derecho
            #("mixamorig2:Neck", "mixamorig2:RightShoulder"),
            ("mixamorig2:RightShoulder", "mixamorig2:RightArm"),
            ("mixamorig2:RightArm", "mixamorig2:RightForeArm"),
            #("mixamorig2:RightForeArm", "mixamorig2:RightHand"),

            # Pierna izquierda
            ("mixamorig2:Hips", "mixamorig2:LeftUpLeg"),
            ("mixamorig2:LeftUpLeg", "mixamorig2:LeftLeg"),
            ("mixamorig2:LeftLeg", "mixamorig2:LeftFoot"),
            ("mixamorig2:LeftFoot", "mixamorig2:LeftToeBase"),

            # Pierna derecha
            ("mixamorig2:Hips", "mixamorig2:RightUpLeg"),
            ("mixamorig2:RightUpLeg", "mixamorig2:RightLeg"),
            ("mixamorig2:RightLeg", "mixamorig2:RightFoot"),
            ("mixamorig2:RightFoot", "mixamorig2:RightToeBase"),
        ]

        # Conexiones de la cara (pintadas en rosa)
        self.face_connections = [
           # Contorno
            ("mixamorig2:FaceContour_0", "mixamorig2:FaceContour_1"),
            ("mixamorig2:FaceContour_1", "mixamorig2:FaceContour_2"),
            ("mixamorig2:FaceContour_2", "mixamorig2:FaceContour_3"),
            ("mixamorig2:FaceContour_3", "mixamorig2:FaceContour_4"),
            ("mixamorig2:FaceContour_4", "mixamorig2:FaceContour_5"),
            ("mixamorig2:FaceContour_5", "mixamorig2:FaceContour_6"),
            ("mixamorig2:FaceContour_6", "mixamorig2:FaceContour_7"),
            ("mixamorig2:FaceContour_7", "mixamorig2:FaceContour_8"),
            ("mixamorig2:FaceContour_8", "mixamorig2:FaceContour_9"),
            ("mixamorig2:FaceContour_9", "mixamorig2:FaceContour_10"),
            ("mixamorig2:FaceContour_10", "mixamorig2:FaceContour_11"),
            ("mixamorig2:FaceContour_11", "mixamorig2:FaceContour_12"),
            ("mixamorig2:FaceContour_12", "mixamorig2:FaceContour_13"),
            ("mixamorig2:FaceContour_13", "mixamorig2:FaceContour_14"),
            ("mixamorig2:FaceContour_14", "mixamorig2:FaceContour_15"),
            ("mixamorig2:FaceContour_15", "mixamorig2:FaceContour_16"),
            ("mixamorig2:FaceContour_16", "mixamorig2:FaceContour_17"),
            ("mixamorig2:FaceContour_17", "mixamorig2:FaceContour_18"),
            ("mixamorig2:FaceContour_18", "mixamorig2:FaceContour_19"),
            ("mixamorig2:FaceContour_19", "mixamorig2:FaceContour_20"),
            ("mixamorig2:FaceContour_20", "mixamorig2:FaceContour_21"),
            ("mixamorig2:FaceContour_21", "mixamorig2:FaceContour_22"),
            ("mixamorig2:FaceContour_22", "mixamorig2:FaceContour_23"),
            ("mixamorig2:FaceContour_23", "mixamorig2:FaceContour_24"),
            ("mixamorig2:FaceContour_24", "mixamorig2:FaceContour_25"),
            ("mixamorig2:FaceContour_25", "mixamorig2:FaceContour_26"),
            ("mixamorig2:FaceContour_26", "mixamorig2:FaceContour_27"),
            ("mixamorig2:FaceContour_27", "mixamorig2:FaceContour_28"),
            ("mixamorig2:FaceContour_28", "mixamorig2:FaceContour_29"),
            ("mixamorig2:FaceContour_29", "mixamorig2:FaceContour_30"),
            ("mixamorig2:FaceContour_30", "mixamorig2:FaceContour_31"),
            ("mixamorig2:FaceContour_31", "mixamorig2:FaceContour_32"),
            ("mixamorig2:FaceContour_32", "mixamorig2:FaceContour_33"),
            ("mixamorig2:FaceContour_33", "mixamorig2:FaceContour_34"),
            ("mixamorig2:FaceContour_34", "mixamorig2:FaceContour_35"),
            ("mixamorig2:FaceContour_35", "mixamorig2:FaceContour_0"),
            
            # Nariz
            ("mixamorig2:Nose_0", "mixamorig2:Nose_1"),
            ("mixamorig2:Nose_1", "mixamorig2:Nose_2"),
            ("mixamorig2:Nose_2", "mixamorig2:Nose_3"),
            ("mixamorig2:Nose_3", "mixamorig2:Nose_4"),
            ("mixamorig2:Nose_4", "mixamorig2:Nose_5"),
            ("mixamorig2:Nose_5", "mixamorig2:Nose_6"),
            ("mixamorig2:Nose_6", "mixamorig2:Nose_7"),
            ("mixamorig2:Nose_7", "mixamorig2:Nose_8"),
            
            # Ojos
            ("mixamorig2:LeftEye_0", "mixamorig2:LeftEye_1"),
            ("mixamorig2:LeftEye_1", "mixamorig2:LeftEye_2"),
            ("mixamorig2:LeftEye_2", "mixamorig2:LeftEye_3"),
            ("mixamorig2:LeftEye_3", "mixamorig2:LeftEye_4"),
            ("mixamorig2:LeftEye_4", "mixamorig2:LeftEye_5"),
            ("mixamorig2:LeftEye_5", "mixamorig2:LeftEye_6"),
            ("mixamorig2:LeftEye_6", "mixamorig2:LeftEye_7"),
            ("mixamorig2:LeftEye_7", "mixamorig2:LeftEye_8"),
            ("mixamorig2:LeftEye_8", "mixamorig2:LeftEye_9"),
            ("mixamorig2:LeftEye_9", "mixamorig2:LeftEye_10"),
            ("mixamorig2:LeftEye_10", "mixamorig2:LeftEye_11"),
            ("mixamorig2:LeftEye_11", "mixamorig2:LeftEye_12"),
            ("mixamorig2:LeftEye_12", "mixamorig2:LeftEye_13"),
            ("mixamorig2:LeftEye_13", "mixamorig2:LeftEye_14"),
            ("mixamorig2:LeftEye_14", "mixamorig2:LeftEye_15"),
            ("mixamorig2:LeftEye_15", "mixamorig2:LeftEye_0"),

            ("mixamorig2:RightEye_0", "mixamorig2:RightEye_1"),
            ("mixamorig2:RightEye_1", "mixamorig2:RightEye_2"),
            ("mixamorig2:RightEye_2", "mixamorig2:RightEye_3"),
            ("mixamorig2:RightEye_3", "mixamorig2:RightEye_4"),
            ("mixamorig2:RightEye_4", "mixamorig2:RightEye_5"),
            ("mixamorig2:RightEye_5", "mixamorig2:RightEye_6"),
            ("mixamorig2:RightEye_6", "mixamorig2:RightEye_7"),
            ("mixamorig2:RightEye_7", "mixamorig2:RightEye_8"),
            ("mixamorig2:RightEye_8", "mixamorig2:RightEye_9"),
            ("mixamorig2:RightEye_9", "mixamorig2:RightEye_10"),
            ("mixamorig2:RightEye_10", "mixamorig2:RightEye_11"),
            ("mixamorig2:RightEye_11", "mixamorig2:RightEye_12"),
            ("mixamorig2:RightEye_12", "mixamorig2:RightEye_13"),
            ("mixamorig2:RightEye_13", "mixamorig2:RightEye_14"),
            ("mixamorig2:RightEye_14", "mixamorig2:RightEye_15"),
            ("mixamorig2:RightEye_15", "mixamorig2:RightEye_0"),
            
            # Cejas
            ("mixamorig2:LeftEyebrow_0", "mixamorig2:LeftEyebrow_1"),
            ("mixamorig2:LeftEyebrow_1", "mixamorig2:LeftEyebrow_2"),
            ("mixamorig2:LeftEyebrow_2", "mixamorig2:LeftEyebrow_3"),
            ("mixamorig2:LeftEyebrow_3", "mixamorig2:LeftEyebrow_4"),
            ("mixamorig2:LeftEyebrow_4", "mixamorig2:LeftEyebrow_5"),
            ("mixamorig2:LeftEyebrow_5", "mixamorig2:LeftEyebrow_6"),
            ("mixamorig2:LeftEyebrow_6", "mixamorig2:LeftEyebrow_7"),
            ("mixamorig2:LeftEyebrow_7", "mixamorig2:LeftEyebrow_0"),

            ("mixamorig2:RightEyebrow_0", "mixamorig2:RightEyebrow_1"),
            ("mixamorig2:RightEyebrow_1", "mixamorig2:RightEyebrow_2"),
            ("mixamorig2:RightEyebrow_2", "mixamorig2:RightEyebrow_3"),
            ("mixamorig2:RightEyebrow_3", "mixamorig2:RightEyebrow_4"),
            ("mixamorig2:RightEyebrow_4", "mixamorig2:RightEyebrow_5"),
            ("mixamorig2:RightEyebrow_5", "mixamorig2:RightEyebrow_6"),
            ("mixamorig2:RightEyebrow_6", "mixamorig2:RightEyebrow_7"),
            ("mixamorig2:RightEyebrow_7", "mixamorig2:RightEyebrow_0"),

            # Boca externa
             ("mixamorig2:MouthOuter_0", "mixamorig2:MouthOuter_1"),
            ("mixamorig2:MouthOuter_1", "mixamorig2:MouthOuter_2"),
            ("mixamorig2:MouthOuter_2", "mixamorig2:MouthOuter_3"),
            ("mixamorig2:MouthOuter_3", "mixamorig2:MouthOuter_4"),
            ("mixamorig2:MouthOuter_4", "mixamorig2:MouthOuter_5"),
            ("mixamorig2:MouthOuter_5", "mixamorig2:MouthOuter_6"),
            ("mixamorig2:MouthOuter_6", "mixamorig2:MouthOuter_7"),
            ("mixamorig2:MouthOuter_7", "mixamorig2:MouthOuter_8"),
            ("mixamorig2:MouthOuter_8", "mixamorig2:MouthOuter_9"),
            ("mixamorig2:MouthOuter_9", "mixamorig2:MouthOuter_10"),
            ("mixamorig2:MouthOuter_10", "mixamorig2:MouthOuter_11"),
            ("mixamorig2:MouthOuter_11", "mixamorig2:MouthOuter_12"),
            ("mixamorig2:MouthOuter_12", "mixamorig2:MouthOuter_13"),
            ("mixamorig2:MouthOuter_13", "mixamorig2:MouthOuter_14"),
            ("mixamorig2:MouthOuter_14", "mixamorig2:MouthOuter_15"),
            ("mixamorig2:MouthOuter_15", "mixamorig2:MouthOuter_16"),
            ("mixamorig2:MouthOuter_16", "mixamorig2:MouthOuter_17"),
            ("mixamorig2:MouthOuter_17", "mixamorig2:MouthOuter_18"),
            ("mixamorig2:MouthOuter_18", "mixamorig2:MouthOuter_19"),
            ("mixamorig2:MouthOuter_19", "mixamorig2:MouthOuter_0"),  # Cierra la boca exterior

            # Boca interna
            ("mixamorig2:MouthInner_0", "mixamorig2:MouthInner_1"),
            ("mixamorig2:MouthInner_1", "mixamorig2:MouthInner_2"),
            ("mixamorig2:MouthInner_2", "mixamorig2:MouthInner_3"),
            ("mixamorig2:MouthInner_3", "mixamorig2:MouthInner_4"),
            ("mixamorig2:MouthInner_4", "mixamorig2:MouthInner_5"),
            ("mixamorig2:MouthInner_5", "mixamorig2:MouthInner_6"),
            ("mixamorig2:MouthInner_6", "mixamorig2:MouthInner_7"),
            ("mixamorig2:MouthInner_7", "mixamorig2:MouthInner_8"),
            ("mixamorig2:MouthInner_8", "mixamorig2:MouthInner_9"),
            ("mixamorig2:MouthInner_9", "mixamorig2:MouthInner_10"),
            ("mixamorig2:MouthInner_10", "mixamorig2:MouthInner_11"),
            ("mixamorig2:MouthInner_11", "mixamorig2:MouthInner_12"),
            ("mixamorig2:MouthInner_12", "mixamorig2:MouthInner_13"),
            ("mixamorig2:MouthInner_13", "mixamorig2:MouthInner_14"),
            ("mixamorig2:MouthInner_14", "mixamorig2:MouthInner_15"),
            ("mixamorig2:MouthInner_15", "mixamorig2:MouthInner_16"),
            ("mixamorig2:MouthInner_16", "mixamorig2:MouthInner_17"),
            ("mixamorig2:MouthInner_17", "mixamorig2:MouthInner_18"),
            ("mixamorig2:MouthInner_18", "mixamorig2:MouthInner_19"),
            ("mixamorig2:MouthInner_19", "mixamorig2:MouthInner_0"),  # Cierra la boca interna
        ]

        # Conexiones de las manos y dedos en azul
        self.hand_connections = [
            # Conectar muñeca con todos los dedos de la mano izquierda
            ("mixamorig2:LeftHand", "mixamorig2:LeftHandThumb1"),
            #("mixamorig2:LeftHand", "mixamorig2:LeftHandIndex1"),
            ("mixamorig2:LeftHand", "mixamorig2:LeftHandPinky1"),

            # Conectar muñeca con todos los dedos de la mano derecha
            ("mixamorig2:RightHand", "mixamorig2:RightHandThumb1"),
            #("mixamorig2:RightHand", "mixamorig2:RightHandIndex1"),
            ("mixamorig2:RightHand", "mixamorig2:RightHandPinky1"),

            # Palma izquierda
            ("mixamorig2:LeftHandIndex1", "mixamorig2:LeftHandThumb1"),
            ("mixamorig2:LeftHandIndex1", "mixamorig2:LeftHandMiddle1"),
            ("mixamorig2:LeftHandMiddle1", "mixamorig2:LeftHandRing1"),
            ("mixamorig2:LeftHandRing1", "mixamorig2:LeftHandPinky1"),

            ("mixamorig2:RightHandIndex1", "mixamorig2:RightHandThumb1"),
            ("mixamorig2:RightHandIndex1", "mixamorig2:RightHandMiddle1"),
            ("mixamorig2:RightHandMiddle1", "mixamorig2:RightHandRing1"),
            ("mixamorig2:RightHandRing1", "mixamorig2:RightHandPinky1"),

            # Conectar segmentos de los dedos (pulgar)
            ("mixamorig2:LeftHandThumb1", "mixamorig2:LeftHandThumb2"),
            ("mixamorig2:LeftHandThumb2", "mixamorig2:LeftHandThumb3"),
            ("mixamorig2:RightHandThumb1", "mixamorig2:RightHandThumb2"),
            ("mixamorig2:RightHandThumb2", "mixamorig2:RightHandThumb3"),
            
            
            # Índice
            ("mixamorig2:LeftHandIndex1", "mixamorig2:LeftHandIndex2"),
            ("mixamorig2:LeftHandIndex2", "mixamorig2:LeftHandIndex3"),
            ("mixamorig2:RightHandIndex1", "mixamorig2:RightHandIndex2"),
            ("mixamorig2:RightHandIndex2", "mixamorig2:RightHandIndex3"),

            # Medio
            ("mixamorig2:LeftHandMiddle1", "mixamorig2:LeftHandMiddle2"),
            ("mixamorig2:LeftHandMiddle2", "mixamorig2:LeftHandMiddle3"),
            ("mixamorig2:RightHandMiddle1", "mixamorig2:RightHandMiddle2"),
            ("mixamorig2:RightHandMiddle2", "mixamorig2:RightHandMiddle3"),

            # Anular
            ("mixamorig2:LeftHandRing1", "mixamorig2:LeftHandRing2"),
            ("mixamorig2:LeftHandRing2", "mixamorig2:LeftHandRing3"),
            ("mixamorig2:RightHandRing1", "mixamorig2:RightHandRing2"),
            ("mixamorig2:RightHandRing2", "mixamorig2:RightHandRing3"),

            # Meñique
            ("mixamorig2:LeftHandPinky1", "mixamorig2:LeftHandPinky2"),
            ("mixamorig2:LeftHandPinky2", "mixamorig2:LeftHandPinky3"),
            ("mixamorig2:RightHandPinky1", "mixamorig2:RightHandPinky2"),
            ("mixamorig2:RightHandPinky2", "mixamorig2:RightHandPinky3"),
        ]

    def draw_skeleton(self, frame_data):
        self.screen.fill((255, 255, 255))

        if "bones" not in frame_data:
            return

        bones = frame_data["bones"]

        # Centrar el modelo en la pantalla
        center_x, center_y = bones.get("mixamorig2:Hips", {"x": 0, "y": 0}).values()

        scale_factor = 300 * self.zoom_factor
        offset_x = self.width // 2
        offset_y = self.height // 2 + 500

        transformed_bones = {}
        for bone, coords in bones.items():
            transformed_x = int((coords["x"] - center_x) * scale_factor + offset_x)
            transformed_y = int((coords["y"] - center_y) * scale_factor + offset_y)
            transformed_bones[bone] = (transformed_x, transformed_y)

         # Dibujar el torso con relleno y bordes
        torso_points = [
            transformed_bones.get("mixamorig2:LeftShoulder"),
            transformed_bones.get("mixamorig2:RightShoulder"),
            transformed_bones.get("mixamorig2:RightUpLeg"),
            transformed_bones.get("mixamorig2:LeftUpLeg"),
        ]
        if None not in torso_points:
            pygame.draw.polygon(self.screen, self.torso_fill_color, torso_points)
            for bone1, bone2 in self.torso_connections:
                pygame.draw.line(self.screen, self.torso_line_color, transformed_bones[bone1], transformed_bones[bone2], 6)

        # Dibujar conexiones del cuerpo
        for bone1, bone2 in self.bone_connections:
            if bone1 in transformed_bones and bone2 in transformed_bones:
                pygame.draw.line(self.screen, (232, 190, 172), transformed_bones[bone1], transformed_bones[bone2], 8)

        # Dibujar conexiones de la cara
        for bone1, bone2 in self.face_connections:
            if bone1 in transformed_bones and bone2 in transformed_bones:
                pygame.draw.line(self.screen, (255, 105, 180), transformed_bones[bone1], transformed_bones[bone2], 4)

        # Dibujar la palma de la mano como un polígono relleno
        for hand in ["LeftHand", "RightHand"]:
            if all(f"mixamorig2:{hand}{finger}1" in transformed_bones for finger in ["Thumb", "Index", "Middle", "Ring", "Pinky"]):
                palm_points = [
                    transformed_bones[f"mixamorig2:{hand}Thumb1"],
                    transformed_bones[f"mixamorig2:{hand}Index1"],
                    transformed_bones[f"mixamorig2:{hand}Middle1"],
                    transformed_bones[f"mixamorig2:{hand}Ring1"],
                    transformed_bones[f"mixamorig2:{hand}Pinky1"],
                    transformed_bones[f"mixamorig2:{hand}"],
                ]
                pygame.draw.polygon(self.screen, self.palm_color, palm_points)

        # Dibujar conexiones de las manos
        for bone1, bone2 in self.hand_connections:
            if bone1 in transformed_bones and bone2 in transformed_bones:
                pygame.draw.line(self.screen, (232, 190, 172), transformed_bones[bone1], transformed_bones[bone2], 6)

        # Dibujar puntos en los dedos con diferentes colores según la parte
        for bone, pos in transformed_bones.items():
            if "Thumb1" in bone or "Index1" in bone or "Middle1" in bone or "Ring1" in bone or "Pinky1" in bone:
                color = self.finger_colors[1]
            elif "Thumb2" in bone or "Index2" in bone or "Middle2" in bone or "Ring2" in bone or "Pinky2" in bone:
                color = self.finger_colors[2]
            elif "Thumb3" in bone or "Index3" in bone or "Middle3" in bone or "Ring3" in bone or "Pinky3" in bone:
                color = self.finger_colors[3]
            else:
                continue
            pygame.draw.circle(self.screen, color, pos, 5)

        pygame.display.flip()
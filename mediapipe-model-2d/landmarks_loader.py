import os
import json

class LandmarkLoader:
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def get_available_files(self):
        return [f for f in os.listdir(self.folder_path) if f.endswith('.json')]

    def load_landmarks(self, selected_files):
        landmarks_data = []
        
        for json_file in selected_files:
            json_file_path = os.path.join(self.folder_path, json_file)

            try:
                with open(json_file_path, 'r') as f:
                    data = json.load(f)

                    for frame_data in data.get('frames', []):
                        bone_positions = {}

                        # Verificar que la clave 'bones' existe y es una lista
                        bones = frame_data.get('bones', [])
                        if isinstance(bones, list):
                            for bone in bones:
                                bone_name = bone.get('name', 'Unknown_Bone')
                                position = bone.get('position', {})

                                if 'x' in position and 'y' in position:
                                    bone_positions[bone_name] = {
                                        'x': position['x'],
                                        'y': -position['y']
                                    }

                        # Si no hay huesos, evitar agregar un frame vacío
                        if bone_positions:
                            landmarks_data.append({
                                'frame': frame_data.get('frame', 0),
                                'bones': bone_positions
                            })
            except Exception as e:
                print(f"Error al cargar {json_file}: {e}")

        return landmarks_data

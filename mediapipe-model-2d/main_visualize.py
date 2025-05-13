import pygame
from landmarks_loader import LandmarkLoader
from frame_renderer4 import FrameRenderer
import os

def parser(landmarks_folder_path):
    input_text = input("Enter a text: ").lower()
    words = input_text.split()
    result = []
    matched_files = []
    index = 0

    # Store available filenames without .json and using underscores
    available_files = {f.replace('.json', '') for f in os.listdir(landmarks_folder_path) if f.endswith('.json')}

    while index < len(words):
        found = False
        phrase = words[index]

        for next_index in range(index + 1, len(words) + 1):
            normalized_phrase = phrase.replace(" ", "_")  # Convert spaces to underscores

            if normalized_phrase in available_files:
                result.append(phrase)
                matched_files.append(f"{normalized_phrase}.json")
                index = next_index - 1
                found = True
                break

            if next_index < len(words):
                phrase += " " + words[next_index]  # Expand phrase

        if not found:
            result.append(words[index])

        index += 1

    print("Result:", " ".join(result))
    return matched_files

def main():
    print("Introduce este texto: Hola me llamo alesia y tengo frio")
    landmarks_folder_path = 'landmarks'
    matched_files = parser(landmarks_folder_path)

    if not matched_files:
        print("No valid files selected. Exiting...")
        return

    pygame.init()
    width, height = 1250, 1000  # Window size
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Esqueleto Animado (Zoom - Cintura hacia arriba)")

    loader = LandmarkLoader(landmarks_folder_path)
    landmarks_data = loader.load_landmarks(matched_files)

    zoom_factor = 3.0  # Increase zoom to focus on torso, arms, and head
    renderer = FrameRenderer(screen, width, height, zoom_factor)

    clock = pygame.time.Clock()
    frame_index = 0
    running = True

    while running:
        screen.fill((255, 255, 255))  # Clear the screen before drawing each frame

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if frame_index < len(landmarks_data):
            renderer.draw_skeleton(landmarks_data[frame_index])
            frame_index += 1
        else:
            frame_index = 0  # Restart animation when finished

        pygame.display.flip()
        clock.tick(20)  # Control animation speed

    pygame.quit()

if __name__ == "__main__":
    main()


from PIL import Image, ImageDraw
import random

def generate_creature(width, height):
    image = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(image)

    # Dessiner le corps de la créature (un cercle)
    body_radius = random.randint(30, 60)
    body_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    body_center = (width // 2, height // 2)
    draw.ellipse((body_center[0] - body_radius, body_center[1] - body_radius,
                  body_center[0] + body_radius, body_center[1] + body_radius),
                 fill=body_color)

    # Dessiner les yeux de la créature (deux petits cercles)
    eye_radius = random.randint(5, 15)
    eye_distance = random.randint(15, 30)
    eye_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    left_eye_center = (body_center[0] - eye_distance, body_center[1])
    right_eye_center = (body_center[0] + eye_distance, body_center[1])
    draw.ellipse((left_eye_center[0] - eye_radius, left_eye_center[1] - eye_radius,
                  left_eye_center[0] + eye_radius, left_eye_center[1] + eye_radius),
                 fill=eye_color)
    draw.ellipse((right_eye_center[0] - eye_radius, right_eye_center[1] - eye_radius,
                  right_eye_center[0] + eye_radius, right_eye_center[1] + eye_radius),
                 fill=eye_color)

    # Dessiner la bouche de la créature (un arc)
    mouth_radius = random.randint(20, 30)
    mouth_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    draw.arc((body_center[0] - mouth_radius, body_center[1] - mouth_radius,
              body_center[0] + mouth_radius, body_center[1] + mouth_radius),
             start=30, end=150, fill=mouth_color, width=5)

    del draw
    return image

if __name__ == "__main__":
    # Générer une créature et l'enregistrer dans un fichier
    creature_image = generate_creature(200, 200)
    creature_image.show()
    creature_image.save("creature.png")

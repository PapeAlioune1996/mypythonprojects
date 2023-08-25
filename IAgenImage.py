import random
from PIL import Image, ImageDraw, ImageFilter

def generate_creature_image(width, height):
    image = Image.new('RGBA', (width, height), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)

    # Draw the creature body (rectangle)
    body_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 255)
    body_width = random.randint(width // 4, width // 2)
    body_height = random.randint(height // 4, height // 2)
    body_x = random.randint(0, width - body_width)
    body_y = random.randint(0, height - body_height)
    draw.rectangle([body_x, body_y, body_x + body_width, body_y + body_height], fill=body_color)

    # Draw some random features on the creature
    for _ in range(random.randint(3, 6)):
        feature_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 255)
        feature_size = random.randint(min(body_width, body_height) // 8, min(body_width, body_height) // 2)
        feature_x = random.randint(body_x, body_x + body_width - feature_size)
        feature_y = random.randint(body_y, body_y + body_height - feature_size)
        draw.rectangle([feature_x, feature_y, feature_x + feature_size, feature_y + feature_size], fill=feature_color)

    # Apply some image filter for additional effects (optional)
    image = image.filter(ImageFilter.GaussianBlur(radius=2))

    return image

if __name__ == "__main__":
    # Specify the dimensions of the creature images
    image_width = 400
    image_height = 400

    # Generate and save a creature image
    creature_image = generate_creature_image(image_width, image_height)
    creature_image.show()  # Show the image (you can also save it using save() method)

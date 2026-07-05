from PIL import Image

def encrypt_image(input_image, output_image, key):
    img = Image.open(input_image)
    img = img.convert("RGB")

    width, height = img.size
    pixels = img.load()

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            # Encrypt each color channel
            r = (r + key) % 256
            g = (g + key) % 256
            b = (b + key) % 256

            pixels[x, y] = (r, g, b)

    img.save(output_image)
    print(f"Encrypted image saved as {output_image}")


def decrypt_image(input_image, output_image, key):
    img = Image.open(input_image)
    img = img.convert("RGB")

    width, height = img.size
    pixels = img.load()

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            # Decrypt each color channel
            r = (r - key) % 256
            g = (g - key) % 256
            b = (b - key) % 256

            pixels[x, y] = (r, g, b)

    img.save(output_image)
    print(f"Decrypted image saved as {output_image}")


# Main Program
key = int(input("Enter encryption key (0-255): "))

encrypt_image("input.jpg.png", "encrypted.jpg", key)
decrypt_image("encrypted.jpg", "decrypted.jpg", key)

print("Process completed successfully!")

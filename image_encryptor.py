# Written by: Shubh Patel
# Cyber Security Intern at Prodigy Infotech
# PRODIGY_CS_Task-02

from PIL import Image
import numpy as np

def encrypt_image(input_image_path, output_image_path, key):
    # Open the image file
    img = Image.open(input_image_path)
    img_array = np.array(img)

    # Apply encryption (XOR operation with key)
    encrypted_array = img_array ^ key

    # Save the encrypted image
    encrypted_img = Image.fromarray(encrypted_array)
    encrypted_img.save(output_image_path)

def decrypt_image(input_image_path, output_image_path, key):
    # Open the image file
    img = Image.open(input_image_path)
    img_array = np.array(img)

    # Apply decryption (XOR operation with key)
    decrypted_array = img_array ^ key

    # Save the decrypted image
    decrypted_img = Image.fromarray(decrypted_array)
    decrypted_img.save(output_image_path)

if __name__ == "__main__":
    key = 123  # Simple key for XOR operation
    encrypt_image("input_image.png", "encrypted_image.png", key)
    decrypt_image("encrypted_image.png", "decrypted_image.png", key)

# End of Code 

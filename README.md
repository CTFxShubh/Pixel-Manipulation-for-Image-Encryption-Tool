# PRODIGY_CS_Task-02
## Simple Image Encryption Tool Using Pixel Manipulation

This Simple Image Encryption Tool is a Python-based application designed to provide basic image encryption and decryption functionality through pixel manipulation. Utilizing the XOR operation with a user-defined key, this tool offers a straightforward approach to encrypting and decrypting images for educational and illustrative purposes.

## Features

1. Pixel-Based Encryption: Encrypts images using XOR operations with a simple key.

2. Decryption: Allows for the decryption of previously encrypted images using the same key.

3. Ease of Use: Simple Python script that can be easily customized and extended.

## Use Cases

1. Educational Purposes: Ideal for understanding basic encryption techniques and image processing.

2. Prototyping: Useful for quick, proof-of-concept encryption solutions.

## Steps to Use the Tool on Linux:

1. Clone the Repository To get started, first clone the repository from GitHub to your local Linux machine:

```bash
git clone https://github.com/CTFxShubh/PRODIGY_CS_Task-02.git
```
![1](https://github.com/user-attachments/assets/e378ce80-1e4e-4cc1-9a54-3d62f5e995fe)

2. Install required libraries:

pip install pillow 

Pillow:- Handles image file opening, manipulation, and saving.

![2](https://github.com/user-attachments/assets/fa4b410e-49f5-4292-8dc9-325baeb5e327)

pip install numpy

NumPy: Converts images to NumPy arrays for easy pixel manipulation.

![3](https://github.com/user-attachments/assets/cc8c5d5b-0aa2-480d-9521-44fb0e0092d2)

3. Give the executable permissions to the file

chmod +x image_encryptor.py

![6](https://github.com/user-attachments/assets/e8d0cc4c-4437-4a47-bfd0-ef63a664f0bd)

4. Now run the tool

python image_encryptor.py

![7](https://github.com/user-attachments/assets/f8194a90-ce8e-40ae-be6b-d16510e2c9fe)

5. Now u can see the encrypted and decrypted file in the list directory then use eog tool to open the .png image file

 eog encrypted_image.png

 ![8](https://github.com/user-attachments/assets/147e87e2-d108-4bc8-a977-3caae55141d8)

This is the image that is encrypted 

![9](https://github.com/user-attachments/assets/67476c28-625b-49e6-b44e-c1b185757600)

Now decrypted_image.png

![10](https://github.com/user-attachments/assets/81d79b5d-9be7-409a-8de9-4041c4fab215)

This is the decrypted image that we used to encrypt

![11](https://github.com/user-attachments/assets/12f838cd-1f7d-4382-8606-d295ad00da7b)

Additional Notes

Image Formats: Ensure that input_image.png is in a format supported by Pillow. If your image is in a different format, update the script accordingly.

Key: The key should be kept secret for security purposes. If you change the key, ensure to use the same key for both encryption and decryption. Here in my case I used 123 as a key for both purposes  

Conclusion

This Simple Image Encryption Tool offers a basic introduction to image encryption through direct pixel manipulation techniques. Utilizing XOR operations with a consistent key, this tool serves as an accessible starting point for understanding image encryption and decryption processes.

Although primarily intended for educational use, the underlying concepts can be adapted and scaled to create more sophisticated encryption solutions. For improved security, consider exploring advanced cryptographic techniques and incorporating complex algorithms.

We welcome contributions, suggestions, and any enhancements to this project. If you have any questions or need further assistance, please don't hesitate to reach out via email at shubhpatel931@gmail.com.

Thank you for your interest in the Simple Image Encryption Tool!


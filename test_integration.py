import sys
import os

# Adiciona o diretório 'src/' ao caminho do Python
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from image_processor import process_image
from ascii_converter import ASCIIConverter

# Integração entre image_processor e ascii_converter
def test_integration():
    input_image = "images/example_image.png"  
    processed_image = "processed_output.jpg"  
    ascii_output = "output_ascii.txt" 

    print("Processing the image...")
    process_image(input_image, processed_image, max_width=100)  

    print("Converting the processed image into ASCII art...")
    converter = ASCIIConverter()
    ascii_art = converter.image_to_ascii(processed_image)  

    print("Saving the ASCII art...")
    converter.save_ascii_art(ascii_art, ascii_output)

    print(f"Test completed! ASCII art saved in {ascii_output}")

# Teste
if __name__ == "__main__":
    test_integration()

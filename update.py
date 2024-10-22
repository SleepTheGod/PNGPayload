import base64

def print_header():
    print("Made By Taylor Christian Newsome")

def create_png():
    png_header = b'\x89PNG\r\n\x1a\n'
    ihdr_chunk = b'\x00\x00\x00\x0dIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x02\x00\x00\x00\x99\x9c\r\xec'
    idat_chunk = b'\x00\x00\x00\x03IDAT\x08\xd7c`\x00\x00\x00\x00\x01'
    iend_chunk = b'\x00\x00\x00\x00IEND\xaeB`\x82'
    png_data = png_header + ihdr_chunk + idat_chunk + iend_chunk

    output_filename = 'payload_image.png'
    with open(output_filename, 'wb') as f:
        f.write(png_data)

    base64_encoded = base64.b64encode(png_data).decode('utf-8')
    html_image_tag = f'<img src="data:image/png;base64,{base64_encoded}" alt="Payload Image">'
    
    with open('image_tag.html', 'w') as f:
        f.write(html_image_tag)
    
    print(f"PNG image saved as '{output_filename}'.")
    print(f"HTML image tag saved as 'image_tag.html'.")
    print(f'HTML Image Tag:\n{html_image_tag}')

if __name__ == "__main__":
    print_header()
    create_png()

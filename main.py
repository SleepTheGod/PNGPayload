import base64

print("Made By Taylor Christian Newsome")

def create_png():
    # Your PNG header and payload
    png_header = b'\x89PNG\r\n\x1a\n'
    ihdr_chunk = b'\x00\x00\x00\x0dIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x02\x00\x00\x00\x99\x9c\r\xec'
    idat_chunk = b'\x78\x9c\xec\x02\x00\x00\x00\x02\x00\x01'
    iend_chunk = b'\x00\x00\x00\x00IEND\xaeB`\x82'

    # Combine all chunks to create a valid PNG
    png_data = png_header + ihdr_chunk + idat_chunk + iend_chunk

    # Save to file
    output_filename = 'payload_image.png'
    with open(output_filename, 'wb') as f:
        f.write(png_data)

    # Encode in Base64
    base64_encoded = base64.b64encode(png_data).decode('utf-8')
    print(f"PNG image saved as '{output_filename}'.")
    
    # Create an HTML image tag
    html_image_tag = f'<img src="data:image/png;base64,{base64_encoded}" alt="Payload Image">'
    
    # Save the HTML image tag to a file
    with open('image_tag.html', 'w') as f:
        f.write(html_image_tag)
    
    print("HTML image tag saved as 'image_tag.html'.")
    print(f'HTML Image Tag:\n{html_image_tag}')

if __name__ == "__main__":
    create_png()

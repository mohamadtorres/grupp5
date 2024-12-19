from PIL import Image

# Paths to the files
sten_path = "C:\\Users\\mrahi\\Desktop\\Grupp 5\\grupp5\\img\\Start.png"
stenros_path = "C:\\Users\\mrahi\\Desktop\\Grupp 5\\grupp5\\img\\stenrös1.png"
output_stenros_path = "C:\\Users\\mrahi\\Desktop\\Grupp 5\\grupp5\\img\\stenrös_resized_transparent.png"

# Open the images
sten_image = Image.open(sten_path)
stenros_image = Image.open(stenros_path).convert("RGBA")  # Convert to RGBA for transparency

# Get the size of the sten.png
sten_size = sten_image.size

# Create a new transparent image
transparent_stenros = Image.new("RGBA", stenros_image.size, (255, 255, 255, 0))

# Remove white background by keeping non-white pixels
for x in range(stenros_image.width):
    for y in range(stenros_image.height):
        r, g, b, a = stenros_image.getpixel((x, y))
        if not (r > 200 and g > 200 and b > 200):  # Retain non-white pixels
            transparent_stenros.putpixel((x, y), (r, g, b, a))

# Resize the transparent image to match the size of sten.png
resized_transparent_stenros = transparent_stenros.resize(sten_size, Image.Resampling.LANCZOS)

# Save the output
resized_transparent_stenros.save(output_stenros_path, "PNG")
print(f"Transparent and resized image saved at: {output_stenros_path}")

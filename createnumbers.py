from PIL import Image, ImageDraw, ImageFont

# Settings
font_size = 64
sprite_width = font_size
sprite_height = font_size
sheet_width = sprite_width * 10

# Create new image
sprite_sheet = Image.new("RGBA", (sheet_width, sprite_height), (0, 0, 0, 0))
draw = ImageDraw.Draw(sprite_sheet)

# Load font
font = ImageFont.truetype("arial.ttf", font_size)

# Draw digits
for i in range(10):
    x = i * sprite_width
    draw.text((x + 10, 0), str(i), font=font, fill="white")

# Save
sprite_sheet.save("number_sprite.png")

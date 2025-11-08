from PIL import Image, ImageFont, ImageDraw

# مسیر فایل‌ها
image_path = "Quit Rect.png"
font_path = "font.ttf"
text = "PEAR"
font_size = 75

# باز کردن تصویر
img = Image.open(image_path)
width, height = img.size

# محاسبه طول متن با فونت داده‌شده
font = ImageFont.truetype(font_path, font_size)
dummy_img = Image.new("RGB", (1, 1))
draw = ImageDraw.Draw(dummy_img)

# استفاده از متد جدید textbbox به جای textsize
bbox = draw.textbbox((0, 0), text, font=font)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]

# تنظیم عرض جدید بر اساس طول متن
new_width = text_width
new_height = height  # ارتفاع ثابت

# تغییر اندازه تصویر
resized_img = img.resize((int(new_width), int(new_height)), Image.Resampling.LANCZOS)

# ذخیره تصویر جدید
output_path = "Quit_Rect_resized_PEAR.png"
resized_img.save(output_path)

print(f"✅ تصویر ساخته شد: {output_path}")

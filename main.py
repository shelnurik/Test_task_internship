from moviepy.editor import VideoClip
from PIL import Image, ImageDraw, ImageFont
import numpy as np

# Настройки
text = "Это пример бегущей строки на видео."  # Текст для бегущей строки
width, height = 100, 100  # Разрешение видео
duration = 3  # Длительность видео в секундах
fps = 60 # Частота кадров
font_size = 30  # Размер шрифта
text_color = 'white'  # Цвет текста
bg_color = 'black'  # Цвет фона

# Загрузка шрифта
font = ImageFont.truetype("arial.ttf", font_size)


# Функция генерации фрейма
def make_frame(t):
    img = Image.new("RGB", (width, height), color=bg_color)
    draw = ImageDraw.Draw(img)

    # Определяем размер текста
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    # Вычисляем позицию текста для эффекта бегущей строки
    x_position = width - int((width + text_width) * (t / duration))
    y_position = (height - text_height) // 2

    # Рисуем текст на изображении
    draw.text((x_position, y_position), text, font=font, fill=text_color)

    # Преобразуем изображение в массив NumPy
    return np.array(img)


# Создание видео
video = VideoClip(make_frame, duration=duration)

# Экспорт видео
video.write_videofile("output_video.mp4", fps=fps)

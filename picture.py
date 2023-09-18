from PIL import Image, ImageDraw
from persiantools.jdatetime import JalaliDate


def percent():
    current_date = JalaliDate.today()
    first_day_of_year = JalaliDate(current_date.year, 1, 1)
    days_passed = (current_date - first_day_of_year).days
    return days_passed

def create():

    width = 1000
    height = 200

    image = Image.new('RGB', (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(image)

    progress_width = 50 + 900*(percent()/365)

    background_color = (0, 0, 0) # Black
    bar_color = (8,255,8)  # Green
    border_color = (255, 255, 255)  # White
    border_color2 = (0, 0 ,0)

    draw.rectangle([(0, 0), (width, height)], fill=background_color)
    draw.rectangle([(0, 0), (progress_width, height)], fill=bar_color)

    border_width = 50 
    draw.rectangle([(0, 0), (width - 1, height - 1)], outline=border_color, width=border_width)
    border_width2 = 1
    draw.rectangle([(20, 20), (980, 180)], outline=border_color2, width=border_width2)
    
    image.save(r"D:\Prj_1\Twitter API\high_quality_progress_bar.jpg", "JPEG", quality=95)  # Adjust quality as needed

    print("High-quality progress bar image with a black border saved as 'high_quality_progress_bar.jpg'")

def year():
    current_jalali_date = JalaliDate.today()
    jalali_year = current_jalali_date.year
    return jalali_year

def num():
    return int(((percent() / 365) * 100) // 1)


create()
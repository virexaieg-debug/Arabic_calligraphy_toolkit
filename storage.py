# storage.py
import json
import os
from models import CalligraphyStyle  # استدعاء الكلاس من ملف models.py

FILE_NAME = "calligraphy_data.json"

def save_styles(styles_dict):
    data_to_save = {name: obj.to_dict() for name, obj in styles_dict.items()}
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(data_to_save, f, ensure_ascii=False, indent=4)

def load_styles():
    if not os.path.exists(FILE_NAME):
        default_styles = {
            "ثلث": CalligraphyStyle("ثلث", 8, 7),
            "نسخ": CalligraphyStyle("نسخ", 2, 5),
            "رقعة": CalligraphyStyle("رقعة", 2, 3),
            "ديواني": CalligraphyStyle("ديواني", 3, 5)
        }
        save_styles(default_styles)
        return default_styles

    with open(FILE_NAME, "r", encoding="utf-8") as f:
        raw_data = info = json.load(f)

    loaded_styles = {}
    for name, info in raw_data.items():
        loaded_styles[name] = CalligraphyStyle(name, info["pen_size"], info["alif_dots"])
    return loaded_styles

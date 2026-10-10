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
            "الكوفي": CalligraphyStyle("الكوفي", 5, 7),
            "الثلث": CalligraphyStyle("الثلث", 3, 7),
            "الثلث الجلي": CalligraphyStyle("الثلث الجلي", 8, 7),
            "النسخ": CalligraphyStyle("النسخ", 1, 5),
            "الرقعة": CalligraphyStyle("الرقعة", 2, 3),
            "الديواني": CalligraphyStyle("الديواني", 2, 6),
            "الديواني الجلي": CalligraphyStyle("الديواني الجلي", 4, 7),
            "النستعليق (الفارسي)": CalligraphyStyle("النستعليق (الفارسي)", 3, 3),
            "الفارسي الجلي": CalligraphyStyle("الفارسي الجلي", 8, 3),
            "الإجازة": CalligraphyStyle("الإجازة", 1, 7),
            "الطومار": CalligraphyStyle("الطومار", 7, 7),
            "الرقاع": CalligraphyStyle("الرقاع", 2, 7),
            "المحقق": CalligraphyStyle("المحقق", 5, 7),
            "الريحاني": CalligraphyStyle("الريحاني", 2, 5),
            "الوسام": CalligraphyStyle("الوسام", 5, 7),
            "السنبلي": CalligraphyStyle("السنبلي", 3, 5)
        }

        save_styles(default_styles)
        return default_styles

    with open(FILE_NAME, "r", encoding="utf-8") as f:
        raw_data = info = json.load(f)

    loaded_styles = {}
    for name, info in raw_data.items():
        loaded_styles[name] = CalligraphyStyle(name, info["pen_size"], info["alif_dots"])
    return loaded_styles

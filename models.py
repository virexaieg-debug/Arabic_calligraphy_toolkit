# models.py

class CalligraphyStyle:
    def __init__(self, name, pen_size, alif_dots):
        self.name = name
        self.pen_size = pen_size
        self.alif_dots = alif_dots

    def get_line_height_mm(self):
        return self.pen_size * self.alif_dots

    def get_line_spacing_mm(self):
        return (self.pen_size * self.alif_dots) * 2

    def to_dict(self):
        return {
            "pen_size": self.pen_size,
            "alif_dots": self.alif_dots
        }

    def get_info(self):
        height = self.get_line_height_mm()
        spacing = self.get_line_spacing_mm()
        return (
            f" خط ({self.name}):\n"
            f"   - مقاس القلم: {self.pen_size} مم\n"
            f"   - عدد نقاط الألف: {self.alif_dots} نقطة\n"
            f"   - ارتفاع السطر (طول الألف): {height} مم\n"
            f"   - المسافة بين سطري أساس: {spacing} مم"
        )


def get_valid_int(prompt_message):
    while True:
        try:
            value = int(input(prompt_message))
            if value <= 0:
                print(" يرجى إدخال رقم أكبر من الصفر!")
                continue
            return value
        except ValueError:
            print(" إدخال غير صحيح! يرجى كتابة رقم بالأرقام فقط (مثال: 3، 5).")

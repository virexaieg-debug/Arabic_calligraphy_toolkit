brush_sizes = {
    "ثلث": 8,
    "نسخ": 2,
    "رقعة": 2,
    "ديواني": 3,
    "فارسي": 4,
    "كوفي": 8,
    "رقاع": 2,
    "محقق": 3,
    "ريحاني": 2
}

def get_pen_size(sizes, style):
    size = sizes.get(style, "غير مسجل")
    return f"حجم القلم لخط ({style}) هو: {size} مم"

def add_new_style(sizes, style, size):
    sizes[style] = size
    return sizes

# نبدأ الحلقة التكرارية هنا
while True:
    print("\n--- برنامج دليل الخطاط العربي ---")
    print("1. البحث عن حجم قلم لخط")
    print("2. إضافة خط جديد")
    print("3. الخروج من البرنامج")

    choice = input("أدخل رقم الخيار (1 أو 2 أو 3): ")

    if choice == "1":
        style_input = input("أدخل اسم الخط للبحث عنه: ").strip()
        result = get_pen_size(brush_sizes, style_input)
        print(result)

    elif choice == "2":
        new_style = input("أدخل اسم الخط الجديد: ").strip()
        new_size = int(input("أدخل حجم القلم (بالمليمتر): "))
        updated_sizes = add_new_style(brush_sizes, new_style, new_size)
        print(f" تم إضافة خط ({new_style}) بنجاح!")

    elif choice == "3":
        print("شكراً لاستخدامك دليل الخطاط العربي. إلى اللقاء! ")
        break  # ينهي البرنامج ويفك الحلقة التكرارية

    else:
        print(" خيار غير صحيح! يرجى اختيار 1 أو 2 أو 3.")

    
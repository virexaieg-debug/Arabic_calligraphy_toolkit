# main.py
from models import CalligraphyStyle, get_valid_int
from storage import load_styles, save_styles

# تحميل بيانات الخطوط عند بدء التشغيل
styles_db = load_styles()

while True:
    print("\n---  دليل الخطاط العربي (Calligraphy Toolkit) ---")
    print("1. عرض معلومات وتفاصيل خط مسجل")
    print("2. إضافة خط جديد لحاسبة الأدوات")
    print("3. عرض قائمة جميع الخطوط المسجلة")
    print("4. الخروج من البرنامج")

    choice = input("أدخل رقم الخيار (1-4): ").strip()

    if choice == "1":
        style_name = input("أدخل اسم الخط (مثلاً: ثلث، نسخ): ").strip()
        if style_name in styles_db:
            print("\n" + styles_db[style_name].get_info())
        else:
            print(" هذا الخط غير مسجل حالياً.")

    elif choice == "2":
        name = input("أدخل اسم الخط الجديد: ").strip()
        pen_size = get_valid_int("أدخل مقاس القلم (بالمليمتر): ")
        alif_dots = get_valid_int("أدخل عدد نقاط الألف للخط: ")

        styles_db[name] = CalligraphyStyle(name, pen_size, alif_dots)
        save_styles(styles_db)
        print(f" تم إضافة خط ({name}) وحفظه في الملف بنجاح!")

    elif choice == "3":
        print("\n الخطوط المسجلة حالياً:")
        for name in styles_db:
            print(f"- {name}")

    elif choice == "4":
        print("شكراً لاستخدامك دليل الخطاط العربي. إلى اللقاء! ")
        break

    else:
        print(" خيار غير صحيح! يرجى اختيار رقم من 1 إلى 4.")

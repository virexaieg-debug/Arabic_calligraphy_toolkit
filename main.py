# main.py
from models import CalligraphyStyle, get_valid_int
from storage import load_styles, save_styles
from ink import InkGuide
from paper import PaperGuide

# تحميل بيانات الخطوط عند بدء التشغيل
styles_db = load_styles()

# داخل ملف main.py في حلقة التشغيل الرئيسية
 while True:
    print("\n---  دليل الخطاط العربي الشامل (Calligraphy Toolkit) ---")
    print("1. عرض معلومات وتفاصيل خط مسجل")
    print("2. إضافة خط جديد لحاسبة الأدوات")
    print("3. عرض قائمة جميع الخطوط المسجلة")
    print("4. فتح دليل الأحبار التجاري ")
    print("5. فتح دليل الورق ومقاساته ")
    print("6. الخروج من البرنامج")

    choice = input("أدخل رقم الخيار (1-6): ").strip()

    if choice == "1":
        style_name = input("أدخل اسم الخط (مثلاً: ثلث، نسخ، رقعة): ").strip()
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

    # [مكان إضافة كود دليل الأحبار في القائمة الرئيسية]
    elif choice == "4":
        ink_guide = InkGuide()
        print("\n1. عرض كافة الأحبار في الدليل التجاري")
        print("2. البحث عن حبر أو استخدام (مثل: سومي، باركر، تدريب)")
        sub_choice = input("أدخل خيار البحث (1 أو 2): ").strip()
        if sub_choice == "1":
            print(ink_guide.display_all_inks())
        elif sub_choice == "2":
            kw = input("أدخل كلمة البحث: ").strip()
            print(ink_guide.search_ink(kw))

    # [مكان إضافة كود دليل الورق في القائمة الرئيسية]
    elif choice == "5":
        paper_guide = PaperGuide()
        print("\n1. عرض كافة أنواع الورق في الدليل")
        print("2. البحث عن ورق أو خط مناسب (مثل: كوشيه، مقهر، ثلث)")
        sub_choice = input("أدخل خيار البحث (1 أو 2): ").strip()
        if sub_choice == "1":
            print(paper_guide.display_all_papers())
        elif sub_choice == "2":
            kw = input("أدخل كلمة البحث: ").strip()
            print(paper_guide.search_paper(kw))

    elif choice == "6":
        print("شكراً لاستخدامك دليل الخطاط العربي. إلى اللقاء! ")
        break

    else:
        print(" خيار غير صحيح! يرجى اختيار رقم من 1 إلى 6.")

        
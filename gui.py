import tkinter as tk
from tkinter import ttk, messagebox
from models import CalligraphyStyle, get_valid_int
from storage import load_styles, save_styles

class CalligraphyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("✒️ دليل الخطاط العربي - Calligraphy Toolkit")
        self.root.geometry("500x550")
        
        # تحميل البيانات
        self.styles_db = load_styles()

        # --- العنوان الرئيسي ---
        title_label = tk.Label(
            root, 
            text="دليل الخطاط العربي", 
            font=("Arial", 18, "bold"), 
            fg="#2c3e50"
        )
        title_label.pack(pady=10)

        # --- الإطار الأول: عرض معلومات خط مسجل ---
        frame_search = tk.LabelFrame(root, text=" الاستعلام عن خط ", font=("Arial", 11, "bold"), padx=10, pady=10)
        frame_search.pack(fill="x", px=15, pady=5)

        tk.Label(frame_search, text="اختر الخط:").grid(row=0, column=0, padx=5, pady=5)
        
        self.style_combobox = ttk.Combobox(frame_search, values=list(self.styles_db.keys()), state="readonly")
        self.style_combobox.grid(row=0, column=1, padx=5, pady=5)
        if self.styles_db:
            self.style_combobox.current(0)

        btn_show = tk.Button(frame_search, text="عرض التفاصيل", bg="#27ae60", fg="white", command=self.show_style_info)
        btn_show.grid(row=0, column=2, padx=5, pady=5)

        # --- الإطار الثاني: إضافة خط جديد ---
        frame_add = tk.LabelFrame(root, text=" إضافة خط جديد ", font=("Arial", 11, "bold"), padx=10, pady=10)
        frame_add.pack(fill="x", px=15, pady=10)

        tk.Label(frame_add, text="اسم الخط:").grid(row=0, column=0, sticky="e", pady=2)
        self.entry_name = tk.Entry(frame_add)
        self.entry_name.grid(row=0, column=1, pady=2)

        tk.Label(frame_add, text="مقاس القلم (مم):").grid(row=1, column=0, sticky="e", pady=2)
        self.entry_pen = tk.Entry(frame_add)
        self.entry_pen.grid(row=1, column=1, pady=2)

        tk.Label(frame_add, text="عدد نقاط الألف:").grid(row=2, column=0, sticky="e", pady=2)
        self.entry_dots = tk.Entry(frame_add)
        self.entry_dots.grid(row=2, column=1, pady=2)

        btn_add = tk.Button(frame_add, text="حفظ الخط الجديد", bg="#2980b9", fg="white", command=self.add_new_style)
        btn_add.grid(row=3, column=0, columnspan=2, pady=10)

        # --- الإطار الثالث: عرض مخرجات النتائج ---
        self.txt_result = tk.Text(root, height=8, font=("Arial", 10))
        self.txt_result.pack(fill="both", expand=True, px=15, pady=10)

    # --- الدوال التنفيذية للواجهة ---

    def show_style_info(self):
        selected_style = self.style_combobox.get()
        if selected_style in self.styles_db:
            info = self.styles_db[selected_style].get_info()
            self.txt_result.delete("1.0", tk.END)
            self.txt_result.insert(tk.END, info)
        else:
            messagebox.showwarning("تنبيه", "يرجى اختيار خط من القائمة!")

    def add_new_style(self):
        name = self.entry_name.get().strip()
        pen_str = self.entry_pen.get().strip()
        dots_str = self.entry_dots.get().strip()

        # التحقق من صحة المدخلات
        if not name or not pen_str or not dots_str:
            messagebox.showerror("خطأ", "يرجى ملء جميع الحقول!")
            return

        try:
            pen_size = int(pen_str)
            alif_dots = int(dots_str)
            if pen_size <= 0 or alif_dots <= 0:
                raise ValueError()
        except ValueError:
            messagebox.showerror("خطأ في المدخلات", "يرجى إدخال أرقام صحيحة أكبر من الصفر لمقاس القلم ونقاط الألف!")
            return

        # إضافة الخط للحافظة والملف
        self.styles_db[name] = CalligraphyStyle(name, pen_size, alif_dots)
        save_styles(self.styles_db)

        # تحديث القائمة المنسدلة
        self.style_combobox['values'] = list(self.styles_db.keys())
        self.style_combobox.set(name)

        # مسح حقول الإدخال
        self.entry_name.delete(0, tk.END)
        self.entry_pen.delete(0, tk.END)
        self.entry_dots.delete(0, tk.END)

        messagebox.showinfo("نجاح", f"تم إضافة خط ({name}) بنجاح وحفظه!")

# --- تشغيل التطبيق ---
if __name__ == "__main__":
    root = tk.Tk()
    app = CalligraphyApp(root)
    root.mainloop()

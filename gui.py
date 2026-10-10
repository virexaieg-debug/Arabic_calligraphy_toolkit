import tkinter as tk
from tkinter import ttk, messagebox, Toplevel
from models import CalligraphyStyle
from storage import load_styles, save_styles
from ink import InkGuide
from paper import PaperGuide

class CalligraphyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("✒️ دليل الخطاط العربي - Calligraphy Toolkit")
        self.root.geometry("600x700")

        # تحميل البيانات
        self.styles_db = load_styles()
        self.ink_guide = InkGuide()
        self.paper_guide = PaperGuide()

        # --- العنوان الرئيسي ---
        title_label = tk.Label(
            root, 
            text="دليل الخطاط العربي الشامل", 
            font=("Arial", 16, "bold"), 
            fg="#2c3e50"
        )
        title_label.pack(pady=5)

        # --- الإطار الأول: عرض معلومات خط مسجل ---
        frame_search = tk.LabelFrame(root, text=" الاستعلام عن خط ", font=("Arial", 10, "bold"), padx=5, pady=5)
        frame_search.pack(fill="x", padx=10, pady=3)

        tk.Label(frame_search, text="اختر الخط:").grid(row=0, column=0, padx=5, pady=2)

        self.style_combobox = ttk.Combobox(frame_search, values=list(self.styles_db.keys()), state="readonly", width=18)
        self.style_combobox.grid(row=0, column=1, padx=5, pady=2)
        if self.styles_db:
            self.style_combobox.current(0)

        btn_show = tk.Button(frame_search, text="عرض التفاصيل", bg="#27ae60", fg="white", command=self.show_style_info)
        btn_show.grid(row=0, column=2, padx=5, pady=2)

        # --- الإطار الثاني: إضافة خط جديد ---
        frame_add = tk.LabelFrame(root, text=" إضافة خط جديد ", font=("Arial", 10, "bold"), padx=5, pady=5)
        frame_add.pack(fill="x", padx=10, pady=3)

        tk.Label(frame_add, text="اسم الخط:").grid(row=0, column=0, sticky="e", pady=1)
        self.entry_name = tk.Entry(frame_add, width=20)
        self.entry_name.grid(row=0, column=1, pady=1)

        tk.Label(frame_add, text="مقاس القلم (مم):").grid(row=1, column=0, sticky="e", pady=1)
        self.entry_pen = tk.Entry(frame_add, width=20)
        self.entry_pen.grid(row=1, column=1, pady=1)

        tk.Label(frame_add, text="عدد نقاط الألف:").grid(row=2, column=0, sticky="e", pady=1)
        self.entry_dots = tk.Entry(frame_add, width=20)
        self.entry_dots.grid(row=2, column=1, pady=1)

        btn_add = tk.Button(frame_add, text="حفظ الخط الجديد", bg="#2980b9", fg="white", command=self.add_new_style)
        btn_add.grid(row=3, column=0, columnspan=2, pady=5)

        # --- الإطار الثالث: أدلة الأحبار والورق (إضافات جديدة) ---
        frame_guides = tk.LabelFrame(root, text=" الأدلة التجارية (الأحبار والورق) ", font=("Arial", 10, "bold"), padx=5, pady=5)
        frame_guides.pack(fill="x", padx=10, pady=3)

        btn_inks = tk.Button(frame_guides, text="墨 استعراض دليل الأحبار", bg="#8e44ad", fg="white", command=self.open_ink_window)
        btn_inks.grid(row=0, column=0, padx=10, pady=5, sticky="ew")

        btn_papers = tk.Button(frame_guides, text="📜 استعراض دليل الورق", bg="#d35400", fg="white", command=self.open_paper_window)
        btn_papers.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

        frame_guides.columnconfigure(0, weight=1)
        frame_guides.columnconfigure(1, weight=1)

        # --- الإطار الرابع: عرض مخرجات النتائج ---
        frame_output = tk.LabelFrame(root, text=" شاشة النتائج والمخرجات ", font=("Arial", 10, "bold"), padx=5, pady=5)
        frame_output.pack(fill="both", expand=True, padx=10, pady=5)

        self.txt_result = tk.Text(frame_output, height=10, font=("Arial", 10))
        self.txt_result.pack(fill="both", expand=True, side=tk.LEFT)

        scrollbar = tk.Scrollbar(frame_output, command=self.txt_result.yview)
        scrollbar.pack(fill="y", side=tk.RIGHT)
        self.txt_result.config(yscrollcommand=scrollbar.set)

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

        if not name or not pen_str or not dots_str:
            messagebox.showerror("خطأ", "يرجى ملء جميع الحقول!")
            return

        try:
            pen_size = int(pen_str)
            alif_dots = int(dots_str)
            if pen_size <= 0 or alif_dots <= 0:
                raise ValueError()
        except ValueError:
            messagebox.showerror("خطأ في المدخلات", "يرجى إدخال أرقام صحيحة أكبر من الصفر!")
            return

        self.styles_db[name] = CalligraphyStyle(name, pen_size, alif_dots)
        save_styles(self.styles_db)

        self.style_combobox['values'] = list(self.styles_db.keys())
        self.style_combobox.set(name)

        self.entry_name.delete(0, tk.END)
        self.entry_pen.delete(0, tk.END)
        self.entry_dots.delete(0, tk.END)

        messagebox.showinfo("نجاح", f"تم إضافة خط ({name}) بنجاح وحفظه!")

    def open_ink_window(self):
        # نافذة منبثقة لدليل الأحبار مع خيار البحث
        win = Toplevel(self.root)
        win.title("دليل الأحبار التجاري")
        win.geometry("450x400")

        tk.Label(win.text if hasattr(win, 'text') else win, text="البحث في الأحبار:", font=("Arial", 10, "bold")).pack(pady=5)
        entry_search = tk.Entry(win, width=30)
        entry_search.pack(pady=5)

        txt_ink_result = tk.Text(win, height=15, font=("Arial", 9))
        txt_ink_result.pack(fill="both", expand=True, padx=10, pady=5)

        # عرض الكل افتراضياً
        all_inks = self.ink_guide.display_all_inks()
        txt_ink_result.insert(tk.END, all_inks)

        def perform_search():
            kw = entry_search.get().strip()
            if kw:
                res = self.ink_guide.search_ink(kw)
            else:
                res = self.ink_guide.display_all_inks()
            txt_ink_result.delete("1.0", tk.END)
            txt_ink_result.insert(tk.END, res)

        btn_s = tk.Button(win, text="بحث", bg="#8e44ad", fg="white", command=perform_search)
        btn_s.pack(pady=5)

    def open_paper_window(self):
        # نافذة منبثقة لدليل الورق مع خيار البحث
        win = Toplevel(self.root)
        win.title("دليل أنواع الورق")
        win.geometry("450x400")

        tk.Label(win, text="البحث في أنواع الورق:", font=("Arial", 10, "bold")).pack(pady=5)
        entry_search = tk.Entry(win, width=30)
        entry_search.pack(pady=5)

        txt_paper_result = tk.Text(win, height=15, font=("Arial", 9))
        txt_paper_result.pack(fill="both", expand=True, padx=10, pady=5)

        # عرض الكل افتراضياً
        all_papers = self.paper_guide.display_all_papers()
        txt_paper_result.insert(tk.END, all_papers)

        def perform_search():
            kw = entry_search.get().strip()
            if kw:
                res = self.paper_guide.search_paper(kw)
            else:
                res = self.paper_guide.display_all_papers()
            txt_paper_result.delete("1.0", tk.END)
            txt_paper_result.insert(tk.END, res)

        btn_s = tk.Button(win, text="بحث", bg="#d35400", fg="white", command=perform_search)
        btn_s.pack(pady=5)

# --- تشغيل التطبيق ---
if __name__ == "__main__":
    root = tk.Tk()
    app = CalligraphyApp(root)
    root.mainloop()

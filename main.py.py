import webbrowser
import tkinter as tk
from tkinter import messagebox


def run_dork():
  target = entry_target.get().strip()
  dork_type = dork_var.get()

  if not target:
    messagebox.showerror(
        "خطأ", "الرجاء إدخال اسم الهدف أو النطاق المستهدف أولاً!"
    )
    return

  # تحديد الـ Dork بناءً على الاختيار
  dorks = {
      "مجلدات مكشوفة (Index of)": (
          f'https://www.google.com/search?q=site:{target}+intitle:"index.of"'
      ),
      "ملفات حساسّة (PDF / Config)": (
          f'https://www.google.com/search?q=site:{target}+filetype:pdf+OR+filetype:config+OR+filetype:env'
      ),
      "صفحات تسجيل الدخول": (
          f'https://www.google.com/search?q=site:{target}+inurl:login+OR+inurl:admin'
      ),
      "بحث شامل عام": f"https://www.google.com/search?q=site:{target}",
  }

  url = dorks.get(dork_type)
  if url:
    webbrowser.open(url)


# تصميم واجهة المستخدم (GUI)
root = tk.Tk()
root.title("My Custom Dork Tool")
root.geometry("450x350")
root.configure(bg="#1e1e1e")

# عنوان الأداة
label_title = tk.Label(
    root,
    text="أداة البحث المتقدم (Custom Dork)",
    font=("Arial", 14, "bold"),
    bg="#1e1e1e",
    fg="#00ffcc",
)
label_title.pack(pady=15)

# حقل إدخال الهدف
label_target = tk.Label(
    root,
    text="أدخل النطاق أو الهدف (مثال: example.com):",
    font=("Arial", 10),
    bg="#1e1e1e",
    fg="white",
)
label_target.pack(anchor="w", padx=30)

entry_target = tk.Entry(root, font=("Arial", 11), width=35)
entry_target.pack(pady=5, padx=30)

# قائمة اختيار نوع الـ Dork
label_type = tk.Label(
    root,
    text="اختر نوع الفحص:",
    font=("Arial", 10),
    bg="#1e1e1e",
    fg="white",
)
label_type.pack(anchor="w", padx=30, pady=(10, 0))

dork_var = tk.StringVar(value="مجلدات مكشوفة (Index of)")
options = [
    "مجلدات مكشوفة (Index of)",
    "ملفات حساسّة (PDF / Config)",
    "صفحات تسجيل الدخول",
    "بحث شامل عام",
]

for option in options:
  rb = tk.Radiobutton(
      root,
      text=option,
      variable=dork_var,
      value=option,
      bg="#1e1e1e",
      fg="white",
      selectcolor="#333333",
      activebackground="#1e1e1e",
      activeforeground="white",
  )
  rb.pack(anchor="w", padx=40)

# زر التنفيد
btn_run = tk.Button(
    root,
    text="تشغيل البحث",
    command=run_dork,
    font=("Arial", 11, "bold"),
    bg="#00aa66",
    fg="white",
    width=20,
)
btn_run.pack(pady=20)

root.mainloop()
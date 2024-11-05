import tkinter as tk
from tkinter import scrolledtext, messagebox
from main import MedicalExpert

class MedicalExpertGUI:
    def __init__(self, master):
        self.master = master
        master.title("Hệ thống chẩn đoán lâm sàng")
        master.geometry("600x400")

        self.label = tk.Label(master, text="Chào mừng đến với hệ thống chẩn đoán lâm sàng!")
        self.label.pack(pady=10)

        self.start_button = tk.Button(master, text="Bắt đầu chẩn đoán", command=self.start_diagnosis)
        self.start_button.pack(pady=10)

        self.text_area = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=70, height=20)
        self.text_area.pack(pady=10)

        self.engine = MedicalExpert()

    def start_diagnosis(self):
        self.text_area.delete('1.0', tk.END)
        self.engine.reset()
        self.redirect_print()
        self.engine.run()
        self.restore_print()
        self.show_result()

    def redirect_print(self):
        self.old_stdout = sys.stdout
        sys.stdout = self

    def restore_print(self):
        sys.stdout = self.old_stdout

    def write(self, text):
        self.text_area.insert(tk.END, text)
        self.text_area.see(tk.END)
        self.master.update()

    def show_result(self):
        disease = self.engine.facts.get(Fact(disease=MATCH.disease))
        if disease:
            messagebox.showinfo("Kết quả chẩn đoán", f"Bệnh được chẩn đoán: {disease[0].value}")
        else:
            messagebox.showinfo("Kết quả chẩn đoán", "Không thể xác định bệnh")

if __name__ == "__main__":
    import sys
    root = tk.Tk()
    gui = MedicalExpertGUI(root)
    root.mainloop()
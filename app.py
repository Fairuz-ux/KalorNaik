import tkinter as tk
from tkinter import ttk, messagebox

kalor_jenis_data = {
    "Air": 4.18,
    "Aluminium": 0.90,
    "Tembaga": 0.39,
    "Besi": 0.45,
    "Emas": 0.13
}

def hitung_kalor():
    try:
        m = float(entry_massa.get())
        t_awal = float(entry_t_awal.get())
        t_akhir = float(entry_t_akhir.get())
        zat = zat_var.get()
        c = kalor_jenis_data.get(zat, 0)

        delta_t = t_akhir - t_awal
        q = m * c * delta_t

        hasil_label.config(text=f"Kalor yang dibutuhkan: {q:.2f} Joule")
    except ValueError:
        messagebox.showerror("Input tidak valid", "Harap isi semua kolom dengan angka yang benar.")

root = tk.Tk()
root.title("KalorNaik - Kalkulator Kalor Zat")

tk.Label(root, text="Pilih Zat:").grid(row=0, column=0, sticky="w")
zat_var = ttk.Combobox(root, values=list(kalor_jenis_data.keys()))
zat_var.grid(row=0, column=1)
zat_var.current(0)

tk.Label(root, text="Massa (gram):").grid(row=1, column=0, sticky="w")
entry_massa = tk.Entry(root)
entry_massa.grid(row=1, column=1)

tk.Label(root, text="Suhu Awal (°C):").grid(row=2, column=0, sticky="w")
entry_t_awal = tk.Entry(root)
entry_t_awal.grid(row=2, column=1)

tk.Label(root, text="Suhu Akhir (°C):").grid(row=3, column=0, sticky="w")
entry_t_akhir = tk.Entry(root)
entry_t_akhir.grid(row=3, column=1)

tk.Button(root, text="Hitung Kalor", command=hitung_kalor).grid(row=4, columnspan=2, pady=10)

hasil_label = tk.Label(root, text="", font=("Arial", 12))
hasil_label.grid(row=5, columnspan=2)

root.mainloop()
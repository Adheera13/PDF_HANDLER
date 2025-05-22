# GUI Launched - Tkinter based
import tkinter as tk
from tkinter import filedialog
from viewer import launch_pdf_viewer
from editor import merge_pdfs, split_pdf

def open_viewer():
    file = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file:
        launch_pdf_viewer(file)

def open_merge():
    files = filedialog.askopenfilenames(filetypes=[("PDF Files", "*.pdf")])
    if files:
        merge_pdfs(list(files), "output/merged_output.pdf")

def open_split():
    file = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file:
        split_pdf(file)

root = tk.Tk()
root.title("PDF Toolkit")

tk.Button(root, text="View PDF", command=open_viewer).pack(pady=5)
tk.Button(root, text="Merge PDFs", command=open_merge).pack(pady=5)
tk.Button(root, text="Split PDF", command=open_split).pack(pady=5)

root.mainloop()

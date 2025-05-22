import fitz  # PyMuPDF
import tkinter as tk
from PIL import Image, ImageTk

def launch_pdf_viewer(filepath):
    doc = fitz.open(filepath)
    current_page = 0

    def render_page(index):
        pix = doc.load_page(index).get_pixmap()
        img = ImageTk.PhotoImage(Image.frombytes("RGB", [pix.width, pix.height], pix.samples))
        canvas.img = img
        canvas.create_image(0, 0, anchor="nw", image=img)

    def next_page():
        nonlocal current_page
        if current_page < len(doc) - 1:
            current_page += 1
            render_page(current_page)

    def prev_page():
        nonlocal current_page
        if current_page > 0:
            current_page -= 1
            render_page(current_page)

    viewer = tk.Toplevel()
    viewer.title(f"Viewing {filepath}")
    canvas = tk.Canvas(viewer, width=800, height=900)
    canvas.pack()

    btn_frame = tk.Frame(viewer)
    btn_frame.pack()

    tk.Button(btn_frame, text="<< Prev", command=prev_page).pack(side=tk.LEFT)
    tk.Button(btn_frame, text="Next >>", command=next_page).pack(side=tk.RIGHT)

    render_page(current_page)
    viewer.mainloop()

import tkinter as tk
from tkinter import filedialog, messagebox
from pypdf import PdfWriter, PdfReader

def select_files():
    files = filedialog.askopenfilenames(
        title="Select PDF files to merge",
        filetypes=[("PDF files", "*.pdf")],
    )
    if files:
        file_list.delete(0, tk.END)
        for f in files:
            file_list.insert(tk.END, f)

def merge_pdfs():
    files = file_list.get(0, tk.END)
    if not files:
        messagebox.showwarning("No Files", "Please select at least two PDF files.")
        return
    
    output_path = filedialog.asksaveasfilename(
        defaultextension=".pdf",
        filetypes=[("PDF files", "*.pdf")],
        title="Save Merged PDF As"
    )
    if not output_path:
        return

    try:
        writer = PdfWriter()
        for pdf in files:
            reader = PdfReader(pdf)
            for page in reader.pages:
                writer.add_page(page)
        with open(output_path, "wb") as output_file:
            writer.write(output_file)
        messagebox.showinfo("Success", f"Merged PDF saved to:\n{output_path}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI setup
root = tk.Tk()
root.title("Simple PDF Merger")
root.geometry("500x300")

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Button(frame, text="Select PDF Files", command=select_files).pack()

file_list = tk.Listbox(frame, width=60, height=10)
file_list.pack(pady=10)

tk.Button(frame, text="Merge PDFs", command=merge_pdfs).pack(pady=5)

root.mainloop()

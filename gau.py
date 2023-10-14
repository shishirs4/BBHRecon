import subprocess
import tkinter as tk
from tkinter import filedialog
from threading import Thread

def execute_command(file_path):
    command = f"cat {file_path} | gau --threads 10 --blacklist png,jpg,gif,svg,ttf,woff > endpoints.txt"
    subprocess.Popen(command, shell=True)

def fetch_endpoints():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        thread = Thread(target=execute_command, args=(file_path,))
        thread.start()
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "Endpoints fetching started. Please wait.")

# Create the main window
window = tk.Tk()
window.title("Endpoint Fetcher")
window.geometry("400x300")

# Create a button to upload the file
upload_button = tk.Button(window, text="Upload And Collect URL's", command=fetch_endpoints)
upload_button.pack(pady=10)

# Create a text area to display the output
output_text = tk.Text(window)
output_text.pack(expand=True, fill=tk.BOTH)

# Start the main event loop
window.mainloop()

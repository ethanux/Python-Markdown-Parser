import tkinter as tk
from tkinter import ttk, scrolledtext
import webview
import threading
import tempfile
import os
import time
from tokenizer.make_token import MakeToken
from parsers.driver_parser import DriverParser
from config.theme import Theme

# --- Markdown to HTML Function ---
def parse_markdown_to_html(markdown_lines):
    if markdown_lines:
        tokenizer = MakeToken(markdown_lines)
        tokens = tokenizer.get_tokens()
        driver = DriverParser(tokens)
        content = "\n".join(driver.html_parser())

        theme = Theme()

        html = f"""
        <html>
            <head>
                <meta charset="UTF-8">
                <title>Markdown Render</title>
                {theme.get_theme()}
            </head>
            <body>
                {content}
            </body>
        </html>
        """
        print(html)
        return html
    return "<h1>No Markdown parsed</h1>"

# --- Demo Markdown ---
demo_markdown = """# Heading 1
## Heading 2

This is a paragraph with **bold**, *italic*, and `inline code`.

### unordered list item
- Item 1
- Item 2

### ordered list item
1. First
2. Second

"""

class MarkdownApp:
    def __init__(self):
        self.html_file_path = self.create_temp_html("<p>Initial render</p>")
        self.window = None

    def create_temp_html(self, html_content):
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".html", mode="w", encoding="utf-8")
        temp_file.write(html_content)
        temp_file.close()
        return temp_file.name

    def convert_and_render(self, markdown_text):
        html_output = parse_markdown_to_html(markdown_text.strip().splitlines())
        with open(self.html_file_path, "w", encoding="utf-8") as f:
            f.write(html_output)

        # Refresh browser if already started
        if self.window:
            self.window.load_html(html_output)

    def start_gui(self):
        # Create the input window
        root = tk.Tk()
        root.title("Markdown Input")
        root.geometry("700x700")
        root.configure(bg="#1e1e1e")

        ttk.Label(root, text="Markdown Input").pack(anchor="w", padx=10, pady=(10, 0))

        input_box = scrolledtext.ScrolledText(
            root, bg="#2d2d2d", fg="#ffffff", insertbackground="white", font=("Consolas", 12)
        )
        input_box.pack(fill="both", expand=True, padx=10, pady=10)
        input_box.insert("1.0", demo_markdown)

        def on_render():
            markdown = input_box.get("1.0", tk.END)
            self.convert_and_render(markdown)

        ttk.Button(root, text="Convert & Render", command=on_render).pack(pady=10)

        root.mainloop()

    def start_webview(self):
        self.window = webview.create_window("HTML Preview", f"file://{self.html_file_path}", width=800, height=700)
        webview.start(debug=False)

    def run(self):
        # Start webview in main thread
        gui_thread = threading.Thread(target=self.start_gui, daemon=True)
        gui_thread.start()

        self.start_webview()


if __name__ == "__main__":
    app = MarkdownApp()
    app.run()


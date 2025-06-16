#  Lightweight Markdown Parser with GUI and Live Preview

## Overview

This project is a lightweight Markdown tokenizer, parser, and renderer built in Python. It converts raw Markdown (.md) input into structured tokens, parses them into HTML, and displays a real-time preview of the rendered content.

Initially designed as a command-line tool for educational purposes—to demonstrate lexical analysis and parsing similar to that used in compilers—it has since been expanded with a graphical user interface (GUI) using tkinter, and a live HTML preview window powered by pywebview.
---
## Image Preview
![Capture](https://github.com/user-attachments/assets/3462c49a-a3f7-4bb1-82f6-e6625964ecac)


## How It Works

**Markdown Input** – Users type or paste Markdown into the GUI.

**Tokenization** – The MakeToken module scans the Markdown and generates tokens representing Markdown elements.

**Parsing** – The DriverParser processes these tokens into corresponding HTML.

**Rendering** – The HTML is styled using a custom theme (Theme) and rendered in a pywebview window.

**Live Feedback** – Every time the user clicks "Convert & Render", the preview updates instantly. 

---


# How tokenization works
### **Line-based Tokenization**:
   - Detects headers (lines starting with `#`)
   - Detects unordered list items (lines starting with `-`)
   - Detects ordered list items (lines starting with `1.` ) numbering is autometically handled
   - Detects code block (line starting with ` ``` `, and ending with ` ``` `)
   - Defaults to plain text if no special formatting is found

   #### **Block-Level Token Types**
   
   | Block Type         | Syntax Pattern                   | Tokenizer Used    |
   | ------------------ | -------------------------------- | ----------------- |
   | **Header**         | `#`, `##`, etc.                  | `HeaderTokenizer` |
   | **Unordered List** | `- item` or `-- item`            | `ListTokenizer`   |
   | **Ordered List**   | `1. item`, `2. item`, etc.       | `ListTokenizer`   |
   | **Code Block**     | Between triple backticks ` ``` ` | `CodeTokenizer`   |
   | **Plain Text**     | Any other line                   | `TextTokenizer`   |


   #### **Will produce**:

   - A header token with inline tokens

   - A text token with multiple inline tokens

   - A list item (unordered)

   - A list item (ordered)

   - A code block token with the Python function as content
  
   After block-level parsing, the value of each token is further scanned for inline formatting using InlineTokenizer

 ### **Inline Tokenization**:

The InlineTokenizer parses inline formatting in a given string and converts recognized styles into structured tokens. Supported formats include:
Supported Syntax:

   | Format Type | Syntax Example           | Token Type          |
   | ----------- | ------------------------ | ------------------- |
   | **Bold**    | `**bold**` or `__bold__` | `InlineType.BOLD`   |
   | *Italic*    | `*italic*` or `_italic_` | `InlineType.ITALIC` |
   | `Code`      | `` `inline code` ``      | `InlineType.CODE`   |
   | `Code`      | ` ` spaced code ` `      | `InlineType.CODE`   |
   
   
   
#### **Example Input:** 
 ```
 This is **bold**, *italic*, and `code`.
 ```

**Output Tokens:**
```
   [
             InlineToken(InlineType.TEXT, "This is "),
             InlineToken(InlineType.BOLD, "bold"),
             InlineToken(InlineType.TEXT, ", "),
             InlineToken(InlineType.ITALIC, "italic"),
             InlineToken(InlineType.TEXT, ", and "),
             InlineToken(InlineType.CODE, "code"),
             InlineToken(InlineType.TEXT, ".")
      ]
```

### **Token Representation**:
   - Each token has a type and value
   - Complex lines may yield nested tokens (e.g., header + inline bold text)

---

## Tokenization Rules

The following rules govern how Markdown elements are tokenized:

- `#`, `##`, ... `######` → Header tokens (levels 1 to 6)
- `-` at the beginning of a line → List item token (unordered)
- `1.` at the beginning of a line → List item token (ordered)
- `**text**` → Bold token
- `__text__` → Bold token
-  `_text_` → Italic token
-  `*text*` → Italic token
- `` `code` `` → Inline code token
- `` ```code``` `` → Block code token
- Default → Plain text token

---
# inline markdown parser rules 

| Markdown     | Token Type | InlineType |
| ------------ | ---------- | ---------- |
| `*italic*`   | Inline     | `ITALIC`   |
| `_italic_`   | Inline     | `ITALIC`   |
| `**bold**`   | Inline     | `BOLD`     |
| `__bold__`   | Inline     | `BOLD`     |
| `` `code` `` | Inline     | `CODE`     |
| Regular text | Inline     | `TEXT`     |


## For each line:
- Check if it’s a header (`#`)
- Check if it's an unordered list (`-`)
- Check if it's an ordered list (`1.`, `2.`, etc.)
- Check if it's a code block  (` ``` `)
- Else: treat as normal text

## For all:
- Tokenize block-level
- Then tokenize inline
- Append either: 
    (block_token, [inline_tokens]) or block_token (if no inline)
- convert to html contents using token types

---
# Topics Covered & Lessons Learned

This project covers a variety of topics in both **programming** and **system design**:

### Programming Concepts
- Object-Oriented Programming (OOP)
- File I/O
- Regular Expressions (Regex)
- Python modules and packages
- Test-driven development (TDD) structure

### System Design Concepts
- Tokenization & Lexical Analysis
- Parser Architecture
- Modularity and Separation of Concerns
- Reusability and Extensibility in Software Design

This makes the project a strong starting point for those interested in building interpreters, compilers, or static analyzers.

---

# How to Run

### Prerequisites

Make sure you have Python 3 installed. You’ll also need the following Python packages:
```
pip install pywebview
```
| **_Note: tkinter comes pre-installed with most Python distributions. If not, you may need to install it manually depending on your OS_**.


### Running the App
1. Clone the Repository on your computer:
   ```
   git clone https://github.com/ethanux/Python-Markdown-Parser.git
   cd Python-Markdown-Parser
   ```
   | **_Note:if not using command line please change directories to the main/root directory of the project_**

2. Run the Main File:
   
   on your teminlal run the following command and make sure u have python3 or heigher installed
   ```
   python main.py
   ```
   | **_Note : if you dont know ho to use the terminal just run the `main.py` file but double clicking on it_**
   
3. This will:

- Launch the GUI for Markdown input

- Open a new window for HTML preview
---

### Test It Out

Try entering this example into the input box:

```
# Hello World

This is a paragraph with **bold**, *italic*, and `inline code`.

## List

- Item 1
- Item 2

1. First
2. Second

```

**Then click “Convert & Render” to see the output in real time!**



## License

This project is open-source and available under the MIT License.

# Markdown Tokenizer and Parser

## Overview

This project is a lightweight Markdown tokenizer and parser built in Python. Its primary purpose is to take a raw Markdown (`.md`) file and convert it into structured tokens that represent different Markdown elements such as headers, lists, inline formatting (bold, italic, code), and plain text.

This modular design allows for easy extension and serves as an educational tool for understanding how parsing and lexical analysis work behind the scenes in compilers and interpreters.

---

## How It Works

The system reads a Markdown file line by line and passes each line through a series of tokenizers. The process involves:

1. **Line-based Tokenization**:
   - Detects headers (lines starting with `#`)
   - Detects unordered list items (lines starting with `-`)
   - Detects unordered list items (lines starting with `1.` ) numbering is autometically handled
   - Defaults to plain text if no special formatting is found

2. **Inline Tokenization**:
   - Extracts inline formatting inside the lines:
     - `**bold**`
     - `*italic*`
     - `` `inline code` ``

3. **Token Representation**:
   - Each token has a type and value
   - Complex lines may yield nested tokens (e.g., header + inline bold text)

---

## Tokenization Rules

The following rules govern how Markdown elements are tokenized:

- `#`, `##`, ... `######` → Header tokens (levels 1 to 6)
- `-` at the beginning of a line → List item token
- `1.` at the beginning of a line → List item token
- `*text*` → Bold token
-  `_text_` → Italic token
- `` `code` `` → Inline code token
- Default → Plain text token

---

## Topics Covered & Lessons Learned

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

## How to Run

### Prerequisites

- Python 3.8 or higher

### Steps

1. Clone or download the repository.
2. Place your Markdown file as `README.md` inside the `markdown/` directory.
3. Run the tokenizer:

```bash
python markdown/main.py
```

This will output the list of tokens detected in the Markdown file, showing how each line is parsed and categorized.

---

## Example Output

Given a `README.md` like:

```markdown
# Welcome
This is **bold** and *italic*.
- List item 1
```

The output will be a structured token list identifying the header, inline styles, and list item accordingly.

---

## License

This project is open-source and available under the MIT License.

class Theme:
	styles = """
<style>
    /* Global Reset and Base Styling */
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    html, body {
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      background-color: #1e1e1e;
      color: #d4d4d4;
      line-height: 1.6;
      padding: 2rem;
    }

    h1, h2, h3 {
      color: #ffffff;
      margin-top: 1.5rem;
      margin-bottom: 0.5rem;
    }

    h1 {
      font-size: 2rem;
      border-bottom: 2px solid #444;
      padding-bottom: 0.3rem;
    }

    h2 {
      font-size: 1.6rem;
      border-bottom: 1px solid #333;
    }

    h3 {
      font-size: 1.3rem;
    }

    p {
      margin-bottom: 1rem;
    }

    pre, code {
      background-color: #2d2d2d;
      color: #f8f8f2;
      padding: 0.75rem;
      border-radius: 5px;
      overflow-x: auto;
      font-family: 'Courier New', Courier, monospace;
    }

    pre {
      margin: 1rem 0;
    }

    code {
      padding: 0.2rem 0.4rem;
      font-size: 0.95rem;
    }

    ul, ol {
      margin-left: 2rem;
      margin-bottom: 1rem;
    }

    li {
      margin-bottom: 0.5rem;
    }

    table {
      width: 100%;
      border-collapse: collapse;
      margin: 1rem 0;
      background-color: #2a2a2a;
    }

    table code {
      background-color: #3a3a3a;
    }

    th, td {
      padding: 0.75rem;
      text-align: left;
      border-bottom: 1px solid #444;
    }

    th {
      background-color: #333;
      color: #fff;
    }

    td {
      color: #ccc;
    }

    a {
      color: #80cbc4;
      text-decoration: none;
    }

    a:hover {
      text-decoration: underline;
    }
  </style>
"""

	def get_theme(self):
		return self.styles
	
		
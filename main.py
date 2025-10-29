#!/usr/bin/env python3

import csv

# Read the CSV file
with open("data.csv", newline='', encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    rows = list(reader)

# Generate HTML
html = """
<html>
<!-- https://blog.miguelgrinberg.com/post/how-to-add-dark-mode-support-to-your-website -->
<doctype !html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <style>
      :root, [data-theme="light"] {
        --page-bg-color: #e8e8ea;
        --page-fg-color: #333333;
        --h1-fg-color: #44446a;
        --h2-fg-color: #64648a;
        --code-fg-color: #a83030;
        --code-bg-color: #d8d8d8;
      }
      [data-theme="dark"] {
        --page-bg-color: #18181a;
        --page-fg-color: #cccccc;
        --h1-fg-color: #bbbbda;
        --h2-fg-color: #9999aa;
        --code-fg-color: #f86060;
        --code-bg-color: #444444;
      }
      body {
        font-family: sans-serif;
        background-color: var(--page-bg-color);
        color: var(--page-fg-color);
      }
      h1 {
        color: var(--h1-fg-color);
      }
      h2 {
        color: var(--h2-fg-color);
      }
      p {
        font-size: 20px;
      } 
      code {
        font-size: 130%;
        color: var(--code-fg-color);
        background-color: var(--code-bg-color);
        padding: 2px;
      }

      <!-- https://www.w3schools.com/html/html_links_colors.asp -->
      a:link {
        color: green;
        background-color: transparent;
        text-decoration: none;
      }

a:visited {
  color: darkgray;
  background-color: transparent;
  text-decoration: none;
}

a:hover {
  color: red;
  background-color: transparent;
  text-decoration: underline;
}

a:active {
  color: yellow;
  background-color: transparent;
  text-decoration: underline;
}
    </style>
    <script>
      const prefersDarkMode = window.matchMedia('(prefers-color-scheme: dark)')

      function updateTheme() {
        const theme = prefersDarkMode.matches ? 'dark' : 'light'
        document.documentElement.setAttribute('data-theme', theme)
      }

      updateTheme();
      prefersDarkMode.addEventListener("change", () => updateTheme());
    </script>
  </head>
<head>
    <title>My Links</title>
    <style>
        table {
            border-collapse: collapse;
            width: 50%;
            margin: 20px auto;
            font-family: Arial, sans-serif;
        }
        th, td {
            border: 1px solid #999;
            padding: 8px;
            text-align: center;
        }
        th {
            <!-- background-color: #f2f2f2; -->
        }
        tr:nth-child(even) {
            <!-- background-color: #f9f9f9; -->
        }
    </style>
</head>
<body>
    <h2 style="text-align:center;">My Links</h2>
    <table>
"""

# Add header row
html += "        <tr>\n"
for header in rows[0]:
    html += f"            <th>{header}</th>\n"
html += "        </tr>\n"

# Add data rows
for row in rows[1:]:
    html += "        <tr>\n"
    html += f"            <td><a href=\"https://{row[0]}\" target=\"_blank\">{row[1]}</a></td>\n"
    html += f"            <td>{row[1]}</td>\n"
    html += "        </tr>\n"

# Close HTML
html += """
    </table>
</body>
</html>
"""

# Write to HTML file
with open("output.html", "w", encoding="utf-8") as f:
    f.write(html)

print("✅ HTML file created successfully: output.html")


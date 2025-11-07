#!/usr/bin/env python3

import csv
import argparse

parser = argparse.ArgumentParser(description="myLinks")
parser.add_argument('--csv', '-c', required=True, help='csv file. reference formatting in example.csv')
parser.add_argument('--out', '-o', required=True, help='html file to create')
args = parser.parse_args()

if args.csv:
    print("csv file:", args.csv)
else:
    print("No csv file provided.")

if args.out:
    print("html file:", args.out)
else:
    print("No html file provided.")


# Read the CSV file
with open(args.csv, newline='', encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    rows = list(reader)
    sorted_data = sorted(rows, key=lambda row: (float(row[2]), row[1]))

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
            width: 80%;
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
html += f"            <th><b>Link</b></th>\n"
html += f"            <th><b>Description</b></th>\n"
html += "        </tr>\n"

# Add data rows
for sorted_data in sorted_data[0:]:
    html += "        <tr>\n"
    html += f"            <td><a href=\"https://{sorted_data[0]}\" target=\"_blank\">{sorted_data[0]}</a></td>\n"
    html += f"            <td>{sorted_data[1]}</td>\n"
    html += "        </tr>\n"

# Close HTML
html += """
    </table>
</body>
</html>
"""

# Write to HTML file
with open(args.out, "w", encoding="utf-8") as f:
    f.write(html)

print("✅ HTML file created successfully:", args.out )


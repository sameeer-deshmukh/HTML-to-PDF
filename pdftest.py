import pdfkit

options = {
    'page-size': 'A5',
    'orientation': 'portrait',
    'margin-top': '0mm',
    'margin-right': '0mm',
    'margin-bottom': '0mm',
    'margin-left': '0mm'
}
config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')

# List of HTML strings for each page
html_page1 = """
<!DOCTYPE html>
<html>
<head>
    <title>Page 1</title>
</head>
<body>
    <h1>Page 1 Content</h1>
    <p>This is the content of page 1.</p>
</body>
</html>
"""

html_page2 = """
<!DOCTYPE html>
<html>
<head>
    <title>Page 2</title>
</head>
<body>
    <h1>Page 2 Content</h1>
    <p>This is the content of page 2.</p>
</body>
</html>
"""

html_page3 = """
<!DOCTYPE html>
<html>
<head>
    <title>Page 3</title>
</head>
<body>
    <h1>Page 3 Content</h1>
    <p>This is the content of page 3.</p>
</body>
</html>
"""

isPartsAdded = False

# Create and save individual PDFs for each page
file_names = ["page1.html", "page2.html"]
file_contents = [html_page1, html_page2]

if isPartsAdded:
    file_names = ["page1.html", "page2.html", "page3.html"]
    file_contents = [html_page1, html_page2, html_page3]

for file, content in zip(file_names, file_contents):
    with open(file, 'w') as f:
        # Write content to the file
        f.write(content)




pdfkit.from_file(["invoice_temp.html", "invoice_temp.html"], 'multi_page.pdf', options=options, configuration=config)


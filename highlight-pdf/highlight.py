import pymupdf

# PDF öffnen
doc = pymupdf.open("file.pdf")
search_text = "text"

# Jede Seite durchgehen
for page in doc:
    text_instances = page.search_for(search_text, quads=True)
    for inst in text_instances:
        page.add_highlight_annot(inst)

# Gespeichertes PDF
doc.save("save-file.pdf")

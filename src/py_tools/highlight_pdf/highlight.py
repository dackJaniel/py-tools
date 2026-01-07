import pymupdf


def highlight_pdf(
    file_path: str,
    search_text: str,
    save_path: str = "",
):
    doc = pymupdf.open(file_path)

    if not save_path:
        save_path = file_path.replace(".pdf", "_highlighted.pdf")

    # Jede Seite durchgehen
    for page in doc:
        text_instances = page.search_for(search_text, quads=True)
        for inst in text_instances:
            page.add_highlight_annot(inst)

    # Gespeichertes PDF
    doc.save(save_path)

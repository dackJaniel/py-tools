import typer

from .highlight import highlight_pdf

app = typer.Typer()


@app.command()
def main(
    i: str = typer.Option(..., "--i", help="Input PDF file"),
    e: str = typer.Option(None, "--e", help="Output PDF file"),
    str: str = typer.Option(..., "--str", help="Text to highlight"),
):
    try:
        """Highlight text in a PDF file"""
        highlight_pdf(file_path=i, search_text=str, save_path=e)
        typer.secho(
            f"✓ PDF erfolgreich erstellt: {e if e else i.replace('.pdf', '_highlighted.pdf')}",
            fg=typer.colors.GREEN,
        )
    except Exception as ex:
        typer.secho(f"✗ Fehler: {ex}", fg=typer.colors.RED, err=True)
        raise typer.Exit(code=1)


app.callback(invoke_without_command=True)(main)

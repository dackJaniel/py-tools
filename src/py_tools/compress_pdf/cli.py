from enum import Enum
from typing import Optional

import typer

from .compress import compress_pdf


class PdfQuality(str, Enum):
    screen = "screen"
    ebook = "ebook"
    printer = "printer"
    prepress = "prepress"
    default = "default"


app = typer.Typer()


@app.command()
def main(
    i: str = typer.Option(..., "--i", help="Input PDF file"),
    o: Optional[str] = typer.Option(
        None, "--o", help="Output PDF file (default: input_small.pdf)"
    ),
    quality: PdfQuality = typer.Option(
        PdfQuality.screen,
        "--quality",
        "-q",
        help="PDF quality setting (screen=lowest, ebook, printer, prepress, default=highest)",
    ),
):
    """Compress a PDF file using Ghostscript"""
    try:
        if o is None:
            o = i.replace(".pdf", "_small.pdf")

        compress_pdf(input_file=i, output_file=o, quality=quality.value)
        typer.secho(
            f"✓ PDF erfolgreich komprimiert: {o}",
            fg=typer.colors.GREEN,
        )
    except Exception as ex:
        typer.secho(f"✗ Fehler: {ex}", fg=typer.colors.RED, err=True)
        raise typer.Exit(code=1)


app.callback(invoke_without_command=True)(main)

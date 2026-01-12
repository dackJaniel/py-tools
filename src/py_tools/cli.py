import typer

from py_tools.compress_pdf import cli as compress_cli
from py_tools.highlight_pdf import cli as pdf_cli

app = typer.Typer(
    name="py-tools",
    help="Python CLI Tools",
)

app.add_typer(
    pdf_cli.app,
    name="pdf-h",
    help="Highlight text in a PDF file",
)

app.add_typer(
    compress_cli.app,
    name="pdf-c",
    help="Compress a PDF file using Ghostscript",
)


@app.command()
def main(tool: str):
    """Mein CLI Tool mit Typer"""
    typer.echo(f"Running {tool}...")


if __name__ == "__main__":
    app()

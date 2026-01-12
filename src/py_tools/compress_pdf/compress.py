import subprocess
from pathlib import Path


def compress_pdf(
    input_file: str,
    output_file: str | None = None,
    quality: str = "screen",
) -> str:
    """
    Compress a PDF file using Ghostscript.

    Args:
        input_file: Path to the input PDF file
        output_file: Path to the output PDF file. If None, uses input_file + _small.pdf
        quality: PDF quality setting. Options:
            - screen: lowest quality, smallest size (72 dpi)
            - ebook: medium quality (150 dpi)
            - printer: high quality (300 dpi)
            - prepress: highest quality, largest size (300 dpi, color preserving)

    Returns:
        Path to the compressed PDF file

    Raises:
        FileNotFoundError: If input file doesn't exist
        ValueError: If quality setting is invalid
        RuntimeError: If Ghostscript command fails
    """
    valid_qualities = ["screen", "ebook", "printer", "prepress"]
    if quality not in valid_qualities:
        raise ValueError(
            f"Invalid quality '{quality}'. Must be one of: {', '.join(valid_qualities)}"
        )

    input_path = Path(input_file)
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_file}")

    if output_file is None:
        output_file = str(input_path.with_suffix("")) + "_small.pdf"

    cmd = [
        "gs",
        "-sDEVICE=pdfwrite",
        f"-dPDFSETTINGS=/{quality}",
        "-dNOPAUSE",
        "-dQUIET",
        "-dBATCH",
        f"-sOutputFile={output_file}",
        str(input_file),
    ]

    try:
        subprocess.run(cmd, check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Ghostscript failed: {e.stderr}") from e
    except FileNotFoundError:
        raise RuntimeError(
            "Ghostscript (gs) not found. Please install it first."
        ) from None

    return output_file

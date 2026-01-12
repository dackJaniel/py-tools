# py-tools 🛠️

Eine Sammlung nützlicher Python CLI-Tools für den täglichen Gebrauch.

[![Python Version](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## ✨ Features

- **PDF Highlighting**: Durchsuche und markiere Text in PDF-Dateien automatisch
- **PDF Compression**: Komprimiere PDF-Dateien mit Ghostscript
- Weitere Tools folgen...

## 📦 Installation

### Option 1: pipx (Empfohlen für CLI-Tools)

`pipx` erstellt automatisch isolierte Umgebungen für jedes Tool und macht sie global verfügbar:

```bash
# pipx installieren (falls noch nicht vorhanden)
sudo apt install pipx  # Debian/Ubuntu
# oder: brew install pipx  # macOS
# oder: pip install --user pipx  # Windows/andere

pipx ensurepath

# py-tools installieren
pipx install git+https://github.com/danielhilmer/py-tools.git
```

### Option 2: uv (Schnell & Modern)

```bash
# uv installieren
curl -LsSf https://astral.sh/uv/install.sh | sh

# py-tools installieren
uv tool install git+https://github.com/danielhilmer/py-tools.git
```

### Option 3: pip mit Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
# oder: venv\Scripts\activate  # Windows

pip install git+https://github.com/danielhilmer/py-tools.git
```

### Option 4: pip --user

```bash
pip install --user git+https://github.com/danielhilmer/py-tools.git

# Stelle sicher, dass ~/.local/bin im PATH ist
export PATH="$HOME/.local/bin:$PATH"
```

### Installation von einem Release

```bash
pipx install https://github.com/danielhilmer/py-tools/releases/latest/download/py_tools-0.1.0-py3-none-any.whl
```

## 🚀 Verwendung

### PDF Compression

Komprimiere PDF-Dateien mit Ghostscript, um die Dateigröße zu reduzieren:

```bash
py-tools pdf-c --i="input.pdf"
```

**Parameter:**
- `--i`: Eingabe-PDF-Datei (erforderlich)
- `--o`: Ausgabe-PDF-Datei (optional, Standard: input_small.pdf)
- `--quality` / `-q`: Qualitätsstufe (optional, Standard: screen)

**Qualitätsstufen:**
- `screen`: Niedrigste Qualität, kleinste Dateigröße (72 dpi) - Standard
- `ebook`: Mittlere Qualität (150 dpi)
- `printer`: Hohe Qualität (300 dpi)
- `prepress`: Höchste Qualität, größte Dateigröße (300 dpi, farberhaltend)

**Beispiele:**

```bash
# Standard-Kompression (screen quality)
py-tools pdf-c --i="dokument.pdf"
# Erzeugt: dokument_small.pdf

# Mit benutzerdefiniertem Output-Namen
py-tools pdf-c --i="dokument.pdf" --o="komprimiert.pdf"

# Mit höherer Qualität
py-tools pdf-c --i="dokument.pdf" --quality ebook

# Kurze Option für Qualität
py-tools pdf-c --i="dokument.pdf" -q printer
```

**Voraussetzung:** Ghostscript (`gs`) muss installiert sein:

```bash
# Debian/Ubuntu
sudo apt install ghostscript

# macOS
brew install ghostscript

# Arch Linux
sudo pacman -S ghostscript
```

### PDF Highlighting

Durchsuche ein PDF nach bestimmten Text und markiere alle Vorkommen:

```bash
py-tools pdf-h --i="input.pdf" --str="Suchtext" --e="output.pdf"
```

**Parameter:**
- `--i`: Eingabe-PDF-Datei (erforderlich)
- `--str`: Text der gesucht und markiert werden soll (erforderlich)
- `--e`: Ausgabe-PDF-Datei (optional, überschreibt Input wenn nicht angegeben)

**Beispiele:**

```bash
# Einfaches Highlighting
py-tools pdf-h --i="dokument.pdf" --str="wichtig" --e="dokument_marked.pdf"

# Input-Datei überschreiben
py-tools pdf-h --i="dokument.pdf" --str="TODO"

# Mehrere Wörter suchen (mehrfache Ausführung)
py-tools pdf-h --i="in.pdf" --str="Fehler" --e="temp.pdf"
py-tools pdf-h --i="temp.pdf" --str="Warnung" --e="out.pdf"
```

### Hilfe anzeigen

```bash
# Allgemeine Hilfe
py-tools --help

# Hilfe für spezifisches Tool
py-tools pdf-h --help
```

## 🔧 Entwicklung

### Voraussetzungen

- Python 3.12+
- Poetry

### Setup

```bash
# Repository klonen
git clone https://github.com/danielhilmer/py-tools.git
cd py-tools

# Dependencies installieren
poetry install

# Im Development-Modus ausführen
poetry run py-tools --help
```

### Tests ausführen

```bash
poetry run pytest
```

### Paket bauen

```bash
poetry build
```

Die gebauten Pakete findest du in `dist/`:
- `py_tools-0.1.0-py3-none-any.whl`
- `py_tools-0.1.0.tar.gz`

## 📝 Update & Deinstallation

### Update

```bash
# Mit pipx
pipx upgrade py-tools

# Mit uv
uv tool upgrade py-tools

# Mit pip
pip install --upgrade git+https://github.com/danielhilmer/py-tools.git
```

### Deinstallation

```bash
# Mit pipx
pipx uninstall py-tools

# Mit uv
uv tool uninstall py-tools

# Mit pip
pip uninstall py-tools
```

## 🤝 Beitragen

Contributions sind willkommen! Bitte öffne ein Issue oder Pull Request.

## 📄 Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert.

## 👤 Autor

**Daniel Hilmer**
- Email: daniel.hilmer@outlook.de
- GitHub: [@danielhilmer](https://github.com/danielhilmer)

## 🐛 Probleme?

Wenn du auf Probleme stößt oder Fragen hast, öffne bitte ein [Issue](https://github.com/danielhilmer/py-tools/issues).

---

Made with ❤️ and Python
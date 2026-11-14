#!/usr/bin/env python3
"""Converte os manuais PDF do abnTeX2 em texto limpo para docs/manuais/*.md.

Uso: python3 scripts/pdf_to_md.py
Depende de pdftotext (poppler). Os PDFs ficam em abntex2/doc/.
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOC = ROOT / "abntex2" / "doc"
OUT = ROOT / "docs" / "manuais"

MANUAIS = {
    "abntex2": "A classe abntex2 (manual)",
    "abntex2cite": "O pacote abntex2cite (manual)",
    "abntex2cite-alf": "O pacote abntex2cite: estilo alfabético (manual)",
}

PAGE_NUMBER = re.compile(r"^\s*(?:\d{1,3}|[ivxlc]{1,6})\s*$", re.IGNORECASE)


def convert(name: str, title: str) -> str:
    raw = subprocess.run(
        ["pdftotext", "-layout", str(DOC / f"{name}.pdf"), "-"],
        check=True,
        capture_output=True,
        text=True,
    ).stdout

    pages = []
    for page in raw.split("\f"):
        lines = page.splitlines()
        # Remove numeração de página e linhas vazias nas bordas.
        while lines and (not lines[0].strip() or PAGE_NUMBER.match(lines[0])):
            lines.pop(0)
        while lines and (not lines[-1].strip() or PAGE_NUMBER.match(lines[-1])):
            lines.pop()
        pages.append("\n".join(lines))

    body = "\n\n".join(p for p in pages if p.strip())
    body = re.sub(r"\n{3,}", "\n\n", body).strip()

    header = (
        f"# {title}\n\n"
        f"> Texto extraído de `abntex2/doc/{name}.pdf` (abnTeX2 v-1.9.7) com\n"
        f"> `pdftotext -layout`; numeração de página removida. Preserva a quebra de\n"
        f"> linha do PDF, então palavras podem aparecer hifenizadas no fim da linha.\n"
        f"> Para regenerar: `python3 scripts/pdf_to_md.py`.\n\n"
    )
    return header + body + "\n"


def main() -> int:
    if not DOC.is_dir():
        sys.exit(f"diretório não encontrado: {DOC}")
    OUT.mkdir(parents=True, exist_ok=True)
    for name, title in MANUAIS.items():
        target = OUT / f"{name}.md"
        target.write_text(convert(name, title), encoding="utf-8")
        print(f"{target.relative_to(ROOT)} ({target.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

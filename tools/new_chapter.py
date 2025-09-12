#!/usr/bin/env python3
import sys, re
from pathlib import Path
from textwrap import dedent

ROOT = Path(__file__).resolve().parents[1]
CHAPTERS = ROOT / "chapters"

TEMPLATE_MD = """# {title}

> Remplis cette fiche depuis Obsidian puis colle-la ici.

## Concepts clés
- 

## Hypothèses / conditions
- 

## Formules utiles
- 

## Pipeline type
- Prétraitement → Modèle → Validation → Métriques

## Pièges & tips
- 

## Références (livre du prof)
- Pages : 
"""

CHEATSHEET = """#!/usr/bin/env python3
\"\"\"{title} — Cheatsheet exécutable\"\"\"
from textwrap import dedent
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parents[2] / "shared"))
from utils import section, bullet  # type: ignore

def main():
    section("{title}")
    print("Scaffold ok. Ajoute tes démos ici.")

if __name__ == "__main__":
    main()
"""

def main():
    if len(sys.argv) < 2:
        print("Usage: python tools/new_chapter.py \"14_new_topic\"")
        sys.exit(1)
    name = sys.argv[1].strip()
    # Normalize "14_new_topic"
    m = re.match(r"^(\d+)[-_](.+)$", name)
    if not m:
        print("Nom attendu: 'NN_slug' (ex: 14_new_topic)")
        sys.exit(2)
    num = int(m.group(1))
    slug = re.sub(r"\s+", "_", m.group(2).lower())
    folder = CHAPTERS / f"{num:02d}_{slug}"
    folder.mkdir(parents=True, exist_ok=False)
    title = re.sub(r"_", " ", slug).title()
    (folder / "notes.md").write_text(TEMPLATE_MD.format(title=title), encoding="utf-8")
    (folder / "cheatsheet.py").write_text(CHEATSHEET.format(title=title), encoding="utf-8")
    (folder / "cheatsheet.py").chmod(0o755)
    print(f"Created {folder}")

if __name__ == "__main__":
    main()

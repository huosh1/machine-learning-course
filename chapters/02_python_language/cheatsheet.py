#!/usr/bin/env python3
"""Python Language — Cheatsheet exécutable
But: garder une synthèse + micro-démos reproductibles.
"""
import sys
from pathlib import Path
from textwrap import dedent

# Permet d'importer shared/utils.py si on lance depuis le repo
sys.path.append(str(Path(__file__).resolve().parents[2] / "shared"))
from utils import bullet, section  # type: ignore


def demo():
    """Ajoute ici 1–3 petites démos minimalistes liées au chapitre."""
    section("Demo 1")
    print("Hello from Python Language!")


def theory_flash():
    section("Rappels théoriques (ultra-court)")
    print(
        dedent(
            """
    - Résume 3–5 points clés à retenir pour réviser vite.
    """
        )
    )


def main():
    section("Python Language")
    theory_flash()
    demo()


if __name__ == "__main__":
    main()

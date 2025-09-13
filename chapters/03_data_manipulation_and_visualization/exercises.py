#!/usr/bin/env python3
"""Data Manipulation And Visualization — Cheatsheet exécutable
But: garder une synthèse + micro-démos reproductibles.
"""
from textwrap import dedent
from pathlib import Path
import sys

# Permet d'importer shared/utils.py si on lance depuis le repo
sys.path.append(str(Path(__file__).resolve().parents[2] / "shared"))
from utils import section, bullet  # type: ignore

def demo():
    """Ajoute ici 1–3 petites démos minimalistes liées au chapitre."""
    section("Demo 1")
    print("Hello from Data Manipulation And Visualization!")

def theory_flash():
    section("Rappels théoriques (ultra-court)")
    print(dedent("""
    - Résume 3–5 points clés à retenir pour réviser vite.
    """))

def main():
    section("Data Manipulation And Visualization")
    theory_flash()
    demo()

if __name__ == "__main__":
    main()

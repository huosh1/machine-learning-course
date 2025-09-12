# Machine Learning Course — Structure des chapitres

Chaque chapitre contient :
- `notes.md` — ta fiche (rédigée dans Obsidian puis copiée ici)
- `cheatsheet.py` — démonstrations exécutables (mini-exemples, prints)

## Lancer un cheatsheet
```bash
python chapters/02_python_language/cheatsheet.py
```

## Environnement
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Ajouter un nouveau chapitre (outil)
```bash
python tools/new_chapter.py "14_new_topic"
```
Cela crée `chapters/14_new_topic` avec le squelette.

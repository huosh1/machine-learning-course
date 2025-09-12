# Chapitre 1 — Écosystème Python pour la Data Science

Ce chapitre présente l’écosystème Python utilisé en data science. Python n’est pas seulement un langage de programmation généraliste : il s’appuie sur un ensemble de bibliothèques spécialisées qui facilitent les calculs numériques, la manipulation de données et la visualisation.

## Bibliothèques principales

Plusieurs librairies sont incontournables dans ce domaine :

- **NumPy** : manipulation de vecteurs, matrices et calculs rapides. C’est la fondation sur laquelle reposent la plupart des autres outils.
- **SciPy** : bibliothèques scientifiques avancées (algèbre linéaire, statistiques, optimisation, décomposition en valeurs singulières…).
- **Pandas** : manipulation de données tabulaires (fichiers Excel, CSV, bases de données). Outil central pour organiser et explorer les datasets.
- **Matplotlib** : visualisation bas niveau, permettant de tracer des courbes, histogrammes et figures diverses.
- **Seaborn** : visualisation haut niveau, basé sur Matplotlib, avec un style orienté statistiques (boxplots, heatmaps, distributions).
- **Statsmodels** : statistiques avancées (modèles linéaires, séries temporelles, tests).
- **Scikit-learn** : cœur du machine learning classique (régressions, arbres de décision, SVM, clustering, pipelines).
- **PyTorch** : apprentissage profond (réseaux de neurones), complémentaire à scikit-learn.

## Environnement de développement

Un environnement Python typique comprend :

1. **Interpréteur Python** (ex. Python 3.x). Il exécute le code et le traduit en instructions machine.
2. **Éditeur de texte ou IDE**.  
   - Éditeurs légers : VS Code, Sublime Text, Atom.  
   - IDEs complets : PyCharm, Spyder, ou encore VS Code avec extensions Python.  
   (Dans certains cas, l’éditeur choisi est **Neovim**, qui reste minimaliste et léger, mais très efficace avec les bons plugins.)
3. **Gestionnaire de paquets**.  
   - `pip` : gestionnaire par défaut pour installer et mettre à jour les bibliothèques.  
   - `conda` : alternative populaire en data science, intégrant gestion des paquets et des environnements.  
   - `pixi` : outil récent et rapide, construit sur l’écosystème conda.
4. **Gestionnaire d’environnements virtuels**.  
   Les environnements isolés permettent de travailler sur plusieurs projets sans conflits de dépendances.  
   - `venv` (intégré à Python).  
   - `virtualenv` (alternative).  
   - `conda` et `pixi` (gèrent à la fois environnements et paquets).
5. **Système de versionnage**.  
   - Git est essentiel pour gérer l’historique du code et collaborer.  
   - GitHub, GitLab ou Bitbucket permettent d’héberger les dépôts.
6. **Débogueur**.  
   - Python intègre `pdb`.  
   - Les IDEs proposent souvent des interfaces graphiques pour déboguer (points d’arrêt, inspection des variables, pas à pas).
7. **Frameworks de tests**.  
   - `unittest` (intégré), `pytest`, ou `nose2` permettent d’automatiser les tests et d’assurer la qualité du code.
8. **Outils de documentation**.  
   - `Sphinx` ou `pdoc` génèrent automatiquement une documentation à partir des docstrings.
9. **Conteneurs (optionnel)**.  
   - Docker permet de créer des environnements reproductibles, utiles pour passer du développement à la production.

## Gestion des dépendances

Les projets de data science nécessitent souvent des versions spécifiques de bibliothèques. Pour éviter les conflits, il est recommandé de créer un environnement par projet.

Exemples :

- **venv** :
  ```bash
  python -m venv .venv
  source .venv/bin/activate
  pip install numpy pandas matplotlib

```

---
## Configuration personnelle

 **Arch Linux** avec le shell **fish**, et comme éditeur **Neovim** configuré avec **LazyVim**. J’ai choisi cette config parce qu’elle est légère, rapide et me permet de rester concentré uniquement sur le code.  

Pour apprendre, c’est parfait : je comprends mieux ce que je fais car je dois gérer moi-même mes environnements, mes dépendances et mes fichiers. Ça m’évite de cliquer dans des menus compliqués comme dans un IDE et je progresse plus vite en Python.  

En plus, Neovim avec LazyVim me donne quand même tout ce qu’il faut : autocomplétion, navigation dans le projet, intégration Git. Fish me simplifie la vie au terminal avec ses suggestions automatiques.  


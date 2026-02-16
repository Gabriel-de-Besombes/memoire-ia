# Contexte du Projet : Mémoire d'Actuariat (IA & ALM)

Ce fichier définit le contexte, la structure et les conventions à respecter pour la rédaction et le développement de ce mémoire d'actuariat.

## 1. Vue d'ensemble
**Sujet :** Optimisation des temps de calcul des modèles de Gestion Actif-Passif (ALM) via des techniques d'agrégation du passif (*Model Points*), sans compromettre la fidélité des indicateurs de risque Solvabilité II.
**Contexte :** Assurance Vie Épargne (Fonds Euros & Unités de Compte) en France.
**Problématique :** Comment concilier rapidité de calcul et précision des indicateurs prudentiels (Best Estimate, SCR, PVFP) dans un contexte industriel ?
**Outils :** Python (Générateur, Modèle ALM, Agrégation), LaTeX (Rédaction).

## 2. Structure du Mémoire
Le mémoire est structuré en 4 chapitres principaux (correspondant aux fichiers `.tex` actuels), précédés d'un préambule (Introduction, Résumé, etc.) et suivis d'une conclusion.

*   **Chapitre 1 : Contexte réglementaire et Principes ALM** (`chapitre1.tex`)
    *   **Contenu :** Présentation de l'assurance vie épargne (cycle inversé), du cadre Solvabilité II, des Générateurs de Scénarios Économiques (GSE) en univers risque neutre.
    *   **ALM :** Explication des principes de la Gestion Actif-Passif et de l'architecture générale du modèle de projection utilisé (interactions actif-passif, stratégie d'investissement, PB).

*   **Chapitre 2 : Construction du Générateur de Portefeuilles** (`chapitre2.tex`)
    *   **Objectif :** Créer des données synthétiques réalistes pour pallier l'absence de données clients (confidentialité).
    *   **Contenu :** Méthodologie de génération, calibration sur données de marché (Insee, etc.), utilité pour le *benchmarking* et les tests de nouveaux produits.

*   **Chapitre 3 : Protocole d'Analyse & Sélection de l'Agrégation** (`chapitre3.tex`)
    *   **Objectif :** Comparer différentes méthodes de réduction de dimension (agrégation).
    *   **Méthodes :** Comparaison entre l'approche "Grid-based" (regroupement par caractéristiques : Âge, Sexe, TMG...) et les méthodes de Clustering (K-Means, HAC...).
    *   **Critères :** Distance sur les indicateurs S2, temps de calcul, compression.

*   **Chapitre 4 : Analyse de Sensibilité & Résultats** (`chapitre4.tex`)
    *   **Objectif :** Valider la robustesse de la méthode retenue.
    *   **Contenu :** Application de chocs (Taux, Actions, Rachats...) sur portefeuilles agrégés vs granulaires. Analyse des écarts sur le SCR et le BE. Validation de l'approche pour un usage industriel.

## 3. Style et Conventions de Rédaction

### Ton et Niveau de Langue
*   **Académique et Formel :** Utiliser un registre soutenu mais pas trop pompeux, ça doit pouvoir être écrit avec des mots qui ne font pas IA.
*   **Impersonnel :** Privilégier la voix passive ("Il a été démontré que...", "Cette analyse permet de..."). **Jamais de "Je" ou de "Nous" ou de "on"**.
*   **Clarté :** Phrases structurées, vocabulaire précis. Éviter les tournures familières ou trop orales.

### Terminologie Spécifique
*   **Utiliser :** "Provision Mathématique" (PM), "Best Estimate" (BE), "Solvency Capital Requirement" (SCR), "Unités de Compte" (UC), "Fonds Euros", "Participation aux Bénéfices" (PB), "Model Point" (MP).
*   **Éviter :** Termes anglais non standards si un équivalent français précis existe (sauf pour les termes consacrés comme "Best Estimate" ou "SCR" qui sont standards dans la profession), toujours utilser Model Point et jamais Point de Modèle.
*   **Mathématiques :** Les formules doivent être rigoureusement formatées en LaTeX.

### Conventions Techniques (LaTeX)
*   **Figures :** Placer les images dans le dossier `images/` (ou sous-dossiers). Utiliser l'environnement `figure` avec `\caption` et `\label`.
*   **Références :** Utiliser `\cite{cle_biblio}` pour la bibliographie et `\ref{label}` pour les renvois internes.
*   **Structure :** Respecter la hiérarchie `\chapter`, `\section`, `\subsection`, `\subsubsection`. Ne pas abuser des niveaux inférieurs.

### Proposition de graphiques à insérer
*   **Graphiques proposés :** Propose des graphiques explicatifs à insérer dans le mémoire dans les différentes parties, les graphiques devront être gérés comme présenté ci-dessus en allant piocher du contenu de `images/` même si l'image ne sera pas encore présente je me chargerai de l'ajouter ultérieurement 
*   **Références :** Propose des sources où je pourrai aller chercher les graphiques que tu me proposes ou des méthodos pour les faire
*   **Structure :** Essaye de suivre toujours la même structure pour implémenter les graphiques

## 4. Points d'Attention
*   **Cohérence :** Vérifier que les notations mathématiques sont uniformes tout au long du document.
*   **Graphiques :** Les graphiques (issus de Python/Excel) doivent être lisibles, titrés et légendés.
*   **Plagiat :** Tout contenu externe doit être reformulé et cité.

Ce fichier servira de référence pour toute tâche de rédaction ou de modification du code LaTeX.

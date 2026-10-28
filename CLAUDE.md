# SMP1_26 – Stochastic Modelling and Processes

Kursusside (engelsk) for valgfaget SMP1. SMP1 bærer den dybere sandsynlighedsteori, simultane fordelinger, stokastiske processer, tidsrækker, Markov-kæder og simulering, som STA1 bevidst ikke dækker.

## Struktur

- Sessioner `00_Prerequisites` til `11_Autoregressive_Models_Forecasting_and_Course_Recap`. Hver session er én `README.md` med Key Concepts, Session Preparation, links og Exercises (`#### Exercise N — Titel`).
- Ingen Tutorial-filer som i STA1_26. Undervisningsnotebooks og slides lægges direkte i sessionsmappen og linkes med `{ download }`, fx `SMP1_26_session06_live_lecture.ipynb`.
- Litteratur: primært probabilitycourse.com (links pr. afsnit). Recap-noter ligger på Google Drive; generelle ressourcer på SharePoint (link i nav).
- `01_Probability_Foundations_and_Random_Variables/` er en tom, ikke-tracket mappe; sessionen i nav er `01_Probability_Foundations/`.

## Konfiguration, der afviger fra den globale opsætning

- Ingen `mkdocs-jupyter`: notebooks renderes ikke som sider, de tilbydes kun som download.
- `requirements.txt` indeholder ikke selve `mkdocs` (det kommer med mkdocs-material).

## Lokalt og ikke publiceret

- `tools/`, `output/`, `tmp/` og `media/` er git-ignoreret. `tools/` og `output/`/`tmp/` er også udelukket fra bygget.
- `manim/smp_intro.py` er tracket i git (modsat STA1_26, hvor `manim/` er privat).
- `.sta_draft/` er en tom lokal mappe.
- `C:\GitHub\SMP1_26_build_check` er en separat byggekonfiguration, der peger på dette repository.

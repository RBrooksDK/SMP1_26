# SMP1_26 – Stochastic Modelling and Processes

Kursusside (engelsk) for valgfaget SMP1. SMP1 bærer den dybere sandsynlighedsteori, simultane fordelinger, stokastiske processer, tidsrækker, Markov-kæder og simulering, som STA1 bevidst ikke dækker.

## Start her

Denne fil beskriver konventionerne, så du ikke behøver at læse mkdocs.yml og flere hele sessioner for at finde stilen.

- Læs kun den session, opgaven gælder. Læs nabosessionerne kun, hvis det drejer sig om progression eller henvisninger.
- List aldrig repoet rekursivt fra roden. Spring over `_site/`, `.git/`, `.venv-manim/`, `media/`, `manim/media/`, `tmp/`, `output/` og `figures/` (store binære filer), medmindre opgaven gælder netop dem.
- Rækkefølge: 07 Poisson-processer, 08–09 Markov-kæder, 10–11 tidsrækker og AR-modeller med kursusrecap. Middelværdi- og kovariansfunktioner for processer hører til session 10, ikke 07. Residualtjek og estimation af AR-koefficienter er taget ud.

## Modelvalg

Før du går i gang med en opgave, der kræver værktøjer eller filer, skriver du én linje: "Anbefalet model: Opus/Sonnet – begrundelse". Ved korte spørgsmål og dialog springer du linjen over. Foreslår du en opfølgende opgave, skriver du også, hvilken model den bør køres med. Gå i gang med opgaven uden at vente på svar, medmindre modelvalget gør en tydelig forskel.

- **Opus**: nyt matematisk indhold, læsemateriale, eksamens- og øvelsesopgaver (Wiseflow), faglig sparring om notation og progression, kontrol af beregninger.
- **Sonnet**: GoodNotes-noter når indholdet ligger fast, mkdocs-nav og sessionsstruktur, kørsel og små rettelser af eksisterende figur- og Manim-scripts, omdøbning, oprydning, formatering.
- **Haiku**: bruges ikke i dette projekt.

## Struktur

- Sessioner `00_Prerequisites` til `11_Autoregressive_Models_Forecasting_and_Course_Recap`. Hver session er én `README.md`. Navigationen står i `mkdocs.yml` under `nav: Sessions`, og oversigten med rytme og progression står i `Sessions/README.md`. Begge opdateres, når en session tilføjes eller omdøbes.
- Ingen tutorial-filer som i STA1_26. Undervisningsnotebooks og PDF'er lægges direkte i sessionsmappen og linkes med `{ download }`.
- Billeder til opgaver ligger i `<session>/src/`.
- Litteratur: primært probabilitycourse.com med links pr. afsnit. Session notes og recap-noter ligger på Google Drive, generelle ressourcer på SharePoint (link i nav).

## Sessionsside-skabelon

Rækkefølgen er som i `07_Stochastic_Processes_and_Poisson_Processes/README.md`:

1. Front matter med `tags:` (3–5 emner).
2. `<h1 align="center">Titel</h1>`.
3. To korte introafsnit. Det første kobler til den forrige session.
4. `#### Key Concepts`: punktliste med substantiver.
5. `!!! tip "Learning Objectives"`: 3–5 punkter, der starter med et verbum (Describe, Calculate, Identify, Simulate).
6. `<hr/>`, derefter `### Session Preparation:` med én sætning, der linker relativt til tidligere sessioner (`../01_Probability_Foundations/README.md`).
7. `**Syllabus and input**`: links til probabilitycourse.com-afsnit.
8. `**Session material**`: Drive-links til "Recap and exercise notes" og "Session notes", eller download-links.
9. `<hr/>`, derefter `### Exercises`.
10. `#### Exercise N — Titel` (tankestreg), en kort kontekst, nummererede delspørgsmål og `??? answer` med et kort svar (indrykket fire mellemrum). Simuleringsopgaver kan stå uden svar.

Delspørgsmål skrives som almindelig nummereret Markdown (`1.`, `2.`, …). `stylesheets/extra.css` viser alle `ol` i indholdet som a, b, c (`.md-content ol { list-style-type: lower-alpha; }`), så der skal ikke være `<style>` på siderne. Det gælder alle nummererede lister på sitet, også dem, der ikke er delspørgsmål.

## Notation

- Følg Pishro-Nik og de eksisterende sessioner. Indfør ikke ny notation uden at spørge.
- Fordelinger skrives med `\operatorname{}`: `\operatorname{Poisson}(\lambda)`, `\operatorname{Binomial}(n,p)` og `\operatorname{Gamma}(k,\lambda)` med form og rate. Det samme gælder `\operatorname{Cov}(X,Y)`.
- `E[X]`, `P(\cdot)`. Tælleproces `N(t)`, ankomsttider `T_n`, rate `\lambda` pr. tidsenhed. Markov-kæder: tilstandsrum `S`, overgangsmatrix `P`, overgangssandsynligheder `p_{ij}`, stationær fordeling `\pi`.
- Matematik på sessionssider: `\(…\)` inline og `\[…\]` display. Brug ikke `$…$` eller `$$…$$`. Sessionerne 03, 04, 05 og 08 bruger stadig `$`, og de rettes ved lejlighed.

## Sprog og stil

- Engelsk med britisk stavemåde (behaviour, realisation, modelling). Ingen emojis.
- Intuition først, derefter formalisme. Simulering før det analytiske resultat, hvor det giver mening.
- Statistisk inferens (estimation, test, regression) hører til STA1. Fordelinger og CLT behandles her ud fra modellering og simulering.
- Kopiér aldrig opgaver eller tekst fra lærebøgerne. Henvis til afsnit.
- Python: NumPy, SciPy, pandas, Matplotlib. Figurer genereres med scripts i `tools/` (fx `tools/session10_11_make_figures.py`).

## Materialetyper

- **GoodNotes-noter** (sessions- og recapnoter): LaTeX i `tools/goodnotes/sessionNN/` eller `recapNN/`. Kurset bruger `tools/goodnotes/goodnotes_style.tex`, som henter den fælles stil og Caveat-fontene fra `C:\GitHub\claude-setup\goodnotes`. Metoden står i `C:\GitHub\claude-setup\session-notes-metode.md`. I gennemregnede eksempler er venstresiden fortrykt, og kun udregning og resultat er markeret.
- **Læsemateriale** (sessioner uden pensum): kapitelstil med mange eksempler, ikke i stil med session notes. LaTeX i `output/pdf/` med `bookstyle.tex`. Den færdige PDF kopieres til sessionsmappen som `SMP1_26_chapterNN_<emne>.pdf`.
- **Filnavne**: `SMP1_26_sessionNN_<indhold>.{tex,pdf,ipynb}`.
- Slides bruges ikke efter session 06. De studerende foretrækker håndskrevne noter.

## Build

- CI (`.github/workflows/ci.yml`) kører `mkdocs build --strict` og `mkdocs gh-deploy` ved push til `main`. Test lokalt med `mkdocs build --strict` før commit.
- `C:\GitHub\SMP1_26_build_check` er en separat byggekonfiguration, der peger på dette repository.

## Konfiguration, der afviger fra den globale opsætning

- Ingen `mkdocs-jupyter`: notebooks renderes ikke som sider, de tilbydes kun som download.
- `requirements.txt` indeholder ikke selve `mkdocs` (det kommer med mkdocs-material).

## Lokalt og ikke publiceret

- `tools/`, `output/`, `tmp/` og `media/` er git-ignoreret. `tools/`, `output/` og `tmp/` er også udelukket fra bygget.
- `manim/smp_intro.py` er tracket i git (modsat STA1_26, hvor `manim/` er privat).

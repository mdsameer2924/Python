# Python Learning Repository — Project Summary

> **Repo:** `git@github.com:mdsameer2924/Python.git` (remote `python`, branch `main`)
> **Local path:** `/home/sameer/Documents/Work/Learning/python`
> **Type:** Personal Python learning / practice monorepo — ~35x `.py` files, 4x `.md`, 1x `.tldr`
> **Environment:** `linux` + `.venv` (Python 3.14)
> **Latest commit:** `7897d5b inheritance is the concept covering right now`

This repo is **not a deployable app/library**. It is a **learn-by-doing notebook in file form**: small runnable scripts + lecture notes tracking a beginner to intermediate Python journey, currently focused on **OOP (Classes, Constructors, Encapsulation, Inheritance, Polymorphism)** and starting **Stdlib modules (`sys`, `os`, `shutil`, `subprocess`, `argparse`, exceptions)**.

## 1. At-a-Glance

| Area | Path | What it does |
| ------ | ------ | -------------- |
| Lecture-style OOP | `oopslecture/` | Clean commented examples + README notes for Class/Object, Constructors, Inheritance |
| Practice-style OOP | `pythonoops/` | 20+ exercises: Class/Constructor, Encapsulation, Inheritance, Polymorphism |
| Stdlib 6 modules | `6md/` | Scaffold for 6 topics: `firstSys` (`sys.argv`), `secOs`, `thirShutil`, `fsubprocess`, `argeparse`, `pexcept2` — only `firstSys` has code |
| Custom module demo | `sameer/muzan.py` + `usemodule.py` | How to create + `import` own package (`table()`, `vote_eligiblity()`, `add()`) |
| Entry demo (broken) | `main.py` | Tries `import oops.Encapsulation...` — path does not exist, good import-path lesson |
| Design notes | `dry_principal.tldr` | tldraw whiteboard JSON (DRY principle diagram), not code |
| Editor notes (misplaced) | `pythonoops/polymorphism/practice/README.md` | Actually NVIM cheatsheet, not polymorphism docs |

## 2. Directory Tree (excludes `.venv`/`.git`)

```
.
├── 6md/
│   ├── argeparse/      # empty — planned argparse
│   ├── firstSys/first.py + practice/fques.py  # sys.argv basics
│   ├── fsubprocess/ pexcept2/ secOs/ thirShutil/  # empty scaffolds
├── oopslecture/
│   ├── Class and object/Oops.py + README.md + readme.md (duplicate notes)
│   ├── Constructor and attrib types/construct.py + typesofma.py + README.md
│   └── Inheritance/inheri.py + bagfactory.py + multipleinheritance.py (stub)
│       └── practice/predict1.py (MRO diamond D(B,C))
├── pythonoops/
│   ├── class.py, methodd.py, predict.py, revision.py (BankAccount kata spec)
│   ├── Class object constructor/q1.py (Student), q2.py (Rectangle),
│   │   q3.py (BankAccount), book_author.py, car speed tracker.py
│   ├── Encapsulation/encap.py, emp_salary_ctrl.py, bank_simulation.py,
│   │   better approach/bank_simulation.py, q1.py (Temperature)
│   ├── Inheritance/1.py (Employee->manager), 2.py (Vehicle->ElectricCar), inheri.py
│   └── polymorphism/poly.py, duc.py, ducktype.py, method_overloading.py
│       └── practice/1.py (notification broadcast) + README.md (nvim notes)
├── sameer/muzan.py
├── main.py + usemodule.py
└── dry_principal.tldr
```

## 3. Concepts Covered

### 3.1 OOP — `oopslecture` (theory + minimal demos)

- **Class & Object:** blueprint vs instance, `ob = Car()`, `obj.attr` vs `obj.method()`, PascalCase.
- **Constructor & Attributes:** `__init__` (dunder/magic), class attrs vs instance attrs, `self`.
- **Method types:** instance, `@classmethod`, `@staticmethod` (`typesofma.py`).
- **Inheritance:** single (`Employee(Human)`), multi-level (`Campus(Rebook(BagFactory))`), multiple (stub), `super().__init__()`, overriding, private `__age` + getter/setter, MRO demo.

### 3.2 OOP — `pythonoops` (practice, task prompt in comments)

- **Class/Constructor:** `Student`, `Rectangle(area/perimeter)`, `BankAccount(deposit)`, `Book(get_summary)`, `Car(accelerate/brake floor 0)`.
- **Encapsulation:** `__balance/__salary/__pin/__celsius` + getters/setters with validation (positive, absolute-zero -273.15, PIN+funds). `better approach/` is cleanest exemplar.
- **Inheritance:** `Animal->Dog`, `Employee->manager`, `Vehicle->ElectricCar` via `super()`.
- **Polymorphism:** duck-typing (`use_bird`, `tool`, `animal`, `broadcast`), simulated overloading via defaults + `*args` (no true overloading in Python).
- **Drills:** `predict.py`, `revision.py` (spec only, no solution yet), notification system.

### 3.3 Stdlib + Modules — `6md`, `sameer`, root

- `sys`: `sys.argv[0]`, `len(sys.argv)`, loop args, `sys.version` (`6md/firstSys/`). `os`/`shutil`/`subprocess`/`argparse`/exceptions folders exist but empty.
- Custom packages: `import sameer.muzan as muzan; muzan.table(4)` pattern.
- Broken import example: `main.py` shows mismatch (`oops` vs `pythonoops`).

## 4. How to Run

```bash
cd /home/sameer/Documents/Work/Learning/python
source .venv/bin/activate
python "oopslecture/Class and object/Oops.py"
python "oopslecture/Constructor and attrib types/construct.py"
python "oopslecture/Inheritance/bagfactory.py"
python "pythonoops/Class object constructor/q1.py"
python pythonoops/Encapsulation/encap.py
python "pythonoops/Encapsulation/better approach/bank_simulation.py"
python pythonoops/polymorphism/poly.py
python pythonoops/polymorphism/method_overloading.py
python usemodule.py
python 6md/firstSys/first.py deploy --force
```

> Quote paths with spaces. `practice/1.py` under Class-constructor is empty. `main.py` fails (`No module named 'oops'`).

## 5. Gaps & Known Issues

- Empty scaffolds: `6md/secOs`, `thirShutil`, `fsubprocess`, `argeparse`, `pexcept2` + `Class object constructor/practice/1.py` (0 lines).
- Duplicates: `Class and object/README.md` vs `readme.md`; NVIM notes misplaced under `polymorphism/practice/`.
- Bugs: `oopslecture/Inheritance/inheri.py:10` calls `get_age()` not `self.get_age()`; `__init__` uses undefined `gender`; `typesofma.py` has unused `from re import purge`.
- Style: print-heavy, no tests, no `requirements.txt`, filenames with spaces.

## 6. Suggested Next Steps

1. Fix `main.py` import to `pythonoops.Encapsulation.bank_simulation`.
2. Finish `multipleinheritance.py` + `revision.py` BankAccount solution.
3. Fill `6md` empty folders with one minimal runnable each.
4. Move NVIM cheatsheet to `notes/nvim.md`, dedupe Class/Object READMEs.

---
*Generated 2026-10-11 by full repo walk (tree + read of all `.py`/`.md`, git log/status). Excludes `.venv`/`.git`; `dry_principal.tldr` summarized from JSON structure.*

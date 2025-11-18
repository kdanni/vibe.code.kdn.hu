# vibe.code.kdn.hu

***vibi'n?  Yes, we are vibi'n!*** 🚀  

>What kind of app or script should we vibe code today? Give me the high-level idea, the "vibe," and I'll help with the execution.

----

# 🧘 Vibe Code Repository: The Art of Intentional Imperfection

![Vibe Status](https://img.shields.io/badge/Vibe_Status-Immaculate-green.svg)
![Code Quality](https://img.shields.io/badge/Code_Quality-Subjective-lightgrey.svg)
![LLM Used](https://img.shields.io/badge/LLM_Focus-GPT_4o%20%7C%20Claude_3.5-blueviolet.svg)

---

## 🔮 What is Vibe Coding?

Welcome to the future of software development, popularized by Andrej Karpathy. **Vibe Coding** is the philosophy that the human programmer’s job is no longer to be a meticulous compiler—writing perfect syntax, managing state, and handling boilerplate—but to be the **Vibe Director**.

As a programmer, you know the technology, but you're too busy/important to write the mundane code. Your job is to describe the intent, the desired outcome, and the high-level **"vibe"** of the application, and then let the Large Language Model (LLM) generate the implementation.

**The Focus Shift:**
| Old Way (2023) | New Way (Vibe Coding) |
| :--- | :--- |
| **How** to implement feature X | **What** feature X should *do* and *feel* like |
| Fixing semicolons and indentation | Fixing the core logic of the prompt |
| Local memory management | Global application flow (the 'Vibe') |

---

## 🗑️ The Vibe Code Philosophy: Embrace the Slop

We accept that AI-generated code, often called **"slop,"** might be verbose, redundant, or inefficient. This repository operates under one guiding principle:

> **If it compiles, runs, and delivers the intended vibe, it is production-ready Vibe Code.**

The goal is to optimize for **developer time** and **rapid iteration (the OODA loop)**, not for lines of code or Cyclomatic Complexity. We don't care about the function signature; we care about the functional output.

---

## 🛠️ Repository Structure

This repository is structured to demonstrate the full Vibe Coding workflow:

### 1. `/prompts`
Contains the **true source code**—the Natural Language Prompts we used. These are the highly descriptive, context-setting, "Vibe-Setting" instructions given to the LLM.

New prompts should start from `prompts/prompt_template.md` and be stored with a unique ID (for example `p001_basic_cli_tool.md`).

* `prompts/p001_basic_cli_tool.md`: *Vibe: "A Python CLI tool that takes a CSV, checks for missing email fields, and outputs a clean JSON file. It should look professional, with clear error messages."*

### 2. `/slop`
This directory holds the raw, **unfiltered AI output** generated directly from the corresponding prompt. This is the code that we accept as long as it works. (Yes, it might be ugly.)

Store generated artifacts next to their prompt ID (e.g., `slop/p001_basic_cli_tool.py`). Use the quick checklist in `slop/README.md` to confirm the vibe before committing.

* `slop/p001_basic_cli_tool.py`: *The generated Python file.*

### 3. `/results`
A short README or image showing the final, successful execution and result of the Vibe Code. This is proof that the Vibe was achieved.

Use `results/result_template.md` to document proof that each artifact runs and meets the success criteria.

* `results/p001_cli_output.md`: *Showing the successful terminal run.*

---

## 🤝 Join the Vibe

Want to try your hand at programming by intent?

1.  **Select a Project Vibe:** Think of a small utility or function you need, but don't want to type out.
2.  **Write the Prompt:** Craft the most expressive, high-context prompt you can in the `/prompts` folder.
3.  **Generate the Slop:** Use your favorite LLM (or editor with Copilot/Cursor) to generate the code. Place it in `/slop`.
4.  **Confirm the Vibe:** Run the code and document the result in `/results`.
5.  **Submit a PR:** Share your beautiful mess with the world!

Let the LLM handle the typing. You handle the **Vibe**.

***
*Built with zero effort and maximum intent.*

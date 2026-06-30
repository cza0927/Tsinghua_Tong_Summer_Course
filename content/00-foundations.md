# 00 · Foundations & Coding

## Overview

Before touching any frontier model, you need a working toolchain and a mental model of how neural
networks learn. This module gets everyone to the same starting line: a reproducible Python
environment, comfort with Git and the Linux command line, the ability to typeset reports in LaTeX,
and a from-scratch understanding of the building block behind essentially every modern AI system —
the **Transformer**. Treat this as the prerequisite for all four pillars that follow; if you are
already fluent here, skim and move on.

## Learning Path

**Environment & tooling** *(Introductory)*
1. Linux command line — [The Missing Semester of Your CS Education (MIT)](https://missing.csail.mit.edu/) (lectures 1–4 cover shell, editors, data wrangling, git).
2. Git & GitHub — [Git tutorial](https://git-scm.com/docs/gittutorial), [GitHub Skills](https://skills.github.com/), [GitHub Student Developer Pack](https://education.github.com/pack).
3. Python environments — [`uv`](https://docs.astral.sh/uv/) (fast, modern) or [Miniconda](https://docs.conda.io/projects/miniconda/); create one isolated env per project.
4. Editor — [VS Code](https://code.visualstudio.com/) with the Python, Jupyter, and Git extensions.

**Math refresher** *(Introductory)* — only what you need, on demand.
5. Linear algebra — [3Blue1Brown: Essence of Linear Algebra](https://www.3blue1brown.com/topics/linear-algebra).
6. Probability & calculus — the appendix chapters of *Dive into Deep Learning* (below).

**Deep learning** *(Introductory → Intermediate)*
7. [*Dive into Deep Learning* (d2l.ai)](https://d2l.ai/) — interactive textbook with PyTorch code; read ch. 1–5.
8. [Andrej Karpathy — Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html) — build backprop, an MLP, and a GPT from scratch. **The single best on-ramp to this course.**
9. [PyTorch — Learn the Basics](https://pytorch.org/tutorials/beginner/basics/intro.html).

**The Transformer** *(Intermediate)*
10. [The Illustrated Transformer (Jay Alammar)](https://jalammar.github.io/illustrated-transformer/) — visual intuition.
11. [The Annotated Transformer (Harvard NLP)](https://nlp.seas.harvard.edu/annotated-transformer/) — paper as runnable code.

## Programming Exercises

1. **Environment setup.** Create a virtual env, install PyTorch, and run a Jupyter notebook locally
   *and* on [Google Colab](https://colab.research.google.com/). Commit a notebook that prints your
   PyTorch + CUDA versions and runs one tensor operation on GPU (if available).
2. **micrograd → makemore.** Work through Karpathy's first two videos and reproduce `micrograd`
   (a tiny autograd engine) and a character-level language model. Push your code to your repo.
3. **Train nanoGPT.** Clone [nanoGPT](https://github.com/karpathy/nanoGPT) and train the
   character-level Shakespeare model end to end; report your final loss and a few generated samples.
4. **LaTeX CV.** Write a one-page professional CV in LaTeX on [Overleaf](https://www.overleaf.com/)
   and export to PDF. (Reuse this LaTeX setup for every report in this course.)

## Paper Reading

- **A. Vaswani et al. (2017), "Attention Is All You Need," NeurIPS.** The Transformer. Read it after
  the two tutorials above — everything in modules 01–04 descends from this paper.
- *(Historical, optional)* **D. Rumelhart, G. Hinton, R. Williams (1986), "Learning representations
  by back-propagating errors," Nature.** Where backpropagation comes from.

## Tools & Setup

| Tool | Use | Link |
|---|---|---|
| `uv` / conda | Python environment management | [uv](https://docs.astral.sh/uv/) · [conda](https://docs.conda.io/) |
| PyTorch | Deep learning framework (used throughout) | [pytorch.org](https://pytorch.org/get-started/locally/) |
| VS Code | Editor with Jupyter + Git | [code.visualstudio.com](https://code.visualstudio.com/) |
| Google Colab | Free GPU notebooks | [colab.research.google.com](https://colab.research.google.com/) |
| Overleaf | Online LaTeX for reports & CV | [overleaf.com](https://www.overleaf.com/) |
| Hugging Face | Models, datasets, libraries hub | [huggingface.co](https://huggingface.co/) |

> **Hardware note:** a laptop is enough for setup, nanoGPT-char, and most exercises. For the larger
> jobs in later modules, use Colab, a department GPU, or the course server (details on Web Learning).

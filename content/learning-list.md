# Learning List / Homework · 通用人工智能系统平台I

This page is the student-facing learning and homework list. The homework items marked **Archive
homework** are carried over from the previous BIGAI learning-list PDF, then lightly adapted to the
current course.

## Submission Convention

- Homework is submitted through the course GitHub organization/repository unless otherwise announced.
- Each student should keep one personal working repository and one submitted pull request per assigned task.
- Reports should be written in LaTeX and committed together with source code when relevant.
- For external university assignments, follow the spirit of the task and cite the original course page; do not submit copied solutions.

## Day 1-2 · Shared Foundations

### Learning Resources

- Linux shell, editors, Git: [MIT The Missing Semester of Your CS Education](https://missing.csail.mit.edu/).
- GitHub workflow: [GitHub Skills: Introduction to GitHub](https://skills.github.com/).
- Python environment and Jupyter: [CS231n software setup](https://cs231n.github.io/setup-instructions/).
- PyTorch basics: [PyTorch Learn the Basics](https://pytorch.org/tutorials/beginner/basics/intro.html).
- LaTeX writing: [Overleaf Learn LaTeX](https://www.overleaf.com/learn) and [Overleaf CV templates](https://www.overleaf.com/gallery/tagged/cv).

### Homework

1. **Archive homework: CS131 environment setup.** Follow the spirit of the CS131 homework guideline:
   set up a Python environment, run a Jupyter notebook locally or on Colab, review Python/NumPy
   notebooks if needed, clone a CS131 homework repository, and install its packages.
   Reference: [StanfordVL CS131 released assignments](https://github.com/stanfordvl/cs131_release).
2. **GitHub repository practice.** Fork/clone the course starter repository, create a branch named
   `day1-<student-id>`, add a short `README.md`, commit at least twice, push the branch, and open a
   pull request.
3. **Environment check notebook.** Create a notebook that prints Python, PyTorch, CUDA/MPS
   availability, and runs one tensor operation. Commit both the notebook and a dependency file.
4. **Archive homework: LaTeX CV.** Prepare a one-page professional CV using LaTeX. Commit the `.tex`
   source and compiled PDF, push to the shared repository, and write a short email draft to a
   potential supervisor using appropriate academic email etiquette.

## Direction A · Foundation Models and NLP

### Learning Resources

- NLP API reference: [Hugging Face Transformers documentation](https://huggingface.co/docs/transformers).
- Practical library path: [Hugging Face LLM Course](https://huggingface.co/learn/llm-course).
- University course path: [Stanford CS224N](https://web.stanford.edu/class/cs224n/) and
  [Stanford CS336: Language Modeling from Scratch](https://stanford-cs336.github.io/spring2024/).
- Code-first tutorial: [The Annotated Transformer](https://nlp.seas.harvard.edu/annotated-transformer/).

### Homework

1. **Archive homework: CS224N Assignment 1.** Play with Jupyter Notebook and finish the word-vector
   assignment. Reference: [CS224N Assignment 1: Exploring Word Vectors](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1246/assignments/a1_preview/exploring_word_vectors.html).
2. **Reference assignment: CS336 Assignment 1 style.** Use
   [CS336 Assignment 1: Basics](https://github.com/stanford-cs336/spring2024-assignment1-basics)
   as the reference form. Implement or inspect the core parts of a small language model pipeline:
   tokenizer, model, optimizer, sampling, and training/evaluation loop.
3. **Course version: NLP tasks with Transformers.** Use the Hugging Face `transformers` library
   to complete the following three practices in one or more reproducible notebooks:
   - **Token classification:** fine-tune a Transformer for part-of-speech tagging or named entity
     recognition, following the [token classification tutorial](https://huggingface.co/docs/transformers/tasks/token_classification).
   - **Text classification:** fine-tune a Transformer for a sentence- or document-level
     classification task, following the [text classification tutorial](https://huggingface.co/docs/transformers/tasks/sequence_classification).
   - **Text generation:** load a small causal language model and compare greedy, sampling,
     top-k, top-p, and temperature-based decoding with the
     [text generation tutorial](https://huggingface.co/docs/transformers/generation_strategies).
4. **Optional extension.** Choose one topic from **Direction A · Foundation Models and NLP** in
   the [Paper Reading List](#paper-reading-list), implement a small-scale experiment, and present
   the problem, method, experimental setup, results, limitations, and possible improvements. The
   suggested report themes and reproduction tasks under each reading-list subsection can be used
   as project references.

## Direction B · Multimodal and Vision

### Learning Resources

- Archive course path: [Stanford CS131](https://cs131.stanford.edu/) and
  [StanfordVL CS131 released assignments](https://github.com/stanfordvl/cs131_release).
- Modern course path: [Stanford CS231n](http://cs231n.stanford.edu/) and
  [CS231n assignment notebooks](https://cs231n.github.io/assignments2024/assignment1/).
- Practical libraries: [torchvision](https://pytorch.org/vision/), [`timm`](https://github.com/huggingface/pytorch-image-models),
  [OpenCLIP](https://github.com/mlfoundations/open_clip), and [diffusers](https://huggingface.co/docs/diffusers).
- Multimodal demos: [LLaVA](https://llava-vl.github.io/) and [SAM 2](https://github.com/facebookresearch/sam2).

### Homework

1. **Archive homework: CS131 HW1.** Complete CS131 HW1 on your own, with modifications to be
   announced by the course staff. Reference: [StanfordVL CS131 released assignments](https://github.com/stanfordvl/cs131_release).
2. **Reference assignment: CS231n notebooks.** Use CS231n-style Colab notebooks for image
   classification, vectorized NumPy, kNN/SVM/Softmax classifiers, and a two-layer network.
3. **Course version.** Train a small classifier on CIFAR-10, then fine-tune a pretrained ViT or
   ResNet and compare accuracy, runtime, and error cases.
4. **Optional extension.** Run CLIP zero-shot classification on personal images and document failure
   cases.

## Direction C · Embodied AI and Robotics

### Learning Resources

- Robotics foundations: [Modern Robotics](https://hades.mech.northwestern.edu/index.php/Modern_Robotics).
- URDF: [ROS URDF tutorials](http://wiki.ros.org/urdf/Tutorials).
- Simulation and RL tools: [PyBullet](https://pybullet.org/), [MuJoCo](https://mujoco.readthedocs.io/),
  [Gymnasium](https://gymnasium.farama.org/), and [Stable-Baselines3](https://stable-baselines3.readthedocs.io/).
- Robot learning course: [CMU 16-831 Introduction to Robot Learning](https://16-831-s24.github.io/).

### Homework

1. **Archive homework: Modern Robotics exercises.** Finish exercises 2.1-2.9 from *Modern Robotics*
   to practice degrees of freedom and configuration space.
2. **Archive homework: URDF + PyBullet.** Build your own robot model with URDF and load it into
   PyBullet for visualization. If you already know rViz, MuJoCo, Isaac Gym, or Isaac Sim, you may use
   one of those instead.
3. **Course version.** Create or modify a simple URDF, command at least one joint, and record a short
   rollout video or screenshot sequence.
4. **Optional extension.** Train PPO on `CartPole` or a small MuJoCo task and plot the learning curve.

## Direction D · Agent Systems and Multi-Agent

### Learning Resources

- Archive course path: [UCL / David Silver RL lectures](https://www.davidsilver.uk/teaching/).
- Modern RL course path: [UC Berkeley CS285 Deep Reinforcement Learning](https://rail.eecs.berkeley.edu/deeprlcourse/).
- Multi-agent environment API: [PettingZoo documentation](https://pettingzoo.farama.org/index.html) and
  [PettingZoo RLlib tutorials](https://pettingzoo.farama.org/tutorials/rllib/index.html).
- LLM agent frameworks: [AutoGen](https://microsoft.github.io/autogen/) or
  [LangGraph](https://langchain-ai.github.io/langgraph/).

### Homework

1. **Archive homework: Theory-of-Mind report.** Submit a LaTeX report summarizing
   [*Planning with Theory of Mind*](https://doi.org/10.1016/j.tics.2022.08.003). Include related
   work, background, method, experiment results, and future improvement; focus on method and future
   improvement.
2. **Archive homework: RL/MARL reading.** Complete selected UCL RL lectures, study the first two
   game-theory lectures, and read one paper from each direction in a MARL paper collection.
3. **Course version.** Run one cooperative and one competitive PettingZoo environment, implement a
   random or scripted baseline, and report observations about coordination or competition.
4. **Optional extension.** Build a small ReAct-style tool-using LLM agent with at least two tools.

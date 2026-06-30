# 01 · Foundation Models & NLP

## Overview

Natural language processing has been reshaped into the study of **large language models (LLMs)** —
general-purpose foundation models trained on internet-scale text and adapted to thousands of tasks.
This module follows the full life cycle of a modern LLM: how text becomes tokens, how a Transformer
is pretrained at scale, how it is aligned to follow instructions and human preferences, and how it
is used in practice through prompting, retrieval, reasoning, and tool use. By the end you should be
able to fine-tune a small open model and stand up a retrieval-augmented application yourself.

## Learning Path

**Courses** *(Introductory → Advanced)*
1. [Hugging Face LLM Course](https://huggingface.co/learn/llm-course) — the fastest practical
   on-ramp to Transformers, tokenizers, and fine-tuning. *(Introductory)*
2. [Stanford CS224N — NLP with Deep Learning](https://web.stanford.edu/class/cs224n/) — word vectors
   through Transformers and LLMs; the canonical NLP course. *(Intermediate)*
3. [Stanford CS336 — Language Modeling from Scratch (2024+)](https://stanford-cs336.github.io/) —
   build a real LLM end to end: data, tokenizer, architecture, training, alignment, inference.
   *The most important course for this module.* *(Advanced)*

**Core topics** — study in this order:
- Tokenization (BPE) and embeddings · self-attention and the decoder-only Transformer
- Pretraining objectives and **scaling laws** (compute-optimal training)
- **Alignment:** supervised instruction tuning → RLHF → DPO and simpler preference methods
- **Inference & use:** prompting, in-context learning, **chain-of-thought**, **RAG**, tool/function calling
- **Reasoning models** and test-time compute
- Evaluation and its pitfalls (benchmarks, contamination, LLM-as-judge)

## Programming Exercises

1. **Tokenizer & sampling.** Use `transformers` to load a small open model (e.g. a 0.5–1.5B Qwen or
   Llama), inspect its tokenizer, and implement greedy / temperature / top-p decoding by hand.
   Report how each changes the output.
2. **LoRA fine-tuning.** Use [PEFT](https://huggingface.co/docs/peft) + TRL to LoRA-fine-tune a small
   instruction model on a tiny dataset. Show before/after generations and your training curve.
3. **Build a RAG pipeline.** Embed a small document corpus, store it in a vector index (e.g. FAISS),
   and answer questions with retrieval + an LLM. Demonstrate a question the base model gets wrong but
   RAG gets right, and discuss failure modes.
4. **Report.** Summarize one paper from the reading list — background, method, experiments, and one
   concrete idea for improvement (focus on method + improvement).

## Paper Reading

**Architecture & pretraining**
1. **Vaswani et al. (2017), "Attention Is All You Need."** The Transformer (shared with module 00).
2. **Brown et al. (2020), "Language Models are Few-Shot Learners" (GPT-3).** In-context learning emerges with scale.
3. **Hoffmann et al. (2022), "Training Compute-Optimal Large Language Models" (Chinchilla).** Scaling laws done right.
4. **Touvron et al. / Dubey et al. (2024), "The Llama 3 Herd of Models."** A detailed open recipe for a frontier-class model.

**Alignment**
5. **Ouyang et al. (2022), "Training language models to follow instructions with human feedback" (InstructGPT).** RLHF.
6. **Rafailov et al. (2023), "Direct Preference Optimization (DPO)."** Preference alignment without a separate reward model.
7. **Wang et al. (2022), "Self-Instruct."** Bootstrapping instruction data from the model itself.

**Use, reasoning & tools**
8. **Wei et al. (2022), "Chain-of-Thought Prompting."** Reasoning by intermediate steps.
9. **Lewis et al. (2020), "Retrieval-Augmented Generation (RAG)."** Grounding generation in retrieved evidence.
10. **Schick et al. (2023), "Toolformer."** LLMs that decide when and how to call tools/APIs.
11. **DeepSeek-AI (2025), "DeepSeek-R1."** Eliciting reasoning with reinforcement learning / test-time compute.

> Conferences to follow: **ACL, EMNLP, NAACL, NeurIPS, ICLR, ICML.** Many recent works appear on
> [arXiv (cs.CL)](https://arxiv.org/list/cs.CL/recent) first.

## Tools & Setup

| Tool | Use | Link |
|---|---|---|
| 🤗 Transformers | Load/run/fine-tune models | [docs](https://huggingface.co/docs/transformers) |
| PEFT + TRL | LoRA, SFT, DPO training | [PEFT](https://huggingface.co/docs/peft) · [TRL](https://huggingface.co/docs/trl) |
| Datasets | Data loading & processing | [docs](https://huggingface.co/docs/datasets) |
| FAISS | Vector search for RAG | [github](https://github.com/facebookresearch/faiss) |
| vLLM | Fast inference / serving | [docs](https://docs.vllm.ai/) |

> **Hardware note:** LoRA on a ≤1.5B model fits in a single Colab/department GPU. Use 4-bit quantized
> loading (`bitsandbytes`) if memory is tight; full pretraining is out of scope — study CS336 for the theory.

# 04 · Agent Systems & Multi-Agent

## Overview

An **agent** is a system that perceives, decides, and acts to achieve goals; a **multi-agent system
(MAS)** is many such agents interacting — cooperating, competing, or negotiating. This module bridges
two traditions. The classical one studies agents through **reinforcement learning and game theory**:
how a policy is learned, when cooperation emerges, what an equilibrium is. The new one studies
**LLM-based agents**: language models that reason, plan, use tools, and coordinate in teams. We
connect them through shared ideas — planning, theory of mind, and cooperation — and you will build a
tool-using agent yourself.

## Learning Path

**Reinforcement learning & game theory** *(Introductory → Advanced)*
1. [David Silver — Introduction to Reinforcement Learning (DeepMind/UCL)](https://www.davidsilver.uk/teaching/) — the classic RL lecture series. *(Introductory)*
2. [Sutton & Barto, *Reinforcement Learning: An Introduction* (2nd ed., free)](http://incompleteideas.net/book/the-book.html) — the standard text. *(Intermediate)*
3. [UC Berkeley CS285 — Deep RL](https://rail.eecs.berkeley.edu/deeprlcourse/) — deep & multi-agent RL (shared with module 03). *(Advanced)*
4. Game theory — a short course such as [Game Theory (Stanford/Coursera)](https://www.coursera.org/learn/game-theory-1) for Nash equilibria and mechanism design. *(Intermediate)*

**LLM agents** *(Intermediate → Advanced)*
5. Read the LLM-agent literature below (ReAct → Reflexion → Generative Agents → AutoGen) and a
   framework's docs ([AutoGen](https://microsoft.github.io/autogen/) or
   [LangGraph](https://langchain-ai.github.io/langgraph/)).

**Core topics** — study in this order:
- MDPs and single-agent RL recap · policy gradients
- **Multi-agent RL (MARL):** cooperation vs. competition, centralized training / decentralized execution
- **Game theory:** Nash equilibria, the evolution of cooperation
- **LLM agents:** ReAct (reason + act), reflection, planning, **tool/function calling**
- **Multi-agent LLM systems:** role-play, debate, generative agent societies
- **Theory of mind** and emergent communication

## Programming Exercises

1. **Multi-agent environment.** Use [PettingZoo](https://pettingzoo.farama.org/) to run a cooperative
   and a competitive multi-agent environment; train or script simple policies and observe the dynamics.
2. **Build a ReAct agent.** Implement a tool-using LLM agent (reasoning + actions) that can call at
   least two tools (e.g. a calculator and web/search or a Python REPL) to solve multi-step questions.
3. **Multi-agent collaboration.** Set up a small multi-agent system (e.g. a "solver + critic" debate,
   or [AutoGen](https://microsoft.github.io/autogen/) / [CAMEL](https://www.camel-ai.org/) roles) and
   measure whether collaboration beats a single agent on a task.
4. **Report.** Summarize *Planning with Theory of Mind* (or another reading-list paper) — related work,
   background, method, experiments, and future improvement (focus on method + improvement).

## Paper Reading

**Multi-agent RL & game theory**
1. **Lowe et al. (2017), "Multi-Agent Actor-Critic for Mixed Cooperative-Competitive Environments (MADDPG)."** Foundational deep MARL.
2. **Yang & Wang (2020), "An Overview of Multi-Agent Reinforcement Learning from a Game-Theoretical Perspective."** A clear survey/bridge.
3. **Nowak (2006), "Five Rules for the Evolution of Cooperation."** Why cooperation can emerge at all.

**LLM agents**
4. **Yao et al. (2023), "ReAct: Synergizing Reasoning and Acting in Language Models."** The core agent loop.
5. **Shinn et al. (2023), "Reflexion: Language Agents with Verbal Reinforcement Learning."** Self-reflection as feedback.
6. **Park et al. (2023), "Generative Agents: Interactive Simulacra of Human Behavior."** A society of LLM agents ("Smallville").
7. **Wang et al. (2023), "Voyager: An Open-Ended Embodied Agent with LLMs."** Lifelong skill learning in Minecraft.
8. **Wu et al. (2023), "AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation."** A practical multi-agent framework.

**Theory of mind & planning**
9. **"Planning with Theory of Mind."** Reasoning about other agents' beliefs and goals to plan (course core reading).
10. **Rabinowitz et al. (2018), "Machine Theory of Mind."** Learning to model other agents.

> Conferences to follow: **AAMAS, NeurIPS, ICML, ICLR, AAAI**. For LLM agents, watch
> [arXiv (cs.AI / cs.MA)](https://arxiv.org/list/cs.MA/recent) closely — the field moves monthly.

## Tools & Setup

| Tool | Use | Link |
|---|---|---|
| Gymnasium | Single-agent RL environments | [docs](https://gymnasium.farama.org/) |
| PettingZoo | Multi-agent environments | [docs](https://pettingzoo.farama.org/) |
| Stable-Baselines3 | RL algorithm implementations | [docs](https://stable-baselines3.readthedocs.io/) |
| AutoGen | Multi-agent LLM conversations | [docs](https://microsoft.github.io/autogen/) |
| LangGraph | Stateful agent / tool orchestration | [docs](https://langchain-ai.github.io/langgraph/) |

> **Hardware note:** MARL toy environments and LLM-agent exercises run on a CPU laptop — the LLM calls
> can use a hosted API or a small local model. No large GPU is required for this module.

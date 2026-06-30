# 03 · Embodied AI & Robotics

## Overview

Embodied AI is where perception, action, and the physical world meet — the crossover between this
module's two fields. We start from classical robot **kinematics** (how to describe and move
a robot) and **simulation** (how to test policies safely and at scale), then move to **robot
learning**: training control policies with reinforcement and imitation learning — increasingly on
real hardware and dexterous, multi-fingered hands — and the new wave of **vision-language-action
(VLA)** models that map camera images and language instructions directly to robot actions. The goal is to understand the full loop — model a robot, simulate it, and learn a
policy that acts in it.

## Learning Path

**Foundations** *(Introductory → Intermediate)*
1. [*Modern Robotics* (Kevin Lynch & Frank Park)](https://hades.mech.northwestern.edu/index.php/Modern_Robotics) —
   free book + videos + [code library](https://github.com/NxRLab/ModernRobotics). Skim ch. 1; study
   **ch. 2 (degrees of freedom & configuration space)**; read ch. 3 (rigid-body motions) as needed.
2. [URDF tutorials (ROS)](http://wiki.ros.org/urdf/Tutorials) — the standard format for describing a robot to a computer.

**Robot learning** *(Intermediate → Advanced)*
3. [UC Berkeley CS285 — Deep Reinforcement Learning](https://rail.eecs.berkeley.edu/deeprlcourse/) — policy gradients, actor-critic, model-based RL. *(shared theory with module 04)*
4. [CMU 16-831 — Robot Learning](https://16831-f24.github.io/) or [Stanford CS panel on robot learning] — imitation learning, sim-to-real, foundation models for robotics. *(Advanced)*

**Core topics** — study in this order:
- Rigid bodies, **degrees of freedom**, configuration space, forward kinematics · **URDF**
- **Simulation:** MuJoCo, Isaac Lab, PyBullet, Genesis — load a robot, step physics, render
- **Control & RL:** Markov decision processes, PPO, reward design
- **Imitation learning & diffusion policy:** learning from demonstrations
- **Vision-Language-Action (VLA):** RT-2, OpenVLA, π0 / π0.6 — language + pixels → actions
- **Real-robot RL & dexterous manipulation:** sample-efficient on-hardware RL (SERL, RL-100), sim-to-real for multi-fingered hands (SimToolReal)
- **Sim-to-real** and **world models** (learning a predictive model of the environment)

## Programming Exercises

1. **Modern Robotics ch. 2.** Finish exercises **2.1–2.9** from the book to internalize DoF and configuration space.
2. **URDF + simulation.** Build a simple robot in URDF and load it into
   [MuJoCo](https://mujoco.readthedocs.io/) (or [PyBullet](https://pybullet.org/)); visualize it and
   command a few joints.
3. **Train an RL policy.** Use [Gymnasium](https://gymnasium.farama.org/) +
   [Stable-Baselines3](https://stable-baselines3.readthedocs.io/) to train PPO on a classic control or
   MuJoCo task (e.g. `CartPole`, `HalfCheetah`); plot the learning curve and record a rollout video.
4. **Robot-learning demo.** Run a published
   [Diffusion Policy](https://diffusion-policy.cs.columbia.edu/) or [OpenVLA](https://openvla.github.io/)
   demo in simulation and write up how it maps observations to actions.

## Paper Reading

**Foundations & simulation**
1. **Lynch & Park, *Modern Robotics*, ch. 2–3.** Configuration space and rigid-body motion (textbook).
2. **Todorov et al. (2012), "MuJoCo: A physics engine for model-based control."** The simulator behind much of modern robot learning.

**Control & imitation learning**
3. **Schulman et al. (2017), "Proximal Policy Optimization (PPO)."** The workhorse RL algorithm.
4. **Chi et al. (2023), "Diffusion Policy: Visuomotor Policy Learning via Action Diffusion."** Diffusion models for control.
5. **Zhao et al. (2023), "Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware (ACT / ALOHA)."** Imitation learning that actually works on real hardware.

**Real-robot RL & dexterous manipulation**
6. **Luo et al. (2024), "SERL: A Software Suite for Sample-Efficient Robotic RL."** Reinforcement learning trained directly and efficiently on real hardware.
7. **Lei et al. (2025), "RL-100: Performant Robotic Manipulation with Real-World Reinforcement Learning."** Real-world RL on diffusion visuomotor policies, reaching near-100% success across diverse tasks.
8. **Kedia et al. (2026), "SimToolReal: An Object-Centric Policy for Zero-Shot Dexterous Tool Manipulation."** Sim-to-real RL that transfers one dexterous tool-use policy zero-shot to real robots.

**Foundation models for action**
9. **Brohan et al. (2023), "RT-2: Vision-Language-Action Models."** Web knowledge transferred to robot control.
10. **Kim et al. (2024), "OpenVLA: An Open-Source Vision-Language-Action Model."** An open, reproducible VLA.
11. **Black et al. (2024), "π0: A Vision-Language-Action Flow Model for General Robot Control."** A recent generalist policy *(see also π0.6, 2025, which improves it with RL from real-world experience).*
12. **Ahn et al. (2022), "Do As I Can, Not As I Say (SayCan)."** Grounding LLM plans in robot affordances.
13. **Hafner et al. (2023), "Mastering Diverse Domains through World Models (DreamerV3)."** Model-based RL / world models.

> Conferences to follow: **CoRL, RSS, ICRA, IROS**, plus **NeurIPS / ICLR / ICML** for learning methods.

## Tools & Setup

| Tool | Use | Link |
|---|---|---|
| MuJoCo | Fast physics simulation | [docs](https://mujoco.readthedocs.io/) |
| Isaac Lab | GPU-accelerated robot learning | [docs](https://isaac-sim.github.io/IsaacLab/) |
| Genesis | Modern generative physics simulator | [github](https://github.com/Genesis-Embodied-AI/Genesis) |
| PyBullet | Lightweight sim & URDF loading | [pybullet.org](https://pybullet.org/) |
| Gymnasium | RL environment API | [docs](https://gymnasium.farama.org/) |
| Stable-Baselines3 | RL algorithm implementations | [docs](https://stable-baselines3.readthedocs.io/) |

> **Hardware note:** URDF/PyBullet work on a CPU laptop. MuJoCo RL trains comfortably on a single GPU;
> Isaac Lab and VLA models want an NVIDIA GPU — use the course server or department machines for those.

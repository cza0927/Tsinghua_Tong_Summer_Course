# Paper Reading List · 通用人工智能系统平台I

> **Owner:** All TAs · **Source format:** adapted from `archive/PaperReadingList_BIGAI_2025.pdf`

Every listed paper has a direct link. Prefer the **Required** papers for reading reports; use
**Optional** papers after TA approval.

## Reading Report Format

- Choose one required paper or one TA-approved optional paper.
- Write a 2-4 page LaTeX report in English or Chinese.
- Include: problem background, main method, experiment design, limitations, and one possible
  improvement or follow-up experiment.
- Submit the `.tex`, compiled PDF, and any reproduction code through the course repository.

## Shared Foundations

> **All TAs please update here:** mark the final subset that every student must read before choosing
> a direction-specific report topic.

### Required

- Rosenblatt, 1958, [**The Perceptron: A Probabilistic Model for Information Storage and Organization in the Brain**](https://doi.org/10.1037/h0042519).
- Rumelhart, Hinton, and Williams, 1986, [**Learning representations by back-propagating errors**](https://doi.org/10.1038/323533a0).
- Ackley, Hinton, and Sejnowski, 1985, [**A Learning Algorithm for Boltzmann Machines**](https://doi.org/10.1207/s15516709cog0901_7).
- Elman, 1990, [**Finding Structure in Time**](https://doi.org/10.1207/s15516709cog1402_1).
- Sutton and Barto, 1981, [**Toward a Modern Theory of Adaptive Networks: Expectation and Prediction**](https://doi.org/10.1037/0033-295X.88.2.135).
- Kingma and Welling, 2014, [**Auto-Encoding Variational Bayes**](https://arxiv.org/abs/1312.6114).
- Kingma and Ba, 2015, [**Adam: A Method for Stochastic Optimization**](https://arxiv.org/abs/1412.6980).
- He et al., 2016, [**Deep Residual Learning for Image Recognition**](https://arxiv.org/abs/1512.03385).
- Silver et al., 2016, [**Mastering the game of Go with deep neural networks and tree search**](https://doi.org/10.1038/nature16961).
- Vaswani et al., 2017, [**Attention Is All You Need**](https://arxiv.org/abs/1706.03762).
- Devlin et al., 2019, [**BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding**](https://arxiv.org/abs/1810.04805).

### Optional

- Lake et al., 2017, [**Building Machines That Learn and Think Like People**](https://doi.org/10.1017/S0140525X16001837).
- Stahl and Feigenson, 2015, [**Observing the unexpected enhances infants' learning and exploration**](https://doi.org/10.1126/science.aaa3799).
- Marr, 1982, [**Vision: A Computational Investigation into the Human Representation and Processing of Visual Information**](https://mitpress.mit.edu/9780262514620/vision/).

## Direction A · Foundation Models and NLP

This direction connects the development of pretrained language models with their use in language understanding, generation, efficient adaptation, alignment, retrieval, and reasoning. The list is ordered by conceptual dependency within each subsection rather than by publication date alone.

### Required

These papers trace the shift from contextual word representations to the three main Transformer paradigms: encoder-only understanding, decoder-only generation, and encoder-decoder text-to-text modeling. 
**Suggested report themes:** compare their pretraining objectives, attention masks, representations, and downstream interfaces. 

- Peters et al., 2018, [**Deep Contextualized Word Representations**](https://aclanthology.org/N18-1202/) (ELMo: contextualized token representations).
- Devlin et al., 2019, [**BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding**](https://aclanthology.org/N19-1423/) (encoder-only masked language modeling).
- Radford et al., 2019, [**Language Models are Unsupervised Multitask Learners**](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) (GPT-2: decoder-only language modeling and zero-shot transfer).
- Raffel et al., 2020, [**Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer**](https://www.jmlr.org/papers/v21/20-074.html) (T5: unifying NLU and NLG as text-to-text tasks).

### Optional

#### Text classification and representation learning

This route studies how pretrained Transformers support token-level prediction, sentence classification, and dense sentence representations. 
**Suggested report themes:** compare a linear-softmax head with a CRF decoder, analyze the effects of RoBERTa's pretraining choices, or compare supervised and unsupervised sentence-embedding objectives. 
**Reproduction tasks:** run BERT-based slot filling or NER with softmax and CRF heads on the same split, or evaluate Sentence-BERT and SimCSE on semantic textual similarity and retrieval with the same metric.

- Chen, Zhuo, and Wang, 2019, [**BERT for Joint Intent Classification and Slot Filling**](https://arxiv.org/abs/1902.10909) (a Transformer encoder with a linear-softmax, or conditional maximum-entropy, head for token-level slot labeling).
- Souza, Nogueira, and Lotufo, 2019, [**Portuguese Named Entity Recognition using BERT-CRF**](https://arxiv.org/abs/1909.10649) (a Transformer encoder with a linear-chain CRF decoding layer for token-level NER).
- Liu et al., 2019, [**RoBERTa: A Robustly Optimized BERT Pretraining Approach**](https://arxiv.org/abs/1907.11692) (pretraining choices and ablation).
- Reimers and Gurevych, 2019, [**Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks**](https://aclanthology.org/D19-1410/) (sentence representation and retrieval).
- Gao et al., 2021, [**SimCSE: Simple Contrastive Learning of Sentence Embeddings**](https://aclanthology.org/2021.emnlp-main.552/) (contrastive sentence representation learning).

#### Scaling, adaptation, and alignment

This route asks how model capability changes with scale, how pretrained models can be adapted efficiently, and how their behavior can be aligned with human instructions and preferences.
**Suggested report themes:** contrast parameter scaling with data scaling, full fine-tuning with LoRA, or RLHF with DPO. 
**Reproduction tasks:** measure zero-/one-/few-shot sensitivity across at least three prompt variants, ablate LoRA rank or training-set size, or compare supervised fine-tuning and DPO using the same compact base model and evaluation set.

- Brown et al., 2020, [**Language Models are Few-Shot Learners**](https://arxiv.org/abs/2005.14165) (in-context learning at scale).
- Hoffmann et al., 2022, [**Training Compute-Optimal Large Language Models**](https://arxiv.org/abs/2203.15556) (scaling laws and compute/data trade-offs).
- Hu et al., 2021, [**LoRA: Low-Rank Adaptation of Large Language Models**](https://arxiv.org/abs/2106.09685) (parameter-efficient fine-tuning).
- Ouyang et al., 2022, [**Training Language Models to Follow Instructions with Human Feedback**](https://arxiv.org/abs/2203.02155) (instruction tuning and RLHF).
- Rafailov et al., 2023, [**Direct Preference Optimization: Your Language Model is Secretly a Reward Model**](https://arxiv.org/abs/2305.18290) (preference learning without an explicit reward model).

#### Reasoning, retrieval, and tool use

This route studies how language models access external knowledge, expose or sample intermediate reasoning steps, call tools, and acquire reasoning behavior through reinforcement learning.
**Suggested report themes:** separate retrieval failures from generation failures, compare chain-of-thought with self-consistency, or contrast prompted, tool-augmented, and RL-trained reasoning. 
**Reproduction tasks:** build a compact RAG pipeline and report retrieval recall and answer accuracy separately, or compare direct answering，chain-of-thought, and self-consistency on a fixed subset of a reasoning benchmark with several random seeds.

- Lewis et al., 2020, [**Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks**](https://arxiv.org/abs/2005.11401) (retrieval with parametric and non-parametric memory).
- Wei et al., 2022, [**Chain-of-Thought Prompting Elicits Reasoning in Large Language Models**](https://arxiv.org/abs/2201.11903) (eliciting intermediate reasoning steps with demonstrations).
- Wang et al., 2022, [**Self-Consistency Improves Chain of Thought Reasoning in Language Models**](https://arxiv.org/abs/2203.11171) (sampling multiple reasoning paths).
- Schick et al., 2023, [**Toolformer: Language Models Can Teach Themselves to Use Tools**](https://arxiv.org/abs/2302.04761) (self-supervised tool use).
- DeepSeek-AI, 2025, [**DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning**](https://arxiv.org/abs/2501.12948) (reinforcement learning for reasoning).

## Direction B · Multimodal and Vision

This direction traces visual representation and generation: from convolutional and Transformer backbones to self-supervised features, from likelihood- and score-based generative models to flow matching, and on to vision-language models, promptable segmentation, and 3D / neural scene representation. Within each subsection, papers are ordered by conceptual dependency rather than by publication date alone.

### Required

- Dosovitskiy et al., 2021, [**An Image is Worth 16x16 Words**](https://arxiv.org/abs/2010.11929).
- Radford et al., 2021, [**Learning Transferable Visual Models From Natural Language Supervision**](https://arxiv.org/abs/2103.00020).
- He et al., 2022, [**Masked Autoencoders Are Scalable Vision Learners**](https://arxiv.org/abs/2111.06377).
- Ho et al., 2020, [**Denoising Diffusion Probabilistic Models**](https://arxiv.org/abs/2006.11239).
- Rombach et al., 2022, [**High-Resolution Image Synthesis with Latent Diffusion Models**](https://arxiv.org/abs/2112.10752).
- Kirillov et al., 2023, [**Segment Anything**](https://arxiv.org/abs/2304.02643) (SAM; see [**SAM 3**](https://arxiv.org/abs/2511.16719), 2025, for open-vocabulary concept prompts and [**SAM 3D**](https://arxiv.org/abs/2511.16624) for single-image 3D).
- Liu et al., 2023, [**Visual Instruction Tuning**](https://arxiv.org/abs/2304.08485) (LLaVA, the canonical VLM recipe; see Qwen2.5-VL / InternVL3 for current systems).
- Mildenhall et al., 2020, [**NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis**](https://arxiv.org/abs/2003.08934).

### Optional

- Oquab et al., 2023, [**DINOv2: Learning Robust Visual Features without Supervision**](https://arxiv.org/abs/2304.07193).
- Zhai et al., 2023, [**Sigmoid Loss for Language Image Pre-Training**](https://arxiv.org/abs/2303.15343) (SigLIP: the vision-language encoder behind many current VLMs).
- Peebles and Xie, 2023, [**Scalable Diffusion Models with Transformers**](https://arxiv.org/abs/2212.09748).
- Esser et al., 2024, [**Scaling Rectified Flow Transformers for High-Resolution Image Synthesis**](https://arxiv.org/abs/2403.03206) (Stable Diffusion 3: rectified flow / flow matching, the basis of today's open generators).
- Kerbl et al., 2023, [**3D Gaussian Splatting for Real-Time Radiance Field Rendering**](https://arxiv.org/abs/2308.04079).
- Su et al., 2020, [**A Stochastic Grammar of Images**](https://doi.org/10.1561/0600000030).

## Direction C · Embodied AI and Robotics

> **李炯烨、巫莹莹请修改补充这里：** finalize robotics required papers, simulator task, and
> reproduction expectations.

### Required

- Todorov, Erez, and Tassa, 2012, [**MuJoCo: A physics engine for model-based control**](https://homes.cs.washington.edu/~todorov/papers/TodorovIROS12.pdf).
- Schulman et al., 2017, [**Proximal Policy Optimization Algorithms**](https://arxiv.org/abs/1707.06347).
- Haarnoja et al., 2018, [**Soft Actor-Critic Algorithms and Applications**](https://arxiv.org/abs/1812.05905).
- Ho and Ermon, 2016, [**Generative Adversarial Imitation Learning**](https://arxiv.org/abs/1606.03476).
- Chi et al., 2023, [**Diffusion Policy: Visuomotor Policy Learning via Action Diffusion**](https://arxiv.org/abs/2303.04137).
- Zhao et al., 2023, [**Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware**](https://arxiv.org/abs/2304.13705).
- Brohan et al., 2023, [**RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control**](https://arxiv.org/abs/2307.15818).
- Kim et al., 2024, [**OpenVLA: An Open-Source Vision-Language-Action Model**](https://arxiv.org/abs/2406.09246).
- Luo et al., 2024, [**SERL: A Software Suite for Sample-Efficient Robotic Reinforcement Learning**](https://arxiv.org/abs/2401.16013) (real-world, sample-efficient vision-based RL).

### Optional

- Ahn et al., 2022, [**Do As I Can, Not As I Say**](https://arxiv.org/abs/2204.01691).
- Hafner et al., 2023, [**Mastering Diverse Domains through World Models**](https://arxiv.org/abs/2301.04104).
- Lei et al., 2025, [**RL-100: Performant Robotic Manipulation with Real-World Reinforcement Learning**](https://arxiv.org/abs/2510.14830) (real-world RL on diffusion visuomotor policies; near-100% success).
- Kedia et al., 2026, [**SimToolReal: An Object-Centric Policy for Zero-Shot Dexterous Tool Manipulation**](https://arxiv.org/abs/2602.16863) (sim-to-real RL for zero-shot dexterous tool use).
- Black et al., 2024, [**pi0: A Vision-Language-Action Flow Model for General Robot Control**](https://arxiv.org/abs/2410.24164).
- Physical Intelligence, 2025, [**π0.6: A VLA that Learns from Experience**](https://website.pi-asset.com/pi06star/PI06_model_card.pdf) (RL-improved successor to π0 / π0.5).

## Direction D · Agent Systems and Multi-Agent

> **陈子昂请修改补充这里：** finalize MARL/LLM-agent required papers, choose report prompts, and
> add reproduction tasks.

### Required

- Littman, 1994, [**Markov Games as a Framework for Multi-Agent Reinforcement Learning**](https://www2.cs.duke.edu/courses/spring07/cps296.3/littman94markov.pdf).
- Lowe et al., 2017, [**Multi-Agent Actor-Critic for Mixed Cooperative-Competitive Environments**](https://arxiv.org/abs/1706.02275).
- Leibo et al., 2017, [**Multi-Agent Reinforcement Learning in Sequential Social Dilemmas**](https://arxiv.org/abs/1702.03037).
- Yang and Wang, 2020, [**An Overview of Multi-Agent Reinforcement Learning from a Game-Theoretical Perspective**](https://arxiv.org/abs/2011.00583).
- Mordatch and Abbeel, 2018, [**Emergence of Grounded Compositional Language in Multi-Agent Populations**](https://arxiv.org/abs/1703.04908).
- Yao et al., 2023, [**ReAct: Synergizing Reasoning and Acting in Language Models**](https://arxiv.org/abs/2210.03629).
- Wu et al., 2023, [**AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation**](https://arxiv.org/abs/2308.08155).
- Ho, Saxe, and Cushman, 2022, [**Planning with Theory of Mind**](https://doi.org/10.1016/j.tics.2022.08.003).

### Optional

- Nowak, 2006, [**Five Rules for the Evolution of Cooperation**](https://doi.org/10.1126/science.1133755).
- Shinn et al., 2023, [**Reflexion: Language Agents with Verbal Reinforcement Learning**](https://arxiv.org/abs/2303.11366).
- Park et al., 2023, [**Generative Agents: Interactive Simulacra of Human Behavior**](https://arxiv.org/abs/2304.03442).
- Wang et al., 2023, [**Voyager: An Open-Ended Embodied Agent with Large Language Models**](https://arxiv.org/abs/2305.16291).
- Rabinowitz et al., 2018, [**Machine Theory of Mind**](https://proceedings.mlr.press/v80/rabinowitz18a.html).

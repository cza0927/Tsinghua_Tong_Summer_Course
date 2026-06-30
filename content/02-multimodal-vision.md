# 02 · Multimodal & Vision

## Overview

Computer vision in 2026 is built on the same Transformer backbone as language, and increasingly
*joined* with it. This module traces the modern stack: from CNNs to **Vision Transformers**, from
supervised labels to **self-supervised representations** (CLIP, DINOv2), from classifiers to
**generative models** (diffusion, flow matching), and finally to **vision-language models (VLMs)** that
see and talk — and, increasingly, *draw* via unified models — plus promptable segmentation (SAM) and **3D / video** generation. The throughline is
*representation* — learning features general enough to transfer, caption, segment, and generate.

## Learning Path

**Courses** *(Introductory → Advanced)*
1. [Stanford CS231n — Deep Learning for Computer Vision](http://cs231n.stanford.edu/) — the canonical
   intro: CNNs, training, ViTs, and (recent editions) generative + multimodal models. *(Intermediate)*
2. [Michigan EECS 498/598 — Deep Learning for Computer Vision (Justin Johnson)](https://web.eecs.umich.edu/~justincj/teaching/eecs498/) — excellent recorded lectures. *(Intermediate)*
3. [CS231A — Computer Vision: 3D Reconstruction to Recognition](https://web.stanford.edu/class/cs231a/) — geometry & 3D. *(Advanced)*

**Core topics** — study in this order:
- Image classification · CNNs (ResNet) → **Vision Transformer (ViT)**
- **Self-supervised / contrastive** learning: CLIP, **SigLIP / SigLIP 2**, MAE, DINOv2 / **DINOv3**
- **Generative models:** GANs (briefly) → **diffusion** (DDPM, latent diffusion, DiT) → **flow matching / rectified flow** (SD3, Flux.1)
- **Vision-language models (VLMs):** connecting a vision encoder to an LLM — from LLaVA / Qwen-VL to **Qwen2.5-VL, InternVL3, Pixtral, Molmo**
- **Unified understanding + generation** *(emerging)*: one model that both sees and draws — Chameleon, Transfusion, Emu3, Janus-Pro
- **Promptable segmentation:** SAM / SAM 2 → **SAM 3** (open-vocabulary text / exemplar "concept" prompts) → **SAM 3D** (single image + mask → 3D object / body)
- **3D & video:** NeRF, 3D Gaussian Splatting, **feed-forward 3D generation** (LRM, InstantMesh, TRELLIS); open text-to-video (**HunyuanVideo, Wan 2.1, CogVideoX, LTX-Video**)

## Programming Exercises

1. **Train a classifier.** Train a small CNN/ResNet on CIFAR-10 with PyTorch + [`timm`](https://github.com/huggingface/pytorch-image-models); then fine-tune a pretrained ViT and compare accuracy and training time.
2. **Zero-shot CLIP.** Use [OpenCLIP](https://github.com/mlfoundations/open_clip) to classify your own
   images with text prompts (no training). Probe where it fails and why, then swap in a **SigLIP / SigLIP 2**
   checkpoint and compare — it's the vision tower behind many of today's VLMs.
3. **Diffusion sampling.** Use 🤗 [`diffusers`](https://huggingface.co/docs/diffusers) to generate
   images from text (try a flow-matching model such as **Flux.1-schnell**), then vary the number of
   denoising steps and guidance scale and report the trade-offs.
4. **VLM + SAM.** Run an open VLM (e.g. **Qwen2.5-VL** / InternVL3) to caption and answer questions about an
   image, and run [SAM 2](https://github.com/facebookresearch/sam2) to segment it from a point/box prompt.

## Paper Reading

**Backbones & representation**
1. **He et al. (2016), "Deep Residual Learning (ResNet)."** The CNN that made very deep nets trainable.
2. **Dosovitskiy et al. (2021), "An Image is Worth 16×16 Words (ViT)."** Transformers for images.
3. **Radford et al. (2021), "Learning Transferable Visual Models from Natural Language (CLIP)."** Image–text contrastive pretraining.
4. **He et al. (2022), "Masked Autoencoders (MAE)"** · **Oquab et al. (2023), "DINOv2."** Strong self-supervised features.

**Generation**
5. **Ho et al. (2020), "Denoising Diffusion Probabilistic Models (DDPM)."** The diffusion foundation.
6. **Rombach et al. (2022), "High-Resolution Image Synthesis with Latent Diffusion (Stable Diffusion)."** Diffusion in latent space.
7. **Peebles & Xie (2023), "Scalable Diffusion Models with Transformers (DiT)."** The backbone behind modern video/image generators.
8. **Lipman et al. (2023), "Flow Matching for Generative Modeling"** · **Esser et al. (2024), "Scaling Rectified Flow Transformers (Stable Diffusion 3)."** The flow-matching / rectified-flow paradigm behind today's open SOTA (Flux.1).

**Multimodal, segmentation, 3D**
9. **Liu et al. (2023), "Visual Instruction Tuning (LLaVA)."** A simple, influential VLM recipe; for current systems see Qwen2.5-VL / InternVL3.
10. **Kirillov et al. (2023), "Segment Anything (SAM)"** *(SAM 2 for video; **SAM 3** (2025) adds open-vocabulary text/exemplar concept prompts; **SAM 3D** (2025) lifts a masked object or body to 3D from one image).* Promptable segmentation.
11. **Mildenhall et al. (2020), "NeRF"** · **Kerbl et al. (2023), "3D Gaussian Splatting."** Neural & real-time 3D scene representation *(see feed-forward LRM / TRELLIS for 3D generation).*
12. **Chameleon Team (2024), "Chameleon"** · **DeepSeek (2025), "Janus-Pro."** Single models that both understand and generate images — the *unified* direction.

> Conferences to follow: **CVPR, ICCV, ECCV** (papers on [CVF Open Access](https://openaccess.thecvf.com/)),
> plus **NeurIPS / ICLR**. Journals: **TPAMI, IJCV**.

## Tools & Setup

| Tool | Use | Link |
|---|---|---|
| `timm` | Pretrained image backbones | [github](https://github.com/huggingface/pytorch-image-models) |
| OpenCLIP | CLIP models & zero-shot | [github](https://github.com/mlfoundations/open_clip) |
| 🤗 diffusers | Diffusion / generative models | [docs](https://huggingface.co/docs/diffusers) |
| SAM 2 | Promptable image/video segmentation | [github](https://github.com/facebookresearch/sam2) |
| torchvision | Datasets, transforms, models | [docs](https://pytorch.org/vision/) |

> **Hardware note:** classification and CLIP run on a single Colab/department GPU. Diffusion sampling
> needs a GPU with ≥8 GB VRAM; prefer inference over training, and reuse pretrained checkpoints.

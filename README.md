# 通用人工智能系统平台 I — Course Resource Hub

Resource repository for **通用人工智能系统平台 I** (*General Artificial Intelligence Systems
Platform I*), the two-week summer course for 清华通班 first-year students.

| | |
|---|---|
| **Audience** | 清华通班 大一下学生 |
| **Dates** | 2026-07-13 to 2026-07-26 |
| **Venue** | 通院 2201 大教室 |
| **Format** | 课堂讲授 + 编程练习 + 实践报告 |

## Content Model

The site follows the archive convention: learning resources and paper readings are two separate
student-facing files.

| Tab | Source file | Purpose |
|---|---|---|
| Syllabus | [`content/syllabus.md`](content/syllabus.md) | two-week course schedule |
| Learning List / Homework | [`content/learning-list.md`](content/learning-list.md) | courses, tutorials, homework links, notebooks |
| Paper Reading List | [`content/paper-reading-list.md`](content/paper-reading-list.md) | required and optional papers for reading reports |

The four direction owners should edit their reserved areas in the two list files:

| Direction | Owner |
|---|---|
| Foundation models and NLP | 林子雍 |
| Multimodal and vision | 巫莹莹 |
| Embodied AI and robotics | 李炯烨 + 巫莹莹 |
| Agent systems and multi-agent learning | 陈子昂 |

Older per-direction Markdown files may remain in `content/` for reference, but they are no longer
rendered as website tabs.

## Build

The Markdown is rendered into a single static page at [`site/index.html`](site/index.html).

```bash
python3 site/build.py
```

Then open `site/index.html` in a browser. No server is required.

## Publishing via GitHub Pages

The workflow at [`.github/workflows/pages.yml`](.github/workflows/pages.yml) rebuilds the site and
publishes `site/` to GitHub Pages on pushes that touch `content/`, `site/`, or the workflow file.

To enable it once:

1. Push this repository to GitHub.
2. Open **Settings -> Pages**.
3. Set **Build and deployment -> Source** to **GitHub Actions**.

## Repository Layout

```text
README.md
.github/workflows/pages.yml
content/
  syllabus.md
  learning-list.md
  paper-reading-list.md
site/
  build.py
  template.html
  assets/marked.min.js
  index.html
archive/
  LearningList_BIGAI_2023.pdf
  PaperReadingList_BIGAI_2025.pdf
```

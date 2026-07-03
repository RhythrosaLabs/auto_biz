<div align="center">

# 🏢 auto_biz

**Generate a complete, investor-ready business plan in minutes using AI**

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=flat&logo=openai&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=flat)

</div>

---

auto_biz is a Streamlit app that uses GPT-4o-mini to automatically draft all sections of a professional business plan. Each section is generated, validated against key criteria, and iteratively revised if anything is missing — no manual writing required.

## ✨ Features

- **8 core sections** — Executive Summary, Company Description, Market Analysis, Organization & Management, Product Line, Marketing & Sales, Funding Request, Financial Projections
- **Auto-validation** — each section is checked against domain-specific criteria; missing elements trigger an automatic revision pass
- **Progress tracking** — live Streamlit progress bar as each section is drafted
- **Single-file output** — full business plan assembled and ready to copy, export, or extend
- **GPT-4o-mini** — fast and cost-effective generation

## 🚀 Quick Start

```bash
git clone https://github.com/RhythrosaLabs/auto_biz.git
cd auto_biz
pip install -r requirements.txt
streamlit run app.py
```

Enter your OpenAI API key in the sidebar and click **Generate Business Plan**.

## 🛠️ Tech Stack

- **Python** — core logic and validation
- **Streamlit** — web UI with live progress tracking
- **OpenAI API (GPT-4o-mini)** — plan generation and revision

## 📋 Output Sections

1. Executive Summary
2. Company Description
3. Market Analysis
4. Organization & Management
5. Product Line
6. Marketing & Sales
7. Funding Request
8. Financial Projections

## 🤝 Contributing

PRs welcome. Open an issue first for major changes.

## 📄 License

MIT

## 💛 Support

If auto_biz saves you hours of planning work, consider supporting development:

👉 [Donate via PayPal](https://paypal.me/noodlebake) — @noodlebake

---
<div align="center">Made with ❤️ by <a href="https://github.com/RhythrosaLabs">RhythrosaLabs</a></div>

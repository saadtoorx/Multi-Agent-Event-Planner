---
title: "Multi-Agent Event Planner"
emoji: "🗓️"
colorFrom: "purple"
colorTo: "pink"
sdk: "streamlit"
sdk_version: "1.48.1"
app_file: "app.py"
pinned: true
---

# 🗓️ Multi-Agent Event Planner

An AI-powered **Multi-Agent Event Planner** built with [CrewAI](https://github.com/joaomdmoura/crewai) and [Streamlit](https://streamlit.io/). This project demonstrates how specialized autonomous agents collaborate to research venues, coordinate logistics, and design marketing & communications for events — producing a usable event plan and downloadable reports.

<div align="center">
  <img src="images/demo_screenshot.png" width="80%" alt="Event Planner Demo Screenshot">
</div>

---

## 🚀 Features

- 🤖 **Multi-Agent Collaboration** — Distinct agents handle venue sourcing, logistics coordination, and marketing/communications so tasks are parallelized and specialized.  
- 📅 **End-to-End Event Workflow** — From venue research to marketing strategy and final downloadable summary.  
- 🔍 **Web Research & Scraping** — Integrates search and scraping tools to gather venue and vendor details.  
- 🧠 **CrewAI Memory & Context** — Agents share context (task outputs) so downstream tasks use validated inputs (e.g., chosen venue feeds logistics & marketing).  
- 🧩 **Simulated or Real Execution** — Supports a simulated planning mode out-of-the-box and an option to execute with real CrewAI agents when configured.  
- 📦 **Downloadable Artifacts** — Venue JSON, marketing report (Markdown), and a complete event summary are exportable.

---

## 🏗️ Architecture Overview

### 🧠 Agents
- **Venue Coordinator** — Identifies candidate venues, checks capacity/availability, and outputs structured venue details.  
- **Logistic Manager** — Plans catering, equipment, transportation, and on-site logistics using venue constraints.  
- **Marketing & Communications Agent** — Designs promotional messaging, suggested channels, and a marketing timeline.

### 📋 Tasks
1. **Venue Task** — Research and select a venue that meets event requirements and produce `venue_details.json`.  
2. **Logistic Task** — Coordinate catering, rentals, transport and create confirmations/checklist.  
3. **Marketing Task** — Produce a marketing strategy and promotional materials as `marketing_report.md`.

### 🛠️ Tools Used
- `WebsiteSearchTool` / SerperDev-style tool — for web search and quick facts.  
- `ScrapeWebsiteTool` — extract structured details from vendor/venue pages.  
- CrewAI framework — orchestrates agents & tasks.  
- OpenAI API (LLM) — agent reasoning, planning, and content generation.  
- Fallback/mock tools are used when live search/scrape packages are not available so the app still runs.

---

## 📁 Project Structure

multi-agent-event-planner/  
├── app.py                      # 🚀 Streamlit app interface (main)  
├── agents.py                   # 🤖 Agent definitions (Venue, Logistics, Marketing)  
├── tasks.py                    # 📋 Task definitions (venue_task, logistic_task, marketing_task)  
├── tools.py                    # 🛠️ Tool configuration & fallbacks for scraping/search  
├── app_utils.py                # 🔑 Helpers: API setup, printing utilities, etc.  
├── requirements.txt            # 📦 Python dependencies  
├── README.md                   # 📖 This documentation  
└── images/  
    └── demo_screenshot.png     # 🖼️ Optional UI screenshot

---

## 🛠️ Installation & Setup

1. Clone the repository  

    git clone https://github.com/saadtoorx/multi-agent-event-planner.git  
    cd multi-agent-event-planner  

2. Install dependencies  

    pip install -r requirements.txt  

3. Configure API keys (required for real-agent execution)

    Create a `.env` file with your keys:
    
        OPENAI_API_KEY=your-openai-key
        SERPER_API_KEY=your-serper-key
        # Optional: set model name used in the app
        OPENAI_MODEL_NAME=gpt-4o-mini

> Note: If you don't provide search/scrape keys or CrewAI packages are missing, the app falls back to simulated execution so you can test the UI and outputs.

---

## ▶️ Running the App

    streamlit run app.py

- Open the sidebar and enter **OpenAI** and **Serper** API keys to enable full functionality.  
- Fill event details (topic, city, date, participants, budget, venue type) and click **Start Planning**.  
- Choose **Simulated** or **Use Real CrewAI Agents** before executing the planning run.  
- Download generated `venue_details.json`, `marketing_report.md`, or the complete summary.

---

## 📦 Tech Stack

- **Python 3.8+**  
- Streamlit (UI)  
- CrewAI (multi-agent orchestration)  
- crewai-tools / SerperDev-like search & scrape tools  
- OpenAI API (LLM)  
- pydantic (output models)  
- python-dotenv

---

## 🤖 Agent Summary

| Agent                          | Responsibility                                                              |
|--------------------------------|------------------------------------------------------------------------------|
| **Venue Coordinator**          | Researches and finalizes venue selection; outputs structured venue details. |
| **Logistic Manager**           | Plans catering, equipment, transport, and on-site logistics.               |
| **Marketing & Communications** | Creates marketing strategy, messaging, and timeline for attendee outreach.  |

---

## 🔮 Future Improvements

- 🌐 Integrate live vendor & venue APIs for booking checks and pricing.  
- 🧾 Add automated budget optimization and cost breakdown.  
- 📅 Export plans to calendar formats (ICS) and PDF reports.  
- 📊 Add UI visualizations for workflow, timelines, and resource allocation.  
- 🧩 Add more specialized agents (e.g., Sponsorship Agent, Budget Analyst).

---

## 📄 License

Licensed under the MIT License. See `LICENSE` for full terms.

---

## ✨ Built By

> Created with ❤️ by [Saad Toor](https://www.linkedin.com/in/saadtoorx/) (`@saadtoorx`)  
> Powered by CrewAI, Streamlit, and OpenAI

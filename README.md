# NexaChat AI

An intelligent conversational assistant featuring a 3D interactive avatar, real-time AI responses, and a modern responsive interface.

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.x-lightgrey?logo=flask)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Live-brightgreen)

### [Live Demo](https://nexachat-ai-new.onrender.com/)

---

## Features

- **AI-Powered Chat** — Real-time conversational AI with automatic model fallback
- **Multi-Model Fallback** — Cycles through Mistral Small 3.1 24B, Qwen3 4B, and Gemma 3 4B for maximum uptime
- **3D Avatar** — Interactive robot assistant rendered with Babylon.js
- **Responsive Design** — Works seamlessly on desktop, tablet, and mobile
- **Modern Dark UI** — Sleek gradient-based interface with smooth animations
- **Typing Indicators** — Animated visual feedback while the AI generates a response
- **Smart Error Handling** — Graceful fallback when individual AI providers are down

---

## Tech Stack

- **Backend:** Python, Flask, Gunicorn
- **Frontend:** HTML5, CSS3, JavaScript
- **3D Engine:** Babylon.js
- **AI Models:** Mistral Small 3.1 24B / Qwen3 4B / Gemma 3 4B (via [OpenRouter](https://openrouter.ai/) API)
- **Hosting:** [Render](https://render.com)

---

## Getting Started

### Prerequisites

- Python 3.9+
- An [OpenRouter](https://openrouter.ai/) API key (free tier available)

### Installation

```bash
git clone https://github.com/Purnachander-Konda/nexachat-ai.git
cd nexachat-ai
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the project root:

```
OPENROUTER_API_KEY=your_api_key_here
```

### Run Locally

```bash
python app.py
```

Open [http://localhost:5000](http://localhost:5000) in your browser.

---

## API Reference

### `GET /`

Serves the main web interface with chat UI and 3D assistant.

### `POST /api/ask`

Send a user prompt and receive an AI response.

**Request:**
```json
{ "prompt": "What is artificial intelligence?" }
```

**Response:**
```json
{ "response": "Artificial intelligence is..." }
```

---

## Deployment

This app is configured for deployment on [Render](https://render.com):

1. Fork this repository
2. Connect your GitHub account to Render
3. Create a new **Web Service** and select this repo
4. Set the environment variable `OPENROUTER_API_KEY`
5. Deploy!

The included `render.yaml` and `Procfile` handle the rest automatically.

---

## Issues Faced & Resolved

### 1. "Not Found" on initial deployment
**Problem:** After deploying to Render, visiting the URL showed a plain "Not Found" page.  
**Cause:** Gunicorn was not binding to the `PORT` environment variable provided by Render.  
**Fix:** Updated `Procfile` and `render.yaml` to use `--bind 0.0.0.0:$PORT`.

### 2. `Server error: 'choices'`
**Problem:** The chat UI loaded, but sending any message returned `Server error: 'choices'`.  
**Cause:** The OpenRouter API was returning an error response (no `choices` key), but the code assumed a successful response and crashed trying to access `result["choices"]`.  
**Fix:** Added error-checking logic to inspect the API response for an `error` key before accessing `choices`.

### 3. `API error: No endpoints found for mistralai/mistral-7b-instruct:free`
**Problem:** The original AI model (`mistral-7b-instruct`) was deprecated and removed from OpenRouter.  
**Cause:** OpenRouter periodically retires older model endpoints.  
**Fix:** Switched to `mistralai/mistral-small-3.1-24b-instruct:free`, a newer and more capable model.

### 4. `API error: Provider returned error`
**Problem:** Even with the updated model, responses intermittently failed with a provider error.  
**Cause:** Free-tier model providers on OpenRouter can experience temporary outages or rate limits.  
**Fix:** Implemented a **multi-model fallback chain** — the app tries up to 3 free models in sequence (Mistral Small 3.1 → Qwen3 4B → Gemma 3 4B). If one provider is down, the next one is used automatically.

---

## Author

**Purnachander Konda**  
GitHub: [@Purnachander-Konda](https://github.com/Purnachander-Konda)

---

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

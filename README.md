# NexaChat AI

An intelligent conversational assistant featuring a 3D interactive avatar, real-time AI responses, and a modern responsive interface.

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.x-lightgrey?logo=flask)
![License](https://img.shields.io/badge/License-MIT-green)

---

## Features

- **AI-Powered Chat** — Real-time conversational AI using Mistral 7B via OpenRouter
- **3D Avatar** — Interactive robot assistant rendered with Babylon.js
- **Responsive Design** — Works seamlessly on desktop, tablet, and mobile
- **Modern Dark UI** — Sleek gradient-based interface with smooth animations
- **Typing Indicators** — Visual feedback while the AI processes your message

---

## Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML5, CSS3, JavaScript
- **3D Engine:** Babylon.js
- **AI Model:** Mistral 7B Instruct (via OpenRouter API)

---

## Getting Started

### Prerequisites

- Python 3.9+
- An [OpenRouter](https://openrouter.ai/) API key

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

This app is configured for one-click deployment on [Render](https://render.com):

1. Fork this repository
2. Connect your GitHub account to Render
3. Create a new **Web Service** and select this repo
4. Set the environment variable `OPENROUTER_API_KEY`
5. Deploy!

---

## Author

**Purnachander Konda**
- GitHub: [@Purnachander-Konda](https://github.com/Purnachander-Konda)

---

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

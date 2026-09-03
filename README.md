# ✈️ TripMate AI

### 🤖 Multi-Agent AI Travel Planner powered by LangGraph, LangChain & FastAPI

TripMate AI is an open-source **AI-powered travel planning application** that transforms a natural-language travel request into a practical and structured travel plan.

Instead of switching between multiple platforms for flights, hotels, destinations, and itinerary planning, TripMate AI combines these tasks into a single intelligent workflow using **specialized AI agents**.

The system uses **LangGraph** to orchestrate multiple agents, **Groq LLMs** for intelligent reasoning and response generation, **AviationStack** for flight research, **Tavily** for web-based hotel research, **FastAPI** for the backend, and **PostgreSQL** for persistent conversation state.

---

## 🌟 Why TripMate AI?

Planning a trip traditionally requires searching across multiple websites:

- ✈️ Flight platforms
- 🏨 Hotel websites
- 🗺️ Travel guides
- 💰 Budget calculations
- 📅 Itinerary planning

TripMate AI brings these tasks together into one workflow.

Simply provide a request such as:

> **"Plan a 5-day trip to Tokyo from Delhi with a budget of $1500."**

The system automatically coordinates multiple agents to research the trip and generate a complete travel plan.

---

# ✨ Features

### ✈️ Flight Research

Uses **AviationStack API** to retrieve flight-related information based on the user's travel requirements.

### 🏨 Hotel Research

Uses **Tavily Search API** to search the web for relevant hotel and accommodation information.

### 🧠 Multi-Agent AI Architecture

Uses **LangGraph** to coordinate specialized agents through a structured workflow.

The system currently contains:

- ✈️ Flight Agent
- 🏨 Hotel Agent
- 🧠 Itinerary Agent
- 📝 Final Response Agent

### 🗓️ Day-by-Day Itinerary

The itinerary agent combines the user's requirements, flight information, and hotel research to generate a practical day-by-day travel plan.

### 💰 Budget-Aware Planning

The generated itinerary considers the user's specified budget and provides estimated travel expenses where sufficient information is available.

> **Note:** Flight APIs may not always provide live ticket prices. When pricing information is unavailable, TripMate AI clearly communicates this instead of fabricating prices.

### 💾 Persistent Conversation State

Uses **PostgreSQL** with the LangGraph PostgreSQL checkpointer to persist travel sessions and workflow state.

### ⚡ FastAPI Backend

Provides a lightweight REST API for interacting with the AI travel planning workflow.

### 🌐 Web Interface

Includes a simple web interface that allows users to submit travel requests through a browser.

---

# 🏗️ System Architecture

```text
                         ┌─────────────────────┐
                         │      User Query     │
                         │ "Plan my trip..."   │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │       FastAPI       │
                         │     REST Backend    │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │      LangGraph      │
                         │  Agent Orchestrator │
                         └──────────┬──────────┘
                                    │
                    ┌───────────────┴───────────────┐
                    │                               │
                    ▼                               ▼
          ┌──────────────────┐            ┌──────────────────┐
          │   Flight Agent   │            │    Hotel Agent   │
          │                  │            │                  │
          │ AviationStack    │            │  Tavily Search   │
          └────────┬─────────┘            └────────┬─────────┘
                   │                               │
                   └───────────────┬───────────────┘
                                   │
                                   ▼
                         ┌─────────────────────┐
                         │   Itinerary Agent   │
                         │                     │
                         │     Groq LLM        │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │    Final Agent      │
                         │                     │
                         │ Structured Response │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   Complete Travel   │
                         │        Plan         │
                         └─────────────────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │     PostgreSQL      │
                         │ Persistent State    │
                         └─────────────────────┘
```

---

# 🤖 Multi-Agent Workflow

TripMate AI follows a structured sequential workflow:

```text
START
  │
  ▼
┌─────────────────┐
│  Flight Agent   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   Hotel Agent   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Itinerary Agent │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   Final Agent   │
└────────┬────────┘
         │
         ▼
        END
```

Each agent has a clearly defined responsibility.

| Agent | Responsibility | Technology |
|------|----------------|------------|
| ✈️ Flight Agent | Flight information research | AviationStack API |
| 🏨 Hotel Agent | Hotel and accommodation research | Tavily API |
| 🧠 Itinerary Agent | Generate practical itinerary | Groq LLM |
| 📝 Final Agent | Format final travel response | Groq LLM |

---

# 🧠 Why Multi-Agent Architecture?

A single LLM can generate a travel itinerary, but a multi-agent architecture provides better separation of responsibilities.

TripMate AI divides the travel planning process into specialized components.

### Benefits

- 🔹 Modular architecture
- 🔹 Clear separation of responsibilities
- 🔹 Easier debugging
- 🔹 Independent API integrations
- 🔹 Structured state management
- 🔹 Easier feature expansion
- 🔹 Better organization of complex workflows

The architecture also makes it easier to add future agents such as:

```text
Weather Agent
     │
     ▼
Restaurant Agent
     │
     ▼
Transportation Agent
     │
     ▼
Activity Agent
```

without redesigning the entire application.

---

# 🔄 How It Works

### Step 1 — User Request

The user provides a natural-language travel request.

Example:

```text
Plan a 3-day trip to Tokyo with a budget of $1200.
```

### Step 2 — Flight Agent

The Flight Agent processes the request and retrieves relevant flight information through AviationStack.

### Step 3 — Hotel Agent

The Hotel Agent searches the web using Tavily to find relevant accommodation information.

### Step 4 — Itinerary Agent

The Itinerary Agent receives:

- User requirements
- Flight information
- Hotel research

It then uses the Groq LLM to generate a practical travel itinerary.

### Step 5 — Final Response Agent

The Final Agent combines all collected information and generates the final structured response.

The final answer is organized into:

```text
1. Trip Summary
2. Flight Information
3. Hotel Suggestions
4. Day-by-Day Itinerary
5. Estimated Budget
6. Final Recommendations
```

---

# 🛠️ Tech Stack

## Programming

- Python 3.10+
- SQL

## AI & Machine Learning

- Large Language Models (LLMs)
- Groq
- LangChain
- LangGraph
- Prompt Engineering

## Backend

- FastAPI
- Uvicorn
- Pydantic
- REST APIs

## External APIs

- AviationStack API
- Tavily Search API
- Groq API

## Database

- PostgreSQL
- Psycopg
- LangGraph PostgreSQL Checkpointer

## Frontend

- HTML
- CSS
- JavaScript
- Jinja2

## Development Tools

- Git
- GitHub
- VS Code
- Postman
- pgAdmin

## Deployment

- Render

---

# 📁 Project Structure

```text
TripMate-AI/
│
├── app.py
│   └── FastAPI application entry point
│
├── backend.py
│   └── LangGraph travel-agent workflow
│
├── requirements.txt
│   └── Python dependencies
│
├── .env
│   └── Environment variables
│
├── static/
│   └── Frontend CSS, JavaScript and assets
│
├── templates/
│   └── HTML templates
│
└── tools/
    │
    ├── tavily_tool.py
    │   └── Tavily web-search integration
    │
    └── flight_tool.py
        └── AviationStack flight integration
```

---

# 🚀 Getting Started

## Prerequisites

Before running TripMate AI locally, make sure you have:

- Python **3.10 or newer**
- PostgreSQL
- Git
- Groq API Key
- Tavily API Key
- AviationStack API Key

---

# 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/TripMate-AI.git
cd TripMate-AI
```

---

# 2️⃣ Create a Virtual Environment

## Windows

```bash
python -m venv .venv
```

Activate the environment:

```bash
.venv\Scripts\activate
```

## macOS / Linux

```bash
python3 -m venv .venv
```

Activate:

```bash
source .venv/bin/activate
```

---

# 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔐 Environment Variables

Create a `.env` file in the project root.

```env
DATABASE_URL=postgresql://user:password@localhost:5432/travel_db

GROQ_API_KEY=your_groq_api_key

AVIATIONSTACK_API_KEY=your_aviationstack_api_key

TAVILY_API_KEY=your_tavily_api_key

DEFAULT_ORIGIN_IATA=DAC
```

### 🔒 Security

Never commit API keys or passwords to GitHub.

Add the following to `.gitignore`:

```gitignore
.env
.venv/
__pycache__/
*.pyc
```

---

# ▶️ Running the Application

Start the FastAPI application:

```bash
python app.py
```

Or use Uvicorn:

```bash
uvicorn app:app --reload
```

The application will start at:

```text
http://127.0.0.1:8000
```

Open the URL in your browser.

---

# 🔌 API Documentation

## Health Check

### Endpoint

```http
GET /health
```

Example:

```bash
curl http://127.0.0.1:8000/health
```

---

## Travel Planning

### Endpoint

```http
POST /api/travel
```

### Request

```json
{
  "message": "Plan a 3-day trip to Tokyo with a budget of $1200"
}
```

### cURL Example

```bash
curl -X POST http://127.0.0.1:8000/api/travel \
  -H "Content-Type: application/json" \
  -d "{\"message\":\"Plan a 3-day trip to Tokyo with a budget of $1200\"}"
```

### Example Response

```json
{
  "thread_id": "user_abc123",
  "answer": "Complete travel plan...",
  "flight_results": "Flight information...",
  "hotel_results": "Hotel suggestions...",
  "itinerary": "Day-by-day itinerary...",
  "llm_calls": 2
}
```

---

# 🧩 LangGraph State Management

TripMate AI maintains a shared state between agents.

```python
class TravelState(TypedDict):

    messages: Annotated[list[AnyMessage], operator.add]

    user_query: str

    flight_results: str

    hotel_results: str

    itinerary: str

    llm_calls: int
```

Each agent reads the required information from the shared state and adds its results for the next agent.

This allows the workflow to maintain a consistent context throughout the entire travel-planning process.

---

# 💾 PostgreSQL Persistence

TripMate AI uses PostgreSQL with the LangGraph PostgreSQL checkpointer.

This provides persistent workflow state and enables:

- Conversation persistence
- Thread-based sessions
- State recovery
- Multi-turn interactions
- Reliable workflow execution

Each travel session is assigned a unique thread ID.

Example:

```text
user_7f8c92a1b3d44e...
```

---

# 🧪 Example Queries

TripMate AI can process different types of travel requests.

### 💰 Budget Travel

```text
Plan a 5-day trip to Bangkok under $800.
```

### 👨‍👩‍👧 Family Vacation

```text
Plan a 7-day family trip to Singapore for 4 people.
```

### 🏖️ Weekend Trip

```text
Plan a weekend trip from Delhi to Goa.
```

### 🌏 International Travel

```text
Plan a 10-day trip to Japan with a budget of $2500.
```

### 🍜 Personalized Travel

```text
Plan a 4-day trip to Dubai focused on food, shopping and sightseeing.
```

---

# 📊 Key Engineering Highlights

### 🔹 Agent-Oriented Design

The system decomposes a complex travel-planning problem into specialized agents with clearly defined responsibilities.

### 🔹 LLM + External Tools

The application combines LLM reasoning with external APIs and web search instead of relying entirely on generated knowledge.

### 🔹 Stateful AI Workflow

LangGraph manages the workflow state while PostgreSQL provides persistence.

### 🔹 API-First Architecture

FastAPI exposes the travel planning workflow through REST endpoints, allowing the same backend to support web, mobile, or other future clients.

### 🔹 Modular Integrations

External services are isolated inside the `tools/` directory, making it easier to replace or extend individual integrations.

### 🔹 Extensible Architecture

New agents can be added to the workflow without completely restructuring the application.

---

# 🌐 Deployment

TripMate AI can be deployed using cloud platforms such as **Render**.

A typical deployment consists of:

```text
                    GitHub Repository
                           │
                           ▼
                         Render
                           │
              ┌────────────┴────────────┐
              │                         │
              ▼                         ▼
        FastAPI Service            PostgreSQL
              │                         │
              └────────────┬────────────┘
                           │
                           ▼
                     TripMate AI
```

Environment variables should be configured securely through the deployment platform rather than committing them to the repository.

---

# 🔮 Future Roadmap

TripMate AI is designed to grow into a more comprehensive AI travel assistant.

### Planned Improvements

- 🗺️ Google Maps integration
- 🚆 Train and bus search
- 🚕 Local transportation planning
- 🌦️ Weather-aware itinerary generation
- 💱 Real-time currency conversion
- 🍽️ Restaurant recommendations
- 🎟️ Attractions and activity discovery
- 💰 Real-time travel cost estimation
- 📍 Route optimization
- 🧳 AI-generated packing lists
- 🌐 Multi-language travel planning
- 🔐 User authentication
- 📱 Mobile application
- 🧠 More specialized AI agents
- 📊 Travel expense tracking

---

# 🤝 Contributing

Contributions are welcome!

If you would like to improve TripMate AI, add new travel features, or fix bugs:

### 1. Fork the repository

### 2. Create a feature branch

```bash
git checkout -b feature/new-feature
```

### 3. Make your changes

Implement and test your feature.

### 4. Commit your changes

```bash
git add .
git commit -m "Add new travel feature"
```

### 5. Push the branch

```bash
git push origin feature/new-feature
```

### 6. Open a Pull Request

Describe your changes and submit a pull request.

---

# 🛡️ Security

Please do not commit:

- API keys
- Database passwords
- `.env` files
- Authentication tokens
- Private credentials

If you discover a security issue, please report it responsibly.

---

# 📜 License

This project is open-source and available under the **MIT License**.

---

# 👨‍💻 Author

## Umesh Kumar Patel

AI/ML & Software Development Enthusiast

### Technologies Used

```text
Python • FastAPI • LangChain • LangGraph • Groq
PostgreSQL • Tavily • AviationStack • REST APIs
Git • GitHub • Render
```

---

# ⭐ Support the Project

If you find TripMate AI useful or interesting:

⭐ **Star the repository**

🍴 **Fork the project**

🐛 **Report issues**

💡 **Suggest new features**

🤝 **Contribute improvements**

---

<p align="center">

## ✈️ TripMate AI

### Plan Smarter. Travel Better. Explore More.

**An intelligent multi-agent travel planning experience.**

</p>
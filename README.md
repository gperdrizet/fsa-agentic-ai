# fsa-agentic-ai

## Quickstart

First, fork this repository to your own GitHub account.

### Option 1: Run in GitHub Codespaces

1. Open your fork on GitHub, click **Code**, select the **Codespaces** tab, and click **Create codespace on main**.
2. In the terminal, create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Copy and complete the environment file:
   ```bash
   cp .env.template .env
   ```
   Open `.env` and fill in your `OPENAI_API_KEY`.

### Option 2: Run on a Local Clone

1. Clone your fork and enter the directory:
   ```bash
   git clone https://github.com/<your-username>/fsa-agentic-ai.git
   cd fsa-agentic-ai
   ```
2. Create and activate a virtual environment:
   - **macOS/Linux:**
     ```bash
     python -m venv .venv
     source .venv/bin/activate
     ```
   - **Windows:**
     ```bash
     python -m venv .venv
     .venv\Scripts\activate
     ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Copy and complete the environment file:
   - **macOS/Linux:**
     ```bash
     cp .env.template .env
     ```
   - **Windows:**
     ```cmd
     copy .env.template .env
     ```
   Open `.env` and fill in your `OPENAI_API_KEY`.

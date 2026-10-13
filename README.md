# Fullstack Academy agentic AI demos

## Demos

| Title                                                        | Entrypoint                                                                                          | Concepts                                                     |
|--------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| LangGraph Augmented LLM: Smart Search Optimization           | [lesson-59/D1.py](https://github.com/gperdrizet/fsa-agentic-ai/blob/main/lesson-59/D1.py)           | Inference APIs, Pydantic schemas, Streamlit                  |
| LangGraph Prompt Chaining for Automated Product Descriptions | [lesson-59/D2.py](https://github.com/gperdrizet/fsa-agentic-ai/blob/main/lesson-59/D2.py)           | LangGraph, state dicts/classes, workflow graph, nodes, edges |
| Parallel AI Content Generation with LangGraph                | [lesson-59/D3.py](https://github.com/gperdrizet/fsa-agentic-ai/blob/main/lesson-59/D3.py)           | Parallel workflow graphs                                     |
| Intelligent Routing for AI Story Generation with LangGraph   | [lesson-59/D4.py](https://github.com/gperdrizet/fsa-agentic-ai/blob/main/lesson-59/D4.py)           | Workflow graph decision points/conditional edges             |
| End-to-End Automated Client Inquiry Workflow                 | [lesson-59/D5/main.py](https://github.com/gperdrizet/fsa-agentic-ai/blob/main/lesson-59/D5/main.py) | Bring it all together!                                       |


## Quickstart

First, fork this repository to your own GitHub account.

### 1. Pick your environment

   #### Option 1: GitHub Codespaces
   
   >Open your fork on GitHub, click **Code**, select the **Codespaces** tab, and click **Create codespace on main**.

   #### Option 2: Local clone (terminal only)
   
   >Clone your fork and enter the directory:
   >```bash
   >git clone https://github.com/<your-username>/fsa-agentic-ai.git
   >cd fsa-agentic-ai
   >```

   #### Option 3: Local clone (VS code)
   
   >Clone your fork and enter the directory:
   >```bash
   >git clone https://github.com/<your-username>/fsa-agentic-ai.git
   >cd fsa-agentic-ai
   >```
   >
   >Open in VS Code:
   >```bash
   >code .
   >```

   #### Option 4: Local clone (VS code + devcontainer)
   
   >Clone your fork and enter the directory:
   >```bash
   >git clone https://github.com/<your-username>/fsa-agentic-ai.git
   >cd fsa-agentic-ai
   >```
   >
   >Open in VS Code:
   >```bash
   >code .
   >```
   >
   >Start the devcontainer: `ctrl`+`shift`+`p` to open the command pallet, then search "Dev Containers: Open Folder in Container". Select the local clone's directory.

### 2. Python dependencies

In the terminal, create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate
```
Install the dependencies:
```bash
pip install -r requirements.txt
```

### 3. Inference API credentials

Copy and complete the environment file:
```bash
cp .env.template .env
```
Open `.env` and fill in your `OPENAI_API_KEY` and or `OPENAI_BASE_URL` if using a compatible provider other than OpenAI. These credentials are read automatically from their respective environment variables by the `OpenAI()` client from OpenAI, or LangChain's `ChatOpenAI()`.

### 4. Run demos

Run any of the demos with Streamlit:

```
streamlit run lesson-59/D1.py
```

Open the link provided in the terminal in your web browser (or the built in VS Code browser).
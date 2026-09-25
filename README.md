# ai-task-manager

A CLI task management utility featuring JSON persistence and automated complex task decomposition powered by OpenAI models.

## Project Overview

`ai-task-manager` is a command-line productivity tool that helps developers and teams organize daily action items. Beyond typical CRUD task capabilities, it integrates an LLM service that analyzes complex or ambiguous tasks and breaks them down into three concise, actionable subtasks.

## Features

- **Task Management**: Create, list, mark as completed, and delete tasks.
- **AI Task Decomposition**: Leverage OpenAI chat models to automatically break high-level tasks into actionable subtasks.
- **Local Persistence**: Tasks are persisted locally in formatted JSON without external database requirements.
- **Robust Error Handling**: Defensive input validation and graceful error responses if network calls or API keys fail.
- **Comprehensive Unit Testing**: Full unit test suite with 100% mocked dependencies for file I/O and CLI interaction.

## Prerequisites

- **Python**: Python 3.10 or higher.
- **OpenAI API Key** (optional, required only for AI features): An active OpenAI account with API credits.

## Installation / Build

1. Clone the repository locally:
   ```bash
   git clone https://github.com/AntonioHellin/ai-task-manager.git
   cd ai-task-manager
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   # Windows (PowerShell):
   .venv\Scripts\Activate.ps1
   # Linux / macOS:
   source .venv/bin/activate
   ```

3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure environment variables:
   Copy the example template and fill in your API key:
   ```bash
   cp .env.example .env
   ```

## Configuration & Environment Variables

Create a `.env` file in the root directory with the following variables:

| Variable | Required | Default | Description |
| :--- | :--- | :--- | :--- |
| `OPENAI_API_KEY` | Conditional | None | Required for AI decomposition feature |
| `OPENAI_MODEL` | No | `gpt-4o-mini` | OpenAI model identifier (e.g. `gpt-4o-mini`, `gpt-4o`) |

## Usage

### Running the Application

Launch the interactive CLI menu:

```bash
python main.py
```

### Menu Options

```text
Task Manager Application
1. Add Task
2. Add Complex Task with AI
3. List Tasks
4. Complete Task
5. Delete Task
6. Exit
```

### Running the Test Suite

Execute the unit tests using Python's built-in `unittest` runner:

```bash
python -m unittest test_task_manager.py
```

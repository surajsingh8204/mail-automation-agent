# Mail Automation Agent

A production-ready mail automation codebase for triage, drafting replies, scheduling, and human review. The project includes multiple agent variants, shared tools, and evaluation utilities.

## What This Project Includes

* Triage and response agent with tool calling.
* Human-in-the-loop workflows for sensitive actions.
* Memory-enabled workflows that learn user preferences.
* Gmail integration for real inbox processing.
* Evaluation utilities and tests.

## Project Layout

* Core agent: [src/email_assistant/email_assistant.py](src/email_assistant/email_assistant.py)
* Human-in-the-loop agent: [src/email_assistant/email_assistant_hitl.py](src/email_assistant/email_assistant_hitl.py)
* Memory-enabled agent: [src/email_assistant/email_assistant_hitl_memory.py](src/email_assistant/email_assistant_hitl_memory.py)
* Gmail integration: [src/email_assistant/email_assistant_hitl_memory_gmail.py](src/email_assistant/email_assistant_hitl_memory_gmail.py)
* Tools and prompts: [src/email_assistant/tools](src/email_assistant/tools)
* Evaluation utilities: [src/email_assistant/eval](src/email_assistant/eval)
* Tests: [tests](tests)

## Setup

### Python Version

* Use Python 3.11 or later.

```shell
python3 --version
```

### Install Dependencies

**Using uv**

```shell
pip install uv
uv sync --extra dev
```

**Using pip**

```shell
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
pip install -e .
```

### Configure Environment

Copy the example file and add your keys and settings.

```shell
cp .env.example .env
```

Required variables:

```text
OPENAI_API_KEY=your_openai_api_key
LANGSMITH_TRACING=true
LANGSMITH_API_KEY=your_langsmith_api_key
LANGSMITH_PROJECT="mail-automation-agent"
```

## Running Tests

Run the full test suite:

```shell
python tests/run_all_tests.py
```




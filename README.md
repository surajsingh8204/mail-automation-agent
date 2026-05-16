# Mail Automation Agent

A production-ready mail automation codebase for triage, drafting replies, scheduling, and human review. It includes multiple agent variants, shared tools, and evaluation utilities.

## What This Project Includes

* Triage and response agent with tool calling.
* Human-in-the-loop workflows for sensitive actions.
* Memory-enabled workflows that learn user preferences.
* Gmail integration for real inbox processing.
* Evaluation utilities and tests.

## How The Agent Works

1. **Ingest**: The input email is parsed into author, recipients, subject, and body.
2. **Triage**: A router model classifies the email into respond, notify, or ignore.
3. **Respond**: If classified as respond, an agent generates a reply and calls tools as needed.
4. **Tools**: Tool calls are executed through a tool node (email drafting, calendar checks, scheduling).
5. **Human Review**: HITL variants pause on sensitive tool calls and wait for approval or edits.
6. **Memory**: Memory variants persist user preferences and update them based on feedback.
7. **Gmail**: The Gmail variant uses Gmail-specific parsing and tools for real inbox workflows.

## Agent Implementations

* LangGraph 101 basics: [src/email_assistant/langgraph_101.py](src/email_assistant/langgraph_101.py)
* Basic email assistant: [src/email_assistant/email_assistant.py](src/email_assistant/email_assistant.py)
* Human-in-the-loop: [src/email_assistant/email_assistant_hitl.py](src/email_assistant/email_assistant_hitl.py)
* Memory-enabled HITL: [src/email_assistant/email_assistant_hitl_memory.py](src/email_assistant/email_assistant_hitl_memory.py)
* Gmail integration: [src/email_assistant/email_assistant_hitl_memory_gmail.py](src/email_assistant/email_assistant_hitl_memory_gmail.py)

## Project Layout

* Core agent code: [src/email_assistant](src/email_assistant)
* Tools and prompts: [src/email_assistant/tools](src/email_assistant/tools)
* Evaluation utilities: [src/email_assistant/eval](src/email_assistant/eval)
* Tests: [tests](tests)

## File Structure

* Agent graphs: [src/email_assistant/email_assistant.py](src/email_assistant/email_assistant.py), [src/email_assistant/email_assistant_hitl.py](src/email_assistant/email_assistant_hitl.py), [src/email_assistant/email_assistant_hitl_memory.py](src/email_assistant/email_assistant_hitl_memory.py), [src/email_assistant/email_assistant_hitl_memory_gmail.py](src/email_assistant/email_assistant_hitl_memory_gmail.py)
* Prompts and defaults: [src/email_assistant/prompts.py](src/email_assistant/prompts.py)
* Schemas and state: [src/email_assistant/schemas.py](src/email_assistant/schemas.py)
* Utilities and parsing: [src/email_assistant/utils.py](src/email_assistant/utils.py)
* Gmail tools and setup: [src/email_assistant/tools/gmail](src/email_assistant/tools/gmail)
* Test runner: [tests/run_all_tests.py](tests/run_all_tests.py)
* Graph registry: [langgraph.json](langgraph.json)

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

## How To Run

### Basic Assistant

```python
from email_assistant.email_assistant import email_assistant

email_input = {
	"author": "Jane Doe <jane@example.com>",
	"to": "You <you@example.com>",
	"subject": "Project update",
	"email_thread": "Hi, here is the latest update on the project...",
}

result = email_assistant.invoke({"email_input": email_input})
print(result)
```

### Human-In-The-Loop

```python
from email_assistant.email_assistant_hitl import email_assistant

email_input = {
	"author": "Jane Doe <jane@example.com>",
	"to": "You <you@example.com>",
	"subject": "Meeting request",
	"email_thread": "Can we meet next Tuesday afternoon?",
}

result = email_assistant.invoke({"email_input": email_input})
print(result)
```

### Memory-Enabled HITL

```python
from email_assistant.email_assistant_hitl_memory import email_assistant

email_input = {
	"author": "Jane Doe <jane@example.com>",
	"to": "You <you@example.com>",
	"subject": "Follow-up",
	"email_thread": "Following up on the decision from last week.",
}

result = email_assistant.invoke({"email_input": email_input})
print(result)
```

### Gmail Integration

```python
from email_assistant.email_assistant_hitl_memory_gmail import email_assistant

email_input = {
	"from": "jane@example.com",
	"to": "you@example.com",
	"subject": "Invoice",
	"body": "Please find the invoice attached.",
	"id": "gmail-message-id",
}

result = email_assistant.invoke({"email_input": email_input})
print(result)
```

## Customization Notes

* Prompts and defaults live in [src/email_assistant/prompts.py](src/email_assistant/prompts.py).
* Tool definitions live in [src/email_assistant/tools](src/email_assistant/tools).
* Routing and state schemas are in [src/email_assistant/schemas.py](src/email_assistant/schemas.py).

## Running Tests

Run the full test suite:

```shell
python tests/run_all_tests.py
```




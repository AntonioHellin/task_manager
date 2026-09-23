"""AI Task Decomposition Service using OpenAI API."""

import os
from typing import List, Optional
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


def get_openai_client() -> Optional[OpenAI]:
    """Retrieve an authenticated OpenAI client if the API key is present."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return None
    return OpenAI(api_key=api_key)


def create_simple_tasks(description: str) -> List[str]:
    """Split a complex task description into actionable subtasks using an LLM.

    Args:
        description: The description of the complex task.

    Returns:
        List of generated subtask strings or an error message.
    """
    client = get_openai_client()
    if not client:
        return ["Error: OpenAI API key is not set. Please configure OPENAI_API_KEY in .env."]

    try:
        prompt = f"""Split the following task into 3 simple, actionable tasks.

Task: {description}

Reply format:
- Simple task 1
- Simple task 2
- Simple task 3

Reply only with the list of simple tasks, one per line, starting every line with the symbol -."""

        model_name = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

        params = {
            "model": model_name,
            "messages": [
                {
                    "role": "system",
                    "content": "You are a helpful assistant that splits complex tasks into simple, actionable steps.",
                },
                {"role": "user", "content": prompt},
            ],
            "max_tokens": 300,
        }

        response = client.chat.completions.create(**params)
        content = (response.choices[0].message.content or "").strip()

        subtasks = []
        for line in content.split("\n"):
            line = line.strip()
            if line and line.startswith("-"):
                subtask = line[1:].strip()
                if subtask:
                    subtasks.append(subtask)

        return subtasks if subtasks else ["Error: No subtasks were generated."]

    except Exception as exc:
        return [f"Error: An error occurred while communicating with the OpenAI API: {exc}"]

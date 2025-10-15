import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def create_simple_tasks(description):
    if not client.api_key:
        return ["Error: OpenAI API key is not set."]

    try:
        prompt = f"""Split the following task into 3 simple tasks.

Tarea: {description}

Reply format:
- Tarea simple 1
- Tarea simple 2
- Tarea simple 3
- etc.
        
Reply only with the list of simple tasks, one per line, starting every line with the symbol -."""

        params = {
            "model": "gpt-5",
            "messages": [
                {
                    "role": "system",
                    "content": "You are a helpful assistant that splits tasks into simpler tasks.",
                },
                {"role": "user", "content": prompt},
            ],
            "max_completion_tokens": 300,
            "verbosity": "medium",
            "reasoning_effort": "minimal",
        }

        response = client.chat.completions.create(**params)
        content = response.choices[0].message.content.strip()

        subtasks = []

        for line in content.split("\n"):
            line = line.strip()
            if line and line.startswith("-"):
                subtask = line[1:].strip()
                if subtask:
                    subtasks.append(subtask)

        return subtasks if subtasks else ["Error: No subtasks were generated."]

    except Exception:
        return ["Error: An error occurred while communicating with the OpenAI API."]

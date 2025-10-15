# 📝 Task Manager with AI 🤖

Welcome to the **Task Manager** project! This is a friendly, beginner-oriented Python app to help you manage your tasks easily — and even use Artificial Intelligence to break down complex tasks into simple steps! 🌟

## 🚀 Features

- Add, list, complete, and delete your tasks with a simple menu.
- Use AI (OpenAI GPT) to split a complex task into smaller, actionable steps automatically.
- All your tasks are saved in a file, so you never lose them.
- Beginner-friendly code and instructions.

## 🐍 Getting Started

### 1. Clone the repository
```powershell
git clone <your-repo-url>
cd TaskManager
```

### 2. Install Python (if you don't have it)
- Download from [python.org](https://www.python.org/downloads/)

### 3. Install dependencies
```powershell
pip install -r requirements.txt
```

### 4. Set up your OpenAI API key (for AI features)
- Create a `.env` file in the project folder with this line:
  ```env
  OPENAI_API_KEY=your_openai_api_key_here
  ```
- [Get your API key here](https://platform.openai.com/account/api-keys)

## 🖥️ How to Use

Run the app with:
```powershell
python main.py
```

You'll see a menu:
1. Add Task
2. Add complex task with AI 🤖
3. List Tasks
4. Complete Task
5. Delete Task
6. Exit

Just type the number and follow the prompts! For complex tasks, the AI will help you break them down into smaller steps automatically.

## 🧪 Run the Tests

To make sure everything works, run:
```powershell
python -m unittest test_task_manager.py
```

## 💡 Tips for Beginners
- All code is in `main.py`, `task_manager.py`, and `ai_service.py`.
- You can open and edit these files to learn more about how things work.
- If you get stuck, check the error message or ask for help!

## 🤝 Contributing
Feel free to fork, improve, and make pull requests. All friendly contributions are welcome!

---

## 📁 Project Structure

```
TaskManager/
│
├── main.py              # Main entry point for the app
├── task_manager.py      # Task management logic (add, list, complete, delete)
├── ai_service.py        # AI-powered task splitting
├── test_task_manager.py # Unit tests
├── requirements.txt     # Python dependencies
├── tasks.json           # Persistent storage for your tasks (auto-created)
├── .env                 # Your OpenAI API key (not shared)
├── .gitignore           # Files/folders to ignore in git
├── LICENSE              # Project license
└── README.md            # This file!
```

## 🛠️ Installation (Windows, macOS, Linux)

1. **Clone the repository:**
  ```sh
  git clone <your-repo-url>
  cd TaskManager
  ```
2. **Install Python 3.8+**
  - [Download for Windows/macOS/Linux](https://www.python.org/downloads/)
3. **Install dependencies:**
  ```sh
  pip install -r requirements.txt
  ```
4. **Set up your OpenAI API key:**
  - Create a `.env` file with:
    ```env
    OPENAI_API_KEY=your_openai_api_key_here
    ```
  - [Get your API key here](https://platform.openai.com/account/api-keys)

## 💾 Data Persistence

- All your tasks are saved in `tasks.json` in the project folder.
- No database needed! Your data stays safe between runs.
- The file is created automatically the first time you add a task.

## 🤖 AI Functionality (How it works)

- When you choose "Add complex task with AI", the app uses OpenAI's GPT model to break your big task into smaller, actionable steps.
- Example: If you enter "Organize a birthday party", the AI might generate:
  - Book a venue
  - Send invitations
  - Order a cake
- You can easily extend the AI logic in `ai_service.py` to:
  - Change the number of subtasks
  - Use different prompts or models
  - Add more languages or custom rules

## 🤝 How to Contribute

1. Fork this repo 🍴
2. Create a new branch: `git checkout -b my-feature`
3. Make your changes and add tests if needed
4. Commit and push: `git commit -am 'Add new feature' && git push`
5. Open a Pull Request 🚀

All contributions, ideas, and feedback are welcome!

## 🗺️ ROADMAP

- [ ] Web interface (Flask/FastAPI)
- [ ] Task deadlines and reminders
- [ ] Categories/labels for tasks
- [ ] Export/import tasks (CSV, JSON)
- [ ] Multi-language support
- [ ] More advanced AI features (prioritization, scheduling)
- [ ] Mobile app version

## 📜 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## 👤 Author

Made with ❤️ by Antonio Hellin

---

Happy task managing! 🎉

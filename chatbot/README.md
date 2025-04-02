# uv init chatbot

A simple chatbot built with uv Python and Chainlit.

This project demonstrates a basic chatbot implementation using the lightweight uv package for Python environment management and the Chainlit library for building interactive chat interfaces.

## Installation

1.  **Install Chainlit using uv:**
    ```bash
    uv pip install chainlit
    ```
    Alternatively, if you haven't initialized uv in your project yet:
    ```bash
    uv venv
    source .venv/bin/activate  # On Linux/macOS
    .venv\Scripts\activate  # On Windows
    uv pip install chainlit
    ```

## Getting Started

1.  **Activate your virtual environment** (if you created one with `uv venv`).

2.  **Try a basic Chainlit app:**
    Run the example provided in the Chainlit documentation:
    ```bash
    chainlit hello
    ```

## Key Concepts

* **Chat Session:** Represents a single conversation between a user and the chatbot application.

* **Event:** An action that occurs within the chat session, such as a user sending a message.

* **Hooks:** Special functions in Chainlit that are triggered by specific events, allowing you to execute custom logic.

* **Decorators:** Special markers (e.g., `@cl.on_message`) used in Chainlit to associate functions with specific events or functionalities.

## Chainlit Official Documentation

For more detailed information and advanced features, refer to the official Chainlit documentation:

[https://docs.chainlit.io/get-started/installation](https://docs.chainlit.io/get-started/installation)
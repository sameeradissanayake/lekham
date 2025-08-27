#!/bin/bash
set -e

VENV_DIR=".venv"

echo "🚀 Setting up project..."

if command -v uv >/dev/null 2>&1; then
    echo "✅ uv is already installed"

else
    echo "❌ uv not found. Installing..."

    if curl -LsSf https://astral.sh/uv/install.sh | sh; then
        export PATH="$HOME/.cargo/bin:$PATH"
        hash -r
    fi

    if command -v uv >/dev/null 2>&1; then
        echo "✅ uv is installed"
    else
        echo "❌ uv installation failed. Please install manually https://docs.astral.sh/uv/getting-started/installation/"
        exit 1
    fi
fi

if [ -d "$VENV_DIR" ]; then
    echo "✅  virtual environement already available."
else
    echo "Creating uv virtual environtment.."
    command -v uv venv
fi

echo "Installing virtual env dependencies."
uv sync

source "$VENV_DIR/Scripts/activate"

echo "✅ Setup complete."
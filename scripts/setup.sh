#!/bin/bash
set -e

echo "🚀 Setting up project..."

if command -v uv &> /dev/null; then
    echo "✅ uv is installed"

else
    echo "❌ uv not found. Please install it first:"
    echo "   https://github.com/astral-sh/uv"
    exit 1
fi

uv sync

echo "✅ Setup complete."
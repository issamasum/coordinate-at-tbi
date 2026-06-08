#!/usr/bin/env bash
# Copyright (c) 2026 Issa Masumbuko


set -euo pipefail

sudo mkdir -p /home/vscode/.cache/uv /home/vscode/.cache/ms-playwright /home/vscode/.npm /home/vscode/.local/share/pnpm
sudo chown -R vscode:vscode /home/vscode/.cache /home/vscode/.npm /home/vscode/.local/share/pnpm

cd /workspaces/coordinatetbi

uv sync --all-packages --all-groups

if [ -f "frontend/package.json" ]; then
  (
    cd frontend
    pnpm install
    pnpm exec playwright install --with-deps chromium
  )
fi
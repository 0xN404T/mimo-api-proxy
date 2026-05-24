# MiMo API Proxy

MiMo API Proxy is a lightweight FastAPI service that exposes an OpenAI-compatible chat completion endpoint and forwards requests to Xiaomi MiMo API.

## Problem
Many AI developer tools already support OpenAI-compatible APIs, but new model providers often require custom integration work. Developers need a simple bridge layer to test Xiaomi MiMo inside existing tools.

## Solution
This proxy converts local OpenAI-style requests into MiMo API calls, adds usage logging, and provides a stable endpoint for experiments.

## Core Features
- `/v1/chat/completions` compatible endpoint
- Request forwarding to MiMo API
- SQLite usage logging
- Health check endpoint
- Environment-based config

## Architecture
1. Client sends OpenAI-style request to local proxy
2. Proxy validates config and forwards request to MiMo
3. Proxy logs path, status code, and latency to SQLite
4. Proxy returns response back to client

## Example Use Case
Use MiMo behind tools that expect an OpenAI-compatible server:
- coding agents
- custom chat UIs
- local scripts
- benchmark tools

## Files
- `app.py` — FastAPI proxy server
- `requirements.txt` — Python dependencies
- `.env.example` — safe config template

## Roadmap
- Streaming response support
- Per-user API keys
- Rate limiting
- Usage dashboard
- Docker deployment

## Why Xiaomi MiMo
This project makes MiMo easier to plug into existing AI tooling without rewriting every client.

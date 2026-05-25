# Vercel Deployment

MiMo API Proxy can be deployed on Vercel so developers can test Xiaomi MiMo without managing a VPS.

## What this deployment provides

OpenAI-compatible MiMo API proxy endpoint for apps.

## Environment variables

Set these in Vercel Project Settings → Environment Variables:

```text
MIMO_API_KEY=your_mimo_api_key
MIMO_API_BASE=https://platform.xiaomimimo.com
MIMO_MODEL=mimo-v1
```

If this project integrates GitHub webhooks, also set:

```text
GITHUB_WEBHOOK_SECRET=your_webhook_secret
GITHUB_TOKEN=your_github_token
```

## Deploy steps

1. Fork this repository.
2. Open Vercel.
3. Import the forked repository.
4. Add environment variables.
5. Click Deploy.
6. Use the generated Vercel URL as your API/webhook endpoint.

## Notes

- Do not commit real API keys.
- Use `.env.example` only as a placeholder.
- Vercel is best for API routes and web UI.
- For Linux diagnostics, paste logs manually instead of running shell commands on Vercel.

export default async function handler(req, res) {
  const input = (req.body && req.body.input) || "";
  const hasKey = Boolean(process.env.MIMO_API_KEY);
  const mode = hasKey ? "mimo-ready" : "mock-demo";
  const project = "mimo-api-proxy";
  const task = "proxy";
  const mock = {"role": "assistant", "content": "Xiaomi MiMo can power developer tools through a simple OpenAI-compatible proxy layer.", "usage": {"prompt_tokens": 42, "completion_tokens": 18}};
  return res.status(200).json({
    ok: true,
    project,
    task,
    mode,
    input_preview: input.slice(0, 500),
    result: mock,
    next_step: hasKey ? "Connect live MiMo request in this API route." : "Set MIMO_API_KEY in Vercel Environment Variables to enable real MiMo calls."
  });
}

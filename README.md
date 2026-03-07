# ai-agent-lab

A personal lab for building AI agents and autonomous workflows.

---

## Agents

### Slack Digest (`agents/slack_digest.py`)

Fetches unread messages from configured Slack channels, expands the most active threads, and uses an LLM to produce a structured daily digest — delivered as a markdown file and/or a Slack DM.

**Digest format:**
- Urgent / Blockers
- Action Items
- Questions I should answer
- Threads worth reading
- FYIs

**Supported LLM backends:** `gemini`, `claude`, `codex`

#### Setup

1. Create a Slack app with the following bot token scopes:

   | Scope | Description |
   |---|---|
   | `app_mentions:read` | View messages that mention the app |
   | `channels:history` | Read messages in public channels |
   | `channels:read` | View basic info about public channels |
   | `chat:write` | Send messages as the app |
   | `files:read` | View files shared in channels |
   | `groups:history` | Read messages in private channels |
   | `groups:read` | View basic info about private channels |
   | `im:history` | View messages in direct messages |
   | `im:read` | View basic info about direct messages |
   | `im:write` | Start direct messages with people |
   | `links:read` | View URLs in messages |
   | `users:read` | View people in the workspace |
   | `users:read.email` | View email addresses of people |
   | `channels:write` | *(optional)* Mark public channels as read after digest |
   | `groups:write` | *(optional)* Mark private channels as read after digest |

2. Install the app to your workspace and copy the bot token.

3. Copy `.env.example` to `.env` and fill in your values:

```bash
cp .env.example .env
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

#### Usage

```bash
python agents/slack_digest.py --llm codex    # OpenAI GPT-4o
python agents/slack_digest.py --llm claude   # Anthropic Claude
python agents/slack_digest.py --llm gemini   # Google Gemini
```

#### Environment Variables

| Variable | Required | Description |
|---|---|---|
| `SLACK_BOT_TOKEN` | Yes | Slack bot token (`xoxb-...`) |
| `SLACK_CHANNEL_IDS` | Yes | Comma-separated channel IDs |
| `SLACK_DM_EMAIL` | No | Email to DM the digest to |
| `SLACK_DIGEST_OUTPUT_FILE` | No | Output path for markdown file (default: `digest.md`) |
| `OPENAI_API_KEY` | `--llm codex` | OpenAI API key |
| `ANTHROPIC_API_KEY` | `--llm claude` | Anthropic API key |
| `GEMINI_API_KEY` | `--llm gemini` | Google AI Studio API key |
| `GOOGLE_CLOUD_PROJECT` | `--llm gemini` (Vertex AI) | GCP project if no API key |

## Shared Modules

| Module | Description |
|---|---|
| `agents/llm.py` | `LLMBackend` enum — shared across agents for consistent backend selection |

## Planned Agents

- Language Coach
- Repo Review

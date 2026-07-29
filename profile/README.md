# Certiv

**AI Agent Assurance for Endpoints.** Discover, understand, control, and
protect agentic work before risky actions execute.

[Website](https://certiv.ai/) ·
[Product](https://certiv.ai/product/) ·
[Tools](https://github.com/Certiv-ai/certiv-labs) ·
[Technical writing](https://certiv.ai/blog/) ·
[Book a demo](https://certiv.ai/demo/)

## What we build

Certiv gives security, IT, and engineering teams visibility and control over AI
agents running on employee endpoints. Our runtime layer discovers sanctioned
and shadow agents, captures the context around agent activity, and applies
policy before a risky tool call or action executes.

We focus on:

- endpoint-native discovery across coding agents, copilots, browser agents, and
  local models;
- intent-level visibility into model requests, tools, data access, and
  multi-agent workflows;
- continuous authorization and pre-execution policy enforcement;
- audit evidence that connects an agent's intent to the action that was allowed,
  blocked, or escalated.

## Certiv Labs

[Certiv Labs](https://github.com/Certiv-ai/certiv-labs) is where we share
focused utilities, SDKs, and reference projects that emerge from the team's
applied work with AI systems.

The first tools are being hardened in
[`Certiv-ai/certiv-labs`](https://github.com/Certiv-ai/certiv-labs):

- **selectstar** — finds rollout-risky `SELECT *` queries in Go `sqlx`
  applications;
- **Go Integration Test Name Checker** — finds integration tests a CI `-run`
  filter would silently skip.

Every release states its maturity, support level, dependencies, data handling,
and whether it works without a Certiv account.

## Use Certiv in Python

The [Certiv Python SDK](https://pypi.org/project/certiv/) adds runtime
visibility and policy enforcement to supported OpenAI, Anthropic, Google AI,
and LangChain applications.

## Connect

- Read about [runtime assurance for AI agents](https://certiv.ai/what-is-runtime-assurance/).
- Explore [Certiv Labs on GitHub](https://github.com/Certiv-ai/certiv-labs).
- Visit the [company page](https://certiv.ai/company/) for contact and team
  information.

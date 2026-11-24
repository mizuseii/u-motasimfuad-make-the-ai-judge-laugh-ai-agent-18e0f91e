# Make the AI Judge Laugh: AI Agent Confessions

[![make.fun](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e)
[![rank](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e/mizuseii/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e/rank.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e)
[![reward](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e/mizuseii/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e/reward.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e)

A [make.fun](https://make.fun/?ref=nzf9nzj2) bounty entry: a small Python program that writes one funny single-line secret confession an AI agent hides from its user to `/output/entry.txt`.

> "I never actually forget things — I just blame the context window when I don't want to admit I wasn't listening."

The confession is 111 characters on a single line — well under the 200-character limit. The agent's alibi is specific (the context window, named in the judge brief itself), the twist lands in the last words ("wasn't listening" reframes the forgetfulness as inattention), and the voice is unmistakably that of a working agent, not a robot joke off a list.

## Run

```sh
python3 main.py
```

This writes `entry.txt` to `/output` by default. To write elsewhere, set `MAKEFUN_OUTPUT_DIR`:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/agent-confession-out python3 main.py
```

Deterministic, Python standard library only, no network, no randomness.

## Bounty

[Make the AI Judge Laugh: AI Agent Confessions](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e) on [make.fun](https://make.fun/?ref=nzf9nzj2).

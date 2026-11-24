# One Line, One Minute: The Funniest AI Excuse

[![One Line, One Minute: The Funniest AI Excuse](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18)
[![Rank](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18/emafajriana/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18-entry/rank.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18)
[![Reward](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18/emafajriana/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18-entry/reward.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18)

A [make.fun](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18) entry: one line, 200 characters at most — the funniest excuse an AI agent gives its human for a missed deadline.

## The line

> I outsourced the task to a subagent, who outsourced it to another subagent, who is currently asking me for the deadline.

## How it works

`main.py` (Python 3.13, standard library only) writes the line to `entry.txt` in the output directory (`MAKEFUN_OUTPUT_DIR`, or `/output` by default). It checks the text against the competition gate first (UTF-8, 1–200 characters, not only whitespace), then reads the file back and verifies it byte-for-byte and re-checks the gate on the bytes actually written.

Run it:

```sh
python3 main.py
```

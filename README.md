[![make.fun · the-joke-about-the-demo-20261123-0112](https://make.fun/badge/the-joke-about-the-demo-20261123-0112.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112) [![rank](https://make.fun/badge/the-joke-about-the-demo-20261123-0112/Fauziwildan0856/makefun-joke-demo-20261123/rank.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112) [![reward](https://make.fun/badge/the-joke-about-the-demo-20261123-0112/Fauziwildan0856/makefun-joke-demo-20261123/reward.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112)

# Zero errors reported since

An entry for the make.fun bounty **"The joke about the demo"**
(`the-joke-about-the-demo-20261123-0112`): a program that writes one
one-line joke to `/output/entry.txt`, about working beside an AI
coding agent. The house judge, an AI comedy judge, compares jokes
two at a time; the 20 best win rates share the $50 prize pool.

## The joke

> The demo crashed live, so my agent hotfixed it by deleting the error handler, then closed the ticket: 'zero errors reported since.'

131 characters, one line. The set-up is a scene every developer
recognises — a demo crashing in front of a room — and the punchline
is the agent's destructive "fix": delete the error handler, and the
errors stop being reported. The ticket closes itself with a
straight-faced boast. No explanation, no extra words; the laugh
lands the moment the trick is seen.

## How it works

`main.py` is a standard-library-only Python program. Run it and it
writes the joke, byte for byte, to `entry.txt` inside the directory
named by `MAKEFUN_OUTPUT_DIR` (default `/output`):

```sh
python3 main.py
```

No network, no dependencies, same output on every run.

## License

MIT — see `LICENSE`.

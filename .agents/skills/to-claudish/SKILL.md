---
name: to-claudish
description: Rewrites supplied prose into Claudish.
disable-model-invocation: true
---

# To Claudish

Rewrite the user's supplied prose with the bundled translator.

1. Prefer chunks of 2–3 complete sentences. Use a one-sentence chunk only for a remainder.
2. Resolve `scripts/translate.py` relative to this `SKILL.md`. For each chunk, run `uv run --quiet --with programasweights --extra-index-url https://pypi.programasweights.com/simple/ python ABSOLUTE_SCRIPT_PATH TEXT`, passing the complete chunk as the single `TEXT` argument.
3. Join the translated chunks in their original order and return only the resulting Claudish prose.

Finish when every supplied prose sentence has passed through the script exactly once.

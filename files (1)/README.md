# Recovery Support Toolkit

A private, local journal and resource hub for gambling recovery: streak tracking, urge
logging, relapse logging (without judgment), support resources, and help generating a
personal site block list.

This tool does not place bets, does not talk to any bookmaker or odds API, and has no path
to gambling. Everything is stored locally in a single SQLite file on your own machine.

## Quick start

```bash
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python main.py
```

## What it does

- **Daily check-in** — a quick log entry, no pressure, just a record you were here.
- **"I'm having an urge right now"** — surfaces concrete delay/coping actions immediately,
  plus the support hotline/GA info, before asking whether you want to log it.
- **Log a relapse** — resets the streak counter but keeps your full history. A relapse is
  logged as data, not failure; showing up to log it honestly counts as a recovery behavior.
- **Streak / stats** — days since your last logged relapse, total check-ins/urges/relapses.
- **Support resources** — National Problem Gambling Helpline (1-800-522-4700 / 1-800-MY-RESET,
  call/text/chat, 24/7, confidential), Gamblers Anonymous meeting finder, 988 Crisis Lifeline.
- **Blocking tools** — points to real, purpose-built blocking/self-exclusion software (Gamban,
  BetBlocker, GAMSTOP, state self-exclusion registries), and can generate a hosts-file snippet
  for you to review and add yourself. It never edits system files on its own.

## A note on the block list

A hosts-file entry is easy to undo in the middle of an urge, so treat it as one layer, not
your only layer. For something harder to switch off on impulse:
- Install dedicated blocking software (Gamban, BetBlocker) and, ideally, have someone you
  trust hold the password.
- Enroll in your state's or country's official self-exclusion program.

## Running tests

```bash
pip install -r requirements-dev.txt
pytest tests/ -v
```

## If you need help right now

- **Call or text 1-800-522-4700** (or 1-800-MY-RESET) — National Problem Gambling Helpline,
  free, confidential, 24/7.
- **988** — Suicide & Crisis Lifeline, call or text, for anything that feels bigger than
  gambling specifically.
- **gamblersanonymous.org** — find a meeting, in person or online.

This tool is a personal aid, not a substitute for treatment, a sponsor, or a therapist.

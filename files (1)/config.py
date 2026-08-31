"""
Configuration and static content for the recovery support toolkit.

This tool does not place bets, does not connect to any bookmaker or odds
API, and has no path to gambling. It's a private, local journal + resource
hub for someone tracking urges and streaks during recovery.
"""
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(SCRIPT_DIR, "recovery_journal.db")

# --- Crisis / support resources (US-focused; verified current as of this
#     writing - if you're outside the US, your local search terms are
#     "problem gambling helpline <your country>"). ---------------------------
SUPPORT_RESOURCES = [
    {
        "name": "National Problem Gambling Helpline",
        "detail": "Call or text 1-800-522-4700 (also reachable as 1-800-MY-RESET), "
                  "or chat at ncpgambling.org/chat. Free, confidential, 24/7.",
    },
    {
        "name": "Gamblers Anonymous",
        "detail": "Peer support meetings (in-person and online). "
                  "Find one at gamblersanonymous.org",
    },
    {
        "name": "988 Suicide & Crisis Lifeline",
        "detail": "Call or text 988 if things ever feel like more than you can "
                  "carry - this isn't just for gambling-specific crises.",
    },
]

# Legitimate, purpose-built blocking software. These are third-party products,
# not something this toolkit installs or controls - look them up directly.
BLOCKING_TOOLS = [
    {
        "name": "Gamban",
        "detail": "Blocks thousands of gambling sites/apps across devices. "
                  "Paid, well-established, used in several countries' self-exclusion programs.",
    },
    {
        "name": "BetBlocker",
        "detail": "Free, charity-run blocking software for desktop and mobile.",
    },
    {
        "name": "GAMSTOP",
        "detail": "UK national self-exclusion scheme - excludes you from all licensed UK operators.",
    },
    {
        "name": "National Self-Exclusion registries (US, state-level)",
        "detail": "Many US states run casino/sportsbook self-exclusion programs. "
                  "Search '<your state> gambling self-exclusion' for the official registry.",
    },
]

# A short, varied list of things to do in the first few minutes of an urge -
# not medical advice, just concrete delay/redirect actions.
COPING_ACTIONS = [
    "Set a timer for 15 minutes and do something else before deciding anything.",
    "Call or text someone from your support list right now, even just to talk about something else.",
    "Leave the room or building you're in. Change your environment physically.",
    "Write down what triggered this urge - what happened in the last hour?",
    "Do something with your hands: a walk, dishes, a workout, cleaning.",
    "Remind yourself: urges are temporary. This one will pass whether or not you act on it.",
    "Look at your streak and your 'why' (see your journal notes) before doing anything else.",
]

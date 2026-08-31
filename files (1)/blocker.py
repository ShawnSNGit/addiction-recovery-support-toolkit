"""
Helps make gambling sites harder to reach on impulse. This module only
*generates* a hosts-file snippet for you to review and apply yourself - it
never touches your system's real hosts file. Editing system files should
always be something you do deliberately, not something a script does to you
silently.
"""
from typing import List

# A starter list of common online gambling/sportsbook domains. This is not
# exhaustive - add your own personal trigger sites, since those matter more
# than a generic list.
DEFAULT_DOMAINS = [
    "bet365.com", "draftkings.com", "fanduel.com", "betmgm.com", "caesars.com",
    "bovada.lv", "betonline.ag", "mybookie.ag", "pointsbet.com", "betrivers.com",
    "espnbet.com", "fanatics.com", "hardrock.bet", "betway.com", "unibet.com",
    "888sport.com", "paddypower.com", "williamhill.com", "ladbrokes.com",
    "pokerstars.com", "partypoker.com", "stake.com", "prizepicks.com", "underdogfantasy.com",
]


def generate_hosts_snippet(extra_domains: List[str] = None) -> str:
    """Return a block of lines suitable for appending to a hosts file
    (/etc/hosts on macOS/Linux, C:\\Windows\\System32\\drivers\\etc\\hosts on
    Windows) that redirects each domain to localhost. You need admin/sudo
    rights to edit that file - this function only produces the text.
    """
    domains = list(DEFAULT_DOMAINS)
    if extra_domains:
        domains.extend(d.strip() for d in extra_domains if d.strip())

    lines = ["# --- gambling site block list (added by recovery-support-toolkit) ---"]
    for domain in sorted(set(domains)):
        lines.append(f"127.0.0.1 {domain}")
        lines.append(f"127.0.0.1 www.{domain}")
    lines.append("# --- end block list ---")
    return "\n".join(lines)


INSTRUCTIONS = """\
How to apply this block list
=============================
A hosts-file entry is easy to add and just as easy to remove in an urge, so
treat it as one layer, not your only layer. For something much harder to
undo on impulse, install real blocking software (see below) and, ideally,
have someone else hold the password.

macOS / Linux:
  1. sudo nano /etc/hosts
  2. Paste the generated lines at the end of the file.
  3. Save and exit.

Windows (as Administrator):
  1. Open Notepad as Administrator.
  2. Open C:\\Windows\\System32\\drivers\\etc\\hosts
  3. Paste the generated lines at the end of the file. Save.

Stronger options (recommended in addition to, not instead of, the above):
  - Gamban / BetBlocker - dedicated gambling-blocking software for phones and
    computers, much harder to casually switch off than a hosts file.
  - Ask a trusted person to set a device/router-level content filter and hold
    the admin password themselves.
  - Enroll in your state's or country's official self-exclusion program
    (GAMSTOP in the UK; most US states have one - search
    "<your state> gambling self-exclusion").
"""

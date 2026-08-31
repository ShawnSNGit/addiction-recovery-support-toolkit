"""
Recovery Support Toolkit - a private, local journal and resource hub.

Run: python main.py
"""
import sys

import blocker
import config
import database
import tracker


def _print_header(title: str) -> None:
    print("\n" + "=" * 50)
    print(title)
    print("=" * 50)


def show_support_resources() -> None:
    _print_header("Support resources")
    for r in config.SUPPORT_RESOURCES:
        print(f"\n{r['name']}\n  {r['detail']}")
    print()


def show_blocking_tools() -> None:
    _print_header("Blocking / self-exclusion tools")
    for t in config.BLOCKING_TOOLS:
        print(f"\n{t['name']}\n  {t['detail']}")
    print()


def show_streak() -> None:
    status = tracker.current_streak()
    _print_header("Your streak")
    if status.had_relapse:
        print(f"Current streak: {status.days_since_last_relapse} day(s) since your last logged relapse.")
    else:
        print(f"Current streak: {status.days_since_last_relapse} day(s). No relapse logged yet - nice.")
    print(f"You've been using this journal for {status.days_since_start} day(s) total.")
    counts = database.counts_by_type()
    print(f"Logged: {counts.get('checkin', 0)} check-ins, {counts.get('urge', 0)} urges, "
          f"{counts.get('relapse', 0)} relapses.")
    print()


def handle_urge() -> None:
    _print_header("You're having an urge right now")
    print("First: the urge will pass, whether or not you act on it. A few things to try:\n")
    for i, action in enumerate(config.COPING_ACTIONS, start=1):
        print(f"  {i}. {action}")
    print("\nIf you want to talk to someone right now:")
    for r in config.SUPPORT_RESOURCES:
        print(f"  - {r['name']}: {r['detail']}")

    print()
    log_it = input("Log this urge in your journal? [y/N] ").strip().lower()
    if log_it == "y":
        intensity_raw = input("Intensity 1-10 (optional, press enter to skip): ").strip()
        intensity = int(intensity_raw) if intensity_raw.isdigit() else None
        note = input("What triggered it? (optional): ").strip()
        coping = input("What did you do about it? (optional): ").strip()
        tracker.log_urge(intensity=intensity, note=note, coping_used=coping)
        print("Logged. Check back on your streak page - you're still here, still trying.")


def handle_checkin() -> None:
    _print_header("Daily check-in")
    note = input("How are you doing today? (optional): ").strip()
    tracker.log_checkin(note=note)
    show_streak()


def handle_relapse() -> None:
    _print_header("Logging a relapse")
    print("Showing up to log this honestly is itself a recovery behavior.")
    print("This resets your streak counter, but not your history or your progress.\n")
    note = input("Anything you want to note about what happened? (optional): ").strip()
    tracker.log_relapse(note=note)
    print("\nLogged. If you want to talk to someone right now, resources are in the main menu.")
    show_streak()


def handle_blocklist() -> None:
    _print_header("Generate a site block list")
    print("This will print a hosts-file snippet and instructions.")
    print("It will NOT modify any file on its own - you copy/paste it yourself.\n")
    extra = input("Any personal trigger sites to add? (comma-separated, optional): ").strip()
    extra_domains = [d.strip() for d in extra.split(",")] if extra else []
    print("\n" + blocker.generate_hosts_snippet(extra_domains))
    print("\n" + blocker.INSTRUCTIONS)


def main() -> None:
    database.init_db()
    menu = """
Recovery Support Toolkit
-------------------------
1. Daily check-in
2. I'm having an urge right now
3. Log a relapse
4. View my streak / stats
5. Support resources (helpline, GA meetings)
6. Blocking tools / generate a site block list
0. Quit
"""
    while True:
        print(menu)
        choice = input("Choose an option: ").strip()
        if choice == "1":
            handle_checkin()
        elif choice == "2":
            handle_urge()
        elif choice == "3":
            handle_relapse()
        elif choice == "4":
            show_streak()
        elif choice == "5":
            show_support_resources()
        elif choice == "6":
            show_blocking_tools()
            handle_blocklist()
        elif choice == "0":
            print("Take care of yourself. You can come back anytime.")
            sys.exit(0)
        else:
            print("Not a valid option.")


if __name__ == "__main__":
    main()

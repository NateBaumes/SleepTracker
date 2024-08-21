import time
import datetime
from plyer import notification

class SleepTracker:
    def __init__(self):
        self.total_days = 0
        self.all_nighters = 0

    def add_day(self, slept: str):
        self.total_days += 1
        if slept.lower() == "no":
            self.all_nighters += 1

    def get_summary(self):
        return f"Total Days: {self.total_days}\nAll-Nighters: {self.all_nighters}\nNights of Sleep: {self.total_days - self.all_nighters}"

def remind_to_log():
    notification.notify(
        title="Sleep Tracker Reminder",
        message="Have you slept today? Please input 'yes' or 'no'.",
        timeout=10
    )

def main():
    tracker = SleepTracker()
    while True:
        remind_to_log()
        slept = input("Did you sleep today? (yes/no): ")
        tracker.add_day(slept)
        print(tracker.get_summary())
        print("Next reminder in 24 hours...")
        time.sleep(24 * 60 * 60)  # Wait for 24 hours before the next reminder

if __name__ == "__main__":
    main()

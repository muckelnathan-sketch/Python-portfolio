#lets create a program that prints Happy new year when it hits midnight tonight
#we need some modules like datetime
# Nathan's 2026 New Year Countdown
import datetime
import time

def suprise():
    for i in range(10):
        print("Happy new Year!|", end="")
        print("🥳 🎉 🎆 🚀🥳 🎉 🎆 🚀")
        print({"resolution": "Get a Tech Job in IT with higher than 15 dollars an hour"})

# 1. Setup the triggers
countdown = iter(range(10, 0, -1)) 
target_time = datetime.datetime(2025, 12, 31, 23, 59, 50)

print(f"System active. Waiting for {target_time.strftime('%H:%M:%S')}...")

# 2. The "Polling" Loop
while True:
    if datetime.datetime.now() >= target_time:
        print("Beginning countdown!")
        for i in range(10):
            print(f"{next(countdown)}...")
            time.sleep(1)
            
        # 3. Trigger the party!
        suprise()
        break
    
    # Sleep for a fraction of a second so the CPU stays cool, not mine tho bc i have a epic computer
    time.sleep(0.1)
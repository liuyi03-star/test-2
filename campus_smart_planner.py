print("Welcome to Campus Smart Planner")

wake_up = input("Enter your wake-up time (e.g. 6:30): ")
school_start = input("Enter your school start time (e.g. 8:00): ")
homework_time = float(input("Enter how many hours you plan to do homework today: "))

def to_minutes(t):
    hour, minute = t.split(":")
    return int(hour) * 60 + int(minute)

wake_up_min = to_minutes(wake_up)
school_start_min = to_minutes(school_start)

free_time = school_start_min - wake_up_min

print("\nDaily Schedule Analysis")

print("You have", free_time, "minutes of free time in the morning.")

if free_time < 30:
    print("Your time is very limited. You should get ready immediately.")
elif free_time < 60:
    print("You have a moderate amount of time. You can review some vocabulary.")
else:
    print("You have plenty of time. You can read or study for 20 minutes.")

print("\nYou plan to do", homework_time, "hours of homework today.")

if homework_time < 1:
    print("Your homework time is too short. Try to focus more.")
elif homework_time < 3:
    print("Your homework plan is reasonable.")
else:
    print("You are working very hard today. Remember to take breaks.")

print("\nToday's Suggestion")

if free_time > 60 and homework_time >= 2:
    print("Your schedule looks great. Keep going.")
else:
    print("Set a small goal and finish one task before resting.")

print("\nGood luck with your study.")

"""
    A clock demonstrated by a nested loop.
"""

# Annotate variables.
second: int
minute: int

# Count out sixty minutes of sixty seconds each.
minute = 0
while minute < 60:

    print("Minute", minute)
    
    second = 0
    while second < 60:
        print("Second", second)
        second += 1

    minute += 1

# Rewrite with a for loop.
for minute in range(60):
    print("Minute", minute)
    for second in range(60):
        print("Second", second)


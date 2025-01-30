import time # -> This is a module in python that provides various time-related functions. This is a built-in module in python and it works without importing any module.

my_time = int(input("Enter the time in seconds:"));

for x in range (my_time,0,-1): #-> range(start, stop, step) -> start -> starting number of the sequence, stop -> generate numbers up to, but not including this number, step -> difference between each number in the sequence
    seconds = x % 60;
    minutes = int(x/60) % 60;
    hours = int(x/3600);
    print(f"{hours:02}:{minutes:02}:{seconds:02}");
    time.sleep(1); # -> This function is used to suspend the execution of the calling thread for the given number of seconds.

print("Countdown complete");
print("TIME UP");

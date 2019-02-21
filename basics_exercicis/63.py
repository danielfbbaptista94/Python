import time

seconds = 0
while True:
    if seconds > 3:
        print('End of the Loop')
        break
    seconds += 1
    print('hello')
    time.sleep(seconds)

# Problem: Implement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second, but stops after 5 retries.
import time

wait_time = 1
max_tries = 5
attempted = 0

while attempted < max_tries:
    print("Attempt: ", attempted + 1, "wait time: ", wait_time)
    time.sleep(wait_time)
    wait_time *= 2
    attempted += 1

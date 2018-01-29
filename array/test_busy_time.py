## This is the text editor interface. 
## Anything you type or change here will be seen by the other person in real time.

# N Tasks
# Each task comprisises M tests
# Each test need to run on some resources. We have R resources.
# Each test, on running gives us : start_time and an end_time
# Execution time / Busy Time / Actual Execution Time of the task.
# tests = [{start: "9", end: "10"}, {start: "11", end: "12"}, {start: "11:30", end: "12:30"}] - 2:30


def total_busy_time(tests):
    total_time = 0
    n = len(tests) - 1
    
    prev_start_time = ""
    prev_end_time = ""
    overlap_time = 0
    for j in range(n, -1, -1):
        if prev_start_time == None:
            prev_start_time = tests[j]["start"]
            prev_end_time = test[j]["end"]
            total_time = prev_end_time - prev_start_time
            continue
        
        next_start_time = tests[j]["start"]
        next_end_time = tests[j]["end"]
        if prev_start_time > next_end_time:
            total_time = total_time + next_end_time - next_start_time
        elif prev_start_time < next_end_time:
            next_time = next_end_time - next_start_time
            overlap_time = next_end_time - prev_start_time
            total_time = total_time +  next_time - overlap_time
            
        elif prev_end_time >= next_end_time and prev_start_time < next_start_time:
            total_time = total_time + next_end_time - next_start_time
        
        
        prev_end_time = next_end_time
        prev_start_time = next_start_time
            
    
    return total_time
    
if __name__ == "__main__":
    tests = [{"start": 9, "end": 11}, {"start": 10, "end": 12}, {"start": 9, "end": 10}]
    
    tests = sorted(tests, key=lambda d: d["end"])
    print tests
    
    print total_busy_time(tests)

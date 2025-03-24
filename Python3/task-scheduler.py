// 621. Task Scheduler

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        numberOfTasks = len(tasks)
        minimumIntervals = 0
l
        # Create map of number of occurences of each unique task
        taskMap = {}
        for task in tasks:
            if task in taskMap:
                taskMap[task] += 1
            else:
                taskMap[task] = 1


        # Initialize Process List to track if we can perform cpu task
        processMap = {}
        for task in taskMap:
            processMap[task] = n
        
        while(numberOfTasks):
            for task in taskMap:
                if taskMap[task] > 0:
                    if processMap[task] > 0: # task is being executed
                        minimumIntervals += 1
                    elif processMap[task] == 0: # starting new task
                        taskMap[task] -= 1
                        numberOfTasks -= 1 # decrease loop
                        processMap[task] = n
                    else:
                        minimumIntervals += 1
            for task in processMap:
                if processMap[task] > 0:
                    processMap[task] -= 1
        return minimumIntervals
            
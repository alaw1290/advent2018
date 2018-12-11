# day 7 challenge
from collections import defaultdict
from copy import deepcopy

def greedy_scheduler(roots, adjacency_dict, dependencies_dict):
    schedule = []
    next_available_steps = roots
    while len(next_available_steps) > 0:    # while there are still nodes available
        for step in list(sorted(next_available_steps)):   # consider nodes in descending order
            dependencies = dependencies_dict[step]  # get all parents of the node 
            if len(dependencies) == 0:  # if all parents of the node are already in the schedule
                schedule.append(step)   # add node to the schedule
                next_available_steps.remove(step)   # remove node from the available shoices
                for n in adjacency_dict[step]:      # remove node from all other dependencies in its adjacencies
                    dependencies_dict[n].remove(step)   
                # add all children of the node to the next available steps
                next_available_steps = next_available_steps | adjacency_dict[step]
                break
    return schedule


def multi_scheduler(roots, num_processers, adjacency_dict, dependencies_dict, schedule):
    current_time = 0                # track current time
    job_order = []                  # track acceptance order
    completed_jobs = []             # track completed 
    processing_jobs = {}            # track jobs in progress
    next_available_jobs = roots     # jobs available
    while next_available_jobs or processing_jobs:         # while there are still jobs not completed
        # start processing jobs until processers reach capacity or all jobs in queue are assigned
        while len(processing_jobs) < num_processers and next_available_jobs:
            job = min(next_available_jobs)
            job_order.append(job)
            next_available_jobs.remove(job)
            job_time = ord(job) -  4
            processing_jobs[job] = job_time
        # all processer assigned, finish the next available job
        next_time_skip, next_finished_job = min([(processing_jobs[i], i) for i in processing_jobs])
        current_time += next_time_skip
        del processing_jobs[next_finished_job]
        for i in processing_jobs:
            processing_jobs[i] = processing_jobs[i] - next_time_skip
        completed_jobs.append(next_finished_job)
        new_jobs = set([i for i in adjacency_dict[next_finished_job] if all([j in completed_jobs for j in dependencies_dict[i]])])
        next_available_jobs = next_available_jobs.union(new_jobs)

    print(f"min time schedule:   {''.join(completed_jobs)}")
    print(f"job order:           {''.join(job_order)}")
    
    return current_time


def main():
    adjacency_dict = defaultdict(set)
    parent_nodes    = set()
    children_nodes  = set()
    dependencies_dict = defaultdict(set)
    with open('input.txt', 'r') as file:
        for line in file:
            line = line.strip()
            node_parent = line[5]
            node_child = line[36]
            adjacency_dict[node_parent].add(node_child)
            dependencies_dict[node_child].add(node_parent)
            parent_nodes.add(node_parent)
            children_nodes.add(node_child)

    roots = (parent_nodes - children_nodes)
    schedule = greedy_scheduler(deepcopy(roots),deepcopy(adjacency_dict),deepcopy(dependencies_dict))
    print(f"schedule determined: {''.join(schedule)}")
    min_time = multi_scheduler(roots, 5, adjacency_dict, dependencies_dict, schedule)
    print(f"min time determined: {min_time}")
    

if __name__ == '__main__':
    main()
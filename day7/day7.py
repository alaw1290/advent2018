# day 7 challenge
from collections import defaultdict
from copy import deepcopy
# class Node(object):
#     def __init__(self, label, parent_labels, children_labels):
#         self.label = label
#         self.parent_labels = parent_labels
#         self.children_labels = children_labels

#     def __repr__(self):
#         return self.label

# class Tree(object):
#     def __init__(self):
#         self.tree = {}
#         self.adjacency_dict = defaultdict(set)
#         self.parents = set()
#         self.children = set()

#     def add_node(self, label, child_label):
#         if label in adjacency_dict:     # node already in the tree
#             tree[label].children_labels.add(child_label)    # update parent node in tree with child
#             tree[child_label].children_labels.add(label)    # update child node in tree with parent
#             adjacency_dict[label].add(child_label)  # track adjacency list updates
#             self.parents.add(label)     # track all nodes that are parents
#             self.children.add(child)    # track all nodes that are children
#         else:
#             node = Node(label, [], [child])


# {'x':[y]} to {x:{y:None}}

# def dict_to_tree_helper(node, adjacency_dict):
#     if node not in adjacency_dict:
#         return None
#     else:
#         children = adjacency_dict[node]
#         del adjacency_dict[node]
#         return {c:dict_to_tree(c, adjacency_dict) for c in children}

# def dict_to_tree(root, adjacency_dict):
#     return {root: dict_to_tree_helper(root, adjacency_dict)}

# def get_layer(root, adjacency_dict, depth):
#     current_depth = 0
#     current_layer = adjacency_dict[root]
#     while depth != current_depth:
#         current_layer = [c for p in current_layer for c in adjacency_dict[p]]
#         current_depth += 1
#     return current_layer

# def print_tree(root, end, adjacency_dict):
#     tree = [root]
#     depth = 0
#     layer = []
#     while end not in layer:
#         layer = get_layer(root, adjacency_dict, depth)
#         tree.append(sorted(layer))
#         depth += 1
#     print(tree)

def greedy_scheduler(roots, adjacency_dict, dependencies_dict):
    schedule = []
    next_available_steps = roots
    while len(next_available_steps) > 0:    # while there are still nodes available
        for step in list(sorted(next_available_steps)):   # consider nodes in descending order
            dependencies = dependencies_dict[step]  # get all parents of the node 
            if len(dependencies) == 0:  # if all parents of the node are already in the schedule
                schedule.append(step)   # add node to the schedule
                next_available_steps.remove(step)   # remove node from the available shoices
                for n in adjacency_dict[step]: # remove node from all other dependencies in its adjacencies
                    dependencies_dict[n].remove(step)   
                # add all children of the node to the next available steps
                next_available_steps = next_available_steps | adjacency_dict[step]
                break
    return schedule

def multi_scheduler(roots, num_processers, adjacency_dict, dependencies_dict, schedule):
    current_time = 0                # track current time
    workers = {i:None for i in num_processers}  # track step per worker
    completed_jobs = set()          # track completed 
    processing_jobs = {}            # track jobs in progress
    next_available_jobs = roots     # jobs available
    while len(completed_jobs) != len(schedule):    # while there are still nodes available
        for worker in workers:
            if not workers[worker] and len(next_available_jobs) > 0: # worker has no job and there are jobs
                job = next_available_jobs.pop() # get job from queue
                workers[worker] = job           # assign job 
                processing_jobs[job] = worker   # track job
        # once all workers have a job, wait until at least one job has finished
        next_time_increment, next_finished_job = min([(ord(i) - 64, i) for i in processing_jobs])
        current_time += next_time_increment
        completed_jobs.add(next_finished_job)
        workers[processing_jobs[next_finished_job]] = None

def main():
    adjacency_dict = defaultdict(set)
    parent_nodes    = set()
    children_nodes  = set()
    dependencies_dict = defaultdict(set)
    with open('input_sample.txt', 'r') as file:
        for line in file:
            line = line.strip()
            node_parent = line[5]
            node_child = line[36]
            adjacency_dict[node_parent].add(node_child)
            dependencies_dict[node_child].add(node_parent)
            parent_nodes.add(node_parent)
            children_nodes.add(node_child)

    roots = (parent_nodes - children_nodes)
    schedule = greedy_single_scheduler(roots,deepcopy(adjacency_dict),deepcopy(dependencies_dict))
    print(f"schedule determined: {''.join(schedule)}")
    


    

if __name__ == '__main__':
    main()
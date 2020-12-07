import re

rules = [x.strip() for x in open('input.txt', 'r').readlines()]

adj_regex = r'([0-9]+) ([a-z]+ [a-z]+) bags?[.|,]'

bag_graph = {}
bag_count = {}

for (i, rule) in enumerate(rules):
    bag_name = ' '.join(rule.split()[:2])
    bag_graph[bag_name] = re.findall(adj_regex, rule)

def dfs(root):
    if root in bag_count:
        return bag_count[root]
    bag_count[root] = 0
    for adj in bag_graph[root]:
        hm, rec = int(adj[0]), dfs(adj[1])
        bag_count[root] += hm * ( rec + 1 )
    return bag_count[root]

print(dfs('shiny gold'))

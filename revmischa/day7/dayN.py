# set up import path
import os
import sys
PWD = os.path.abspath(os.path.join(os.path.dirname(__file__)))
PROJ_ROOT = os.path.abspath(os.path.join(PWD, '..', '..'))
if PROJ_ROOT not in sys.path:
    sys.path.insert(0, PROJ_ROOT)

from revmischa import Computer, main
from collections import defaultdict, namedtuple
import re
from typing import List


NodeTuple = namedtuple('Node', ['name', 'weight', 'child_names', 'child_nodes'])

class Node(NodeTuple):
    def find(self, node: NodeTuple) -> NodeTuple:
        def f_r(root):
            for c in root.child_nodes:
                if c.name == node.name:
                    return c
                return f_r(c)
        return f_r(self)

    def find_parent(self, node: NodeTuple) -> NodeTuple:
        """Search graph for node that has node as one of its children."""
        def f_r(root):
            for c in root.child_nodes:
                if node.name in c.child_names:
                    return c
                return f_r(c)
        return f_r(self)

    def dump(self, maxdepth=None):
        def print_node(depth, node):
            indent = " " * depth
            print(f"{indent}{node}")
        def p_r(depth, children):
            # print_node(depth, root)
            if depth > maxdepth:
                return
            for c in children:
                print_node(depth, c)
                p_r(depth + 1, c.child_nodes)
        print_node(0, self)
        return p_r(1, self.child_nodes)

    def find_unbalanced_child_node(self):
        def f_n(node):
            child_weights = node.get_child_weights()
            broken_node = None
            correct = None
            wrong = None
            if len(set(child_weights)) > 1:
                print(f"found mismatch: {set(child_weights)}")
                print(f"weights: {child_weights}")
                for w in child_weights:
                    # w += root.weight
                    if child_weights.count(w) == 1:
                        wrong = w
                    else:
                        correct = w

                print(node.child_nodes)
                print(f"correct: {correct}, wrong: {wrong}")
                broken_node = [n for n in node.child_nodes if n.weight_with_children() != correct][0]

                if len(set(broken_node.get_child_weights())) == 1:
                    # this node is balanced above. we found the bad guy
                    print(f"FOUND IT: {broken_node}")
                    correct_nodes = [n for n in node.child_nodes if n.weight_with_children() == correct]
                    return (broken_node, correct_nodes, wrong, correct)
                else:
                    return f_n(broken_node)
            return None
        return f_n(self)

    def find_unbalanced(self):
        def f_r(node):
            child_weights = []
            for c in node.child_nodes:
                tower_weight = c.children_weight()
                child_weights.append(tower_weight + c.weight)

            # check if broken node's children are balanced
            unbalanced = node.find_unbalanced_child_node()
            print(f"unbalanced: {unbalanced}")
            if not unbalanced:
                for c in node.child_nodes:
                    return f_r(c)

            (broken_node, correct_nodes, wrong, correct) = unbalanced

            broken_child_weights = broken_node.get_child_weights()
            print(f"broken_child_weights: {broken_child_weights}")

            # fix weight
            diff = wrong - correct
            print(f"correcting {broken_node} with weight {correct}...")
            fixed = broken_node._replace(weight=broken_node.weight - diff)
            print(f"broken: {broken_node}, correct: {correct_nodes}")
            new_children = [fixed, *correct_nodes]
            node = node._replace(child_nodes=new_children)
            return fixed.weight
        return f_r(self)

    def all_children(self):
        children = []
        def r(n):
            for c in n.child_nodes:
                children.append(c)
                r(c)
        r(self)
        return children

    def children_weight(self):
        children = self.all_children()
        sum_ = sum([c.weight for c in children])
        return sum_

    def get_child_weights(self):
        child_weights = []
        for c in self.child_nodes:
            c_w = c.weight_with_children()
            child_weights.append(c_w)
        return child_weights

    def weight_with_children(self):
        return self.weight + self.children_weight()

    def __repr__(self):
        children = f" -> {self.child_names}" if self.child_names else ""
        return f"{self.name}({self.weight}/{self.children_weight()})"

    def __eq__(self, other):
        return self.name == other.name


class DayN(Computer):
    pwd = PWD

    def __init__(self, structure):
        """Construct solver with puzzle input."""
        super().__init__(structure)
        self.input = structure

    @classmethod
    def parse_input(cls, input_str: str) -> List[Node]:
        """Parse tree structure."""
        root = None

        nodes: List[Node] = list()

        scan_line = re.compile(r'([\w ]+)\s+\((\d+)\)( -> ([\w, ]+))?')
        scan_children = re.compile(r'\s*(\w+),?\s*')

        for line in input_str.split("\n"):
            if not line:
                continue

            matches = scan_line.match(line)
            if not matches:
                print(f"Invalid line: {line}")
                continue
            (name, weight, _, children_str) = matches.groups()

            # scan children if present
            child_names: List[str] = []
            child_nodes: List[Node] = []
            if children_str:
                child_names = scan_children.findall(children_str)

            node = Node(
                name=name,
                weight=int(weight),
                child_names=child_names,
                child_nodes=child_nodes,
            )
            nodes.append(node)

        return nodes

    def gen_graph(self) -> Node:
        """Generate dependency graph from nodes."""
        nodes = self.input
        root = None
        for node in nodes:
            # search for a node with this node as a child
            parent = None
            for s in nodes:
                if node.name in s.child_names:
                    # found parent
                    parent = s
                    break

            if parent:
                # print(f"Found parent for {node}: {parent}, parent.child_nodes: {parent.child_nodes}")
                if not node in parent.child_nodes:
                    parent.child_nodes.append(node)
            else:
                # print(f"No parent for {node}, moving to root")
                root = node
        return root

    def run_part1(self):
        root = self.gen_graph()
        return root

    def run_part2(self):
        root = self.gen_graph()
        unbalanced = root.find_unbalanced()
        return unbalanced

if __name__ == '__main__':
    main(DayN)

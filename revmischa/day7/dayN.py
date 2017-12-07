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

    def dump(self):
        def print_node(depth, node):
            indent = " " * depth
            print(f"{indent}{node}")
        def p_r(depth, children):
            # print_node(depth, root)
            for c in children:
                print_node(depth, c)
                p_r(depth + 1, c.child_nodes)
        print_node(0, self)
        return p_r(1, self.child_nodes)

    def __repr__(self):
        children = f" -> {self.child_names}" if self.child_names else ""
        return f"{self.name} ({self.weight}){children}"

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

        scan_line = re.compile(r'(\w+)\s\((\d+)\)( -> ([\w, ]+))?')
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
                weight=weight,
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
                print(f"Found parent for {node}: {parent}, parent.child_nodes: {parent.child_nodes}")
                if not node in parent.child_nodes:
                    parent.child_nodes.append(node)
            else:
                print(f"No parent for {node}, moving to root")
                root = node
        return root

    def run_part1(self):
        root = self.gen_graph()
        root.dump()
        return root

    def run_part2(self):
        pass

if __name__ == '__main__':
    main(DayN)

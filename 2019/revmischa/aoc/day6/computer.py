import os
import sys


PWD = os.path.abspath(os.path.join(os.path.dirname(__file__)))
PROJ_ROOT = os.path.abspath(os.path.join(PWD, "..", ".."))
if PROJ_ROOT not in sys.path:
    sys.path.insert(0, PROJ_ROOT)

from aoc.computer import Computer
from pprint import pprint  # noqa: F401
from typing import Dict, Optional, Set

NodeList = Set["Node"]

NodeTree = Dict["Node", Optional["Node"]]


class Node:
    children: NodeList
    parent: Optional["Node"]

    def __init__(self, name: str, child: str = None, parent=None):
        self.name = name
        self.parent = parent
        self.children = {Node(child)} if child else set()

    def __repr__(self):
        child = f"->{self.children}" if self.children else ""
        return f"{self.name}{child}"

    def __hash__(self):
        return hash(self.name)

    def insert(self, n: "Node") -> bool:
        """Insert into tree, return if we found a place to insert or not."""
        if n.name == "COM":
            self.name = n.name
            self.children = set(n.children)
            return True
        if not self.children:
            return False
        for c in self.children:
            # found parent of n
            if c.name == n.name:
                # delete existing child leaf and replace with node and transfer over children
                old_subtree = c.children
                self.children.remove(c)
                n.children.update(old_subtree)
                self.children.add(n)
                n.parent = self
                return True

            # try to insert into child path
            if c.insert(n):
                # inserted
                return True
        return False


class Day6(Computer):
    pwd: str = PWD
    nodes_in: NodeList = set()

    def __init__(self, structure, **kwargs):
        """Construct solver with puzzle input."""
        super().__init__(structure, **kwargs)
        self.nodes_in = structure

    @classmethod
    def parse_input(cls, input_str: str):
        ni = []
        for line in input_str.split("\n"):
            parent, child = line.split(")")
            ni.append(Node(parent, child))
        return ni

    def find_node(self, name: str) -> Node:
        for n in self.nodes_in:
            if n.name == name:
                return n
        raise Exception(f"Failed to find {name}")

    def find_node_with_child(self, name: str) -> Node:
        for n in self.nodes_in:
            if name in [c.name for c in n.children]:
                return n
        raise Exception(f"Failed to find {name}")

    def build_tree(self) -> Node:
        root = self.find_node("COM")
        nodes = self.nodes_in.copy()
        nodes.remove(root)

        to_insert = nodes.copy()
        for i in range(10000):
            # print("to insert", to_insert)
            # print("root", root)
            inserted = False
            for n in to_insert.copy():
                if root.insert(n):
                    # inserted it ok
                    to_insert.remove(n)
                    inserted = True
            if not inserted:
                break

        return root

    def run_part1(self):
        root = self.build_tree()

        # count
        total = 1

        def count_tree(n: Node, name="", count=1):
            nonlocal total
            if not n:
                return
            for c in n.children:
                # if name != n.name:
                total += count
                count_tree(c, n.name, count + 1)

        count_tree(root)

        return total - 1

    def count_ancestor_distances(self, n: Node) -> dict:
        parent = n.parent
        distances = {}
        distance = 1
        while parent:
            distances[parent] = distance
            distance += 1
            parent = parent.parent
        return distances

    def run_part2(self):
        src = self.find_node_with_child("YOU")
        dst = self.find_node_with_child("SAN")
        self.build_tree()
        # find length of path from src to dest
        # calculate distance of every ancestor of src and dest
        src_parents = self.count_ancestor_distances(src)
        dst_parents = self.count_ancestor_distances(dst)

        # find first common ancestor
        for n1, d1 in src_parents.items():
            for n2, d2 in dst_parents.items():
                if n1.name == n2.name:
                    # answer is distance from src and dst to common ancestor
                    return d1 + d2


if __name__ == "__main__":
    print(Day6.part1_result(debug=False))
    print(Day6.part2_result(debug=False))

#!/usr/bin/env python3
"""
generate_daily_notebook.py
--------------------------
Run this script each day to scaffold the next DSA notebook.

Usage:
    python generate_daily_notebook.py           # uses today's date
    python generate_daily_notebook.py 2026-06-19  # override date
"""

import json
import sys
from datetime import date, datetime

# ── 30-day DSA curriculum ─────────────────────────────────────────────────────
CURRICULUM = [
    # (day, data_structure, sort_or_search, preview_of_next)
    (1,  "Array",                  "Bubble Sort · Linear Search",    "Linked List · Selection Sort · Jump Search"),
    (2,  "Singly Linked List",     "Selection Sort · Jump Search",   "Doubly Linked List · Insertion Sort · Binary Search"),
    (3,  "Doubly Linked List",     "Insertion Sort · Binary Search", "Stack · Shell Sort · Sentinel Linear Search"),
    (4,  "Stack",                  "Shell Sort · Sentinel Search",   "Queue · Merge Sort · Interpolation Search"),
    (5,  "Queue (deque)",          "Merge Sort · Interpolation Search","Circular Queue · Quick Sort · Fibonacci Search"),
    (6,  "Circular Queue",         "Quick Sort · Fibonacci Search",  "Binary Tree · Heap Sort · Exponential Search"),
    (7,  "Binary Tree",            "Heap Sort · Exponential Search", "BST · Counting Sort · Ternary Search"),
    (8,  "Binary Search Tree",     "Counting Sort · Ternary Search", "AVL Tree · Radix Sort · Jump Search"),
    (9,  "AVL Tree",               "Radix Sort · Jump Search",       "Hash Table · Bucket Sort · Hashing Search"),
    (10, "Hash Table",             "Bucket Sort · Hash Search",      "Min-Heap · Comb Sort · Sublist Search"),
    (11, "Min-Heap / Max-Heap",    "Comb Sort · Sublist Search",     "Trie · Cocktail Sort · Recursive Linear Search"),
    (12, "Trie",                   "Cocktail Sort · Recursive Search","Graph (Adj List) · Gnome Sort · BFS"),
    (13, "Graph (Adjacency List)", "Gnome Sort · BFS",               "Graph (Adj Matrix) · Odd-Even Sort · DFS"),
    (14, "Graph (Matrix)",         "Odd-Even Sort · DFS",            "Disjoint Set · Bitonic Sort · A* Search"),
    (15, "Disjoint Set (Union-Find)","Bitonic Sort · A* Search",     "Segment Tree · Pancake Sort · Ternary Search"),
    (16, "Segment Tree",           "Pancake Sort · Ternary Search",  "Fenwick Tree · Strand Sort · Order-Statistic"),
    (17, "Fenwick Tree (BIT)",     "Strand Sort · Order-Statistic",  "Sparse Table · Cycle Sort · Meta Binary Search"),
    (18, "Sparse Table",           "Cycle Sort · Meta Binary Search","Skip List · Tim Sort · Interpolation Search"),
    (19, "Skip List",              "Tim Sort · Interpolation Search", "Deque · Stooge Sort · Exponential Search"),
    (20, "Deque",                  "Stooge Sort · Exponential Search","LRU Cache · Sleep Sort · Ternary Search"),
    (21, "LRU Cache",              "Sleep Sort demo · Ternary Search","Priority Queue · 3-Way Quick Sort · Fibonacci Search"),
    (22, "Priority Queue (heapq)", "3-Way Quick Sort · Fibonacci",   "Monotonic Stack · Counting Sort · Hashing"),
    (23, "Monotonic Stack",        "Counting Sort · Hash Search",    "Monotonic Queue · Radix Sort · Binary Search"),
    (24, "Monotonic Queue",        "Radix Sort · Binary Search",     "Suffix Array · MSD Radix Sort · Suffix Search"),
    (25, "Suffix Array",           "MSD Radix Sort · Suffix Search", "Rope · In-Place Merge Sort · Rope Search"),
    (26, "Rope",                   "In-Place Merge Sort · Rope Srch","Bloom Filter · Pigeonhole Sort · Bloom Search"),
    (27, "Bloom Filter",           "Pigeonhole Sort · Bloom Search", "B-Tree · External Merge Sort · B-Tree Search"),
    (28, "B-Tree (conceptual)",    "External Merge Sort · B-Tree",   "Red-Black Tree · Intro Sort · BST Search"),
    (29, "Red-Black Tree",         "Intro Sort · BST Search",        "KD-Tree · Patience Sort · Nearest Neighbour"),
    (30, "KD-Tree",                "Patience Sort · kNN Search",     "— Series complete! Review all 30 notebooks —"),
]

TEMPLATE = '''{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Day %(day_str)s — %(ds)s · %(algo)s\\n",
    "**Date:** %(date)s  |  **Difficulty:** %(difficulty)s  |  **Series:** Daily DSA\\n",
    "\\n",
    "---\\n",
    "\\n",
    "> Run each cell top-to-bottom with **Shift+Enter** to follow along interactively.\\n",
    "\\n",
    "---\\n",
    "## Coming Up\\n",
    "**Tomorrow — Day %(next_day)s:** %(next_topic)s"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# ── Scaffold: fill in your implementation here ────────────────────────────────\\n",
    "# Data Structure : %(ds)s\\n",
    "# Algorithm      : %(algo)s\\n",
    "print('Day %(day_str)s notebook ready — implement %(ds)s and %(algo)s!')"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
  "language_info": {"name": "python", "version": "3.11.0"}
 },
 "nbformat": 4,
 "nbformat_minor": 5
}'''


def get_difficulty(day):
    if day <= 6:   return "Beginner"
    if day <= 15:  return "Intermediate"
    if day <= 24:  return "Advanced"
    return "Expert"


def scaffold(target_date: date, day_num: int):
    entry     = CURRICULUM[day_num - 1]
    next_entry= CURRICULUM[day_num] if day_num < len(CURRICULUM) else None

    ctx = {
        "day_str"   : f"{day_num:03d}",
        "ds"        : entry[1],
        "algo"      : entry[2],
        "date"      : target_date.isoformat(),
        "difficulty": get_difficulty(day_num),
        "next_day"  : f"{day_num+1:03d}" if next_entry else "—",
        "next_topic": next_entry[2] if next_entry else "Review",
    }

    ds_slug   = entry[1].replace(" ", "_").replace("(", "").replace(")", "").replace("/", "_")
    algo_slug = entry[2].split(" · ")[0].replace(" ", "_")
    filename  = f"{target_date.isoformat()}_Day{ctx['day_str']}_{ds_slug}_{algo_slug}.ipynb"

    with open(filename, "w") as f:
        f.write(TEMPLATE % ctx)

    print(f"Created: {filename}")
    return filename


if __name__ == "__main__":
    if len(sys.argv) > 1:
        target = date.fromisoformat(sys.argv[1])
    else:
        target = date.today()

    # Determine day number from start date (Day 1 = 2026-06-18)
    start = date(2026, 6, 18)
    day_num = (target - start).days + 1

    if not (1 <= day_num <= 30):
        print(f"Day {day_num} is outside the 30-day curriculum range. Exiting.")
        sys.exit(1)

    scaffold(target, day_num)

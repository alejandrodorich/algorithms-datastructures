# algorithms-datastructures
This repository contains implementations of fundamental algorithms and data structures in Python.
Each module is a self-contained, well-documented, and thoroughly tested standalone implementation.

## Table of contents
- [Modules](#modules)
- [Installation](#installation)
- [Usage and Tests](#usage-and-tests)
- [Tests](#tests)
- [Project Goal](#project-goal)


## Modules

This repository includes the following modules:
- [**Binary Tree**](Binary%20Tree/README.md): Recursive implementation of a binary tree with insertion, deletion, and searching methods, as well as traversal (pre-, in-, and post-order).
- [**Doubly Linked List**](Doubly%20Linked%20List/README.md): Iterative implementation of a doubly linked list with insertion, deletion, and element traversal operations.
- [**Quicksort**](Quicksort/README.md): Recursive implementation of quicksort with median-of-three pivot selection for efficient list sorting.

As stated above, each module works as a standalone implementation with its own:
- **README.md file**
- **Implementation file**
- **Test file**
- **Test output screenshot**

## Installation
- No external libraries required. All modules tested on Python 3.12.3.

```bash
# clone the repository
git clone https://github.com/alejandrodorich/algorithms-datastructures.git

# navigate to the module folder
cd "algorithms-datastructures/<module>"

# for example, navigate to the Quicksort module:
cd "algorithms-datastructures/Quicksort"
```

## Usage and Tests

Each module has its own usage example in its corresponding README.md file, as well as its own Python test file, written in snake_case.

Run tests with pytest:
```bash
pip install pytest
pytest -v <test_file>.py
```

For example, to run the tests for the Doubly Linked List module:
```bash
pytest -v test_doubly_linked_list.py
```

## Project Goal
This repository demonstrates core algorithmic, object-oriented programming (OOP), iterative and recursive programming principles, serving
as a foundation for understanding and implementing efficient algorithms and data structures.

# B Tree Index implementation in Python
### This implementation is based on the article [_"The Case for Learned Index Structures"_](https://arxiv.org/pdf/1712.01208.pdf)

The following application is an example for using B-Tree index. We are going to have a sorted array with a fixed size. Based on this array we will create a B-Tree. The scope is to find a specific key in the array using the B-tree.

Observation:
- a node in the B-tree is <key, value> where key =  is the key we are looking for and value = is the page number where the key exist

Database = is just a simple array in this example

### How to test the program:
1. Clone this repository
2. Open command line in the directory of the folder, and use the following command with 2 additionally parameters:
                ```python main_run.py array_size key``` => ```python main_run.py 100 19```
               

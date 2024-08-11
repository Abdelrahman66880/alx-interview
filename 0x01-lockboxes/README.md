# Lockboxes

## Problem Statement

You have `n` locked boxes in front of you, numbered sequentially from 0 to `n-1`. Each box may contain keys to other boxes. A key with a number equal to a box's number opens that box.

Write a method to determine if all the boxes can be opened, given the following:

- Prototype: def canUnlockAll(boxes)
- boxes is a list of lists
- The first box (`boxes[0]`) is unlocked initially.
- Each box contains a list of keys to other boxes.
- Return True if all boxes can be opened, else return False

## Problem of the 8 Trees
Create a function that receives as input a list of integers representing the presence (_1_) or absence (_0_) of trees. <br>

> Adjacent trees form a _set_ of trees. <br>

The function should return ***0*** if the number of sets is even and ***1*** if it's odd. <br>

### Examples
Input: `[0, 1, 1, 0, 1, 0, 0, 1]`  <br>
Sets: `3`  <br>
Output: `1`  <br>

Input: `[1, 1, 1, 1, 1, 1, 1, 1]`  <br>
Sets: `1`  <br>
Output: `1`  <br>

Input: `[1, 1, 1, 0, 1, 1, 1, 1]`  <br>
Sets: `2`  <br>
Output: `0`  <br>

Input: `[0, 0, 1, 1, 1, 1, 1, 1]`  <br>
Sets: `1`  <br>
Output: `1`  <br>

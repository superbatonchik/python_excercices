#### Задачи из курса [Adaptive Python](https://stepik.org/course/568)

2. Given a two-dimensional array (matrix) and the two numbers: i and j. Swap the columns with indices i and j within the matrix.
Input contains matrix dimensions n and m, not exceeding 100, then the elements of the matrix, then the indices i and j.  
##### Sample Input:  
3 4  
11 12 13 14  
21 22 23 24  
31 32 33 34  
0 1  
##### Sample Output:  
12 11 13 14  
22 21 23 24  
32 31 33 34  

3. Implement the data structure "set of strings" based on a dynamic hash table with open addressing. Stored strings are not empty and contain lowercase Latin letters. The initial size of the table should be equal to 8. Perform rehashing only in the case when the table-filling coefficient reaches 3/4.

The structure of the data should support the operation of adding a string to the set, deleting a string from the set and membership testing of this string to the set.

Use quadric probing to resolve collisions, i-th sample

g(k,i)=g(k,i−1)+i(mod m), m - power of 2. 

Each line of the input data sets one operation over the set. The record of the operation consists of the type of operation, a space, and a string, which is a subject for this operation.

Type of operation - one of the following three symbols:
   \+ means adding this string to the set;
   \- means deleting this string from the set;  
   ? means membership testing of this string to the set.

When adding an element to the set IT IS NOT GUARANTEED that this element is not already present in the set. When deleting an element from the set IT IS NOT GUARANTEED that this element is present in this set. 

For each of the operations the program should display one of the two lines OK or FAIL, depending on whether this word is found in our set.

##### Sample Input:  
\+ hello  
\+ bye  
? bye  
\+ bye  
\- bye  
? bye  
? hello 
##### Sample Output:  
OK  
OK  
OK  
FAIL  
OK  
FAIL  
OK 

*Site does not accept my solution

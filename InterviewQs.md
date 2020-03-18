### INTERVIEW QUESTIONS ###

*** What is the runtime complexity to access an array, add or remove from the front, and add or remove from the back? ***

- Access an array: O(1) because it takes a single step to access an item of an array. To access an array you calculate the base address of the array plus the index times the size of the element in the array. 

- Add/remove from front: Adding or removing from the front makes it so every item that is after has to be re-indexed. For example: if we have an array of [1,2,3] then the index would be 1[0], 2[1], and 3[2].If we add to the beginning of the array [5,1,2,3] then the index of every element after 5 would increase by 1. That would give us 5[0], 1[1], 2[2], and 3[3]. Which would result in a runtime of O(n) because time taken to run would relate to the size of the list.

- Add/remove from back: Adding to the end or removing from the end is faster because you are adding the new element to the next highest index of the array. You don't have to re-index the array. That would give it a runtime of O(1) constant time because as it grows the runtime stays consistent. The exception is if the array is full when you are trying to insert an element and then it needs to resize (see below). That would change the run time to O(n).

Example: array [4, 5] --> index 4[0], 5[1]
adding to end of array -> [4,5,1] -> index 4[0], 5[1], 1[2]
removing from end of array -> [4,5,1] --> off last element (1) --> [4, 5] --> index 4[0], 5[1]

*** What is the worse case scenario if you try to extend the storage size of a dynamic array? ***

The worst case scenario is that the space is full and you need to resize the array. Which means that you would need to create a new array, then copy the content of the original array into the new array and double the size to create more space for data. I think that would be O(n)

*** Explain how a blockchain is structured. What are the blocks, what is the chain? How is the data organized? ***

(See attached image)

*** Explain how proof of work functions. How does it operate. How does this protect the chain from attack. What kind of attack is possible? ***
Proof of work is the the algorithm used to confirm transactions and and create new blocks in the chain. It is dependent on the number of users. The hash of each block contains the hash of the previous block, which increases security and prevents any block violation. When a block is mined, it is added to the chain. If it is a valid solution, the node will hash the previous block and add it to the new block along with its properties. 

Each block needs the hash of the previous block. If someone attempts to change a block they break the chain. They would have to recreate all of the following blocks in the chain as well. That would take alot of effort, time, and computer power. DoS attacks are possible but would require alot of work because of the effort required. 
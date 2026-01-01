#First program initiate 15 years old at beginning
#lets designate the function TwoSum()

#lets use the original type hinting used in the original problem
def TwoSum(nums:list[int],goal:int) -> list[int,int]|None:
 #lets recieve a list of integers, a goal number (int), and lets return a int or nothing
 seen = {} #lets create a hashmap tracking the numbers that we have looked through with the corresponding index but for now its empty.
 for index,i in enumerate(nums):#lets then cycle through all the integers in nums and find the index and the value of each iterable
    diff = goal - i #lets then find the difference in the goal and the value then see if we can find the corresponding value inside seen
    if diff in seen: #lets return the indexes of the two values
      return [seen[diff], index]
    seen[i] = index
#now lets create a one liner input to output function call
print(TwoSum(map(int,list(input("numbers: ").split())), int(input("goal: "))))

#ig we can make it more lines and make it simpler but size is key
#ive witnessed a error beginning debug

#lol i completely forgot about adding elements to the hashmap so the result was returning None bc there was no diff inside the seen bc i wasnt adding anything beginning clean up
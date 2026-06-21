'''Exercise 3. Sum and Average of All Numbers in a List
Practice Problem: Calculate the total sum of all integers in a list and find the arithmetic mean (average).

Exercise Purpose: Aggregation is the heart of data science. This exercise teaches you how to reduce a collection of multiple data points into a single, meaningful summary statistic.'''

input = [10,20,30,40,50]
total_sum =  sum(input)
Average = total_sum / len(input)
print("SUM = ", total_sum)
print("Average = ", Average)

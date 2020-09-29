# Week2 

## Python Regular Expression Quick Guide
^ : Matches the beginning of a line
$ : Matches the end of the line
. : Matches any character
\s : Matches whitespace
\S : Matches any non-whitespace character
* : Repeats a character zero or more times
*? : Repeats a character zero or more times (non-greedy)
+ : Repeats a character one or more times
+? : Repeats a character one or more times (non-greedy)
[aeiou] : Matches a single character in the listed set
[^XYZ] : Matches a single character not in the listed set
[a-z0-9] : The set of characters can include a range
( : Indicates where string extraction is to start
) : Indicates where string extraction is to end

## Regular Expressions
1. Which of the following regular expressions would extract 'uct.ac.za' from this string using re.findall?
~~~python
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
~~~
A. @(\S+)

2. Which of the following is the way we match the "start of a line" in a regular expression?
A. ^

3. What would the following mean in a regular expression? [a-z0-9]
A. Match a lowercase letter or digit

4. What is the type of the return value of the re.findall() method?
A. A list of strings

5. What is the "wild card" character in a regular expression (i.e., the character that matches any character)?
A. .

6. What is the difference between the "+" and " * " character in regular expressions?
A. The "+" matches at least one character and the " * " matches zero or more characters

7. What does the "[0-9]+" match in a regular expression?
A. One or more digits

8. What does the following Python sequence print out?
~~~python
x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)
~~~
A. ['From: Using the :']

9. What character do you add to the "+" or "*" to indicate that the match is to be done in a non-greedy manner?
A. $

10. Given the following line of text:
~~~python
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
~~~
What would the regular expression '\S+?@\S+' match?
A. stephan.marquard@uct.ac.za

## Week2 Assessment
### Finding Numbers in a Haystack
In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.

**Data Files**
We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.
- Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt (There are 90 values with a sum=445833)
- Actual data: http://py4e-data.dr-chuck.net/regex_sum_996182.txt (There are 77 values and the sum ends with 685)
These links open in a new window. Make sure to save the file into the same folder as you will be writing your Python program. Note: Each student will have a distinct data file for the assignment - so only use your own data file for analysis.

**Data Format**
The file contains much of the text from the introduction of the textbook except that random numbers are inserted throughout the text. Here is a sample of the output you might see:
~~~
Why should you learn to write programs? 7746
12 1929 8827
Writing programs (or programming) is a very creative 
7 and rewarding activity.  You can write programs for 
many reasons, ranging from making your living to solving
8837 a difficult data analysis problem to having fun to helping 128
someone else solve a problem.  This book assumes that 
everyone needs to know how to program ...
~~~
The sum for the sample text above is **27486**. The numbers can appear anywhere in the line. There can be any number of numbers in each line (including none).

**Handling The Data**
The basic outline of this problem is to read the file, look for integers using the **re.findall()**, looking for a regular expression of **'[0-9]+'** and then converting the extracted strings to integers and summing up the integers.

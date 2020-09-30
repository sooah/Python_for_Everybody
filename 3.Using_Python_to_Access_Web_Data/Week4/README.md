# Week4

## Python Strings to Bytes
~~~python
while True:
    data = mysock.recv(512)
    if( len(data) < 1):
        break
    mystring = data.decode()
    print(mystring)
~~~

## Week4 Assessment

### QUIZ : Reading Web Data From Python
1. Which of the following Python data structures is most similar to the value returned in this line of Python:
~~~python
x = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
~~~
A. file handle

2. In this Python code, which line actually reads the data?
~~~python
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()
~~~
A. mysock.recv()

3. Which of the following regular expressions would extract the URL from this line of HTML:
~~~html
<p>Please click <a href="http://www.dr-chuck.com">here</a></p>
~~~
not A. href=".+"

4. In this Python code, which line is most like the open() call to read a file:
~~~python
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()
~~~
A. mysock.connect()

5. Which HTTP header tells the browser the kind of document that is being returned?
A. Content-Type:

6. What should you check before scraping a web site?
A. That the web site allows scraping

7. What is the purpose of the BeautifulSoup Python library?
A. It repairs and parses HTML to make it easier for a program to understand

8. What ends up in the "x" variable in the following code:
~~~python
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
x = soup('a')
~~~
A. A list of all the anchor tags (<a..) in the HTML from the URL

9. What is the most common Unicode encoding when moving data between systems?
A. UTF-8

10. What is the decimal (Base-10) numeric value for the upper case letter "G" in the ASCII character set?
A. 71

11. What word does the following sequence of numbers represent in ASCII:
108, 105, 110, 101
A. line

12. How are strings stored internally in Python 3?
A. Unicode

13. When reading data across the network (i.e. from a URL) in Python 3, what method must be used to convert it to the internal format used by strings?
A. decode()

### Week4 Assessment : Scraping Numbers from HTML using BeautifulSoup 
In this assignment you will write a Python program similar to http://www.py4e.com/code3/urllink2.py. The program will use urllib to read the HTML from the data files below, and parse the data, extracting numbers and compute the sum of the numbers in the file.

We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

- Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
- Actual data: http://py4e-data.dr-chuck.net/comments_996184.html (Sum ends with 44)

You do not need to save these files to your folder since your program will read the data directly from the URL. Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.

### Week4 Assessment : Following Links in Python
In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py. The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat the process a number of times and report the last name you find.

We provide two files for this assignment. One is a sample file where we give you the name for your testing and the other is the actual data you need to process for the assignment

- Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html 
    Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times.
    The answer is the last name that you retrieve.
    Sequence of names: Fikret Montgomery Mhairade Butchi Anayah 
    Last name in sequence: Anayah
- Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Thrinei.html 
    Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times.
    The answer is the last name that you retrieve.
    Hint: The first character of the name of the last page that you will load is: M

**Strategy**
The web pages tweak the height between the links and hide the page after a few seconds to make it difficult for you to do the assignment without writing a Python program. But frankly with a little effort and patience you can overcome these attempts to make it a little harder to complete the assignment without writing a Python program. But that is not the point. The point is to write a clever Python program to solve the program.

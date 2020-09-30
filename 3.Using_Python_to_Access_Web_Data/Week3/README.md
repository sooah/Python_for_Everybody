# Week3 

## 12.1 Networked Technology
- sockets in Python
~~~python
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
~~~

## 12.2 Hypertext Transfer Protocol (HTTP)
~~~python
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encod()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data)<1):
        break
    print(data.decode())
mysock.close()
~~~

## If you want to learn more
This chapter covers networking at a very high level. If you want to learn more, there is both a free book and a Coursera course that I would recommend:

Introduction to Networking (free textbook) : http://www.net-intro.com
Internet History, Technology, and Security (Coursera Course) : https://www.coursera.org/learn/python-network-data/supplement/ZrNry/if-you-want-to-learn-more

Neither of these is essential for this course or the Python Specialization as we quickly move from how the network works to how to write Python code using the urllib library - which makes the very complex Internet protocols exceedingly simple.

## Quiz : Network and Sockets
1. What do we call it when a browser uses the HTTP protocol to load a file or page from a server and display it in the browser?
    A. The Request/Response Cycle
    
2. Which of the following is most similar to a TCP port number?
    not A. A telephone number

3. What must you do in Python before opening a socket?
    A. import socket
    
4. Which of the following TCP sockets is most commonly used for the web protocol (HTTP)?
    A. 80
    
5. Which of the following is most like an open socket in an application?
    A. An "in-progree" phone conversation
    
6. What does the "H" of HTTP stand for?
    A. HyperText
    
7. What is an important aspect of an Application Layer protocol like HTTP?
    A. Which application talks first? The client or server?
    
8. What are the three parts of this URL (Uniform Resource Locator)?
~~~
http://www.dr-chuck.com/page1.htm
~~~
A. Protoco, host, and document

9. When you click on an anchor tag in a web page like below, what HTTP request is sent to the server?
~~~
<p>Please click <a href="page1.htm">here</a>.</p>
~~~
A. GET

10. Which organization publishes Internet Protocol Standards?
    A. IETF

## Week3 Assessment

cmd
~~~
telnet data.pr4e.org 80

GET http://data.pr4e.org/romeo.txt HTTP/1.0

~~~


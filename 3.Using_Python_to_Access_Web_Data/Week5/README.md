#  Week5 

## Parsing XML
~~~python
import xml.etree.ElementTree as ET
data ='''<person>
    <name>Chunk</name>
    <phone type="intl">
        +1 734 303 4456
    </phone>
    <email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))
~~~

## QUIZ : eXtensible Markup Language
1. What is "serialization" when we are talking about web services?
A. The act of taking data stored in a program and formatting it so it can be sent across the network

2. Which of the following are not commonly used serialization formats?
A. Dictionaries, HTTP, TCP

3. In this XML, which are the "simple elements"?
~~~
<people>
    <person>
       <name>Chuck</name>
       <phone>303 4456</phone>
    </person>
    <person>
       <name>Noah</name>
       <phone>622 7421</phone>
    </person>
</people>
~~~
A. name, phone

4. In the following XML, which are attributes?
~~~
<person>
  <name>Chuck</name>
  <phone type="intl">
     +1 734 303 4456
  </phone>
  <email hide="yes" />
</person>
~~~
A. type, hide

5. In the following XML, which node is the parent node of node e
~~~
<a>
  <b>X</b>
  <c>
    <d>Y</d>
    <e>Z</e>
  </c>
</a>
~~~
A. c

6. Looking at the following XML, what text value would we find at path "/a/c/e"
~~~ 
<a>
  <b>X</b>
  <c>
    <d>Y</d>
    <e>Z</e>
  </c>
</a>
~~~
A. Z

7. What is the purpose of XML Schema?
A. To establish a contract as to what is valid XML

8. Question 8
If you were building an XML Schema and wanted to limit the values allowed in an xs:string field to only those in a particular list, what XML tag would you use in your XML Schema definition?
A. xs:element

9. What does the "Z" mean in this representation of a time:
~~~
2002-05-30T09:30:10Z
~~~
This time is in the UTX timezone

10. Which of the following dates is in ISO8601 format?
A. 2002-05-30T09:30:10Z

## Week5 Assessment : Extracting Data from XML
In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py. The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.

We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

- Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
- Actual data: http://py4e-data.dr-chuck.net/comments_996186.xml (Sum ends with 63)

You do not need to save these files to your folder since your program will read the data directly from the URL. Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.

**Data Format and Approach**
The data consists of a number of names and comment counts in XML as follows:
~~~xml
<comment>
  <name>Matthias</name>
  <count>97</count>
</comment>
~~~
You are to look through all the <comment> tags and find the <count> values sum the numbers. The closest sample code that shows how to parse XML is geoxml.py. But since the nesting of the elements in our data is different than the data we are parsing in that sample code you will have to make real changes to the code.
To make the code a little simpler, you can use an XPath selector string to look through the entire tree of XML for any tag named 'count' with the following line of code:
~~~
counts = tree.findall('.//count')
~~~
Take a look at the Python ElementTree documentation and look for the supported XPath syntax for details. You could also work from the top of the XML down to the comments node and then loop through the child nodes of the comments node.

**Sample Execution**
~~~
$ python3 solution.py
Enter location: http://py4e-data.dr-chuck.net/comments_42.xml
Retrieving http://py4e-data.dr-chuck.net/comments_42.xml
Retrieved 4189 characters
Count: 50
Sum: 2...
~~~

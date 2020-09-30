# Week 6

## QUIZ : REST, JSON, and APIs

1. Who is credited with the REST approach to web services?

2. What Python library do you have to import to parse and handle JSON?

3. What is the method used to parse a string containing JSON data so that you can work with the data in Python?

4. What kind of variable will you get in Python when the following JSON is parsed:
~~~
[ "Glenn", "Sally", "Jen" ]
~~~
5. Which of the following is not true about the service-oriented approach?

6. If the following JSON were parsed and put into the variable x,
~~~
{
    "users": [
        {
            "status": {
                "text": "@jazzychad I just bought one .__.",
             },
             "location": "San Francisco, California",
             "screen_name": "leahculver",
             "name": "Leah Culver",
         },
   ...
~~~
what Python code would extract "Leah Culver" from the JSON?

7. What library call do you make to append properly encoded parameters to the end of a URL like the following:
~~~
http://maps.googleapis.com/maps/api/geocode/json?sensor=false&address=Ann+Arbor%2C+MI
~~~

8. What happens when you exceed the Google geocoding API rate limit?

9. What protocol does Twitter use to protect its API?

10. What header does Twitter use to tell you how many more API requests you can make before you will be rate limited?

## Week6 Assessment : Extracting Data from JSON
**Extracting Data from JSON**

In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py. The program will prompt for a URL, read the JSON data from that URL using **urllib** and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:

We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

- Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
- Actual data: http://py4e-data.dr-chuck.net/comments_996187.json (Sum ends with 33)

You do not need to save these files to your folder since your program will read the data directly from the URL. Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.

**Data Format**
The data consists of a number of names and comment counts in JSON as follows:
~~~
{
  comments: [
    {
      name: "Matthias"
      count: 97
    },
    {
      name: "Geomer"
      count: 97
    }
    ...
  ]
}
~~~
The closest sample code that shows how to parse JSON and extract a list is json2.py. You might also want to look at geoxml.py to see how to prompt for a URL and retrieve data from a URL.

**Sample Execution**
~~~
$ python3 solution.py
Enter location: http://py4e-data.dr-chuck.net/comments_42.json
Retrieving http://py4e-data.dr-chuck.net/comments_42.json
Retrieved 2733 characters
Count: 50
Sum: 2...
~~~

## Week6 Assessment : Caliing a JSON API
**Calling a JSON API**

In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geojson.py. The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data, and retrieve the first place_id from the JSON. A place ID is a textual identifier that uniquely identifies a place as within Google Maps.

**API End Points**

To complete this assignment, you should use this API endpoint that has a static subset of the Google Data:
~~~
http://py4e-data.dr-chuck.net/json?
~~~
This API uses the same parameter (address) as the Google API. This API also has no rate limit so you can test as often as you like. If you visit the URL with no parameters, you get "No address..." response.


To call the API, you need to include a key= parameter and provide the address that you are requesting as the address= parameter that is properly URL encoded using the urllib.parse.urlencode() function as shown in http://www.py4e.com/code3/geojson.py


Make sure to check that your code is using the API endpoint is as shown above. You will get different results from the geojson and json endpoints so make sure you are using the same end point as this autograder is using.


**Test Data / Sample Execution**

You can test to see if your program is working with a location of "South Federal University" which will have a place_id of "ChIJJ2MNmPl_bIcRt8t5x-X5ZhQ".
~~~
$ python3 solution.py
Enter location: South Federal University
Retrieving http://...
Retrieved 2290 characters
Place id ChIJJ2MNmPl_bIcRt8t5x-X5ZhQ
~~~

**Turn In**

Please run your program to find the place_id for this location:
~~~
NIT ROURKELA
~~~
Make sure to enter the name and case exactly as above and enter the place_id and your Python code below. Hint: The first seven characters of the place_id are "ChIJw2H ..."


Make sure to retreive the data from the URL specified above and not the normal Google API. Your program should work with the Google API - but the place_id may not match for this assignment.

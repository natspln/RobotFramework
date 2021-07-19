# RobotFramework

Steps to execute:

1. Use PyCharm as IDE
2. Open PyCharm Terminal
3. To run individual test use a marker or run the commands below:

    **pytest -m "TS01" --html="report.html"**
    
    **pytest -m "TS02" --html="report.html"**
    
    **pytest -m "TS03" --html="report.html"**
    
    **pytest -m "TS04" --html="report.html"**

    
4. To run parallel testing or multiple testing at the same time run the command below:

    **py.test -n4 --html="report1.html"**
    
5. Copy the generated html file, paste it on a browser.

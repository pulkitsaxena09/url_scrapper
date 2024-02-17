URL Scraper
A simple tool designed to extract all URLs from a web page using web scraping methods.

Basic Requirements
------------------

Python 3


Steps to Follow
----------------

Step 1
======
Install the required packages by running the following command:

  pip3 install -r requirements.txt

Step 2
======
  Run the main.py file with the following syntax:
  python3 main.py <URL> -oFR <Format [csv/txt]> -oFL <[Full_Path + File_Name]>


Example
========
python3 main.py https://google.com -oFR csv -oFL C:\Users\Alice\Desktop\Google_URLs.csv


Note
=====
Make sure to replace <URL> with the target web page's URL, <Format> with the desired output format (csv or txt), and <[Full_Path + File_Name]> with the complete file path and name where you want to save the extracted URLs.






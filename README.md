* The project is mainly used for crawling all articles of www.woshipm.com, the professional Chinese Product Manager(PM) media.

## Environment, Architecture

Language: Python2.7

Environment: MacOS, 8G RAM

Database: MongoDB

* Mainly uses the scrapy reptile framework.
* Join to the Spider randomly by extracted from the Cookie pool and UA pool.
* Start_requests start five Request based on PornHub classification, and crawl the five categories at the same time.
* Support paging crawl data, and join to the queue.

## Instructions for use

### Pre-boot configuration

* Install MongoDB and start without configuration
* Install Python dependent modules：Scrapy, pymongo, requests or `pip install -r requirements.txt`
* Modify the configuration by needed, such as the interval time, the number of threads, etc.

### Start up

* sudo mongod
* cd ./Woshipm
* python quickstart.py

## Database description

The table in the database that holds the data is PhRes. The following is a field description:

#### PhRes table：
  
    item_title :         article title
    item_url :           article link
    item_des :           short description
    item_auth_name :     author name
    item_auth_link :     author homepage
    item_date :          publish date
    item_eye  :          number of view
    item_stars :         number of collection
    item_thumbs_up :     number of agreement

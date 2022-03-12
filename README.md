# Infinity Influencer Marketing

## Project Description


* Build a Python microservice to identify whether a given post_text is sponsored or not.
* post_text is a english language text which may contain emoji (e.g 😀) or special
  characters
* To determine whether a post_text is sponsored or not we would like to use the following
  logic:
  * If below keywords are present in the post_text, we say that post_text is a
    sponsored post
  * Non-sponsored otherwise
* We should be able to add new keywords to the original set of keywords so that our vocabulary is not static.

## System Requirements

Please check the requirements.txt file ( This file contains all the dependencies )

Python and Flask are used to build the microservice that categorize the post_text is sponsored or non-sponsered. Flask is a micro web framework and it does not require particualar tools or libraries so it is more easier to implement. 

## Web services(

### GET(HTTP Method) : Send to URL-Pattern - end point(`/api/vocab`) and should return list of keywords used to determine whether or not post_text is sponosored.
### POST(HTTP Method) : Send to URL-Pattern - end point(`/api/vocab`) and should add new keyword in already existing vocabulary.
### POST(HTTP Method) : Send to URL-Pattern - end point(`/api/prediction`) and should predict to categorizing if the given post_text is sponsored or not.

## Steps

1. Download the repository.
2. Install all dependencies in requirements.txt 
  ```bash
  pip install -r requirements.txt
  ```
3. Move to directory where files are located
4. Run post.py file.
  ```bash
  python post.py
  ```
5. Result will be displayed and check.

If using test.py file, two cmd should be opened and run post.py file and test.py on each cmd.

## Results

In order to demonstrate the built microservice, Postman and test.py is used to verfiy the output. Postman is an API platform for building and using APIs.
Also, the test.py file will return the output with simplicity.

![GET vocab](https://github.com/ybchojo/lin_take_home/blob/main/output_img/1.PNG)

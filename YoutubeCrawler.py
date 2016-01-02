import requests
from bs4 import BeautifulSoup
from math import floor
video_minutes = 0
video_seconds = 0
video_hours = 0

'''
The Purpose of this program is to enter a youtube playlist url and check to see the total time it will
take to view the entire playlist. The program is mostly used for time management while watching tutorials
on youtube. The program can be modified however you will have to check the source code of the web page to determine
how to find the time stamps of each video.
*** NOTE: I wasn't able to input a url and hit enter as this would open the url in the browser. So I added
          a space at the end as input to work around this problem.
'''


def youtube_time_crawler():
    url = input('Enter Your URL Here and add a space at the end: ')
    source_code = requests.get(url[:-1])
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    for link in soup.findAll('span'):                   # Check all span tags
        title = link.get_text()                         # use get_text() to extract text fields in span tag
        if ":" in title:                                # : denotes that there is a time stamp with HH:MM:SS format
            check_number = title[0]                     # Check the first character in the string for a number
            if is_number(check_number) is True:
                add_youtube_video_time(title)
    convert_numbers_to_time(video_hours, video_minutes, video_seconds)

'''
This part of the program takes the first character of a string and determines if it is a number
or not a number.
'''


def is_number(number_check):
    try:
        float(number_check)
        return True
    except ValueError:
        return False

'''
This method takes the global variables for minutes and seconds and sums them, however since our time stamp is
in the HH:MM:SS format we must manipulate the string to separate the minutes from the seconds.
'''


def add_youtube_video_time(video_time):
    global video_hours
    global video_minutes
    global video_seconds
    hours = video_time[:-6]
    if is_number(hours) is True:
        video_hours += int(hours)
    minutes = video_time[-5:-3]
    video_minutes += int(minutes)
    seconds = video_time[-2:]
    video_seconds += int(seconds)

'''
This method takes the final values of the global variables video_minutes and video_seconds and converts it into
a HH:MM:SS format so that we can see the total time it will take to view all videos in the series.
Additionally this method can be used elsewhere to convert minutes and seconds input into a more readable format.
'''


def convert_numbers_to_time(hours, minutes, seconds):
    print(str(minutes) + " minutes")
    print(str(seconds) + " seconds")
    seconds_remainder = floor(seconds % 60)
    total_minutes = minutes + floor(seconds/60)
    total_hours = hours + floor(total_minutes/60)
    total_minutes = floor(total_minutes % 60)

    print("Total Time is " +
          "{h} hours:{m} minutes:{s} seconds".format(h=total_hours, m=total_minutes, s=seconds_remainder))

youtube_time_crawler()

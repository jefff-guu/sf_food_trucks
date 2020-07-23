"""
This is the main program to retreive the data dynamically from following url
http://data.sfgov.org/resource/jjew-r69b.json

And the Mobile Food Schedule Data API usage can be found at:
https://data.sfgov.org/Economy-and-Community/Mobile-Food-Schedule/jjew-r69b
"""

import os
import requests
from query.SoQL import SoQL_query


def call_api(page_num=0):
    """
    This function is to make an API call to he Mobile Food Schedule Data API.
    With SoQL query string attached to the base url
    """
    base_url = "http://data.sfgov.org/resource/jjew-r69b.json"
    query_string = SoQL_query(page_num=page_num).generate_query()
    url = base_url+query_string
    response = requests.get(url)
    return response

def switch_page(page_num):
    """
    This function calls to the API to retrieve the next page of data.
    """
    if page_num <=1:
        page_num == 1
    
    response = call_api(page_num)
    return (page_num, response)

def print_results(results):
    """
    This function is to print the result in an individual page
    """
    print("\033[4m\033[1m%-75s%s\033[0m" % ("NAME", "ADDRESS"))

    for selections in data:
        print("%-75s%s" % (selections['applicant'], selections['location']))
        
    print("\n\033[1m--- PAGE ", page_num, "---\033[0m\n")


page_num = 1
response = call_api(page_num)

while page_num >= 1:
    if response.ok:
        data = response.json()
        if len(data) == 0:
            print("\nThat's it, no more to show, exiting ...\n")
            break

        print_results(data)

        user_input = input("Please select: Next, Back, Quit: ").lower()

        if user_input == "next" or user_input == "n":
            (page_num, response) = switch_page(page_num + 1)
        elif (user_input == "back" or user_input == "b") and page_num >= 2:
            (page_num, response) = switch_page(page_num - 1)
        elif user_input == "quit" or user_input == "q":
            page_num = 0
            break
    else:
        print("Could not get the data successfully, please check connection.")

print("The end. Have a good day!")

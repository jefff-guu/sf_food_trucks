# Find The San Francisco Food Trucks
This is a python3 command line program that gets all food trucks in alphabetically order (10 at a time) through The San Francisco Data API page at the time when you run this program. 

You can find the Data API, query types, filter and SoQL query examples from here: https://data.sfgov.org/Economy-and-Community/Mobile-Food-Schedule/jjew-r69b).

This Program is using its json output and put SoQL query strings after it as the filter.


## Prerequisites
- This program requires Python 3 to be installed (I'm using 3.7), run following commands to check your python version:
  - `python --version`

  or

  - `which python3`
  - `python3 --version`

  - In case you do not have python3 installed on your system, please follow below steps to install it.
    1. On MacOS:
    `$ sudo ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`
    `$ brew install python`

    2. On CentOS:
    $ sudo yum install rh-python37

- In this program, it will need a python library called requests to make an API call, you can install it using pip. Usually pip will be installed by default along with python installation. If you do not have pip installed, please follow this instruction: https://pip.pypa.io/en/stable/installing/
  `pip3 install requests`

## How to run this python command line program:
`$ git clone https://github.com/jefff-guu/sf_food_trucks.git`
`$ cd sf_food_trucks`
`$ python3 get_foodtruck_location.py`


## For future design:
things to improve:
- Provide search filter like food type/flavor as argument on command line
- Provide a GUI or to fresh terminal console during swithcing pages




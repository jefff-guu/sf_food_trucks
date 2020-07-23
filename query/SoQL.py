"""
This module is to generate a SoQL query/filter with current time in the range of business start and end time window, and fileter with 
current day of a week and where applicant in a ASC order so that we do not have to handle it in a result, SoQL query string looks like below: 
$select=applicant, location&$where='19:09' BETWEEN start24 AND end24 AND dayorder=3&$order=applicant ASC&$limit=10&$offset=0
"""

import datetime

class SoQL_query():
    def __init__(self, *args, **kwargs):
        self.current_time = datetime.datetime.now()
        self.select_fields = ["applicant", "location"]
        self.results_per_page = 10
        self.offset = (kwargs['page_num'] - 1) * self.results_per_page


    def generate_query(self):
        """
        Formats the query in SoQL. Attaching the returned string to the
        base_url will form an API query.
        https://dev.socrata.com/docs/queries/
        """
        
        # Convert current time to 24 hour format.
        time = "\'%s:%02d\'" % (self.current_time.hour,self.current_time.minute)
        
        # Get the current day of a week presented as a number
        dayorder = self.current_time.isoweekday()

        hash_map = {
            'selection_fields': ", ".join(self.select_fields),
            'time_between': "{0} BETWEEN start24 AND end24".format(time)
        }

        query_string = (
            "?$select={selection_fields}"
            "&$where={time_between} AND dayorder={0}"
            "&$order=applicant ASC"
            "&$limit={1}"
            "&$offset={2}").format(dayorder, self.results_per_page, self.offset, **hash_map)
        
        return query_string


if __name__ == '__main__':
    query_string=SoQL_query(page_num=1).generate_query()
    print(query_string)

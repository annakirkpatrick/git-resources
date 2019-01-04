#!/usr/bin/env

import argparse
import os
import sys
from datetime import datetime
import time #for time.sleep()
import re #regular expressions

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('name', type=str, help='name of commit author whose time to compute')
    parser.add_argument('since', type=str, help='time period over which to sum time recorded in commits, valid strings are those accepted by "git log --since=string"')
    parser.add_argument('--repository_path', type=str, help='path to repository; if not provided uses cwd')


    args = parser.parse_args()
    required_params_provided = args.name != None and args.since != None
    assert required_params_provided, "Must specify both commit author name and time range for commits"

    author_name = args.name
    time_since = args.since

    #set proper working directory
    if args.repository_path == None:
        repo_path = os.getcwd()
    else:
        repo_path = args.repository_path
        os.chdir(repo_path)

    #save off today's date and time
    current_date = datetime.now().strftime('%Y-%m-%d_%H-%M-%S') #use '-' rather than ':' in timestamp for Windows file naming rules

    #save time log to disk
    file_header = "# Time tracking log \n# Repo: " + repo_path + "\n# Commit author: " + author_name + "\n# Since: " + time_since + "\n# Current date: " + current_date + "\n"
    file_name = 'time_log_' + current_date + '.tlog'
    log_file = open(file_name, 'w')
    log_file.write(file_header)
    log_file.close()

    print("git log --author=\"{0}\" --pretty=format:\"%ad %an : %s\" --since=\"{1}\" >> {2}".format(author_name, time_since, file_name))
    os.system("git log --author=\"{0}\" --pretty=format:\"%ad %an : %s\" --since=\"{1}\" >> {2}".format(author_name, time_since, file_name))

    #set up some regular expressions for parsing
    min_only = re.compile('\d+[mM]')
    hour_only = re.compile('\d+[hH]')
    both_hour_min = re.compile('\d+[hH]\d+[mM]')

    #read newly-written log
    #include delay because /projects is slow
    time.sleep(1)
    with open(file_name, 'r') as log_file:
        for line in log_file:
            if line.startswith("#"): #header comment lines we wrote
                continue
            words = line.split() #split on whitespace
            time_string = words[len(words) - 1] #grab last chunk of each log entry
            #if a time tracking entry exists, it should be here




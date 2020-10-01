import os
import csv
total_votes = 0
candidates = []
count_candidates = []
candidate_details = dict()
polldata_path = os.path.join('','Resources','election_data.csv')

with open(polldata_path) as csvfile:
    poll_reader = csv.reader(csvfile, delimiter=",")
    poll_header = next(poll_reader)

    for row in poll_reader:
        total_votes += 1
        if str(row[2]) not in candidates:
            candidates.append(str(row[2]))
        count_candidates.append(str(row[2]))
    
    for i in range(len(candidates)):
        candidate_details.update({candidates[i]:count_candidates.count(candidates[i])})


    print("Election Results")
    print("-------------------")
    print("Total Votes : "+str(total_votes))
    print("-------------------")
    for i in range(len(candidates)):
        print(str(candidates[i]) + " : " + str(round((float((candidate_details[candidates[i]])/total_votes)*100),4)) + "%  (" + str(candidate_details[candidates[i]]) + ")") 
    print("-------------------")
    winnervotes = max(list(candidate_details.values()))
    print("Winner : " + str(list(candidate_details.keys())[list(candidate_details.values()).index(winnervotes)]))

output_poll = os.path.join('','analysis','poll_output.txt')

with open(output_poll, 'w') as csvfile:
    csvfile.truncate()
    csvfile.write("Election Results")
    csvfile.write("\n")
    csvfile.write("-------------------")
    csvfile.write("\n")
    csvfile.write("Total Votes : "+str(total_votes))
    csvfile.write("\n")
    csvfile.write("-------------------")
    csvfile.write("\n")
    for i in range(len(candidates)):
        csvfile.write(str(candidates[i]) + " : " + str(round((float((candidate_details[candidates[i]])/total_votes)*100),4)) + "%  (" + str(candidate_details[candidates[i]]) + ")") 
        csvfile.write("\n")
    csvfile.write("-------------------")
    csvfile.write("\n")
    csvfile.write("Winner : " + str(list(candidate_details.keys())[list(candidate_details.values()).index(winnervotes)]))

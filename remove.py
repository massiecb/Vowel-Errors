# Program removes Tiny and Candy, the multisyllable words, from the output of extract_april3.py. 
# Output will be in the same order.

import sys

def remove():
    print ("start\n")
    try:
        fin = open ("output_raw_data.txt", "r") # name of the output from extract_april3.py
    except:
        print ("Failed to open input file\n")
        
    fout = open ("output_raw_data_single_syll.txt", "w")
    for line in fin:
        if "candy" in line or "tiny" in line or "dress":
            #print ("Remove:", line)
            #skip
            continue
        else:
            #print ("keep:", line)
            fout.write(line)
    fin.close()
    fout.close()
    print ("end\n")
    sys.exit()
    
    
remove()
# Collects experiement information and codes for use in statistical analysis. Has to be in parent directory. Stable Version 1.0 July17 

import sys
import os

def get_info (file, fout):
    #print ("here")
    file = file.strip()
    aline = []
    conerrorlist = ['practice', 'n/a', 'st', 'pv', 'cc']
    vowerrorlist = ['practice', 'n/a', 'lx', 'bk', 'dr']
    wavlist = ['v', 'r', 'c', 'cm'] #remember to add 1
    fin = open ("%s" %file, 'r', encoding = 'utf - 16 - le', errors = 'ignore')
    for line in fin:
        line = line.strip()
        line = line.lower()
        
        if "correct" in line:
            line = line.split(":")
            #print (line)
            line[1] = line[1].strip()
            aline.append (line[1])
            
        if "conerrortype" in line:
            line = line.split(":")
            line[1] = line[1].strip()
            #print (line)
            #print (line[1])
            #print (line[1] in conerrorlist)
            if line[1] in conerrorlist:
               # if line[1] == conerrorlist[0]:
               #     aline.append ((conerrorlist.index(line[1]))+1)
               # else:
                aline.append (conerrorlist.index(line[1]))
                    
        if "vowerrortype" in line:
            line = line.split(":")
            #print (line)
            line[1] = line[1].strip()
            if line[1] in vowerrorlist:
                #if line[1] in vowerrorlist [0] :
                #    aline.append((vowerrorlist.index(line[1]))+1)
                #else:
                aline.append (vowerrorlist.index(line[1]))
                    
        if "audio" in line:
            line = line.split(":")
            #print (line)
            line[1] = line[1].strip()
            #print (line[1])
            wav = line[1].split("_")
            #print (wav)
            wav[1] = wav[0].strip()
            #print (wav[0])
            if wav[0] == 'p':
                #print (wav[1] == 'p')
                aline.append("0")
            elif wav[0] in wavlist:
                aline.append (wavlist.index(wav[0]) +1)
            #aline.append (line[1])
            
        if "audslide.resp" in line:
            line= line.split (":")
            #print (line)
            line[1] = line[1].strip()
            aline.append (line[1])
            
        if "confidence.resp" in line:
            line = line.split(":")
            #print (line)
            line[1] = line[1].strip()
            aline.append(line[1])
            #print (aline)
            
        #if "level" in line:
        #    print (fin.readline())
        
        if "level" in line:
            #print (len(aline))
            if len (aline) == 6:
                #print ("aline =  %s" %aline)
                fout.write ('{:<20}{:<20}{:<20}{:<20}{:<20}{:<20}{:<20}'.format (file, aline[1], aline[4], aline[0], aline[2], aline[3], aline[5]))
                if aline[0] == aline[4]:
                    fout.write ("1")
                else:
                    fout.write ("0")
                
                fout.write ("\n")
                fout.write ("\n")
                aline = []
                
def main():
    print ("start")
    folderout = []
    #print ("here")
    current_dir = os.getcwd()
    try:
        for file in os.listdir("./"):
            if os.path.isdir ("%s" %file):
                folderout.append (file)
                
    except:
        print ("Error: Failed to find folders in directory")
    
    for folder in folderout:
        #print ("here")
        fout = open ("output_%s.txt" %folder, 'w')
        fout.write ('{:<20}{:<20}{:<20}{:<20}{:<20}{:<20}{:<20}{:<20}'.format ("participxant number", "stimuli", "response", "answer", "conerror", "vowerror", "confidence", "accuracy"))
        fout.write("\n")
        fout.write("\n")
        os.chdir ("%s" %folder)
        newdirect = os.popen ("ls")
       # print (folder)
        for file in newdirect:
            #print (file)
            get_info (file, fout)
        fout.close()
        os.chdir ("%s" %current_dir)
        print ("End\n")
        
    sys.exit()
        
main()
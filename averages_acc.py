import os
import sys


#stable version 1.1 July 17 accuracy
def writeto(liblist, libname, fout):
    # need to fprint in order
    for dic in libname:
        fout.write ("\n")
        fout.write (dic)
        fout.write ("\n")
        sort_list = []
        index= libname.index(dic)
        #print ("here")
        for key in liblist[index]:
            sort_list.append (key)
        sort_list.sort()
        #print (sort_list)
        for element in sort_list:
            #print (element, key)
            for key in liblist[index]:
            #for element in sort_list:
                if key == element:
                    #print (element, key)
                    fout.write (key)    
                    fout.write (":")    
                    entry_len = len (liblist[index][key]) 
                    anum = 0    
                    for num in liblist[index][key]:
                        anum = anum + int (num)
                   # print (liblist[index], key)
                   # print (anum, entry_len, anum/entry_len)
                    writenum = anum/entry_len
                    fout.write (str (writenum))
                    fout.write ("\n")
        fout.write ("\n")
        
        for element in sort_list:
            #print ("here")
            anum = 0
            length = 0
            #print (int (element[2]) > 1)
            if element[0] == '1' and element[2] == '1':
                #print ("here")
                for num in liblist[index][element]:
                    anum = anum + int (num)
                    length = length + 1
                writenum = anum/length
                #print (writenum)
                #fout.write (str(writenum))
                #fout.write ("\n")
            
    
    
def makelib(adict, line, fout): #takes a line from the file and transforms it into a dictionary
    line_index = len (line) - 1
    string = line[4] + '-' + line[5]
    if string in adict:
        adict[string].append (line[line_index])
    else:
        adict[string] = list()
        adict[string].append (line[line_index])
    
    return adict                    
    

def get(fin, fout, liblist, libname): #will it matter if the dictionary already exists? won't it just add to it? search for the dictionary name rather than have 2 dictionaries
    for line in fin:
        if "dis" in line:
            line = line.lower()
            line = line.strip()
            line = line.split() # try if line[0] in libname and liblist, elif not in libname and liblist, else raise error
            if line[0] in libname:
                lib_index = libname.index (line[0])
                makelib (liblist[lib_index], line, fout)
            else:
                libname.append (line[0])
                liblist.append (line[0])
                lib_index = (len (liblist)) - 1 # track index of the library
                liblist[lib_index] = dict ()
                makelib (liblist[lib_index], line, fout)
    

    
def main ():
    print ("Start\n")
    liblist = [] # list of all libraries
    libname = [] # hold name of libraries, index of library to be same as library in liblist
    #print (os.listdir())
    try:
        fin = open ("output_raw_data_single_syll.txt", "r")  #this is the name of the input file output_ParticipantTxtFiles.txt
        fout = open ("output_narrow_acc_ss.txt", "w")
        get (fin, fout, liblist, libname)
        writeto (liblist, libname, fout)
        fout.close()
        fin.close()
        print ("End")
    except:
        print ("Failed to find input file\n")
        
    sys.exit()
main()
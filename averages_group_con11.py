import os
import sys


#stable version 1.2 August 25
def writeto(liblist, libname, fout):
    # need to print in order
    # group1 1-2,1-3,1-4, group 2 2-1,3-1,4-1, group 3 2-2,2-3,2-4,3-2,3-3,3-4,4-2,4-3, 4-4 ie the rest
    for dic in libname:
        no_error = []
        practice = []
        vowel_list = []
        con_list = []
        rest_list = []
        fout.write ("\n")
        fout.write (dic)
        fout.write ("\n")
        #sort_list = []
        index= libname.index(dic)
        for key in liblist[index]:
            if key == "1-1":
                for i in liblist[index][key]:
                    no_error.append(i)
            if key == "0-0":
                for i in liblist[index][key]:
                    practice.append(i)
            if key == "1-2" or key == "1-3" or key == "1-4":
                   # print (libname[index])
                   # print (key, ":", liblist[index][key])
                for i in liblist[index][key]:
                    con_list.append (i)
            if key == "2-1" or key == "3-1" or key == "4-1":
                #print (libname[index])
                #print (key, ":", liblist[index][key])                    
                for i in liblist[index][key]:
                    vowel_list.append(i)
                        
            if key == "2-2" or key == "2-3" or key == "2-4" or key == "3-2" or key == "3-3" or key == "3-4" or key == "4-2" or key == "4-3" or key =="4-4":
                for i in liblist[index][key]:
                    rest_list.append(i)
            #else:
                #print (libname[index])
                #print (key, ":", liblist[index][key])
             #   for i in liblist[index][key]:
              #      no_error.append (i)
                        
        vow_num = len(vowel_list)
        #print (vow_num)
        con_num = len(con_list)
        #print (con_num)
        rest_num = len(rest_list)
        #print (rest_num)
        noerror_num = len (no_error)
        #print (no_error)
        #print (noerror_num)
        practice_num = len(practice)
        fout.write ("Con error: ")
        num = 0
        for anum in vowel_list:
            num = float (anum) + num
        write_num = str (num/vow_num)
        fout.write (write_num)
        fout.write ("\n")
        num = 0
        
        fout.write ("Vowel error: ")
        for anum in con_list:
            num = num + float (anum)
        write_num = str (num/con_num)
        fout.write (write_num)
        fout.write ("\n")
        num = 0
        
        fout.write ("Rest errors: ")
        for anum in rest_list:
            num = num + float (anum)
        write_num = str(num/rest_num)
        fout.write (write_num)
        fout.write ("\n")
        num = 0
        
        fout.write ("No errors: ")
        for anum in no_error:
            num = num + float (anum)
        write_num = str(num/noerror_num)
        fout.write (write_num)
        fout.write ("\n")
        num = 0
        
        fout.write ("Practice: ")
        for anum in practice:
            num = num + float (anum)
        write_num = str(num/practice_num)
        fout.write(write_num)
        fout.write("\n")
        num = 0

        
                
            #for element in sort_list:
               # if key == element:
                    #print (element, key)
                    #fout.write (key)    
                    #fout.write (":")    
                    #entry_len = len (liblist[index][key]) 
                    #anum = 0    
                    #for num in liblist[index][key]:
                    #    anum = anum + int (num)
                   # print (liblist[index], key)
                   # print (anum, entry_len, anum/entry_len)
                    #writenum = anum/entry_len
                    #fout.write (str (writenum))
                    #fout.write ("\n")
       # fout.write ("\n")
    
    
def makelib(adict, line, fout): #takes a line from the file and transforms it into a dictionary
    line_index = len (line) - 2 # confidence
    #if "14154" in line[0]:
    #    print (line[2], line[3])
    string = line[4] + '-' + line[5]
   # if "14154" in line[0]:
   #     if string == "2-1":
            #print (line[2], line[3])
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
        fin = open ("output_raw_data_single_syll.txt", "r")  #this is the name of the input file output_MultiSyllables Removed_aug24.txt
    except:
        print ("Failed to find input file\n")    
    fout = open ("condata_ss.txt", "w")
    get (fin, fout, liblist, libname)
    writeto (liblist, libname, fout)
    fout.close()
    fin.close()
    print ("End")
        
    sys.exit()
main()
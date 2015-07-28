def writeto (liblist, libname, fout):
    for dic in libname:
        fout.write("\n")
        fout.write(dic)
        fout.write("\n")
        sum = []
        total = 0
        index = libname.index(dic)
        for key in liblist[index]:
            for i in liblist[index][key]:
                sum.append(i)
        for num in sum:
            total = float(num) + total
        write_num = str(total/(len (sum)))
        fout.write(write_num)
        fout.write("\n")
            
        
def makelib(adict, line, fout):
    line_index = len (line) - 2
    string = line[4] + '-' + line[5]
    if string in adict:
        adict[string].append (line[line_index])
    else:
        adict[string] = list()
        adict[string].append (line[line_index])
    
    return adict                    
        

def get(fin, fout, liblist, libname):
    for line in fin:
        if "dis" in line:
            line = line.lower()
            line = line.strip()
            line = line.split()
            if line[0] in libname:
                lib_index = libname.index(line[0])
                makelib(liblist[lib_index], line, fout)
            else:
                libname.append(line[0])
                liblist.append(line[0])
                lib_index = len(liblist) - 1
                liblist[lib_index] = dict()
                makelib(liblist[lib_index], line, fout)

def main():
    print ("begin\n")
    try:
        fin = open ("output_raw_data_single_syll.txt", "r")
    except:
        print ("file not found\n")
    liblist = []
    libname = []
    fout = open ("output_overall_con_ss.txt", "w")
    get (fin, fout, liblist, libname)
    writeto(liblist, libname, fout)
    fout.close()
    fin.close()
    print ("end\n")

main()
    
    
import struct

import dataReader
import dataWriter

print("rrl")


class RRLDataProcessing:

    def read_files(self):
        rrlfiles = dataReader.readfilelist("..\RRLPy_data")
        print("len:  ",len(rrlfiles))
        dt = list()
        for i in rrlfiles[3:13]:
            dt.append(i[1])
        print(dt)
        self.rrlfiles = rrlfiles

    def write_to_excel(self):
        dataWriter.write_excel('datapro/rrl_data.xlsx', self.rrlfiles)

    def load_data_from_file(self,num=0):
        # if num<0:
        #     filename = self.rrlfiles[num][0]
        # else:

        filename = "datapro/d_2005_5_6_casa.001"
        print(filename)

        with open(filename, mode='rb') as lines:
            c = lines.read()

            n_one_sp = 1025*4
            n = int(len(c)/4)
            n_sp = n / n_one_sp

            print("size: ",len(c), "   n:", n, "  ", n_sp)

            dt = struct.unpack('I'*n, c)

            print(len(dt)/n_sp)
            for i in range(0,4):
                x = (i+1)*1024+i  +  4100*0
                print(i,"  ",x,"  ",dt[x])





r = RRLDataProcessing()
r.load_data_from_file(-1)


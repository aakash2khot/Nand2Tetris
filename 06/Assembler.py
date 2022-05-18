#!/usr/bin/env python3

import sys

class Parser:
    def __init__(self,code):
        self.code = code
        self.type=None
        self.value=None
        self.dest=None
        self.comp=None
        self.jump=None
        self.Remove_unwanted()
        self.Type_of_code()

    def Type_of_code(self):
        if self.code == '':
            return
        elif self.code.startswith('@'):
            self.type='A'
        elif self.code.startswith('('):
            self.type='L'
        else:
            self.type = 'C'

    def put_value(self):
        if self.type != 'A':
            return None
        # Take all after first word till a space occurs
        self.value = self.inst[1:].split(' ')[0]
        return self.value

    def Remove_unwanted(self):
        #Remove unwanted spaces
        self.code=self.code.strip()
        comment = self.code.find('//')
        
        if comment==-1:
            self.code=self.code.strip() #No comment
        elif comment==0:
            self.code='' # discard the line of comment
        else:
            self.code=self.code[0:comment].strip() # Take only the part before comment
        
    def dest1(self):
        # As we know dest=comp;jump
        # So we need a part before "=" and C type
        Comparator = self.code.find('=')
        if self.type != 'C':
            return None
        if Comparator == -1:
            return None
        self.dest=self.code[0:Comparator].strip()
        return self.dest
    
    def comp1(self):
        # As we know dest=comp;jump
        # So we want part after '=' and before ';'
        after = self.code.find('=')
        before = self.code.find(';')
        if self.type != 'C':
            return None
        if after != -1 and before !=-1:
            self.comp = self.code[after+1:before].strip()
        elif after != -1 and before == -1:
            self.comp = self.code[after+1:].strip()
        elif after == -1 and before != -1:
            self.comp = self.code[0:before].strip()
        elif before==-1 and after==-1:
            self.comp = self.code.strip()
        return self.comp

    def jump1(self):
        # As we know dest=comp;jump
        # So we want part after ';'
        after = self.code.find(';')
        if self.type != 'C':
            return None
        if after == -1:
            return None
        self.jump = self.code[after+1:].strip()
        return self.jump

class Code:
    def __init__(self,part):
        self.part = part
        self.value=None
        self.dest=None
        self.comp=None
        self.jump=None

    def Dec_to_Bin(self,decimal):
        return format(decimal,'016b') # Convert to 16 bit binary
    def put_value(self):
        if self.part == None:
            return None
        self.value = self.Dec_to_Bin(int(self.part))
        return self.value
    def dest1(self):
        if self.part==None:
            self.dest = '000'
        elif self.part =='M':
            self.dest='001'
        elif self.part =='D':
            self.dest='010'
        elif self.part =='MD':
            self.dest='011'
        elif self.part =='A':
            self.dest='100'
        elif self.part =='AM':
            self.dest='101'
        elif self.part =='AD':
            self.dest='110'
        elif self.part =='AMD':
            self.dest='111'
        return self.dest
    def comp1(self):
        # For comp part, we will se values of a and c1c2c3c4c5c6
        a='0'
        c=''
        if self.part == None:
            self.comp= None
        elif self.part =='0':
            a='0'
            c='101010'
        elif self.part =='1':
            a='0'
            c='111111'
        elif self.part =='-1':
            a='0'
            c='111010'
        elif self.part == 'D':
            a='0'
            c='001100'
        elif self.part =='A':
            a='0'
            c='110000'
        elif self.part =='!D':
            a='0'
            c='001101'
        elif self.part =='!A':
            a='0'
            c='110001'
        elif self.part =='-D':
            a='0'
            c='001111'
        elif self.part =='-A':
            a='0'
            c='110011'
        elif self.part =='D+1':
            a='0'
            c='011111'
        elif self.part =='A+1':
            a='0'
            c='110111'
        elif self.part =='D-1':
            a='0'
            c='001110'
        elif self.part =='A-1':
            a='0'
            c='110010'
        elif self.part =='D+A':
            a='0'
            c='000010'
        elif self.part =='D-A':
            a='0'
            c='010011'
        elif self.part =='A-D':
            a='0'
            c='000111'
        elif self.part =='D&A':
            a='0'
            c='000000'
        elif self.part =='D|A':
            a='0'
            c='010101'
        elif self.part =='M':
            a='1'
            c='110000'
        elif self.part =='!M':
            a='1'
            c='110001'
        elif self.part =='-M':
            a='1'
            c='110011'
        elif self.part =='M+1':
            a='1'
            c='110111'
        elif self.part =='M-1':
            a='1'
            c='110010'
        elif self.part =='D+M':
            a='1'
            c='000010'
        elif self.part =='D-M':
            a='1'
            c='010011'
        elif self.part =='M-D':
            a='1'
            c='000111'
        elif self.part =='D&M':
            a='1'
            c='000000'
        elif self.part =='D|M':
            a='1'
            c='010101'
        self.comp = a+c
        return self.comp
    def jump1(self):
        if self.part == None:
            self.jump = '000'
        elif self.part == 'JGT':
            self.jump = '001'
        elif self.part == 'JEQ':
            self.jump = '010'
        elif self.part == 'JGE':
            self.jump = '011'
        elif self.part == 'JLT':
            self.jump = '100'
        elif self.part == 'JNE':
            self.jump = '101'
        elif self.part == 'JLE':
            self.jump = '110'
        elif self.part == 'JMP':
            self.jump = '111'
        return self.jump
    
class Symbol_Table:
    def __init__(self):
        self.table={}
        self.Symbols()
    def Symbols(self):
        for n in range(16):
            self.table["R"+str(n)]=n
        self.table["SCREEN"]=16384
        self.table["KBD"]=24576
        self.table["SP"]=0
        self.table["LCL"]=1
        self.table["ARG"]=2
        self.table["THIS"]=3
        self.table["THAT"]=4
    def check(self,sym):
        if self.table.get(sym)==None:
            return False
        else:
            return True
    def Add_Symbol(self,sym,val):
        self.table[sym]=val
    def Get_Value(self,sym):
        return self.table.get(sym)

class Iterate:
    def __init__(self,table):
        self.table=table
    def Iteration(self):
        with open(sys.argv[1],'r') as file_asm:
            i=-1
            for code in file_asm:
                pars=Parser(code)
                if pars.type=='A' or pars.type=='C':
                    i=i+1
                if pars.type=='L':
                    sym=pars.code[1:-1]
                    if not self.table.check(sym):
                        self.table.Add_Symbol(sym,i+1)
    def Functions(self):
        with open(sys.argv[1].split('.')[0]+'.hack','w') as file_hack:
            with open(sys.argv[1],'r') as file_asm:
                bits=16
                for code in file_asm:
                    pars=Parser(code)
                    if pars.type=='A':
                        sym=pars.code[1:]
                        if self.table.check(sym):
                            in_binary = Code(self.table.Get_Value(sym))
                            file_hack.write(in_binary.put_value()+'\n')
                        else:
                            try:
                                v=int(sym)
                                in_binary = Code(v)
                                file_hack.write(in_binary.put_value()+'\n')
                            except ValueError:
                                self.table.Add_Symbol(sym,bits)
                                in_binary = Code(bits)
                                file_hack.write(in_binary.put_value()+'\n')
                                bits+=1
                    elif pars.type=='C':
                        dest = Code(pars.dest1())
                        comp = Code(pars.comp1())
                        jump = Code(pars.jump1())
                        file_hack.write('111'+comp.comp1()+dest.dest1()+jump.jump1()+'\n')
    
def main():
    Table = Symbol_Table()
    I = Iterate(Table)
    I.Iteration()
    I.Functions()

if __name__ == '__main__':
    main()



        
        

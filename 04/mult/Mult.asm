// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

// Put your code here.

// i=0
@i
M=0
// RAM[2]=0
@2
M=0

(ADD)
@i
D=M // D reg -> i
@0
D=D-M // D reg -> i-RAM[0]
@END
D;JGE // Jump if D>=0 to END

@1
D=M // D-> RAM[1]
@2
M=M+D// R2-> R2+R1
@i
M=M+1
@ADD
0;JMP

(END)
@END
0;JMP// If END is called, calculation is over so you can stop
// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

(START)
@SCREEN 
D=A    
@st      
M=D // st-> screen  
@KBD    
D=M     // input from keyboard
@WHITE
D;JEQ  // if no input then white
@BLACK
0;JMP   //else black

(WHITE)
@st
A=M
M=0 //starting from 0
@st
M=M+1
@st
D=M  
@KBD 
D=A-D 
@START
D;JEQ   // equal to 0 -> end
@WHITE   
0;JMP   // else continue

(BLACK)
@st
A=M
M=-1  
@st
M=M+1
@st
D=M 
@KBD
D=A-D 
@START
D;JEQ    // equal to 0->end 
@BLACK 
0;JMP  // else continue

#!/usr/bin/python3

import sys
import os


u8_vars = {}
u16_vars = {}
variables = {}

functions = []
section_data = []
section_text = []
errors = []

lines = []
try:
  lines = open(sys.argv[1],"r").readlines()
except:
  print("File doesnt exists")
  sys.exit(0)





msgnum = 1
line_num = 1

section_data.append("worker dq 0")

functions_instructions = open("functions.asm","r").readlines()
for x in functions_instructions:
  functions.append(x)




def pr(msg):
  global msgnum
  section_data.append("msg" + str(msgnum) + " db " + msg)
  section_text.append("mov rax,1")
  section_text.append("mov rdi,1")
  section_text.append("mov rsi,msg" + str(msgnum))
  section_text.append("mov rdx,msglen" + str(msgnum))
  section_data.append("msglen" + str(msgnum) + ": equ $ - msg" + str(msgnum))
  section_text.append("syscall")
  msgnum = msgnum + 1
  
def prl(msg):
  global msgnum
  section_data.append("msg" + str(msgnum) + " db " + msg)
  section_text.append("mov rax,1")
  section_text.append("mov rdi,1")
  section_text.append("mov rsi,msg" + str(msgnum))
  section_text.append("mov rdx,msglen" + str(msgnum))
  section_data.append("msglen" + str(msgnum) + ": equ $ - msg" + str(msgnum))
  section_text.append("syscall")
  msgnum = msgnum + 1
  section_text.append("mov rax,1")
  section_text.append("mov rdi,1")
  section_text.append("mov rsi,endl")
  section_text.append("mov rdx,1")
  section_text.append("syscall")
  
def endline():
   section_text.append("mov rax,1")
   section_text.append("mov rdi,1")
   section_text.append("mov rsi,endl")
   section_text.append("mov rdx,1")
   section_text.append("syscall")


for line in lines:
   parse = line.split(" ")
   if parse[0] == "print":
     arg_string = parse[1]
     if arg_string[0] == '"':
       if arg_string[len(arg_string)-1] == '"':
         pr(arg_string)
     elif arg_string[0] == "'":
       if arg_string[len(arg_string)-1] == "'":
         pr(arg_string)
     else:
       errors.append("Invalid definition of string argument for function print on line " + str(line_num))
   elif parse[0] == "println":
     arg_string = parse[1]
     if arg_string[0] == '"':
       if arg_string[len(arg_string)-1] == '"':
         prl(arg_string)
     elif arg_string[0] == "'":
       if arg_string[len(arg_string)-1] == "'":
         prl(arg_string)
     elif arg_string in variables:
       if variables[arg_string] == "u8":
         section_text.append("mov al, byte [" + arg_string + "]" )
         section_text.append("mov rdi,rax")
         section_text.append("call print_num")
         endline()

       elif variables[arg_string] == "u16":
         section_text.append("mov ax, word [" + arg_string + "]" )
         section_text.append("mov rdi,rax")
         section_text.append("call print_num")
         endline()
     else:
       errors.append("Invalid definition of  argument  for function println on line " + str(line_num))
   elif parse[0] == "let":
     if len(parse) == 4:
       if parse[1] == "u8":
         section_data.append(parse[2] + " db " + parse[3])
         variables[parse[2]] = "u8"
         u8_vars[parse[2]] = int(parse[3])
       elif parse[1] == "u16":
         section_data.append(parse[2] + " dw " + parse[3])
         variables[parse[2]] = "u16"
         u16_vars[parse[2]] = int(parse[3])
       else:
         errors.append("Uknown data type on line " + str(line_num))
     else:
       errors.append("Invalid definition of arguments for function let on line " + str(line_num))
   elif parse[0] == "add":
     if len(parse) == 3:
       if parse[1] in variables:
         if variables[parse[1]] == "u8":
           section_text.append("add byte [" + parse[1] + "]," + parse[2])
         elif variables[parse[1]] == "u16":
           section_text.append("add word [" + parse[1] + "]," + parse[2])
   else:
     errors.append("Undefined function '" + parse[0] + "' on line " + str(line_num))
   line_num += 1

if len(errors) != 0:
   for error in errors:
     print("Error:" + error)
   sys.exit(0)

section_text.append("mov rax,60")
section_text.append("mov rdi,0")
section_text.append("syscall")
section_data.append("endl db 10")


file_out = "global _start\n"
file_out = file_out + "section .text\n"

for x in functions:
  file_out += x + "\n"

file_out = file_out + "_start:\n"
for x in section_text:
   file_out += x + "\n"

file_out = file_out + "section .data\n"
for x in section_data:
   file_out += x + "\n"

open(sys.argv[1] + ".asm","w").write(file_out)
os.system("nasm " + sys.argv[1] + ".asm" + " -f elf64 -o object.o")
os.system("ld object.o -o " + sys.argv[1] + ".out")
print("Success build")
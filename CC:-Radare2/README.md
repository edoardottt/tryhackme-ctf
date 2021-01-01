# CC: Radare2

- Read the above 

	no answer needed

- What flag you set to analyze the binary upon entering the r2 console (equivalent to running aaa once your inside the console)

	- `-a`

- How do you enable the debugger?

	- `-d`

- How do you open the file in write mode?

	- `-w`

- How do you enter the console without opening a file

	- `-`

- What command "Analyzes Everything" (all functions and their arguments: Same as running with radare with -A)

	- `aaa`

- What command does basic analysis on functions?

	- `af`

- How do you list all functions?

	- `afl`

- How many functions are in the example1 binary?

	- `r2 -d example1`
	- `aaa`
	- `afl`
	- `12`

- What is the name of the secret function in the example1 binary?

	- `secret_func`

- What command shows all the information about the file that you're in?

	- `iA`

- How do you get every string that is present in the binary?

	- `izz`

- What if you want the address of the main function?

	- `iM`

- What character do you add to the end of every command to get the output in JSON format?

	- `j`

- How do you get the entrypoint of the file?

	- `ie`

- What is the secret string hidden in the example2 binary?

	- `r2 -d example2`
	- `aaa`
	- `izz`
	- `*******`

- How do you print out the the current memory address your located at in the binary?

	- `s`

- What command do you use to go to a specific point in memory with the syntax `<command> <address>`?

	- `s`

- What command would you run to go 5 bytes forward?

	- `s+ 5`

- What about 12 bytes backward?

	- `s- 12`

- How do you undo the previous seek?

	- `s-`

- How would go to the memory address of the main function?

	- `s main`

- What if you wanted to go to the address of the rax register?

	- `sr rax`

- Play around with the s command in the example1 and example2 binaries

	no answer needed

- How would you print the hex output of where you currently are in memory?

	- `px`

- How would you print the disassembly of where you're currently at in memory?

	- `pd`

- What if you wanted the disassembly of the main function?

	- `pd f main`

- What command prints out the emoji hexdump? (this is not useful at all I just find it funny)

	- `pxe`

- What if you decided you were too good for rows and you wanted the disassembly in column format?

	- `pc`

- What is the value of the first variable in the main function for the example 3 binary?

	- `r2 -d example3`
	- `aaa`
	- `pdf @ main`
	- `1`

- What about the second variable?

	- `5`

- How many functions are in the binary?

	- `r2 -d midterm`
	- `aaa`
	- `afl`
	- `13`

- What is the value of the hidden string?

	- `izz`
	- `you*******me`

- What is the return value of `secret_func()`?

	- `pdf @ sym.secret_func`
	- `4`

- What is the value of the first variable set in the main function(in decimal format)?

	- `pdf @ main`
	- `12`

- What about the second one(also in decimal format)?

	- `192`

- What is the next function in memory after the main function?

	- `afl`
	- `*******_func`

- How do you get a hexdump of four bytes of the memory address your currently at?

	- `px 2`

- How do you set a breakpoint?

	- `db`

- What command is used to print out the values of all the registers?

	- `dr`

- How do you run through the program until the program either ends or you hit the next breakpoint?

	- `dc`

- What if you want to step through the binary one line at a time?

	- `ds`

- How do you go forth 2 lines in the binary?

	- `ds 2`

- How do you list out the indexes and memory addresses of all breakpoints?

	- `dbi`

- Go back through all previous binaries and mess around with debug mode.

	no answer needed

- How do you enter "graph mode" which allows everything to be organized in nice readable boxes?(A personal favorite of mine. Also note that the second character is uppercase)

	- `vV`

- What character do you press to run normal radare commands inside visual mode?

	- `:`

- How do you go back to the regular radare shell(leaving visual mode)?

	- `q`

- What if you want to step through the binary inside Visual mode?

	- `s`

- How do you add a comment?

	- `;`

- Look through any of the binaries in Visual Mode and see just how much more beautiful everything looks.

	no answer needed

- How do you write a string to the current memory address.

	- `w`

- What command lists all write changes?

	- `wc`

- What command modifies an instruction at the current memory address?

	- `wa`

- Get the example4 binary to show the You win! message

	no answer needed

- What is the password that outputs the you win! message?

	- `r2 -d the_final_exam`
	- `aaa`
	- `afl`
	- `pdf @ main`
	- `pdf @ sym.get_password`
	- `db 0x5635b2cf682f`
	- `dc`
	- `edordottt`
	- `dr`
	- `s 0xffffffffffffffda`
	- `px 10`
	- `onykbnyddd`
	- So it's ROT-10
	- `********`




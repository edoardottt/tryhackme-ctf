# Linux FUndamentals - Part 3

- Read the above

	no answer needed

- Deploy the machine attached to this task!
NOTE: If you have a machine open in the Welcome room (or any other room) please go to that room and terminate it before deploying the machine attached to this task. These machines are not the same, and only the one attached to this room will work.

	no answer needed
	
	- `ssh shiba3@<TARGET_IP>`
	- Type `yes` and enter the password `happynootnoises`

- Using relative paths, how would you cd to your home directory.

	- `cd ~`

- Using absolute paths how would you make a directory called test in /tmp

	- `mkdir /tmp/test`

- How would I link /home/test/testfile to /tmp/test?

	- `ln /home/test/testfile /tmp/test`

- How do you find files that have specific permissions?

	- `-perm`

- How would you find all the files in /home

	- `find /home`

- How would you find all the files owned by paradox on the whole system

	- `find / -user paradox`

- What flag lists line numbers for every string found?

	- `-n`

- How would I search for the string boop in the file aaaa in the directory /tmp

	- `grep boop /tmp/aaaa`

- What is shiba4's password

	- `mkdir test && touch test/test1234`
	- `find / -name shiba4 | grep shiba4 | grep shiba4`
	- `/opt/secret/shiba4`
	- `test1234`
	- `su shiba4` and enter password `test1234`

- Read the above

	no answer needed

- How do you specify which user you want to run a command as.

	- `-u`

- How would I run whoami as user jen?

	- `sudo -u jen whoami`

- How do you list your current sudo privileges(what commands you can run, who you can run them as etc.)

	- `-l`

- How would I add the user test to the group test?

	- `sudo usermod -a -G test test`

- Read the above

	no answer needed

- Read the above.

	no answer needed

- Read the above

	no answer needed

- Read the above

	no answer needed

- Read the above!

	no answer needed



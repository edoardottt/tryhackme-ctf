# Introduction to Django

- Read the above.

	  no answer needed

- How would we create an app called Forms?

	- `python3 manage.py startapp Forms`

- How would we run our project to a local network?

	- `python3 manage.py runserver 0.0.0.0:80`

- Read the above

	  no answer needed

- Flag from GitHub page

	- `THM{**************}`

- Admin panel flag?

	- Retrieve the `db.sqlite3` file.
	- `sqlite3 db.sqlite3`
	- `.databases`
	- `select * from db.auth_user`
	- `THM{************}`

- User flag?

	- `select * from db.auth_user`
	- Go to the PasteBin link
	- `hash-identifier`
	- Go to [crackstation](https://crackstation.net) and crack the hash
	- `su StrangeFox` and crack the hash
	- `cat ~/user.txt`
	- `THM{************}`

- Hidden flag?

	- `cd ~/messagebox/messagebox`
	- `cat * | grep THM`
	- `THM{************}`





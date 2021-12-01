# Day 1 - A Christmas Crisis

- **Deploy your AttackBox (the blue "Start AttackBox" button)** and the tasks machine (green button on this task) if you haven't already. Once both have deployed, open FireFox on the AttackBox and copy/paste the machines IP into the browser search bar.

		no answer needed

- Register for an account, and then login.
What is the name of the cookie used for authentication?

	- Go into a browser (I suggest you Chrome or Firefox) and fire up browser developers tools (F12). Go into the storage tab and select cookies on the left. `auth`.

- In what format is the value of this cookie encoded?

	- `hexadecimal`

- Having decoded the cookie, what format is the data stored in?

	- `json`

- Figure out how to bypass the authentication.
What is the value of Santa's cookie?

	- Decode your cookie value from hexadecimal to Text. I used [this](https://cryptii.com/pipes/hex-decoder). Then change your username to `santa`. You should have something like: `************************************************************************************************d65223a2253616e7461227d`
	- Now, if you change the previous cookie with this new one and refresh the page you will see some changes...

- Now that you are the santa user, you can re-activate the assembly line!
What is the flag you're given when the line is fully active?

	- `THM{********************************}`

## see you...

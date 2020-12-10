# Don't be sElfish!

Before we begin, we're going to need to deploy two Instances:

	1. The THM AttackBox by pressing the " Start AttackBox" button at the top-right of the page.
	2. The vulnerable Instance attached to this task by pressing the "Deploy" button at the top-right of this task/day.

- Using enum4linux, how many users are there on the Samba server?

	- `enum4linux -a <TARGET_IP>`
	- `3`

- Now how many "shares" are there on the Samba server?

	- `4`

- Use smbclient to try to login to the shares on the Samba server (10.10.151.244). What share doesn't require a password?

	- `smbclient //<TARGET_IP>/<SHARE>`
	- `tbfc-santa`

- Log in to this share, what directory did ElfMcSkidy leave for Santa?

	- `jingle-tunes`



### see you ...

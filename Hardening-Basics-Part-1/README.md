# Hardening Basics Part 1

- Deploy the VM and let's get started!

	  no answer needed

- No questions

	  no answer needed

- No questions

	  no answer needed

- No questions

	  no answer needed

- No questions

	  no answer needed

- No questions

	  no answer needed

- No questions

	  no answer needed

- No questions

	  no answer needed

- No questions

	  no answer needed

- No questions

	  no answer needed

- What group are users automatically added to in Ubuntu?

	- `sudo`

- What would be the command to add an existing user, nick, to the sudo group? You're running as root

	- `usermod -aG nick sudo`

- What command as a user can we enter to see what we are allowed to execute with sudo?

	- `sudo -l`

- Where is the sudo policy file stored?

	- `/etc/sudoers`

- When in visudo and you see `%____`, what does the % sign indicate that you are dealing with?

	- `group`

- This Alias lets the user assign a name, like "ADMINS" to a group of people 

	- `user`

- Which Alias allows you to create a set of commands that you can then assign to a User Alias?

	- `Command`

- Yey/Ney - emacs has a shell escape

	- `yey`

- What is the minimum recommended password length set by NIST?

	- `8`

- When using the pwhistory module, which file will contain the previous passwords for the user?

	- `opasswd`

- What principle states that every user only has enough access to do their daily duties and tasks

	- `Principle of least privilege`

- No questions

	  no answer needed

- No questions

	  no answer needed

- No questions

	  no answer needed

-  This type of Firewall typically has two NIC cards

	- `network-based`

- This type of Firewall is typically installed on a host computer and rules apply to that specific host only

	- `host-based`

- Web Application Firewalls help add an extra layer of security to your web servers.  Where should these be installed?

	- `Demilitarized zone`

- iptables is not the name of the Linux Firewall.  What is the framework that iptables allows us to interact with?

	- `netfilter`

- This 3 letter acronym is a set of rules that defines what the Firewall should allow and what it should deny

	- `ACL`

- Which iptables option allows us to keep track of the connection state?

	- `--ctstate`

- Which iptable Chain is responsible for packets on the local network that are being carried onwards?

	- `FORWARD`

- Which table mashes up the packets as they go through the Firewall?

	- `mangle`

- What is the last rule that should be added to an access control list?

	- `Implicit Deny`

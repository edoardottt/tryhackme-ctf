# Day 2 - The Elf Strikes Back!

- What string of text needs added to the URL to get access to the upload page?

	- `?id=YOUR-ID-HERE`

- What type of file is accepted by the site?

	- Open the browser and check the page source code. You will find this string: `<input type=file id="chooseFile" accept=".jpeg,.jpg,.png">`
	- `image`

- Bypass the filter and upload a reverse shell.
In which directory are the uploaded files stored?

	- Change the ip in the file reverse.jpeg.php with your ip (in the vpn...so tun0) and upload that file.

	- `/uploads/`

- Activate your reverse shell and catch it in a netcat listener!

	- `nc -lvnp 1234`

	- Go to `http://<TARGET_IP>/uploads/` and click on reverse.jpeg.php

	- You should see a shell.

- What is the flag in /var/www/flag.txt?

	- `cat /var/www/flag.txt`

	- `THM{**********************************}`

## see you ...

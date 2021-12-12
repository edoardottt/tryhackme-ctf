Day12 - Sharing Without Caring

- Scan the target server with the IP 10.10.112.197. Remember that MS Windows hosts block pings by default, so we need to add -Pn, for example, nmap -Pn 10.10.112.197 for the scan to work correctly. How many TCP ports are open?

	- `*`

- In the scan results you received earlier, you should be able to spot NFS or mountd, depending on whether you used the -sV option with Nmap or not. Which port is detected by Nmap as NFS or using the mountd service?

	- `****`

- How many shares did you find?

	- `*`

- How many shares show “everyone”?

	- `*`

- What is the title of file 2680-0.txt?

	- `***********`

- It seems that Grinch Enterprises has forgotten their SSH keys on our system. One of the shares contains a private key used for SSH authentication (id_rsa). What is the name of the share?

	- `************`

- We can calculate the MD5 sum of a file using md5sum FILENAME. What is the MD5 sum of id_rsa?

	- `*******************************`
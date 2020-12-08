# What's unders the Christmas Tree?


- When was Snort created?

	- A Google search is enough (as always...).
	- `1998`

- Using Nmap on <TARGET_IP>, what are the port numbers of the three services running?  (Please provide your answer in ascending order/lowest -> highest, separated by a comma)

	- `nmap <TARGET_IP>`
	- `80,2222,3389`

- Run a scan and provide the -Pn flag to ignore ICMP being used to determine if the host is up

	no answer needed
	
	- `nmap -Pn <TARGET_IP>`

- Experiment with different scan settings such as -A and -sV whilst comparing the outputs given.

	no answer needed

	- `nmap -A <TARGET_IP>`
	- `nmap -sV <TARGET_IP>`

- Use Nmap to determine the name of the Linux distribution that is running, what is reported as the most likely distribution to be running?

	- `nmap -Pn -sV <TARGET_IP>`
	- `Ubuntu`

- Use Nmap's Network Scripting Engine (NSE) to retrieve the "HTTP-TITLE" of the webserver. Based on the value returned, what do we think this website might be used for?

	- `nmap --script=http-title <TARGET_IP>`
	- `blog`

- Now use different scripts against the remaining services to discover any further information about them

	no answer needed

	- `nmap --script=vuln <TARGET_IP>`
	- `nmap --script=ssh-auth-methods -p 2222 <TARGET_IP>`




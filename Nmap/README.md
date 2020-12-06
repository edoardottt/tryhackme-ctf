# Nmap

- Deploy the attached VM

	  no answer needed

- What networking constructs are used to direct traffic to the right application on a server?

	- `ports`

- How many of these are available on any network-enabled computer?

	- `65535`

- [Research] How many of these are considered "well-known"? (These are the "standard" numbers mentioned in the task)

	- `1024`

- What is the first switch listed in the help menu for a 'Syn Scan' (more on this later!)?

	- `-sS`

- Which switch would you use for a "UDP scan"?

	- `-sU`

- If you wanted to detect which operating system the target is running on, which switch would you use?

	- `-O`

- Nmap provides a switch to detect the version of the services running on the target. What is this switch?

	- `-sV`

- The default output provided by nmap often does not provide enough information for a pentester. How would you increase the verbosity?

	- `-v`

- Verbosity level one is good, but verbosity level two is better! How would you set the verbosity level to two?
(Note: it's highly advisable to always use at least this option)

	- `-vv`

- We should always save the output of our scans -- this means that we only need to run the scan once (reducing network traffic and thus chance of detection), and gives us a reference to use when writing reports for clients.

What switch would you use to save the nmap results in three major formats?

	- `-oA`

- What switch would you use to save the nmap results in a "normal" format?

	- `-oN`

- A very useful output format: how would you save results in a "grepable" format?

	- `-oG`

- Sometimes the results we're getting just aren't enough. If we don't care about how loud we are, we can enable "aggressive" mode. This is a shorthand switch that activates service detection, operating system detection, a traceroute and common script scanning.

How would you activate this setting?

	- `-A`

- Nmap offers five levels of "timing" template. These are essentially used to increase the speed your scan runs at. Be careful though: higher speeds are noisier, and can incur errors!

How would you set the timing template to level 5?

	- `-t5`

- We can also choose which port(s) to scan.

How would you tell nmap to only scan port 80?

	- `-p 80`

- How would you tell nmap to scan ports 1000-1500?

	- `-p 1000-1500`

- A very useful option that should not be ignored:

How would you tell nmap to scan all ports?

	- `-p-`

- How would you activate a script from the nmap scripting library (lots more on this later!)?

	- `--script`

- How would you activate all of the scripts in the "vuln" category?

	- `--script=vuln`

- Read the Scan Types Introduction.

	no answer needed

- Which RFC defines the appropriate behaviour for the TCP protocol?

	- `RFC 793`

- If a port is closed, which flag should the server send back to indicate this?

	- `rst`

- There are two other names for a SYN scan, what are they?

	- `Half-open,stealth`

- Can Nmap use a SYN scan without Sudo permissions (Y/N)?

	- `N`

- If a UDP port doesn't respond to an Nmap scan, what will it be marked as?

	- `open|filtered`

- When a UDP port is closed, by convention the target should send back a "port unreachable" message. Which protocol would it use to do so?

	- `icmp`

- Which of the three shown scan types uses the URG flag?

	- `Xmas`

- Why are NULL, FIN and Xmas scans generally used?

	- `firewall evasion`

- Which common OS may respond to a NULL, FIN or Xmas scan with a RST for every port?

	- `Microsoft Windows`

- How would you perform a ping sweep on the 172.16.x.x network (Netmask: 255.255.0.0) using Nmap? (CIDR notation)

	- `nmap -sn 172.16.0.0/16`

- What language are NSE scripts written in?

	- `Lua`

- Which category of scripts would be a very bad idea to run in a production environment?

	- `intrusive`

- What optional argument can the ftp-anon.nse script take?

	- `maxlist`

- Search for "smb" scripts in the /usr/share/nmap/scripts/ directory using either of the demonstrated methods.
What is the filename of the script which determines the underlying OS of the SMB server?

	- `ls -lah | grep smb`
	- `smb-os-discovery.nse`

- Read through this script. What does it depend on?

	- `cat smb-os-discovery.nse`, see the line `dependencies = {"smb-brute"}`
	- `smb-brute`

- Which simple (and frequently relied upon) protocol is often blocked, requiring the use of the -Pn switch?

	- `icmp`

- [Research] Which Nmap switch allows you to append an arbitrary length of random data to the end of packets?

	- `--data-length`

- Does the target (<TARGET_IP>) respond to ICMP (ping) requests (Y/N)?

	- `N`

- Perform an Xmas scan on the first 999 ports of the target -- how many ports are shown to be open or filtered?

	- `sudo nmap -sX -vv -Pn -p -999 <TARGET_IP>`
	- `999`

- There is a reason given for this -- what is it?
Note: The answer will be in your scan results. Think carefully about which switches to use -- and read the hint before asking for help!

	- `no responses`

- Perform a TCP SYN scan on the first 10000 ports of the target -- how many ports are shown to be open?

	- `sudo nmap -sS -Pn -vv -p -10000 <TARGET_IP>`
	- `5`

- Open Wireshark and perform a TCP Connect scan against port 80 on the target, monitoring the results. Make sure you understand what's going on.

	  no answer needed

- Deploy the ftp-anon script against the box. Can Nmap login successfully to the FTP server on port 21? (Y/N)

	- `Y`

- Read the conclusion.

	  no answer needed




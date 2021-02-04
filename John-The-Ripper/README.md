# John The Ripper

- Read and understand the basic concepts of hashing and hash cracking

	  no answer needed

- What is the most popular extended version of John the Ripper?

	- `jumbo john`

- What website was the rockyou.txt wordlist created from a breach on?

	- `rockyou.com`

- What type of hash is hash1.txt?

	- `hash-identifier`
	- Paste that hash.
	- `MD5`

- What is the cracked value of hash1.txt?

	- `john --format=raw-MD5 --wordlist=/usr/share/wordlists/rockyou.txt hash1.txt`
	- `*******`

- What type of hash is hash2.txt?

	- `hash-identifier`
	- Paste that hash.
	- `sha1`

- What is the cracked value of hash2.txt

	- `john --format=raw-SHA1 --wordlist=/usr/share/wordlists/rockyou.txt hash2.txt`
	- `*********`

- What type of hash is hash3.txt?

	- `hash-identifier`
	- Paste that hash
	- `sha256`

- What is the cracked value of hash3.txt

	- `john --format=raw-SHA256 --wordlist=/usr/share/wordlists/rockyou.txt hash3.txt`
	- `***********`

- What type of hash is hash4.txt?

	- `hash-identifier`
	- Paste that hash.
	- `whirlpool`

- What is the cracked value of hash4.txt

	- `john --format=whirlpool --wordlist=/usr/share/wordlists/rockyou.txt hash4.txt`
	- `**********`

- What do we need to set the "format" flag to, in order to crack this?

	- `nt`

- What is the cracked value of this password?

	- `john --format=nt --wordlist=/usr/share/wordlists/rockyou.txt ntlm.txt`
	- `********`

- What is the root password?

	- Copy the first line inside a file called `passwd`.
	- Copy the second part inside a file called `shadow`.
	- `unshadow passwd shadow > password.txt`
	- `john --wordlist=/usr/share/wordlists/rockyou.txt --format=sha512crypt password.txt`
	- `****`

- What is Joker's password?

	- Insert the username `Joker` before the hash and then insert `:` between the two.
	- `john --single --format=raw-MD5 hash7.txt`
	- `*****`

- What do custom rules allow us to exploit?

	- `Password complexity predictability`

- What rule would we use to add all capital letters to the end of the word?

	- `Az"[A-Z]"`

- What flag would we use to call a custom rule called "THMRules"

	- `--rule=THMRules`

- What is the password for the secure.zip file?

	- `zip2john secure.zip > zip.zip`
	- `john --wordlist=/usr/share/wordlists/rockyou.txt zip.zip`
	- `*******`

- What is the contents of the flag inside the zip file?

	- `unzip secure.zip` and enter password.
	- `cat zippy/flag.txt`
	- `**********************`

- What is the password for the secure.rar file?

	- `rar2john secure.rar > rar.rar`
	- `john --wordlist=/usr/share/wordlists/rockyou.txt rar.rar`
	- `********`

- What is the contents of the flag inside the zip file?

	- `unrar x secure.rar` and enter the pwd.
	- `*************************`

- What is the SSH private key password?

	- `python2 /usr/share/john/ssh2john.py idrsa.id_rsa > id.id`
	- `john --wordlist=/usr/share/wordlists/rockyou.txt id.id`
	- `*****`

- Update me..

	  no answer needed




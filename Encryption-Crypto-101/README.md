# Encryption - Crypto 101

- I'm ready to learn about encryption

	  no answer needed

- I agree not to complain too much about how theory heavy this room is.

	  no answer needed

- Are SSH keys protected with a passphrase or a password?

	- `passphrase`

- What does SSH stand for?

	- `secure shell`

- How do webservers prove their identity?

	- `certificate`

- What is the main set of standards you need to comply with if you store or process payment card details?

	- `PCI-DSS`

- What's 30 % 5?

	- `0`

- What's 25 % 7

	- `4`

- What's 118613842 % 9091

	- `python3`
	- `118613842 % 9091`
	- `****`

- Should you trust DES? Yea/Nay

	- `Nay`

- What was the result of the attempt to make DES more secure so that it could be used for longer?

	- Google it!

- Is it ok to share your public key? Yea/Nay

	- `Yea`

- p = 4391, q = 6659. What is n?

	- `python3`
	- `4391 * 6659`
	- `********`

- I understand enough about RSA to move on, and I know where to look to learn more if I want to.

	  no answer needed

-  I understand how keys can be established using Public Key (asymmetric) cryptography. 

	  no answer needed

- What company is TryHackMe's certificate issued to?

	- In your browser click on the lock icon near to the URL of tryhackme.
	- Look at the certificate.
	- `**********`

- I recommend giving this a go yourself. Deploy a VM, like Learn Linux and try to add an SSH key and log in with the private key.

	  no answer needed

- Download the SSH Private Key attached to this room.

	  no answer needed

- What algorithm does the key use?

	- `rsa`

- Crack the password with John The Ripper and rockyou, what's the passphrase for the key?

	- `python2 /usr/share/john/ssh2john.py  idrsa.id_rsa > id_rsa.hash`
	- `john --wordlist=/usr/share/wordlists/rockyou.txt id_rsa.hash`
	- `*********`

- I understand how Diffie Hellman Key Exchange works at a basic level

	  no answer needed

- Time to try some GPG. Download the archive attached and extract it somewhere sensible.

	  no answer needed

- You have the private key, and a file encrypted with the public key. Decrypt the file. What's the secret word?

	- `gpg --import tryhackme.key`
	- `gpg -d message.gpg`
	- `*********`

- I understand that quantum computers affect the future of encryption. I know where to look if I want to learn more.

	  no answer needed






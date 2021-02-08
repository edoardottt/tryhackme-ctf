# Hashing - Crypto 101

- Is base64 encryption or encoding?

	- `encoding`

- What is the output size in bytes of the MD5 hash function?

	- `16`

- Can you avoid hash collisions? (Yea/Nay)

	- `Nay`

- If you have an 8 bit hash output, how many possible hashes are there?

	- `256`

- Crack the hash "d0199f51d2728db6011945145a1b607a" using the rainbow table manually.

	- `basketball`

- Crack the hash "5b31f93c09ad1d065c0491b764d04933" using online tools

	- Just google it

- Should you encrypt passwords? Yea/Nay

	- `Nay`

- How many rounds does sha512crypt ($6$) use by default?

	- `5000`

- What's the hashcat example hash (from the website) for Citrix Netscaler hashes?

	- [here](https://hashcat.net/wiki/doku.php?id=example_hashes)

- How long is a Windows NTLM hash, in characters?

	- `32`

- Crack this hash: $2a$06$7yoU3Ng8dHTXphAg913cyO6Bjs3K5lBnwq5FJyA6d01pMSrddr1ZG

	- Copy this hash inside a file called `hash`
	- `hashcat -m 3200 hash /usr/share/wordlists/rockyou.txt`
	- `***********`

- Crack this hash: 9eb7ee7f551d2f0ac684981bd1f1e2fa4a37590199636753efe614d4db30e8e1

	- `hash-identifier` and paste the hash
	- `echo "9eb7ee7f551d2f0ac684981bd1f1e2fa4a37590199636753efe614d4db30e8e1" > hash`
	- `john --format=raw-sha256 hash -w /usr/share/wordlists/rockyou.txt`
	- `************`

- Crack this hash: $6$GQXVvW4EuM$ehD6jWiMsfNorxy5SINsgdlxmAEl3.yif0/c3NqzGLa0P.S7KRDYjycw5bnYkF5ZtB8wQy8KnskuWQS3Yr1wQ0

	- Just google it
	- `********`

- Bored of this yet? Crack this hash: b6b0d451bbf6fed658659a9e7e5598fe

	- Just google it
	- `*********`

- What's the SHA1 sum for the amd64 Kali 2019.4 ISO? http://old.kali.org/kali-images/kali-2019.4/

	- http://old.kali.org/kali-images/kali-2019.4/SHA1SUMS
	- `**************************`

- What's the hashcat mode number for HMAC-SHA512 (key = $pass)?

	- `hashcat --help | grep HMAC-SHA512`
	- `****`



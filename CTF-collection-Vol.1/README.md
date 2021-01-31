# CTF collection Vol.1

- High five!

	  no answer needed

- Feed me the flag!

	- `echo "VEhNe2p1NTdfZDNjMGQzXzdoM19iNDUzfQ==" | base64 -d`
	- `THM{********************}`

- I'm hungry, I need the flag.

	- `exiftool Findme.jpg`
	- `THM{************}`

- It is sad. Feed me the flag.

	- `steghide info Extinction.jpg` and then `y`
	- `steghide extract -sf Extinction.jpg` and then enter (without passphrase)
	- `cat Final_messge.txt`
	- `THM{********************************}`

- Did you find the flag?

	- Highlight the text or check the page source code.
	- `THM{**********}`

- More flag please!

	- Download the image and check the QR code.
	- `THM{*****************}`

- Found the flag?

	- `strings hello.hello | grep THM`
	- `THM{******************}`

- Oh, Oh, Did you get it?

	- Visit [CyberChef](https://gchq.github.io/CyberChef)
	- Recipe from Base58
	- `THM{*********************}`

- What did you get?

	- Caesar Cipher (19)
	- `THM{***************}`

- I'm hungry now... I need the flag

	- Check the HTML source code
	- `THM{***********************}`

- What is the content?

	- `xxd --plain spoil.png > hex.txt`
	- Replace the first 8 characters with `89504E47`
	- Go to Cyberchef and the recipe is `From Hex` and then `Render Image`.
	- `THM{**********}`

- Did you found the hidden flag?

	- Just search `Tryhackme reddit`
	- `THM{********************************}`

- Can you decode it?

	- Search on Google for BinaryFuck Interpreter
	- `THM{**********}`

- Did you crack it? Feed me now!

	- [XOR Calculator](http://xor.pw/#) and output as ASCII.
	- `THM{************}`

- Flag! Flag! Flag!

	- `binwalk hell.jpg -e`
	- `cd _hell.jpg.extracted`
	- `cat hello_there.txt`
	- `THM{****************}`

- What does the flag said?

	- `wget http://www.caesum.com/handbook/Stegsolve.jar -O stegsolve.jar
chmod +x stegsolve.jar`
	- `./stegsolve.jar`
	- Open the dark.png file and try to see the flag with the arrows.
	- `THM{**********************}`

- What does the bot said?

	- Follow the link on the QR code and play the track.
	- `THM{**********}`

- Did you found my past?

	- Use wayback (https://web.archive.org/web/20200102131252/https://www.embeddedhacker.com/)
	- Load the snapshot on Jan 2, 2020.
	- Search for string `THM{` on the page.
	- `THM{******************}`

- The deciphered text

	- Input `MYKAHODTQ{RVG_YVGGK_FAL_WXF}` in [CyberChef](https://gchq.github.io/CyberChef/) with recipe Vigenere Decode and key=TRYHACKME.
	- Output is `THMTHMTHM{*****************}`
	- Change the key to `THMTHMTHM`
	- `TRYHACKME{*****************}`

- What is the flag?

	- `python3`
	- `n = 581695969015253365094191591547859387620042736036246486373595515576333693`
	- `h = hex(n)[2:]`
	- `bytearray.fromhex(h).decode()`
	- `THM{***********************}`

- Did you captured my neighbor's flag?

	- Open the file with Wireshark.
	- `THM{****************}`





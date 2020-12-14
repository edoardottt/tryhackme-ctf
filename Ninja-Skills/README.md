# Ninja Skills

- Which of the above files are owned by the best-group group(enter the answer separated by spaces in alphabetical order)

	- This is our base command: `find / -type f \( -name 8V2L -o -name bny0 -o -name c4ZX -o -name D8B3 -o -name FHl1 -o -name oiMO -o -name PFbD -o -name rmfX -o -name SRSq -o -name uqyw -o -name v2Vb -o -name X1Uy \) 2>>/dev/null`
	- `find / -type f \( -name 8V2L -o -name bny0 -o -name c4ZX -o -name D8B3 -o -name FHl1 -o -name oiMO -o -name PFbD -o -name rmfX -o -name SRSq -o -name uqyw -o -name v2Vb -o -name X1Uy \) 2>>/dev/null | xargs ls -alh`
	- `D8B3 v2Vb`

- Which of these files contain an IP address?

	- `find / -type f \( -name 8V2L -o -name bny0 -o -name c4ZX -o -name D8B3 -o -name FHl1 -o -name oiMO -o -name PFbD -o -name rmfX -o -name SRSq -o -name uqyw -o -name v2Vb -o -name X1Uy \) 2>>/dev/null | xargs grep -Eo "([0-9]{1,3}[\.]){3}[0-9]{1,3}"`
	- `oiMO`

- Which file has the SHA1 hash of 9d54da7584015647ba052173b84d45e8007eba94

	- `find / -type f \( -name 8V2L -o -name bny0 -o -name c4ZX -o -name D8B3 -o -name FHl1 -o -name oiMO -o -name PFbD -o -name rmfX -o -name SRSq -o -name uqyw -o -name v2Vb -o -name X1Uy \) 2>>/dev/null | xargs sha1sum`
	- `c4ZX`

- Which file contains 230 lines?

	- The solution is `bny0`, but this file is not shown on the ls output. I'm doing something wrong?

- Which file's owner has an ID of 502?

	- `find / -type f \( -name 8V2L -o -name bny0 -o -name c4ZX -o -name D8B3 -o -name FHl1 -o -name oiMO -o -name PFbD -o -name rmfX -o -name SRSq -o -name uqyw -o -name v2Vb -o -name X1Uy \) 2>>/dev/null | xargs ls -ln`
	- `X1Uy`

- Which file is executable by everyone?

	- `find / -type f \( -name 8V2L -o -name bny0 -o -name c4ZX -o -name D8B3 -o -name FHl1 -o -name oiMO -o -name PFbD -o -name rmfX -o -name SRSq -o -name uqyw -o -name v2Vb -o -name X1Uy \) 2>>/dev/null | xargs ls -la`
	- `8V2L`







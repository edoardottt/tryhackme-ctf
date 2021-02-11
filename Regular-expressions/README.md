# Regular expressions

- Read the above.

	  no answer needed

- Match all of the following characters: c, o, g

	- `[cog]`

- Match all of the following words: cat, fat, hat

	- `[cfh]at`

- Match all of the following words: Cat, cat, Hat, hat

	- `[CcHh]at`

- Match all of the following filenames: File1, File2, file3, file4, file5, File7, file9

	- `[Ff]ile[1-9]`

- Match all of the filenames of question 4, except "File7" (use the hat symbol)

	- `[Ff]ile[^7]`

- Match all of the following words: Cat, fat, hat, rat

	- `.at`

- Match all of the following words: Cat, cats

	- `[Cc]ats?`

- Match the following domain name: cat.xyz

	- `cat\.xyz`

- Match all of the following domain names: cat.xyz, cats.xyz, hats.xyz

	- `[ch]ats?\.xyz`

- Match every 4-letter string that doesn't end in any letter from n to z

	- `...[^n-z]`

- Match bat, bats, hat, hats, but not rat or rats (use the hat symbol)

	- `[^r]ats?`

- Match the following word: catssss

	- `cats{4}`

- Match all of the following words (use the * sign): Cat, cats, catsss

	- `[cC]ats*`

- Match all of the following sentences (use the + sign): regex go br, regex go brrrrrr

	- `regex go br+`

- Match all of the following filenames: ab0001, bb0000, abc1000, cba0110, c0000 (don't use a metacharacter)

	- `[abc]{1,3}[01]{4}`

- Match all of the following filenames: File01, File2, file12, File20, File99

	- `[fF]ile\d{1,2}`

- Match all of the following folder names: kali tools, kali     tools

	- `kali\s+tools`

- Match all of the following filenames: notes~, stuff@, gtfob#, lmaoo!

	- `\w{5}\W`

- Match the string in quotes (use the * sign and the \s, \S metacharacters): "2f0h@f0j0%!     a)K!F49h!FFOK"

	- `\S*\s*\S*`

- Match every 9-character string (with letters, numbers, and symbols) that doesn't end in a "!" sign

	- `\S{8}[^!]`

- Match all of these filenames (use the + symbol): `.bash_rc`, `.unnecessarily_long_filename`, and note1

	- `\.?\w+`

- Match every string that starts with "Password:" followed by any 10 characters excluding "0"

	- `Password:[^0]{10}`

- Match "username: " in the beginning of a line (note the space!)

	- `^username:\s`

- Match every line that doesn't start with a digit (use a metacharacter)

	- `^\D`

- Match this string at the end of a line: EOF$

	- `EOF\$$`

- Match all of the following sentences:

	- `I use nano`
    	- `I use vim`
	- `I use (nano|vim)`

- Match all lines that start with $, followed by any single digit,
followed by $, followed by one or more non-whitespace characters

	- `\$\d\$\S+`

- Match every possible IPv4 IP address (use metacharacters and groups)

	- `(\d{1,3}\.){3}\d{1,3}`

- Match all of these emails while also adding the username and the domain name (not the TLD) in separate groups (use \w): `hello@tryhackme.com`, `username@domain.com`, `dummy_email@xyz.com`

	- `(\w+)@(\w+)\.com`

- Thanks!

	  no answer needed

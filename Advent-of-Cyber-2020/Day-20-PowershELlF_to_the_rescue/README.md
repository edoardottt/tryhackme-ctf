# PowershELlF to the rescue

- Search for the first hidden elf file within the Documents folder. Read the contents of this file. What does Elf 1 want?

	- `ssh -l mceager <TARGET_IP>`
	- Enter the password `r0ckStar!`
	- `powershell` and wait until you see a new terminal
	- `Set-Location ./Documents/`
	- `Get-ChildItem -File`
	- `Get-ChildItem -File -Hidden`
	- Notice there is a hidden file `e1fone.txt` and a visible `elfone.txt`.
	- `Get-Content elfone.txt`
	- `Get-Content e1fone.txt`
	- `2 front teeth`

- Search on the desktop for a hidden folder that contains the file for Elf 2. Read the contents of this file. What is the name of that movie that Elf 2 wants? 
	- `cd ..`
	- `Set-Location Desktop`
	- `Get-Content -File -Hidden`
	- `Set-Location .\elf2wo\`
	- `Get-Content .\e70smsW10Y4k.txt`
	- `Scrooged`

- Search the Windows directory for a hidden folder that contains files for Elf 3. What is the name of the hidden folder? (This command will take a while)

	- `Set-Location C:\Windows`
	- `Get-ChildItem -Filter "*3*" -Recurse -Directory -Hidden -ErrorAction SilentlyContinue`
	- `Set-Location .\System32\3lfthr3e\`
	- `3lfthr3e`

- How many words does the first file contain?

	- `Get-Content 1.txt | Measure-Object -Word`
	- `9999`

- What 2 words are at index 551 and 6991 in the first file?

	- `(Get-Content .\1.txt)[551]`
	- `(Get-Content .\1.txt)[6991]` or `Get-Content 1.txt | Select-Object -Index 551,6991`
	- `Red Ryder`

- This is only half the answer. Search in the 2nd file for the phrase from the previous question to get the full answer. What does Elf 3 want? (use spaces when submitting the answer)

	- `Get-Content 2.txt | Select-String -Pattern "redryder"`
	- `Red Ryder bb gun`




### see you ...

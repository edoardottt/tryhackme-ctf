# Day 4 - Santa's watching

Our malicious, despicable, vile, cruel, contemptuous, evil hacker has defaced Elf's forums and completely removed the login page! However, we may still have access to the API. The sysadmin also told us that the API creates logs using dates with a format of **YYYYMMDD**.

Recommended list: [big.txt](https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/big.txt)

- Deploy your AttackBox (the blue "Start AttackBox" button) and the tasks machine (green button on this task) if you haven't already. Once both have deployed, open FireFox on the AttackBox and copy/paste the machines IP (10.10.135.56) into the browser search bar.

	  no answer needed
	
	If you navigate with your browser to the <TARGET_IP> you should see this page:


	![site](https://github.com/edoardottt/tryhackme-ctf/blob/main/Advent-of-Cyber-2020/Day-04-Santa's_watching/site.png)
	
- Given the URL "http://shibes.xyz/api.php", what would the entire wfuzz command look like to query the "breed" parameter using the wordlist "big.txt" (assume that "big.txt" is in your current directory)
**Note: For legal reasons, do not actually run this command as the site in question has not consented to being fuzzed!**

	- `wfuzz -c -z file,big.txt http://shibes.xyz/api.php?breed=FUZZ`

- Use GoBuster (against the target you deployed -- not the shibes.xyz domain) to find the API directory. What file is there?

	- `gobuster dir -u <TARGET_IP> -w big.txt`
	- You will find a directory and the a php file.

- Fuzz the date parameter on the file you found in the API directory. What is the flag displayed in the correct post?

	- Execute the python file with `python3 create_list.py`. It will create a list for you with format `YYYYMMDD`.
	- `wfuzz -c -z file,YYYYMMDD-list.txt -d "date=FUZZ" --hw 0 http://<TARGET_IP>/api/site-log.php`
	- Executing this command, it will try to fuzz the date parameter, and I've inserted the --hw parameter set to 0 because I tried few times and I saw the incorrect answers contains no words.
	- The only respone you get is from one word. Just append that word, let's say is YYYYMMDD. Go to browser and query `http://<TARGET_IP>/api/site-log.php?date=YYYYMMDD`.
	- `THM{********}`

# see you ...

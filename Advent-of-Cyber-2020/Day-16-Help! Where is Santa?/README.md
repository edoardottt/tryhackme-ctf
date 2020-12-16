# Help! Where is Santa?

Oh no! Santa 🎅 has taken off, leaving you -- the faithful elves behind! Can you help find Santa's location?

Santa has a webpage at `<TARGET_IP>/static/index.html`

- What is the port number for the web server?

	- `nmap -p -10000 <TARGET_IP>`
	- `8000`

- What is the directory for the API, without the API key?

	- Visit `http://<TARGET_IP>:8000/` and inspect code
	- `/api/`

- Where is Santa right now?
	
	- Change the `TARGET_API` in `api_fuzzer.py`
	- `python3 api_fuzzer.py`
	- `Winter Wonderland, Hyde Park, London`

- Find out the correct API key. Remember, this is an odd number between 0-100. After too many attempts, Santa's Sled will block you. 
To unblock yourself, simply terminate and re-deploy the target instance (<TARGET_IP>)

	- `57`




### see you ...

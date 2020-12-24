# Sublist3r

- You can find Sublist3r [here!](https://github.com/aboul3la/Sublist3r) We'll install this in the next task.

	  no answer needed

- First, let's change to our opt directory: `cd /opt`

	  no answer needed

- Next, let's clone the Sublist3r repository into opt: `git clone https://github.com/aboul3la/Sublist3r.git`

	  no answer needed

- Now let's move into the Sublist3r directory we've just created: `cd /opt/Sublist3r`

	  no answer needed

- Finally, let's install the requirements for running Sublist3r: `pip3 install -r requirements.txt`

	  no answer needed

- What switch can we use to set our target domain to perform recon on?

	- `-d`

- How about setting which engines we'll use for searching? (i.e. google, bing, etc)

	- `-e`

- Saving our output is important both so we don't have to run recon again but also so we can return to our returns and review them at a later time. What switch do we use to define an output file?

	- `-o`

- Sublist3r can sometimes take some time to run but we can speed through up the use of threads. Which switch allows us to set the number of threads?

	- `-t`

- Last but not least, we can also bruteforce the domains for our target. This isn't always the most useful, however, it can sometimes find a key domain that we might have missed. What switch allows us to enable brute forcing?

	- `-b`

- Let's run sublist3r now against `nbc.com`, a fairly large American news company. Run this now with the command: `python3 sublist3r.py -d nbc.com -o sub-output-nbc.txt`

	  no answer needed

- Once that completes open up your results and take a look through them. Email domains are almost always interesting and typically have an email portal (usually Outlook) located at them. Which subdomain is likely the email portal?

	- `mail`

- Administrative control panels should never be exposed to the internet! Which subdomain is exposed that shouldn't be?

	- `admin`

- Company blogs can sometimes reveal information about internal activities, which subdomain has the company blog at it?

	- `blog`

- Development sites are often vulnerable to information disclosure or full-blown attacks. Two developer sites are exposed, which one is associated directly with web development?

	- `dev-www`

- Customer and employee help desk portals can often reveal internal nomenclature and other potentially sensitive information, which dns record might be a helpdesk portal?

	- `help`

- Single sign-on is a feature commonly used in corporate domains, which dns record is directly associated with this feature? Include both parts of this subdomain separated by a period.

	- `ssologin.stg`

- One last one for fun. NBC produced a popular sitcom about typical office work environment, which dns record might be associated with this show?

	- `office-words`


 

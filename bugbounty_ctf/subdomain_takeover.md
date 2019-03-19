# Step By Step
1. List all the Subdomains from the scope --Tools


**** 


## Notable tools

There is a wide variety of tools out there for subdomain takeovers. This section contains some notable ones that have not been mentioned so far.

#### Altdns

In order to recursively brute force subdomains, take a look at Shubham Shah's Altdns script. Running your custom word list after fingerprinting a target through Altdns can be extremely rewarding. I like to use Altdns to generate word lists to then run through other tools.

#### Commonspeak

Yet another tool by Shubham, Commonspeak is a tool to generate word lists using Google's BigQuery. The goal is to generate word lists that reflect current trends, which is particularly important in a day and age where technology is rapidly evolving. It is worth reading https://pentester.io/commonspeak-bigquery-wordlists/ if you want to get a better understanding of how this tool works and where it gathers keywords from.

#### SubFinder

A tool that combines both scraping and brute forcing beautifully is SubFinder. I have found myself using SubFinder more than Sublist3r now as my general-purpose subdomain discovery tool. In order to get better results, make sure to include API keys for the various services that SubFinder scrapes to find subdomains.

#### Massdns

Massdns is a blazing fast subdomain enumeration tool. What would take a quarter of an hour with some tools, Massdns can complete in a minute. Please note, if you are planning on running Massdns, make sure you provide it with a list of valid resolvers. Take a look at https://public-dns.info/nameservers.txt, play around with the resolvers, and see which ones return the best results. If you do not update your list of resolvers, you will end up with a lot of false-positives.

```
$ ./scripts/subbrute.py lists/names.txt example.com | ./bin/massdns -r lists/resolvers.txt -t A -o S -w results.txt

```


#### SUBLIST3R
```
$ git clone https://github.com/aboul3la/Sublist3r.git
$ cd Sublist3r
$ sudo pip install -r requirements.txt
```
#### Aliases 

```
alias sublist3r='python /path/to/Sublist3r/sublist3r.py -d '

alias sublist3r-one=". <(cat domains | awk '{print \"sublist3r \"$1 \" -o \" $1 \".txt\"}')"
```

#### Dirsearch

```
$ git clone https://github.com/maurosoria/dirsearch.git
$ cd dirsearch/db
$ wget https://gist.githubusercontent.com/EdOverflow/c4d6d8c43b315546892aa5dab67fdd6c/raw/7dc210b17d7742b46de340b824a0caa0f25cf3cc/open_redirect_wordlist.txt

```

##### 💬 Aliases

```
alias dirsearch='python3 /path/to/dirsearch/dirsearch.py -u '

alias dirsearch-one=". <(cat domains | awk '{print \"dirsearch \"\$1 \" -e *\"}')"

alias openredirect=". <(cat domains | awk '{print \"dirsearch \"\$1 \" -w /path/to/dirsearch/db/open_redirect_wordlist.txt -e *\"}')"

```

####  webscreenshot 

```
$ git clone https://github.com/maaaaz/webscreenshot.git
```

*****

# So how do you exploit this vulnerability?

1.You basically start with brute forcing for subdomains to find one of those error pages.
2.When you find one you check for the subdomain’s CNAME and register it as yours with the service provider and that’s it now you have taken over the subdomain.

###  Steps to take when approaching a target 


1) Verify target’s scope (*.example.com);

2) Run Sublist3r on example.com and output all findings to a file called output:

```
$ sublist3r example.com -o output
...
$ cat output
foo.example.com
bar.example.com
admin.example.com
dev.example.com
www.example.com
git.example.com

```
3) Check which domains resolve:
```
$ while read domain; do if host "$domain" > /dev/null; then echo $domain; fi; done < output >> domains
```
4) Run webscreenshot on the domains file:
```
$ python webscreenshot.py -i domains output example
...
$ eog example
```
Tip: Look for 404 pages, login panels, directory listings and old-looking pages when reviewing the screenshots.

5) Run dirsearch on the domains file:
```
$ dirsearch-one
```

6) Check for open redirects using dirsearch on the domains file:
```
$ openredirect
```

## Getting Start

When brute forcing subdomains, the hacker iterates through a wordlist and based on the response can determine whether or not the host is valid. Please note, that it is very important to always check if the target has a wildcard enabled, otherwise you will end up with a lot of false-positives. Wildcards simply mean that all subdomains will return a response which skews your results. You can easily detect wildcards by requesting a seemingly random hostname that the target most probably has not set up.

``` $ host randomifje8z193hf8jafvh7g4q79gh274.example.com ```

host - host is a simple utility for performing DNS lookups. It is normally used to convert names to IP addresses and vice versa.

dig - Dig stands for (Domain Information Groper) is a network administration command-line tool for querying Domain Name System (DNS) name servers. It is useful for verifying and troubleshooting DNS problems and also to perform DNS lookups and displays the answers that are returned from the name server that were queried.

For the best results while brute forcing subdomains, I suggest creating your own personal wordlist with terms that you have come across in the past or that are commonly linked to services that you are interested in. For example, I often find myself looking for hosts containing the keywords "jira" and "git" because I sometimes find vulnerable Atlassian Jira and GIT instances.

If you are planning on brute forcing subdomains, I highly recommend taking a look at Jason Haddix's word list. Jason went to all the trouble of merging lists from subdomain discovery tools into one extensive list.


[Jason Hadix Wordlist](https://gist.github.com/jhaddix/86a06c5dc309d08580a018c66354a056)
 
## Automating your workflow

When hunting for subdomain takeovers, automation is key. The top bug bounty hunters constantly monitor targets for changes and continuously have an eye on every single subdomain that they can find. For this guide, I do not believe it is necessary to focus on monitoring setups. Instead, I want to stick to simple tricks that can save you time and can be easily automated.

The first task that I love automating is filtering out live subdomains from a list of hosts. When scraping for subdomains, some results will be outdated and no longer reachable; therefore, we need to determine which hosts are live. Please keep in mind, as we will see later, just because a host does not resolve, does not necessarily mean it cannot be hijacked. This task can easily be accomplished by using the.

```
while read subdomain; do
if host "$subdomain" > /dev/null; then
# If host is live, print it into
# a file called "live.txt".
echo "$subdomain" >> live.txt
fi
done < subdomain-list.txt
```
![Alt text](./scripts/sd1.png)

For taking screenshots, my go-to tool is currently EyeWitness. This tool generates an HTML document containing all the screenshots, response bodies, and headers from your list of hosts.

```$ ./EyeWitness -f live.txt -d out --headless```

EyeWitness can be a little too heavy for some cases and you might only want to store the page's contents via a simple GET request to the top-level directory of the subdomain. For cases like these, I use Tom Hudson's meg. meg sends requests concurrently and then store the output into plain-text files. This makes it a very efficient and light-weight solution for sieving through your subdomains and allows you to grep for keywords.

```$ meg -d 10 -c 200 / live.txt```



## Exploitation

Right, now you control a subdomain belonging to the target, what can you do next? When determining plausible attack scenarios with a misconfigured subdomain, it is crucial to understand how the subdomain interacts with the base name and the target's core service.

### Cookies

If the base name is vulnerable to session fixation and uses HTTPOnly cookies, you can set a cookie and then when the user restarts their browser, your malicious cookie will take precedence over the newly generated cookie because cookies are sorted by age.

### Cross-Origin Resource Sharing

Cross-Origin Resource Sharing (CORS), is a technology that allows a host to share contents of a page cross-origin. Applications create a scope with a set of rules that permits hosts to extract data including authenticated data. Some applications permit subdomains to make cross-origin HTTP requests with the assumption that subdomains are trusted entities. When you hijack a subdomain look for CORS headers — Burp Suite Pro's scanner usually picks them up — and see if the application whitelists subdomains. This could allow you to steal data from an authenticated user on the main application.

### Oauth whitelisting

Similar to Cross-Origin Resource Sharing, the Oauth flow also has a whitelisting mechanic, whereby developers can specify which callback URIs should be accepted. The danger here once again is when subdomains have been whitelisted and therefore you can redirect users during the Oauth flow to your subdomain, potentially leaking their Oauth token.

### Content-Security Policies

The Content-Security Policy (CSP) is yet another list of hosts that an application trusts, but the goal here is to restrict which hosts can execute client-side code in the context of the application. This header is particularly useful if one wants to minimise the impact of cross-site scripting. If your subdomain is included in the whitelist, you can use your subdomain to bypass the policy and execute malicious client-side code on the application.

```
$ curl -sI https://hackerone.com | grep -i "content-security-policy"
content-security-policy: default-src 'none'; base-uri 'self'; block-all-mixed-content; child-src www.youtube-nocookie.co
m; connect-src 'self' www.google-analytics.com errors.hackerone.net; font-src 'self'; form-action 'self'; frame-ancestor
s 'none'; img-src 'self' data: cover-photos.hackerone-user-content.com hackathon-photos.hackerone-user-content.com profi
le-photos.hackerone-user-content.com hackerone-us-west-2-production-attachments.s3-us-west-2.amazonaws.com; media-src 's
elf' hackerone-us-west-2-production-attachments.s3-us-west-2.amazonaws.com; script-src 'self' www.google-analytics.com;
style-src 'self' 'unsafe-inline'; report-uri https://errors.hackerone.net/api/30/csp-report/?sentry_key=61c1e2f50d21487c
97a071737701f598

```

### Reporting subdomain takeovers

Before you even attempt to report a subdomain takeover, make sure that you are in fact able to serve content on the subdomain. However, whatever you do, do not publish anything on the index page, even if it is a harmless picture of a frog as demonstrated earlier. It is best practice to serve an HTML file on a hidden path containing a secret message in an HTML comment. That should be enough to demonstrate the issue when initially contacting the programme about your finding. Only once the team has given you permission, should you attempt to escalate the issue and actually demonstrate the overall impact of the vulnerability. In most cases though, the team should already be aware of the impact and your report should contain information concerning the exploitability of subdomain takeovers.

Take your time when writing up a report about a subdomain takeover as this type of issue can be extremely rewarding and nobody can beat you to the report since you are — hopefully — the only one that has control over the subdomain.


****

# Important Links 
[Hackerone-SubDomain - Takeover](https://www.hackerone.com/blog/Guide-Subdomain-Takeovers)


[Automating your reconnaissance workflow with meg ](https://dev.to/edoverflow/-automating-your-reconnaissance-workflow-with-meg-2koi)

[Edoverflow-blog](https://dev.to/edoverflow)


[Subdomain-Takeover-Basics](https://0xpatrik.com/subdomain-takeover-basics/)

[How To Do Your Reconnaissance Properly Before Chasing A Bug Bounty](https://medium.com/bugbountywriteup/guide-to-basic-recon-bug-bounties-recon-728c5242a115)

[10 Rules of Bug Bounty](https://hackernoon.com/10-rules-of-bug-bounty-65082473ab8c)

[BUG BOUNTY HUNTING (METHODOLOGY , TOOLKIT , TIPS & TRICKS , Blogs)](https://medium.com/bugbountywriteup/bug-bounty-hunting-methodology-toolkit-tips-tricks-blogs-ef6542301c65)


[LevelUp 0x02 — Bug Bounty Hunter Methodology v3 — Notes](https://medium.com/@nicklaus_park/levelup-0x02-bug-bounter-hunter-methodology-v3-8f5b802af2ad)

[Subdomain Takeover-Cheatsheet](https://pentester.land/cheatsheets/2018/11/14/subdomains-enumeration-cheatsheet.html)

[Hackerone-Subdomain Takeover](https://www.hackerone.com/blog/Guide-Subdomain-Takeovers)

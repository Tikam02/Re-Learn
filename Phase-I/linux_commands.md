# Basic Commands - Level Zero
### Index of Linux Commands
```
alias:   allows launching of any command or combination of commands by using a preset character or series of characters.

apropos:   displays a list of all topics in the built-in user manual that are related to the subject of a query.

bzip2:   used for compressing and decompressing files.

cat:   (short for concatenate) has three related functions with regard to text files: displaying them, combining copies of them and creating new ones.

cd:   changes directories.

clear:   removes all previous commands and output from consoles and terminal windows.

cp:   copies files and directories.

df:   reports the amount of space used and available on currently mounted filesystems.

dmesg:   reads the kernel messages.

du:   shows the sizes of directories and files.

fdformat:   performs low-level formatting of floppy disks.

file:   classifies filesystem objects.

free:   provides information about unused and used memory and swap space.

grep:   searches text.

head:   by default reads the first ten lines of text.

hostname:   shows or sets a computer's host name and domain name.

kdesu:   opens KDE su, the graphical front end for the su command.

kill:   terminates stalled processes without having to log out or reboot.

killall:   terminates all processes associated with programs whose names are provided to it as arguments.

locate:   finds files and directories.

man:   formats and displays the built-in manual pages.

mkbootdisk:   creates an emergency boot floppy.

mkdir:   creates new directories.

mkfs:   creates a filesystem on a disk or on a partition thereof.

mv:   renames and moves files and directories.

ps:   (short for process status) lists the currently running processes and their process identification numbers (PIDs).

pstree:   displays the processes on the system in the form of a tree diagram.

pwd:   (short for present working directory) displays the full path to the current directory.

reboot:   restarts a computer without having to turn the power off and back on.

rm:   deletes the specified files and directories.

rmdir:   deletes the specified empty directories.

runlevel:   reports the current and previous runlevels.

shred:   destroys files.

spell:   checks spelling.

strings:   returns each string of printable characters in files.

su:   (short for substitute user) changes a login session's owner without the owner having to first log out of that session.

tail:   by default reads the final ten lines of text.

tar:   converts a group of files into an archive.

touch:   the easiest way to create new, empty files.

tr:   translates or deletes characters.

unalias:   removes entries from the current user's list of aliases.

uname:   provides basic information about a system's software and hardware.

uptime:   shows the current time, how long the system has been running since it was booted up, how many user sessions are currently open and the load averages.

w:   shows who is logged into the system and what they are doing.

wc:   by default counts the number of lines, words and characters that are contained in text.

whatis:   provides very brief descriptions of command line programs and other topics related to Unix-like operating systems.

whereis:   locates the binary, source code and man page for any specified program.

whoami:   returns the user name of the owner of the current login session. 

chmod : To make a file executable, you can use the command “chmod +x numbers.py” in this case. You can use “chmod 755 numbers.py” to give it root permissions or “sudo chmod +x numbers.py” for root executable.

df : Use the df command to see the available disk space in each of the partitions in your system.
```
****
# Network Commands 

## host 
``` host command in Linux system is used for DNS (Domain Name System) lookup operations. In simple words, this command is used to find the IP address of a particular domain name or if you want to find out the domain name of a particular IP address the host command becomes handy. You can also find more specific details of a domain by specifying the corresponding option along with the domain name.```



#### 1. Making simple query for any site say google.com using sitename :
```
$ host google.com
google.com has address 173.194.78.139
google.com has address 173.194.78.113
google.com has address 173.194.78.100
google.com has address 173.194.78.138
google.com has address 173.194.78.102
google.com has address 173.194.78.101
google.com has IPv6 address 2a00:1450:400c:c00::64
google.com mail is handled by 30 alt2.aspmx.l.google.com.
google.com mail is handled by 40 alt3.aspmx.l.google.com.
google.com mail is handled by 10 aspmx.l.google.com.
google.com mail is handled by 50 alt4.aspmx.l.google.com.
google.com mail is handled by 20 alt1.aspmx.l.google.com.
```
#### 2. Making host query using IP address :
```

$ host 173.194.78.101
101.78.194.173.in-addr.arpa domain name pointer www-google-analytics.l.google.com.
```

#### 3. To display MX records for google.com domain
```
$ host -n -t mx google.com
google.com mail is handled by 30 alt2.aspmx.l.google.com.
google.com mail is handled by 40 alt3.aspmx.l.google.com.
google.com mail is handled by 10 aspmx.l.google.com.
google.com mail is handled by 50 alt4.aspmx.l.google.com.
google.com mail is handled by 20 alt1.aspmx.l.google.com.
```
#### 4. To find out the domain name servers
```
$ host -t ns google.com
google.com name server ns3.google.com.
google.com name server ns1.google.com.
google.com name server ns4.google.com.
google.com name server ns2.google.com.
```
#### 5. Find out the domain TXT record
```
$ host -t txt google.com
google.com descriptive text "v=spf1 include:_spf.google.com ip4:216.73.93.70/31 ip4:216.73.93.72/31 ~all"
```
#### 6. Find out the SOA record
```
$ host -t soa google.com
google.com has SOA record ns1.google.com. dns-admin.google.com. 2013120500 7200 1800 1209600 300
```
#### 7. Query Particular Name Server
```
$ host google.com ns4.google.com
Using domain server:
Name: ns4.google.com
Address: 216.239.38.10#53
Aliases: 
 
google.com has address 74.125.236.134
google.com has address 74.125.236.131
google.com has address 74.125.236.136
google.com has address 74.125.236.133
google.com has address 74.125.236.128
google.com has address 74.125.236.132
google.com has address 74.125.236.137
google.com has address 74.125.236.142
google.com has address 74.125.236.135
google.com has address 74.125.236.129
google.com has address 74.125.236.130
google.com has IPv6 address 2404:6800:4009:801::1001
google.com mail is handled by 20 alt1.aspmx.l.google.com.
google.com mail is handled by 50 alt4.aspmx.l.google.com.
google.com mail is handled by 10 aspmx.l.google.com.
google.com mail is handled by 40 alt3.aspmx.l.google.com.
google.com mail is handled by 30 alt2.aspmx.l.google.com.
```
#### 8. Display all information regarding Domain Records and Zone
```
$ host -a amazon.in
Trying "amazon.in"
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 18506
;; flags: qr rd ra; QUERY: 1, ANSWER: 12, AUTHORITY: 10, ADDITIONAL: 2
 
;; QUESTION SECTION:
;amazon.in.			IN	ANY
 
;; ANSWER SECTION:
amazon.in.		5	IN	A	87.238.81.156
amazon.in.		5	IN	A	87.238.85.156
amazon.in.		5	IN	NS	pdns6.ultradns.co.uk.
amazon.in.		5	IN	NS	ns4.p31.dynect.net.
amazon.in.		5	IN	NS	ns1.p31.dynect.net.
amazon.in.		5	IN	NS	pdns4.ultradns.org.
amazon.in.		5	IN	NS	pdns1.ultradns.net.
amazon.in.		5	IN	NS	ns2.p31.dynect.net.
amazon.in.		5	IN	NS	pdns3.ultradns.org.
amazon.in.		5	IN	NS	pdns5.ultradns.info.
amazon.in.		5	IN	NS	ns3.p31.dynect.net.
amazon.in.		5	IN	NS	pdns2.ultradns.net.
 
;; AUTHORITY SECTION:
amazon.in.		5	IN	NS	ns1.p31.dynect.net.
amazon.in.		5	IN	NS	pdns1.ultradns.net.
amazon.in.		5	IN	NS	pdns3.ultradns.org.
amazon.in.		5	IN	NS	pdns5.ultradns.info.
amazon.in.		5	IN	NS	ns4.p31.dynect.net.
amazon.in.		5	IN	NS	pdns4.ultradns.org.
amazon.in.		5	IN	NS	ns3.p31.dynect.net.
amazon.in.		5	IN	NS	pdns2.ultradns.net.
amazon.in.		5	IN	NS	pdns6.ultradns.co.uk.
amazon.in.		5	IN	NS	ns2.p31.dynect.net.
 
;; ADDITIONAL SECTION:
pdns1.ultradns.net.	5	IN	A	204.74.108.1
pdns1.ultradns.net.	5	IN	AAAA	2001:502:f3ff::1
 
Received 497 bytes from 127.0.1.1#53 in 456 ms
```
#### 9. Get TTL Information
```
$ host -v -t a google.com
Trying "google.com"
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 42913
;; flags: qr rd ra; QUERY: 1, ANSWER: 6, AUTHORITY: 4, ADDITIONAL: 4
 
;; QUESTION SECTION:
;google.com.			IN	A
 
;; ANSWER SECTION:
google.com.		5	IN	A	173.194.78.139
google.com.		5	IN	A	173.194.78.102
google.com.		5	IN	A	173.194.78.138
google.com.		5	IN	A	173.194.78.113
google.com.		5	IN	A	173.194.78.101
google.com.		5	IN	A	173.194.78.100
 
;; AUTHORITY SECTION:
google.com.		5	IN	NS	ns4.google.com.
google.com.		5	IN	NS	ns1.google.com.
google.com.		5	IN	NS	ns3.google.com.
google.com.		5	IN	NS	ns2.google.com.
 
;; ADDITIONAL SECTION:
ns3.google.com.		5	IN	A	216.239.36.10
ns2.google.com.		5	IN	A	216.239.34.10
ns4.google.com.		5	IN	A	216.239.38.10
ns1.google.com.		5	IN	A	216.239.32.10
 
Received 260 bytes from 127.0.1.1#53 in 511 ms
```
#### 10. Find Domain CNAME Record
```
$ host -t cname mail.yahoo.com
mail.yahoo.com is an alias for login.yahoo.com.
```
host domain_name: This will print the IP address details of the specified domain. 

*****
## dig
```
The command dig is a tool for querying DNS nameservers for information about host addresses, mail exchanges, nameservers, and related information. This tool can be used from any Linux (Unix) or Macintosh OS X operating system. The most typical use of dig is to simply query a single host.
```

dig will let you perform any valid DNS query, the most common of which are:

    - A (the IP address),
    - TXT (text annotations),
    - MX (mail exchanges), and
    - NS nameservers.

Use the following command to get the addresses for example.com :

``` dig example.com A +noall +answer ```

Use the following command to get a list of all the mailservers for example.com : 

 ```dig example.com MX +noall +answer```

Use the following command to get a list of authoritative DNS servers for example.com :

 ```dig example.com NS +noall +answer```

Use the following command to get a list of all the above in one set of results :

```dig example.com ANY +noall +answer ```

Use the following command to query using a specific nameserver :

```dig @ns1.mediatemple.net example.com``` 

Use the following to trace the path taken :

 ```dig example.com +trace```

#### 1. Simple dig Command Usage (Understand dig Output)

When you pass a domain name to the dig command, by default it displays the A record (the ip-address of the site that is queried) as shown below.

In this example, it displays the A record of redhat.com in the “ANSWER SECTION” of the dig command output.

```
$ dig redhat.com

; <<>> DiG 9.7.3-RedHat-9.7.3-2.el6 <<>> redhat.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 62863
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 4, ADDITIONAL: 3

;; QUESTION SECTION:
;redhat.com.                    IN      A

;; ANSWER SECTION:
redhat.com.             37      IN      A       209.132.183.81

;; AUTHORITY SECTION:
redhat.com.             73      IN      NS      ns4.redhat.com.
redhat.com.             73      IN      NS      ns3.redhat.com.
redhat.com.             73      IN      NS      ns2.redhat.com.
redhat.com.             73      IN      NS      ns1.redhat.com.

;; ADDITIONAL SECTION:
ns1.redhat.com.         73      IN      A       209.132.186.218
ns2.redhat.com.         73      IN      A       209.132.183.2
ns3.redhat.com.         73      IN      A       209.132.176.100

;; Query time: 13 msec
;; SERVER: 209.144.50.138#53(209.144.50.138)
;; WHEN: Thu Jan 12 10:09:49 2012
;; MSG SIZE  rcvd: 164

```

The dig command output has the following sections:

Header: This displays the dig command version number, the global options used by the dig command, and few additional header information.

QUESTION SECTION: This displays the question it asked the DNS. i.e This is your input. Since we said ‘dig redhat.com’, and the default type dig command uses is A record, it indicates in this section that we asked for the A record of the redhat.com website

ANSWER SECTION: This displays the answer it receives from the DNS. i.e This is your output. This displays the A record of redhat.com

AUTHORITY SECTION: This displays the DNS name server that has the authority to respond to this query. Basically this displays available name servers of redhat.com

ADDITIONAL SECTION: This displays the ip address of the name servers listed in the AUTHORITY SECTION.
Stats section at the bottom displays few dig command statistics including how much time it took to execute this query

#### 2. Display Only the ANSWER SECTION of the Dig command Output

For most part, all you need to look at is the “ANSWER SECTION” of the dig command. So, we can turn off all other sections as shown below.

    +nocomments – Turn off the comment lines
    +noauthority – Turn off the authority section
    +noadditional – Turn off the additional section
    +nostats – Turn off the stats section
    +noanswer – Turn off the answer section (Of course, you wouldn’t want to turn off the answer section)

The following dig command displays only the ANSWER SECTION.

```
$ dig redhat.com +nocomments +noquestion +noauthority +noadditional +nostats

; <<>> DiG 9.7.3-RedHat-9.7.3-2.el6 <<>> redhat.com +nocomments +noquestion +noauthority +noadditional +nostats
;; global options: +cmd
redhat.com.             9       IN      A       209.132.183.81
```

Instead of disabling all the sections that we don’t want one by one, we can disable all sections using +noall (this turns off answer section also), and add the +answer which will show only the answer section.

The above command can also be written in a short form as shown below, which displays only the ANSWER SECTION.

```
$ dig redhat.com +noall +answer

; <<>> DiG 9.7.3-RedHat-9.7.3-2.el6 <<>> redhat.com +noall +answer
;; global options: +cmd
redhat.com.             60      IN      A       209.132.183.81
```

#### 3. Query MX Records Using dig -t MX

To query MX records, pass MX as an argument to the dig command as shown below.
```
$ dig redhat.com  MX +noall +answer

; <<>> DiG 9.7.3-RedHat-9.7.3-2.el6 <<>> redhat.com MX +noall +answer
;; global options: +cmd
redhat.com.             513     IN      MX      5 mx1.redhat.com.
redhat.com.             513     IN      MX      10 mx2.redhat.com.
```
You can also use option -t to pass the query type (for example: MX) as shown below.

$ dig -t MX redhat.com +noall +answer

; <<>> DiG 9.7.3-RedHat-9.7.3-2.el6 <<>> -t MX redhat.com +noall +answer
;; global options: +cmd
redhat.com.             489     IN      MX      10 mx2.redhat.com.
redhat.com.             489     IN      MX      5 mx1.redhat.com.

#### 4. Query NS Records Using dig -t NS

To query the NS record use the type NS as shown below.
```
$ dig redhat.com NS +noall +answer

; <<>> DiG 9.7.3-RedHat-9.7.3-2.el6 <<>> redhat.com NS +noall +answer
;; global options: +cmd
redhat.com.             558     IN      NS      ns2.redhat.com.
redhat.com.             558     IN      NS      ns1.redhat.com.
redhat.com.             558     IN      NS      ns3.redhat.com.
redhat.com.             558     IN      NS      ns4.redhat.com.
```
You can also use option -t to pass the query type (for example: NS) as shown below.
```
$ dig -t NS redhat.com +noall +answer

; <<>> DiG 9.7.3-RedHat-9.7.3-2.el6 <<>> -t NS redhat.com +noall +answer
;; global options: +cmd
redhat.com.             543     IN      NS      ns4.redhat.com.
redhat.com.             543     IN      NS      ns1.redhat.com.
redhat.com.             543     IN      NS      ns3.redhat.com.
redhat.com.             543     IN      NS      ns2.redhat.com.
```
#### 5. View ALL DNS Records Types Using dig -t ANY

To view all the record types (A, MX, NS, etc.), use ANY as the record type as shown below.
```
$ dig redhat.com ANY +noall +answer

; <<>> DiG 9.7.3-RedHat-9.7.3-2.el6 <<>> redhat.com ANY +noall +answer
;; global options: +cmd
redhat.com.             430     IN      MX      5 mx1.redhat.com.
redhat.com.             430     IN      MX      10 mx2.redhat.com.
redhat.com.             521     IN      NS      ns3.redhat.com.
redhat.com.             521     IN      NS      ns1.redhat.com.
redhat.com.             521     IN      NS      ns4.redhat.com.
redhat.com.             521     IN      NS      ns2.redhat.com.
```
(or) Use -t ANY
```
$ dig -t ANY redhat.com  +noall +answer

; <<>> DiG 9.7.3-RedHat-9.7.3-2.el6 <<>> -t ANY redhat.com +noall +answer
;; global options: +cmd
redhat.com.             367     IN      MX      10 mx2.redhat.com.
redhat.com.             367     IN      MX      5 mx1.redhat.com.
redhat.com.             458     IN      NS      ns4.redhat.com.
redhat.com.             458     IN      NS      ns1.redhat.com.
redhat.com.             458     IN      NS      ns2.redhat.com.
redhat.com.             458     IN      NS      ns3.redhat.com.
```
#### 6. View Short Output Using dig +short

To view just the ip-address of a web site (i.e the A record), use the short form option as shown below.

$ dig redhat.com +short
209.132.183.81

You can also specify a record type that you want to view with the +short option.
```
$ dig redhat.com ns +short
ns2.redhat.com.
ns3.redhat.com.
ns1.redhat.com.
ns4.redhat.com.
```
#### 7. DNS Reverse Look-up Using dig -x

To perform a DNS reverse look up using the ip-address using dig -x as shown below

For example, if you just have an external ip-address and would like to know the website that belongs to it, do the following.
```
$ dig -x 209.132.183.81 +short
www.redhat.com.
```
To view the full details of the DNS reverse look-up, remove the +short option.
```
$ dig -x 209.132.183.81

; <<>> DiG 9.7.3-RedHat-9.7.3-2.el6 <<>> -x 209.132.183.81
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 62435
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 4, ADDITIONAL: 3

;; QUESTION SECTION:
;81.183.132.209.in-addr.arpa.   IN      PTR

;; ANSWER SECTION:
81.183.132.209.in-addr.arpa. 600 IN     PTR     www.redhat.com.

;; AUTHORITY SECTION:
183.132.209.in-addr.arpa. 248   IN      NS      ns2.redhat.com.
183.132.209.in-addr.arpa. 248   IN      NS      ns1.redhat.com.
183.132.209.in-addr.arpa. 248   IN      NS      ns3.redhat.com.
183.132.209.in-addr.arpa. 248   IN      NS      ns4.redhat.com.

;; ADDITIONAL SECTION:
ns1.redhat.com.         363     IN      A       209.132.186.218
ns2.redhat.com.         363     IN      A       209.132.183.2
ns3.redhat.com.         363     IN      A       209.132.176.100

;; Query time: 35 msec
;; SERVER: 209.144.50.138#53(209.144.50.138)
;; WHEN: Thu Jan 12 10:15:00 2012
;; MSG SIZE  rcvd: 193
```
#### 8. Use a Specific DNS server Using dig @dnsserver

By default dig uses the DNS servers defined in your /etc/resolv.conf file.

If you like to use a different DNS server to perform the query, specify it in the command line as @dnsserver.

The following example uses ns1.redhat.com as the DNS server to get the answer (instead of using the DNS servers from the /etc/resolv.conf file).
```
$ dig @ns1.redhat.com redhat.com

; <<>> DiG 9.7.3-RedHat-9.7.3-2.el6 <<>> @ns1.redhat.com redhat.com
; (1 server found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 20963
;; flags: qr aa rd; QUERY: 1, ANSWER: 1, AUTHORITY: 4, ADDITIONAL: 4
;; WARNING: recursion requested but not available

;; QUESTION SECTION:
;redhat.com.                    IN      A

;; ANSWER SECTION:
redhat.com.             60      IN      A       209.132.183.81

;; AUTHORITY SECTION:
redhat.com.             600     IN      NS      ns1.redhat.com.
redhat.com.             600     IN      NS      ns4.redhat.com.
redhat.com.             600     IN      NS      ns3.redhat.com.
redhat.com.             600     IN      NS      ns2.redhat.com.

;; ADDITIONAL SECTION:
ns1.redhat.com.         600     IN      A       209.132.186.218
ns2.redhat.com.         600     IN      A       209.132.183.2
ns3.redhat.com.         600     IN      A       209.132.176.100
ns4.redhat.com.         600     IN      A       209.132.188.218

;; Query time: 160 msec
;; SERVER: 209.132.186.218#53(209.132.186.218)
;; WHEN: Thu Jan 12 10:22:11 2012
;; MSG SIZE  rcvd: 180
```
#### 9. Bulk DNS Query Using dig -f (and command line)
Query multiple websites using a data file:

You can perform a bulk DNS query based on the data from a file.

First, create a sample names.txt file that contains the website that you want to query.
```
$ vi names.txt
redhat.com
centos.org
```
Next, execute dig -f as shown below, which will perform DNS query for the websites listed in the names.txt file and display the output.
```
$ dig -f names.txt +noall +answer
redhat.com.             60      IN      A       209.132.183.81
centos.org.             60      IN      A       72.232.194.162
```
You can also combine record type with the -f option. The following example displays the MX records of multiple websites that are located in the names.txt file.
```
$ dig -f names.txt MX +noall +answer
redhat.com.             600     IN      MX      10 mx2.redhat.com.
redhat.com.             600     IN      MX      5 mx1.redhat.com.
centos.org.             3600    IN      MX      10 mail.centos.org.
```
Query multiple websites from dig command line:

You can also query multiple websites from the dig command line as shown below. The following example queries MX record for redhat.com, and NS record for centos.org from the command line
```
$ dig redhat.com mx +noall +answer centos.org ns +noall +answer

; <<>> DiG 9.7.3-RedHat-9.7.3-2.el6 <<>> redhat.com mx +noall +answer centos.org ns +noall +answer
;; global options: +cmd
redhat.com.             332     IN      MX      10 mx2.redhat.com.
redhat.com.             332     IN      MX      5 mx1.redhat.com.
centos.org.             3778    IN      NS      ns3.centos.org.
centos.org.             3778    IN      NS      ns4.centos.org.
centos.org.             3778    IN      NS      ns1.centos.org.
```
#### 10. Use $HOME/.digrc File to Store Default dig Options

If you are always trying to view only the ANSWER section of the dig output, you don’t have to keep typing “+noall +answer” on your every dig command. Instead, add your dig options to the .digrc file as shown below.
```
$ cat $HOME/.digrc
+noall +answer
```
Now anytime you execute dig command, it will always use +noall and +answer options by default. Now the dig command line became very simple and easy to read without you have to type those options every time.
```
$ dig redhat.com
redhat.com.             60      IN      A       209.132.183.81
```
```
$ dig redhat.com MX
redhat.com.             52      IN      MX      5 mx1.redhat.com.
redhat.com.             52      IN      MX      10 mx2.redhat.com.
```
*****
# Linux Cron Jobs
Cron allows Linux and Unix users to run commands or scripts at a given date and time. You can schedule scripts to be executed periodically. Cron is one of the most useful tool in a Linux or UNIX like operating systems. It is usually used for sysadmin jobs such as backups or cleaning /tmp/ directories and more. The cron service (daemon) runs in the background and constantly checks the /etc/crontab file, and /etc/cron.*/ directories. It also checks the /var/spool/cron/ directory.


## crontab command
You need to use the crontab command to edit/create, install, deinstall or list the cron jobs in Vixie Cron. Each user can have their own crontab file, and though these are files in /var/spool/cron/crontabs, they are not intended to be edited directly. You need to use crontab command for editing or setting up your own cron jobs.

## Types of cron configuration files

There are different types of configuration files:

1.The UNIX / Linux system crontab : Usually, used by system services and critical jobs that requires root like privileges. The sixth field (see below for field description) is the name of a user for the command to run as. This gives the system crontab the ability to run commands as any user.

2.The user crontabs: User can install their own cron jobs using the crontab command. The sixth field is the command to run, and all commands run as the user who created the crontab


## How Do I install or create or edit my own cron jobs?

To edit or create your own crontab file, type the following command at the UNIX / Linux shell prompt:
``` $ crontab -e ```

Do I have to restart cron after changing the crontable file?
 - No. Cron will examine the modification time on all crontabs and reload those which have changed. Thus cron need not be restarted whenever a crontab file is modified.

## Syntax of crontab (field description)

The syntax is:

``` 1 2 3 4 5 /path/to/command arg1 arg2 ```

OR 

```1 2 3 4 5 /root/backup.sh```

Where,

- 1 : Minute(0-59)
- 2 : Hours (0-23)
- 3 : Day   (0-31)
- 4 : Month (0-12 [12 == December])
- 5 : Day of the week(0-7[7 or 0 == sunday 

### How do I use operators?

An operator allows you to specifying multiple values in a field. There are three operators:

1. The asterisk (*) : This operator specifies all possible values for a field. For example, an asterisk in the hour time field would be equivalent to every hour or an asterisk in the month field would be equivalent to every month.
2. The comma (,) : This operator specifies a list of values, for example: “1,5,10,15,20, 25”.
3. The dash (-) : This operator specifies a range of values, for example: “5-15” days , which is equivalent to typing “5,6,7,8,9,….,13,14,15” using the comma operator.
4. The separator (/) : This operator specifies a step value, for example: “0-23/” can be used in the hours field to specify command execution every other hour. Steps are also permitted after an asterisk, so if you want to say every two hours, just use */2.

### Task: List all your cron jobs

Type the following command:
```# crontab -l```
``
```# crontab -u username -l```

To remove or erase all crontab jobs use the following command:
# Delete the current cron jobs #
```crontab -r```

## Delete job for specific user. Must be run as root user ##
```crontab -r -u username```

### Instead of the first five fields, you can use any one of eight special strings. It will not just save your time but it will improve readability.
Special string	Meaning

- @reboot	Run once, at startup.
- @yearly	Run once a year, “0 0 1 1 *”.
- @annually	(same as @yearly)
- @monthly	Run once a month, “0 0 1 * *”.
- @weekly	Run once a week, “0 0 * * 0”.
- @daily	Run once a day, “0 0 * * *”.
- @midnight	(same as @daily)
- @hourly	Run once an hour, “0 * * * *”.

### Examples

Run ntpdate command every hour:
```@hourly /path/to/ntpdate```

Make a backup everyday:
```@daily /path/to/backup/script.sh```

## More about /etc/crontab file and /etc/cron.d/* directories
/etc/crontab is system crontabs file. Usually only used by root user or daemons to configure system wide jobs. All individual user must must use crontab command to install and edit their jobs as described above. /var/spool/cron/ or /var/cron/tabs/ is directory for personal user crontab files. It must be backup with users home directory.


## Understanding Default /etc/crontab

Typical /etc/crontab file entries:
```
SHELL=/bin/bash
PATH=/sbin:/bin:/usr/sbin:/usr/bin
MAILTO=root
HOME=/
```

### run-parts

- 01 * * * * root run-parts /etc/cron.hourly
- 02 4 * * * root run-parts /etc/cron.daily
- 22 4 * * 0 root run-parts /etc/cron.weekly
- 42 4 1 * * root run-parts /etc/cron.monthly

First, the environment must be defined. If the shell line is omitted, cron will use the default, which is sh. If the PATH variable is omitted, no default will be used and file locations will need to be absolute. If HOME is omitted, cron will use the invoking users home directory.

Additionally, cron reads the files in /etc/cron.d/ directory. Usually system daemon such as sa-update or sysstat places their cronjob here. As a root user or superuser you can use following directories to configure cron jobs. You can directly drop your scripts here. The run-parts command run scripts or programs in a directory via /etc/crontab file:
Directory	Description
```
/etc/cron.d/	Put all scripts here and call them from /etc/crontab file.
/etc/cron.daily/	Run all scripts once a day
/etc/cron.hourly/	Run all scripts once an hour
/etc/cron.monthly/	Run all scripts once a month
/etc/cron.weekly/	Run all scripts once a week
```

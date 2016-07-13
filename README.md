# fail2ban-regex-test
fail2ban regex test utility

__Author__: James Hohman

__Date__: 7/12/2016


## Description
This utility will read fail2ban filter configuration files of your 
choosing and scan log files of your choosing and report line 
matches. Alternatively, you can provide a regex string and it 
will search the log files for matches.

When you have complicated regex strings, multiple rules, and 
lots of log entries, this can help you tune your fail2ban regex.


## Usage
Search the log for filter violations.
```
$ ./fail2bantest.py -f /etc/fail2ban/filter/my_filter.conf -l /var/log/mysite/apache.log
```

Search the log for regex matches.
```
$ ./fail2bantest.py -r '<some regex in here>' -l /var/log/mysite/apache.log
```

Multiple files can be searched.
```
$ ./fail2bantest.py -r '<some regex in here>' -l /var/log/mysite1/apache1.log /var/log/mysite2/apache2.log
```

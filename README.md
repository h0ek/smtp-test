# smtp test
Sedn emails using PowerShell and Python

When I was testing email servers and smtp relay and was able to send unauthorised emails via a Telnet session, I wrote myself a script like this to automate the sending of spoofed emails. Perhaps someone will find it useful.

Here is how you can test SMTP manually:

```
C:\Windows\System32> telnet
Microsoft Telnet> set localecho
Microsoft Telnet> set logfile c:\TelnetTest.txt
Microsoft Telnet> OPEN mail1.fabrikam.com 25
220 mail1.fabrikam.com Microsoft ESMTP MAIL Service ready at Fri, 5 Aug 2016 16:24:41 -0700
EHLO contoso.com
250-mail1.fabrikam.com Hello [172.16.0.5]
250-SIZE 37748736
250-PIPELINING
250-DSN
250-ENHANCEDSTATUSCODES
250-STARTTLS
250-X-ANONYMOUSTLS
250-AUTH NTLM
250-X-EXPS GSSAPI NTLM
250-8BITMIME
250-BINARYMIME
250-CHUNKING
250 XRDST
MAIL FROM: <chris@contoso.com>
250 2.1.0 Sender OK
RCPT TO: <kate@fabrikam.com> NOTIFY=success,failure
250 2.1.5 Recipient OK
DATA
354 Start mail input; end with <CRLF>.<CRLF>
Subject: test

This is a test message.
.
```
Source: https://learn.microsoft.com/en-us/exchange/mail-flow/test-smtp-telnet?view=exchserver-2019

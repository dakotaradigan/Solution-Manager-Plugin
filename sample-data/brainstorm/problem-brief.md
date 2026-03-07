# Intake: Pricing Issue (forwarded)

---------- Forwarded message ---------
From: Dave Kowalski (Head of Trading)
To: Sarah Chen (PM Lead)
Date: Tuesday 2:47 PM

Sarah — forwarding this from Mike's desk. He put on a 50k share buy in CVX this morning using our internal mark from last night. Bloomberg had it $1.20 higher at the time. He got filled at the Bloomberg price obviously, so now we're showing a P&L hit on a trade that was supposed to be at-market. This is the third time this quarter.

Can someone figure out why our prices are stale? Or at least tell me which price I'm supposed to trust?

— Dave

---

**#trading-desk** (Slack, same day)

**mike.t:** anyone else seeing CVX internal price stuck at yesterday's close? Bloomberg has 161.40, we're showing 160.20

**priya.r:** our Refinitiv feed has 161.38 so it's not just Bloomberg. internal is definitely stale

**jason.ops:** I checked — custodian file came in at 6am, hasn't updated since. so yeah the "price" in our system is last night's NAV price

**mike.t:** so we have three different prices and no way to know which one to use?

**priya.r:** basically

**jason.ops:** I'll ask the data team but this has come up before and nothing happened

---

## Try It

```
/solution-work:brainstorm
```

Then paste or reference this file when asked what you're exploring.

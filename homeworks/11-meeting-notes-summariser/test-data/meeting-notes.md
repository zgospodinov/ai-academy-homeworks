# Meeting notes (test data)

Generated with Claude (R1). Same text as in the `Collect Meeting Notes` Code node.

## Engineering

Attendees: Maria (Engineering Manager), Ivan (Backend Lead), Petya (QA Lead), Georgi (DevOps).
- Release 4.2 slips from Thursday to next Tuesday. The payment-service migration to the new database failed 2 of 38 regression tests (currency rounding on refunds). Ivan owns the fix, ETA Friday; Petya reruns the full regression on Monday.
- Yesterday's staging outage (14:10-15:05) was caused by an expired TLS certificate on the internal gateway. Georgi will add certificate-expiry alerts (30/14/7 days) by end of the week.
- Decision: feature freeze for 4.2 starts today. The bulk-export API moves from 4.2 to 4.3 and is not expected before mid-November.
- Risk: only Ivan knows the legacy billing module. Maria asked HR for a senior backend hire and will schedule a knowledge-transfer session next week.
- Open question: keep supporting API v1 after December? Maria collects usage numbers from Georgi's dashboards by Wednesday.
- Security: the quarterly penetration test found 3 medium findings in the public API (missing rate limiting on two endpoints, verbose error messages). Georgi opens tickets today; fixes must ship with 4.2 or the release needs a documented exception from the CTO.
- Tech debt: the CI pipeline takes 41 minutes, up from 25. Petya and Georgi will profile it and propose parallelisation options at next week's sync; target is under 30 minutes.

## Sales

Attendees: Dimitar (Head of Sales), Elena (Enterprise AE), Nikolay (SMB Lead), Rositsa (Sales Ops).
- Q4 pipeline is at 2.1M EUR against a 2.6M target. Enterprise is on track; SMB is 18% behind because the autumn webinar series produced fewer leads than planned.
- Elena promised Northwind Logistics (deal worth 340k EUR) the bulk-export API before the end of October. Dimitar notes this depends on the Engineering release; he will ask Engineering for a firm date and warn the customer if it slips past November 5.
- Nikolay proposes a 10% discount for annual SMB contracts signed before Nov 15. It needs Finance approval; Dimitar sends the request today.
- Rositsa will clean up about 250 duplicate CRM accounts by Friday so that forecasts are reliable.
- Two enterprise renewals (Contoso, Fabrikam) are at risk: both asked for SSO improvements. Elena schedules customer calls this week.
- Competitor update: a rival launched a free tier last week. Nikolay saw 3 SMB prospects mention it in calls; Dimitar asks Marketing for a battlecard by Thursday.
- Forecast hygiene: deals without a next step older than 30 days are moved to "stalled" automatically from Monday. Reps must update their opportunities before then.

## HR

Attendees: Svetla (HR Director), Boris (Recruiter), Anna (Learning & Development), Tihomir (HR Business Partner).
- Open positions: 6 (2 backend, 1 QA, 2 sales, 1 finance analyst). Average time-to-hire is 52 days against a target of 40. Boris proposes dropping the second technical interview round for junior roles; Svetla must approve by Thursday.
- Engineering requested a senior backend engineer. The budget is not approved yet, so the role stays pending until Finance confirms headcount.
- Employee survey: engagement score 7.4 (down from 7.9). Main complaint: unclear career paths. Anna launches career-framework workshops starting Nov 3 and needs a room booking plus manager sign-off.
- Two engineers (one backend, one QA) gave notice last week. Tihomir runs exit interviews by next Wednesday and reports the themes.
- Reminder: annual compliance training deadline is Oct 31; 64% completed.
- Onboarding: 5 new hires start on Nov 3. Boris coordinates laptops with IT; Anna prepares the buddy programme and asks managers to name a buddy by Friday.
- Policy: the hybrid-work policy review is due in November. Tihomir collects feedback from managers and will present the options at the leadership meeting.

## Finance

Attendees: Katerina (CFO), Plamen (FP&A), Veselin (Accounts Payable), Nadia (Controller).
- September close finished 2 days late because of unreconciled intercompany invoices. Nadia introduces a mid-month reconciliation checkpoint starting in October.
- Q3 revenue was 7.8M EUR, 3% below forecast, mostly because two enterprise deals slipped to Q4. Plamen updates the Q4 forecast and shares it on Friday; the forecast assumes the Northwind deal closes in October.
- Katerina will decide on the additional senior backend headcount only after seeing the updated forecast; no decision before next Monday.
- Sales proposes a 10% discount for annual SMB contracts. Katerina wants a margin-impact analysis first; Plamen delivers it by Wednesday.
- Veselin flagged 14 vendor invoices overdue by more than 30 days (96k EUR total); two vendors threatened to suspend services. Payment run is scheduled for Thursday.
- Risk: the cash buffer drops below the 3-month policy minimum if the Q4 slippage continues.
- Audit: the external auditors arrive Nov 17. Nadia needs the fixed-asset register and the updated revenue-recognition memo from Plamen by Nov 7.
- Tooling: the expense-approval tool renewal costs 18% more. Veselin gets a competing quote from two vendors and reports back next Tuesday.

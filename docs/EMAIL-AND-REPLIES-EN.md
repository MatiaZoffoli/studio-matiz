# Emails and replies in English

Date: 2026-10-09. English counterpart of `docs/EMAIL-E-RISPOSTE.md` (A3-A5, B1-B10, C1-C3). A1 and A2 (the automatic confirmation and the internal alert) are in the code, `supabase/functions/contatto/email.ts`, in both languages. Semantic translation, not word for word, in the voice of the Italian originals: direct, precise, one action per message, a number or fact per line, no exclamation marks. Fields in double braces are variables. "Settling in" is the English name of the first free-hours month (Italian: rodaggio).

Words to avoid, as in Italian: solutions, free (use "offered" or "complimentary"), "contact us", "discover", "no obligation", "tailor-made".

---

## A. Automatic

### A3. Out-of-office (email)

**Subject:** Message received

> Hello,
>
> this is an automatic reply. Your message has arrived and Matia will send a first reply within one working day. On closing days the reply comes on the first working day after.
>
> If it cannot wait, a message on WhatsApp (+39 333 958 0381) is the quickest channel.
>
> Studio Matiz, by Matia Zoffoli

### A4. First meeting confirmation (after booking on the calendar)

**Subject:** First meeting: {{day}} at {{time}}

> Hello {{name}},
>
> the first meeting is set for {{day}} at {{time}}, for one hour, {{place_or_link}}.
>
> There is nothing to prepare. It helps to have three things to hand: the address of the website or profiles that already exist, an example of a typical working day, and one number you would like to improve (enquiries, bookings, members, hours lost).
>
> If the meeting needs to move, just reply to this email.
>
> Studio Matiz, by Matia Zoffoli

### A5. Reminder the day before (automatic)

**Subject:** Tomorrow at {{time}}: first meeting

> Hello {{name}}, a reminder: tomorrow at {{time}} is the first meeting, {{place_or_link}}. One hour, with nothing to do beforehand.
>
> Studio Matiz

---

## B. Written by Matia along the way

### B1. After the first meeting: summary and next step

**Subject:** After the meeting: the starting numbers and the next step

> Hello {{name}},
>
> thank you for yesterday's hour. In short, what came out:
> - Where time is lost: {{point_1}}
> - The number to measure: {{number}}, starting today from {{starting_value}}
> - What is best to do first: {{priority}}
>
> The next step can be a check-up (200 euro, credited towards the work that follows; a report within three working days of confirmation and access) or directly a written quote, if the direction is already clear. Let me know which you prefer.
>
> Matia

### B2. Sending the check-up

**Subject:** Check-up for {{business}}: three priorities

> Hello {{name}},
>
> attached is the check-up report, also on the private page: {{link}}.
>
> In short: three things to do first, with the cost of each, in order of effect on the number chosen ({{number}}). The check-up fee ({{amount}} euro) is credited towards the work that follows, with the credit that applies from the date of confirmation.
>
> If you want to go ahead, the written quote arrives within three working days of your reply.
>
> Matia

### B3. Sending the quote

**Subject:** Quote no. {{number}} for {{business}}

> Hello {{name}},
>
> attached are quote no. {{number}} and the service agreement. The price is fixed, the delivery time runs from the moment all the material arrives, and two rounds of revisions are included.
>
> To accept, just reply "I accept", or sign the last page. The quote is valid until {{expiry}}.
>
> Matia

### B4. Gentle reminder on the quote (after seven days)

**Subject:** Quote no. {{number}}: valid until {{expiry}}

> Hello {{name}},
>
> a reminder about quote no. {{number}}, valid until {{expiry}}. If something does not add up, a doubt about price or timing, a first reply comes within one working day. If now is not the moment, no problem: the material stays, and we can pick it up when it suits.
>
> Matia

### B5. Welcome after acceptance

**Subject:** We start: what is needed and the first dates

> Hello {{name}},
>
> thank you for your trust. This is the sequence:
> - By {{date_1}}: the material needed ({{material_list}}) and access.
> - From when everything arrives: {{time}} to deliver, with an update halfway through.
> - On delivery: two rounds of revisions, and right after that the settling-in month starts.
>
> For any doubt, WhatsApp or this email: a first reply comes within one working day.
>
> Matia

### B6. Delivery and start of the settling-in month

**Subject:** Delivery of {{work}} and start of the settling-in month

> Hello {{name}},
>
> the work is ready: {{link}}. Two rounds of revisions are included and start now.
>
> From today the first month of ongoing care also begins, at a flat fee and with no cap on hours: anything routine can be included, and what to include is decided together according to needs. At the end of the month a report with the real hours sets the level for the following months.
>
> Matia

### B7. Monthly report (accompanies the PDF)

**Subject:** Report for {{month}}: {{hours}} hours, {{number_of_items}} changes

> Hello {{name}},
>
> attached is the report for {{month}}. In short: {{hours}} hours used out of {{included}} included, {{number_of_items}} changes, and the three performance numbers in section four. At the bottom of the page, the recommendation for next month, with its cost.
>
> Matia

### B8. End of the settling-in month (accompanies the first-month report)

**Subject:** End of the settling-in month: what we learned and the recommended level

> Hello {{name}},
>
> the first month is over. Attached is the report: real hours used ({{hours}}), requests handled ({{requests}}), and the level I recommend from now on ({{level}}, {{fee}} euro a month, {{included_hours}} hours included).
>
> If the level suits, one reply is enough and it starts on {{date}}. If a different balance is needed, we can talk it over in a ten-minute call.
>
> Matia

### B9. Asking for a testimonial and permission to tell the case

**Subject:** Two lines on the work, and a permission

> Hello {{name}},
>
> as agreed at the start, two requests now the work is done. The first: two or three lines on how it went, in the words you prefer. The second: permission to tell the case on the website and social media, with the name of the business and the numbers ({{number}}: from {{before}} to {{after}}). The final text arrives before publication, and it is published only with a written "ok".
>
> Matia

### B10. Request outside the scope (polite refusal)

**Subject:** About your request on {{topic}}

> Hello {{name}},
>
> thank you for the message. {{topic}} is not part of what is done here: websites, digital menus, automations and tools for small businesses. So it would not be a good job, and it is better to say so straight away.
>
> If useful, a direction towards someone who can help: {{pointer}}. And for anything else in the fields above, the door is open.
>
> Matia

---

## C. WhatsApp Business

### C1. Welcome message (automatic, on first contact)

> Hello, this is Studio Matiz, by Matia Zoffoli. Your message has arrived and a first reply comes within one working day. For a one-hour first meeting, offered by the studio, the calendar is here: {{calendar_link}}.

### C2. Away message (outside hours)

> Hello, thank you for your message. The studio is closed at the moment: the reply comes on the first working day after. To set up a meeting, the calendar can already be used: {{calendar_link}}.

### C3. Quick replies

- **/meeting** - The first meeting lasts one hour, in person or by video, and is offered. Book here: {{calendar_link}}. There is nothing to prepare.
- **/price** - The price is written after the first meeting and does not change along the way. For an estimate right now, the estimator on the website gives a starting price in four questions: {{site_link}}.
- **/timing** - Timing is written in the quote and runs from the moment all the material arrives: from a few days for a menu to a few weeks for a complete website.
- **/checkup** - The check-up is research on what already exists: a report within three working days of confirmation and access, with the three priorities and the cost of each. The cost is credited towards the work that follows.
- **/care** - Ongoing care includes updates, security, backups and changes, with a monthly block of support time. The first month is a flat fee with no cap on hours, to see how much is really needed.

---

## Check before sending

- [ ] The subject says what is inside, with no exclamation marks.
- [ ] The first line gives the reason for the message.
- [ ] One clear action, with the link.
- [ ] A number, a time or a fact on every important line.
- [ ] Automatic replies say they are automatic and say when Matia replies.
- [ ] Signature: "Matia" in personal messages, "Studio Matiz, by Matia Zoffoli" in automatic ones.

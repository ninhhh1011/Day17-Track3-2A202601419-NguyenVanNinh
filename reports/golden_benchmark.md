# Lab 17 Golden Set Report

- Implementation: `student`
- Kind: `golden`
- Cases: **20**
- Passed: **20/20**
- Evidence hit rate: **100.0%**
- Average retrieval latency: **1591.9 ms**
- Average token reduction vs full source context: **6.3%**
- Golden bonus: **10/10** (100% required)

| Case | Layer | Pass | Latency ms | Retrieved tokens | Token reduction | Missing / Error |
| --- | --- | --- | ---: | ---: | ---: | --- |
| G01 | short_term | PASS | 0.5 | 227 | 0.0% |  |
| G02 | short_term | PASS | 0.0 | 133 | 0.0% |  |
| G08 | long_term | PASS | 2695.6 | 957 | 0.0% |  |
| G09 | long_term | PASS | 2373.0 | 2299 | 0.0% |  |
| G12 | semantic | PASS | 343.7 | 418 | 8.9% |  |
| G14 | semantic | PASS | 269.0 | 270 | 30.2% |  |
| G15 | semantic | PASS | 263.9 | 270 | 41.2% |  |
| G19 | mixed | PASS | 1937.3 | 581 | 0.0% |  |
| G03 | long_term | PASS | 2148.6 | 2301 | 0.0% |  |
| G04 | long_term | PASS | 1845.3 | 2313 | 0.0% |  |
| G05 | long_term | PASS | 1862.4 | 2251 | 0.0% |  |
| G10 | episodic | PASS | 294.1 | 291 | 0.0% |  |
| G11 | episodic | PASS | 299.2 | 295 | 0.0% |  |
| G13 | semantic | PASS | 378.7 | 416 | 26.4% |  |
| G16 | mixed | PASS | 2253.1 | 581 | 0.0% |  |
| G18 | mixed | PASS | 636.2 | 500 | 11.5% |  |
| G20 | mixed | PASS | 2798.1 | 831 | 0.0% |  |
| G06 | long_term | PASS | 3637.6 | 2311 | 0.0% |  |
| G07 | long_term | PASS | 3375.8 | 2301 | 0.0% |  |
| G17 | mixed | PASS | 4426.7 | 581 | 8.1% |  |

## Evidence excerpts

### G01 - short_term

`<SESSION_SUMMARY> user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. | assistant: Noted standup constraint. | user: Constraint HOLD-BETA-STAGING: writes go to staging DB only. | assistant: Noted staging constraint. | user: Filler A about button padding. | assistant: Filler A. | user: Filler B about color tokens. | assistant: Filler B. | user: Filler C about copy tone. | assistant: Filler C. </SESSION_SUMMARY> <DURABLE_NOTES> - user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. - assistant: Noted standup constraint. - user: Constraint HOLD-BETA-STAGING: writes go to staging DB only. - assistant: Noted staging constraint. </DURA`

### G02 - short_term

`<RECENT_TURNS> user: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. assistant: Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan. user: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. assistant: Toi se uu tien timeline khi giai thich coroutine va Task. user: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. </RECENT_TURNS>`

### G08 - long_term

`<USER_SUMMARY> Lan's project is LOTUS-88. They prioritize Java and Spring Boot for backend examples and do not use Python for the backend. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-17 05:32:33     Source: message     Content: [user] {   "user_id": "lan-lab17",   "first_name": "Lan",   "last_name": "Tran",   "user_alias": "Evaluation User" }: Minh la Lan, minh dang muon them retry cho phan goi payment trong san pham cua minh va minh muon vi du code hop voi dung stack ma minh dang dung chu dung dua cho minh vi du cua ngon ngu khac. Ban gy y gium minh: dua theo backend ma minh da chon cho san pham cua minh, min`

### G09 - long_term

`<USER_SUMMARY> The user's personal project is named ORCHID-27, for which they prefer to use Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, not Python. The user is debugging async HTTP for ORCHID-27, having identified connection churn as the primary issue. Reusing the aiohttp ClientSession and setting concurrency to 20 has been an effective solution.  The user prefers Python and dislikes Java. The user prefers Python for personal demos like ORCHID-27. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS.  When explaining coroutines and Tasks, the AI should prioritize using a timeline. </USER_SUMMARY>  <EPISODES> Episodes a`

### G12 - semantic

`EPISODE: {"id":"kb-payment-retry","entity":"Payment API Retry Policy","summary":"For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3.","source":"internal-api-guideline-v3","updated_at":"2026-08-10T00:00:00Z"} metadata= EPISODE: For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3. metadata= EPISODE: {"id":"kb-memory-privacy","entity":"Agent Memory Privacy Rule","summary":"Do not persist personal `

### G14 - semantic

`EPISODE: {"id":"kb-memory-privacy","entity":"Agent Memory Privacy Rule","summary":"Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL.","source":"memory-governance-policy","updated_at":"2026-08-12T00:00:00Z"} metadata= EPISODE: Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL. metadata= EPISODE: {"id":"kb-context-budget","entity":"Memory Context Budget","summary":"Reserve bounded context for memory. This lab uses short-term 10 percent, long-term 4 percent, episodi`

### G15 - semantic

`EPISODE: {"id":"kb-memory-privacy","entity":"Agent Memory Privacy Rule","summary":"Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL.","source":"memory-governance-policy","updated_at":"2026-08-12T00:00:00Z"} metadata= EPISODE: Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL. metadata= EPISODE: {"id":"kb-context-budget","entity":"Memory Context Budget","summary":"Reserve bounded context for memory. This lab uses short-term 10 percent, long-term 4 percent, episodi`

### G19 - mixed

`<LONG_TERM> <USER_SUMMARY> Lan's project is LOTUS-88. They prioritize Java and Spring Boot for backend examples and do not use Python for the backend. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-17 05:34:15     Source: message     Content: [user] {   "user_id": "lan-lab17",   "first_name": "Lan",   "last_name": "Tran",   "user_alias": "Evaluation User" }: Lan uu tien stack backend nao cho LOTUS-88?   - Created At: 2026-08-01 11:00:20     Source: message     Content: Lab Assistant (assistant): Da hieu: LOTUS-88, Java + Spring Boot cho backend examples.   - Created At: 2026-08-01 11:00:00     Source: message    `

### G03 - long_term

`<USER_SUMMARY> The user's personal project is named ORCHID-27, for which they prefer to use Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, not Python. The user is debugging async HTTP for ORCHID-27, having identified connection churn as the primary issue. Reusing the aiohttp ClientSession and setting concurrency to 20 has been an effective solution.  The user prefers Python and dislikes Java. The user prefers Python for personal demos like ORCHID-27. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS.  When explaining coroutines and Tasks, the AI should prioritize using a timeline. </USER_SUMMARY>  <EPISODES> Episodes a`

### G04 - long_term

`<USER_SUMMARY> The user's personal project is named ORCHID-27, for which they prefer to use Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, not Python. The user is debugging async HTTP for ORCHID-27, having identified connection churn as the primary issue. Reusing the aiohttp ClientSession and setting concurrency to 20 has been an effective solution.  The user prefers Python and dislikes Java. The user prefers Python for personal demos like ORCHID-27. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS.  When explaining coroutines and Tasks, the AI should prioritize using a timeline. </USER_SUMMARY>  <EPISODES> Episodes a`

### G05 - long_term

`<USER_SUMMARY> The user's personal project is named ORCHID-27, for which they prefer to use Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, not Python. The user is debugging async HTTP for ORCHID-27, having identified connection churn as the primary issue. Reusing the aiohttp ClientSession and setting concurrency to 20 has been an effective solution.  The user prefers Python and dislikes Java. The user prefers Python for personal demos like ORCHID-27. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS.  When explaining coroutines and Tasks, the AI should prioritize using a timeline. </USER_SUMMARY>  <EPISODES> Episodes a`

### G10 - episodic

`EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Da ghi nhan trajectory: increase timeout khong hieu qua; ClientSession + concurrency=20 giai quyet connection churn. EPISODE: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. EPISODE: TODO: hoan thanh benchmark report truoc thu Sau luc `

### G11 - episodic

`EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Cap nhat moi: voi du an cong ty BLUEBIRD-42, backend bat buoc dung TypeScript voi NestJS; khong dung Python cho backend du an nay. Preference Python van dung cho demo ca nhan ORCHI EPISODE: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fai`

### G13 - semantic

`EPISODE: {"id":"kb-async-http","entity":"Async HTTP Incident Playbook","summary":"When async HTTP calls time out, inspect connection pooling, downstream saturation and concurrency before increasing timeout. Reuse a long-lived client session where possible. Marker: CONN-POOL-FIRST.","source":"incident-playbook-2026","updated_at":"2026-08-11T00:00:00Z"} metadata= EPISODE: When async HTTP calls time out, inspect connection pooling, downstream saturation and concurrency before increasing timeout. Reuse a long-lived client session where possible. Marker: CONN-POOL-FIRST. metadata= EPISODE: {"id":"kb-memory-privacy","entity":"Agent Memory Privacy Rule","summary":"Do not persist personal data witho`

### G16 - mixed

`<LONG_TERM> <USER_SUMMARY> The user's personal project is named ORCHID-27, for which they prefer to use Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, not Python. The user is debugging async HTTP for ORCHID-27, having identified connection churn as the primary issue. Reusing the aiohttp ClientSession and setting concurrency to 20 has been an effective solution.  The user prefers Python and dislikes Java. The user prefers Python for personal demos like ORCHID-27. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS.  When explaining coroutines and Tasks, the AI should prioritize using a timeline. </USER_SUMMARY>  <EPISODES`

### G18 - mixed

`<EPISODIC> EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. EPISODE: Cap nhat moi: voi du an cong ty BLUEBIRD-42, backend bat buoc dung TypeScript voi NestJS; khong dung Python cho backend du an nay. Preference Python van dung cho demo ca nhan ORCHI EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nh`

### G20 - mixed

`<LONG_TERM> <USER_SUMMARY> The user's personal project is named ORCHID-27, for which they prefer to use Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, not Python. The user is debugging async HTTP for ORCHID-27, having identified connection churn as the primary issue. Reusing the aiohttp ClientSession and setting concurrency to 20 has been an effective solution.  The user prefers Python and dislikes Java. The user prefers Python for personal demos like ORCHID-27. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS.  When explaining coroutines and Tasks, the AI should prioritize using a timeline. </USER_SUMMARY>  <EPISODES`

### G06 - long_term

`<USER_SUMMARY> The user's personal project is named ORCHID-27, for which they prefer to use Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, not Python. The user is debugging async HTTP for ORCHID-27, having identified connection churn as the primary issue. Reusing the aiohttp ClientSession and setting concurrency to 20 has been an effective solution.  The user prefers Python and dislikes Java. The user prefers Python for personal demos like ORCHID-27. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS.  When explaining coroutines and Tasks, the AI should prioritize using a timeline. </USER_SUMMARY>  <EPISODES> Episodes a`

### G07 - long_term

`<USER_SUMMARY> The user's personal project is named ORCHID-27, for which they prefer to use Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, not Python. The user is debugging async HTTP for ORCHID-27, having identified connection churn as the primary issue. Reusing the aiohttp ClientSession and setting concurrency to 20 has been an effective solution.  The user prefers Python and dislikes Java. The user prefers Python for personal demos like ORCHID-27. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS.  When explaining coroutines and Tasks, the AI should prioritize using a timeline. </USER_SUMMARY>  <EPISODES> Episodes a`

### G17 - mixed

`<LONG_TERM> <USER_SUMMARY> The user's personal project is named ORCHID-27, for which they prefer to use Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, not Python. The user is debugging async HTTP for ORCHID-27, having identified connection churn as the primary issue. Reusing the aiohttp ClientSession and setting concurrency to 20 has been an effective solution.  The user prefers Python and dislikes Java. The user prefers Python for personal demos like ORCHID-27. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS.  When explaining coroutines and Tasks, the AI should prioritize using a timeline. </USER_SUMMARY>  <EPISODES`

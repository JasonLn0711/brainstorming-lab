# 114 學年度國科會暨教育部博士生獎學金申請紀錄

Created: 2026-05-11
Owner: Jason Lin / 林家聖
Canonical summary: this file
Raw local archive: `/home/jnln3799/system-hub/admin/inventory/applications/2025-2026-moe-nstc-phd-scholarship/`
Source index: `docs/personal-admin/2026-05-11-moe-nstc-phd-scholarship-114-sources.csv`

## Privacy Boundary

This is a redacted working record. It intentionally avoids full identity numbers, home address, bank account data, labor-insurance raw identifiers, recommendation-letter images, and exact personal contact fields.

Raw PDFs and extracted text are archived local-only under `system-hub` with owner-only permissions. Do not move those raw files into git.

## Current Status

- Outcome so far: awarded 114 academic-year Ministry of Education doctoral scholarship through the NYCU college/department route.
- Award period stated in the award notice: 2025-09-01 to 2026-08-31.
- Active next deadline: 2026-05-20, renewal review / annual evaluation and MOE bonus-application materials must be uploaded to the specified Google Form.
- Jason's internal deadline: 2026-05-13, finish packet preparation and ask Prof. Wu for a 2026-05-14 school/lab signature time; 2026-05-15 remains the latest ready-to-route fallback before the weekend, except the final labor-insurance refresh that must happen after 2026-05-18.
- Current missing operational check: whether the 2026-03-16 matching-fund statement was fully handled by the department/advisor route, whether the 2026-05-20 renewal packet has been signed, routed, includes the institute director's seal / `所長蓋章`, has a post-2026-05-18 labor-insurance record, and has been uploaded.
- 2026-05-13 current-machine update: the May renewal attachments are now archived locally under the planning repo ignored folder `.local/admin/2026-05-nycu-doctoral-scholarship-renewal/`; student-side form prefill, supporting-report draft, works-output section, evidence checklist, advisor message, advisor-section helper, upload checklist, Google Form answer sheet, completion matrix, and office-routing note are prepared there.
- 2026-05-13 advisor-routing update: Jason manually sent Prof. Wu a LINE review/signature request at 04:43 with the renewal application form PDF and supporting-review report PDF attached. Prof. Wu replied at 06:03 that he would sign later and returned the signed renewal application form PDF at 08:12. Next gates are lab printout with Guan-Ting, institute-office director signature or seal routing, college routing, Google Form upload, and receipt capture.
- 2026-05-14 office-call update: at 16:10 Jason recorded that the uploaded renewal materials must include the institute director's seal / `所長蓋章`, and that the labor-insurance record must be from after 2026-05-18. At 16:11, Jason pulled the paper packet back for scanning / rework.

## FIRST PRINCIPLE Decision Record

- Scarce resource: signature-routing time, seal/scan handling, and the dated labor-insurance evidence window, not the final Google Form upload click.
- External deadline: 2026-05-20 is the official upload deadline.
- Internal deadline: 2026-05-15 is the packet-readiness deadline so advisor, department, and college review can happen before the official deadline.
- Canonical output by Friday: ready-to-sign evaluation form, supporting-PDF evidence checklist, seal/scan routing note, and a queued post-2026-05-18 labor-insurance refresh.
- Boundary: do not place raw identity, payment, labor-insurance, or signature files in git; keep those in the private local archive.

ROC date conversion used here:

- 114 academic year = roughly 2025-09 to 2026-08.
- 115 dates in the emails = 2026 Gregorian dates.

## Source Coverage

Local files moved from Downloads:

- 7 Gmail/PDF source files were renamed and moved into the local archive.
- `pdftotext -layout` extraction was saved under the archive's `extracted-text/`.
- SHA-256 checksums were saved in `manifest.sha256`.

Gmail connector coverage:

- Gmail search/read confirmed additional relevant messages not present as local PDFs, including the initial 2025-10-07/08 application announcement, the 2025-10-09 briefing-PPT forward, the 2026-03-05 matching-fund statement notice, and the 2026-05-11 renewal-review attachments.
- This pass parsed the current 2026-05-11 renewal attachments where supported, including the NSTC/MOE rule PDFs, updated NYCU rule PDF, bonus-journal list, labor-insurance SOP, replacement-student spreadsheet example, renewal-flow note, and evaluation-report form.
- It also parsed the initial 2025-10 application-notes PDF. Other initial official templates are captured by attachment list and purpose, but not all Gmail attachment binaries were saved into local storage; raw attachments remain in Gmail unless separately archived later.

2026-05-13 current-machine packet build:

- User-provided Downloads files were renamed and moved into the ignored local packet folder:
  `/home/jnclaw/every_on_git_jnclaw/phd-life-system/planning-everything-track/.local/admin/2026-05-nycu-doctoral-scholarship-renewal/`.
- Gmail connector recovered missing May attachments 4, 6, and the PDF copy of attachment 9 so the local source folder now matches the email packet.
- Extracted text and source checksums were generated locally.
- Working drafts prepared:
  - prefilled official evaluation form student-owned/verifiable fields as DOCX/PDF,
  - normalized unsigned application-form files using student ID naming,
  - supporting report draft as Markdown/HTML/PDF/DOCX with research results, works-output, collaboration, internationalization, and bonus self-check,
  - Prof. Wu advisor-section helper as Markdown/HTML/PDF/DOCX,
  - review-packet preview PDF for advisor routing,
  - required-order evidence checklist,
  - Prof. Wu signature-request message,
  - Google Form upload checklist,
  - Google Form answer sheet,
  - required-form completion matrix,
  - department/college routing note.
- Practical consequence: the current blocker has shifted from locating attachments to human-gated evidence and routing: labor-insurance record download, transcript download, advisor signature/comments, department/institute seal, college routing, and Google Form upload.

## Timeline

| Date | Event | What Happened | Evidence |
| --- | --- | --- | --- |
| 2025-10-03 | OAA opened the 114 scholarship application route | The scholarship system was unavailable because of technical/security-policy issues, so the school used a manual email-based process similar to 113. | Gmail initial announcement forwarded on 2025-10-07 |
| 2025-10-07 | College route forwarded application instructions | Students had to submit one merged PDF by 2025-10-19 23:59 to the college contact and cc the department office. Required pieces: application form, labor-insurance record, pledge, enrollment certificate, eligibility evidence, and doctoral research plan. | `SRC-GMAIL-01` |
| 2025-10-08 | Institute forwarded the application notice | Institute of Biophotonics told interested students to email Ms. Kuan by 2025-10-19 23:59 and cc the institute office. | `SRC-GMAIL-02` |
| 2025-10-09 | Scholarship briefing PPT circulated | Prof. Wu forwarded the 2025-10-09 scholarship briefing PDF from the college route. | `SRC-GMAIL-03` |
| 2025-10-14 17:31 | Jason submitted the application packet | Jason sent a single merged PDF titled for the 114 doctoral scholarship application to the college contact, with department office, advisor, and related contacts copied. | `SRC-LOCAL-02`, `SRC-GMAIL-05` |
| 2025-10-14 17:42 | College confirmed receipt and paper route | College replied that pages 1-3 of the application form should be printed and sent to the institute office for director seal, then transmitted to the college office. | `SRC-LOCAL-02` |
| 2025-11-07 09:57 | Student data spreadsheet requested | College asked students to fill the student data summary spreadsheet and place payment-account supporting material on worksheet 2 by 2025-11-10 14:00. | `SRC-LOCAL-03` |
| 2025-11-07 12:55 | Jason returned the data spreadsheet | Jason replied that the spreadsheet was filled and the payment-account supporting material was placed on worksheet 2. | `SRC-LOCAL-03`, `SRC-GMAIL-06` |
| 2025-11-07 14:31 | College confirmed receipt | College replied "收到". | `SRC-LOCAL-03` |
| 2025-11-13 | MOE second-batch announcement circulated | General announcement for second batch, deadline 2025-11-26. This appears after Jason's first packet was already submitted, so it is context rather than the original application route. | `SRC-LOCAL-04` |
| 2025-11-20 | Distribution data form requested | Institute required students to fill a Google Form by 2025-11-21 17:00 for scholarship distribution; the reminder emphasized payment-account information and warned that missing data could block or delay distribution. | `SRC-LOCAL-05`, `SRC-GMAIL-07` |
| 2025-12-19 / 2025-12-22 | Award list notice | College notice said the college-ranked list passed school-level re-review. Institute forwarded the notice to awardees; Jason was listed under MOE scholarship. | `SRC-LOCAL-06`, `SRC-GMAIL-08` |
| 2025-12 to 2026-01 | Expected first disbursement | OAA had completed roster work for 2025-09 to 2025-12 scholarship payments; actual entry was estimated around late 2025-12 to 2026-01 depending on cashier/disbursement work. | `SRC-LOCAL-06` |
| 2026-03-05 | 114-1 MOE matching-fund statement notice | Institute asked students to quickly handle the Excel attachment and signatures for the college route. OAA details covered 2025-09-01 to 2026-02-28, total matching fund NT$60,000, and 2026-03-16 institutional deadline. | `SRC-GMAIL-09` |
| 2026-05-11 | Renewal review and bonus-application notice | Institute forwarded renewal review / annual evaluation and MOE bonus application. Student upload deadline is 2026-05-20. Department/college review committee name reply deadline is 2026-05-15 for units. | `SRC-LOCAL-07`, `SRC-GMAIL-10` |
| 2026-05-13 | Guan-Ting LINE routing clarification | Guan-Ting confirmed the procedure should start early: after Prof. Wu finishes comments/signature, students still need to bring the paper `定期評量報告表` for department/institute office signature or seal routing; paper delivery to the college office is due by 2026-05-20 before leaving work. Jason said this should be handled today, will go to the lab tomorrow, and proposed going together; Guan-Ting agreed. | User-provided LINE screenshot/transcript |
| 2026-05-13 04:43-08:26 | Prof. Wu LINE advisor-routing completion | Jason sent Prof. Wu a concise review/signature request and attached the renewal application form PDF plus supporting-review report PDF. Prof. Wu replied at 06:03 that he would sign later, returned the signed renewal application form PDF at 08:12, Jason thanked him at 08:25, and Prof. Wu replied with a sticker at 08:26. Tracked record keeps only routing status; raw PDFs and LINE evidence remain local-only. | User-provided LINE transcript |
| 2026-05-14 16:10 | Institute-office phone update | Jason recorded that the uploaded renewal materials must include the institute director's seal / `所長蓋章`, and that the labor-insurance record must be from after 2026-05-18. At `16:11`, Jason pulled the paper packet back for scanning / rework. | User-provided note; raw scan/evidence stays local-only |

## Application Packet

The 69-page application packet contains:

- Application form.
- Labor-insurance query record.
- Full-time doctoral scholarship pledge.
- 114 academic-year semester-1 enrollment certificate.
- Eligibility and achievement evidence.
- Doctoral research plan.
- Additional review-supporting materials.

Application-form summary:

- Scholarship preference on the form: NSTC doctoral research scholarship as first preference, MOE doctoral scholarship as second preference; final award notice lists Jason under MOE scholarship.
- College/department: College of Biomedical Science and Engineering / Institute of Biophotonics.
- Doctoral status at application: first-year doctoral student, ROC nationality, direct-PhD route marked.
- Eligibility condition selected: important academic journal or conference publications, with two first/co-first-author works listed.
- Labor-insurance query period: 2025-09-01 to 2025-10-13; downloaded after 2025-10-13; result shown as no records found.
- Declarations: no full-time job, no duplicate government scholarship of the same nature, truthful materials, and agreement to follow academic-performance and career-flow tracking obligations.

Sensitive fields redacted from this tracked record:

- National ID, birthdate, home address, phone number, full email routing metadata, signature images, payment-account document copy, labor-insurance raw display, recommendation-letter images, and transcript/certificate images.

## Doctoral Research Plan

Research-plan title:

- Chinese: `JANUS：一個整合檢索增強生成與蒸餾強化裝置上 AI 之跨領域敘事理解框架`
- English: `JANUS: Toward a Cross-Domain Framework for Narrative Understanding via Retrieval-Augmented Generation and Distillation-Enhanced On-Device AI`

Core problem:

- Voice services in fraud detection, medical triage, customer service, and legal contexts generate noisy, unstructured narratives.
- Manual transcription and summarization are slow, inconsistent, and risky when information is incomplete or domain-specific.

Proposed framework:

- ASR for Taiwanese Mandarin and Mandarin-English code switching.
- LLM reasoning for classification, slot filling, missing-information detection, and structured summaries.
- RAG for grounding, knowledge updates, hallucination reduction, and external knowledge integration.
- Knowledge distillation, quantization, and edge deployment for privacy, low latency, and security.

Prior foundation used in the application:

- CIB 165 fraud-method classification using 12,031 summaries and 37 categories; reported approximately 84.13% accuracy and 0.84 macro-F1 in the supporting materials.
- RaaS / Medusa / CrazyHunter analysis and ZTAID-based defense thinking.
- Threat Pulse Modeling integrated with ZTAID zero-trust maturity assessment.

Expected deliverables in the plan:

- Domain-specific ASR model targeting WER below 10%.
- Structured case-summarization LLM targeting at least 90% call-type classification accuracy and F1 at least 0.8 for key-field extraction.
- RAG validation with reduced hallucinations and 5-10 point F1 gain on externally grounded slot filling.
- Lightweight on-device model retaining at least 95% of teacher-model performance with near-real-time inference.
- Cross-domain transfer blueprint for anti-fraud, medical triage, customer support, and legal deposition style workflows.

## Supporting Evidence Included In The Packet

Academic and technical materials:

- `A Deep Learning Approach to Classifying Fraud Methods Using CIB Crime Datasets`
  - 12,031 fraud-case summaries.
  - 37 fraud-method categories.
  - Chinese RoBERTa-wwm full fine-tuning.
  - Reported 84.13% accuracy and 0.84 macro-F1.
  - Back-translation and class-weight strategies for long-tail fraud types.
  - Deployment comparison including DistilBERT and TextCNN.
- `Real-Time Offline ASR Optimization for Anti-Fraud Conversational AI Using Breeze ASR-25`
  - Offline real-time ASR workflow.
  - WebSocket audio streaming, VAD, GPU inference, and local privacy-preserving operation.
  - Breeze ASR-25 for Taiwan Mandarin / code-switching; supporting material states up to 56% lower recognition error than Whisper in code-switched speech.
- CISC 2025 paper 1:
  - `AI 時代下 Ransomware-as-a-Service 之演進與防禦挑戰：以 Medusa 及 CrazyHunter 為例之技術與對策分析`
  - First-author conference paper.
  - Frames RaaS evolution, BYOVD, LOTL, Medusa, CrazyHunter, healthcare/education/manufacturing impact, ZTAID, MSSP/CERT collaboration, and future ZTAID maturity research.
- CISC 2025 paper 2:
  - `威脅脈動建模(Threat Pulse Modeling)對接於 ZTAID 零信任成熟度評估模型之整合分析`
  - First-author conference paper.
  - Proposes TPM as a dynamic CTI-to-zero-trust maturity feedback framework with pulse coverage and detection-feedback loop time.

Professional achievements:

- Major fraud investigation involving high-value gold bar handoff.
- Major cross-border drug smuggling investigation.
- Long-term fugitive / drug-distribution case.
- Major violence-group investigation.

International and language evidence:

- Selected to represent Taiwan in New Jersey State Police advanced homicide investigation training at Princeton University in 2017.
- Selected to represent Taiwan in France CRS high-level crowd-management training in 2017.
- TOEIC total 800; speaking 150; writing 180.

## Email And Attachment Content Matrix

| Source | Email / Attachment | Content Captured |
| --- | --- | --- |
| 2025-10 initial announcement | School/college/institute emails | System unavailable; manual route; deadlines; required documents; selection/review workflow; payment schedule; matching-fund rules; eligibility restrictions; renewal mechanism. |
| Initial official attachments | Guidelines, application notes, student-data forms, application form, matching-fund consent, pledge, labor-insurance SOP | Attachment names and purposes captured from Gmail. The initial application-notes PDF was parsed: it confirms the 2025-10-03 to 2025-10-19 application window, college/department review schedule, 2025-12 award notice target, 4 萬/month scholarship amount, MOE matching-fund split, annual renewal requirement, and 115 renewal priority for 114 awardees. Raw binaries were not all archived locally. |
| 2025-10-14 submitted application PDF | Jason's full packet | Full extracted text archived. Tracked summary above covers form, declarations, labor-insurance query, research plan, and supporting materials. |
| 2025-10-14 receipt reply | College reply | College received the PDF and required paper pages 1-3 to go through institute-office seal and college office routing. |
| 2025-11-07 student-data spreadsheet | College request and Jason reply | Requested student data spreadsheet plus payment-account supporting material on worksheet 2; Jason returned filled spreadsheet; college confirmed receipt. |
| 2025-11-13 second-batch notice | OAA / institute forwarded context | Eligibility, award amount, matching-fund breakdown, renewal mechanism, application method, selection criteria, deadline 2025-11-26. |
| 2025-11-20 distribution form | Institute reminders | Google Form by 2025-11-21 17:00; payment-account info needed because scholarships would be distributed in one batch. |
| 2025-12-22 award list notice | College award-list notice | Jason listed as MOE scholarship awardee; period 2025-09-01 to 2026-08-31; 2025-09 to 2025-12 roster processed; matching-fund obligation emphasized. |
| 2026-03-05 matching-fund statement | Institute/OAA matching-fund notice | 114-1 period 2025-09-01 to 2026-02-28; monthly NT$10,000 matching fund; total NT$60,000 for the semester; signatures and accounting-route requirements; next semester expected around 2026-09. |
| 2026-05-11 renewal notice | Institute/college renewal review email | Upload by 2026-05-20: renewal application/evaluation form, supporting PDF, labor-insurance record. Bonus review is merged with renewal review. |
| May attachment 1 | NSTC excellent doctoral student scholarship pilot guideline | Older NSTC excellent-doctoral-student basis: supports research-potential students, annual evaluation before renewal, maximum original award structure for 108-112 style cohorts, conflict/eligibility restrictions, and post-award tracking obligations. |
| May attachment 2 | NSTC doctoral research scholarship pilot plan | Current NSTC doctoral research scholarship basis: 4 萬/month, generally doctoral years 1-3, no full-time paid work, no duplicate government scholarship, annual learning/research/international-activity report before renewal, and no replacement for NSTC selection awardees. |
| May attachment 3 | MOE doctoral scholarship implementation points | MOE basis: ROC-national non-employed PhD year 1-3 students, 4 萬/month split as 2 萬 MOE + 1 萬 school + 1 萬 college/department/advisor side, annual evaluation, matching-fund/TA/RA offset rule, and bonus paths including top journal publication. |
| May attachment 4 | NYCU doctoral scholarship guideline updated 2026-04-20 | Updated integrated school rule: combines NSTC and MOE scholarship categories, confirms no full-time paid work, no duplicate same-nature scholarship, maximum 3 years/6 semesters, MOE limit through doctoral year 3, annual evaluation, replacement mechanism, and added MOE bonus categories plus possible penalty for incomplete data or unpaid matching fund. |
| May attachment 5 | MOE bonus-award journal list | Lists top journals including Nature/Science/Cell and IF > 40 journals; bonus note says first-author publication during award period may be reviewed for up to NT$240,000, one student per paper, with publication or acceptance proof. |
| May attachment 6 | Labor-insurance record SOP | Explains why the labor-insurance record is required and gives three routes: online mobile-phone authentication, online natural-person certificate, or in-person Labor Insurance Bureau application. The tracked record keeps only the process summary; the SOP itself contains identity-field examples. |
| May attachment 7 | Replacement student data example xlsx | Example spreadsheet for replacement-student routing. Required fields include scholarship type/year/category, college/department, year, direct-PhD flag, student identifiers, payment-account field, nationality, gender, prior school, registration date, contact fields, address, and advisor name; second worksheet is for payment-account evidence. |
| May attachment 8 | Renewal review process and notes | Annual renewal flow: student report, advisor/department/college review, OAA compilation, school-level review, NSTC/MOE claim/disbursement; max 3 years/6 semesters; MOE scholarship limited to doctoral year 3. |
| May attachment 9 | Regular evaluation report form PDF/DOCX | Student basic info; award category/year; renewal yes/no/period-ended choice; declarations; advisor questions and 0-100 recommendation scale; advisor/department/college consent; required report sections: labor-insurance record, grades, doctoral research reflection, academic results, industry collaboration, international activities. |

## Active Renewal Packet Checklist

Official deadline: 2026-05-20 before the Google Form deadline in the May 11 email; paper `定期評量報告表` also needs delivery to the college office before leaving work that day.
Internal deadline: 2026-05-13 for packet preparation and Prof. Wu scheduling message; 2026-05-15 remains the latest ready-to-route fallback before the weekend, except the final labor-insurance refresh that must happen after 2026-05-18.

- [ ] Confirm whether Jason will apply for 115 academic-year renewal.
- [x] Locate the actual May renewal email attachments / evaluation form from Gmail, Downloads, or the correct private archive.
- [x] Fill known student-side fields in a local copy of the regular evaluation report form.
- [x] Draft the supporting report body and prepare one supporting PDF assembly plan in the order requested:
  - labor-insurance record with correct query/download period; after the 2026-05-14 office call, the final record must be refreshed after 2026-05-18,
  - annual learning grades / transcript evidence,
  - doctoral research reflection,
  - academic research results,
  - works/output evidence,
  - industry collaboration execution status, if any,
  - international activity participation report/evidence, if any.
- [x] Download and file the initial working labor-insurance record.
- [ ] After 2026-05-18, refresh the labor-insurance record for final Google Form upload.
- [ ] Download current transcript/grade evidence.
- [ ] Merge final supporting PDF after the private evidence files exist.
- [x] Route evaluation report to advisor for comments, recommendation score, renewal consent, and signature.
  - Sent to Prof. Wu on LINE at 2026-05-13 04:43 with the renewal application form PDF and supporting-review report PDF.
  - Prof. Wu returned the signed renewal application form PDF at 2026-05-13 08:12.
- [>] Route to department/program meeting or responsible unit for consent/signature and institute director seal / `所長蓋章`.
  - Office-call update at 2026-05-14 16:10: final upload packet must include the seal, and Jason pulled the paper packet back at 16:11 for scanning / rework.
- [ ] Route to college for consent/signature if required before upload.
- [x] Message Prof. Wu on 2026-05-13 to ask for review/signature.
  - Manual LINE send completed at 04:43.
- [>] Coordinate with Guan-Ting about paper routing / going to the office together.
  - Next action is lab printout plus institute-office director signature/seal routing on 2026-05-14.
- [ ] Check whether MOE bonus application applies.
  - Current evidence in this record shows first-author conference/research outputs, but the bonus attachment targets Nature, Science, Cell, or equivalent/top IF journals during the scholarship period. Treat bonus eligibility as unconfirmed unless publication evidence matches that rule.
- [ ] Upload to the Google Form by 2026-05-20.
- [ ] Save receipt/status evidence back to the local archive and add a short planning note.

## Internal Plan To Friday

Target by Friday `2026-05-15`: the renewal packet should be ready for advisor / department / college signature routing, or any blocker should be explicit enough to ask the office/advisor immediately.

| Date | Target State | Minimum Output |
| --- | --- | --- |
| 2026-05-12 Tue | Scope and evidence map locked | Decide renewal intent, list required form fields, list supporting evidence already available, and identify missing evidence. |
| 2026-05-13 Wed | Draft packet body | Draft the regular evaluation report content and outline the single supporting PDF in the required order. |
| 2026-05-14 Thu | Evidence bundle assembled | Add transcript/grade evidence, research-output evidence, works/output evidence, international activity evidence if applicable, and check bonus eligibility. |
| 2026-05-15 Fri | Ready-to-route packet | Produce a ready-to-sign / ready-to-seal evaluation form plus supporting PDF checklist; prepare scan route and queue the post-`2026-05-18` labor-insurance refresh before the official `2026-05-20` upload deadline. |

## Operational Lessons

- Keep scholarship files split by lifecycle:
  - raw identity/payment/labor-insurance/application files: `system-hub/admin/inventory/applications/`;
  - searchable redacted summary: this repo;
  - daily/weekly capacity and deadline status: planning repo.
- For renewal, the bottleneck is not writing alone; it is signature routing and proof assembly.
- The next renewal packet should reuse the application packet's strongest evidence but update it into an annual-progress report, not resubmit the old application narrative unchanged.

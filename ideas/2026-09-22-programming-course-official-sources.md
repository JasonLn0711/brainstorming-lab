# 「程式設計與軟體系統架構概論」來源核對

查核日期：2026-09-22。使用者提供七個網址；另查Claude權限頁補足工具差異。以下是官方資料可支持的範圍，課程安排與教學效果仍是設計建議。[完整草案](2026-09-22-programming-software-systems-course-draft.md) · [canonical idea](raw/idea_000048_ai_software_literacy_for_working_professionals.yaml)。

| 引用 | 本次確認 | 證據界線 |
| --- | --- | --- |
| [1 NYCU招生頁](https://exam.nycu.edu.tw/mas-crime.html) | 正式名稱為「資訊學院科技犯罪偵查資通訊碩士在職專班」；宗旨包含完整系統性資通訊教育與研究／實務合作。 | 支持班名與定位，不支持多數學生無基礎的比例，也不代表新課已核定；頁中114年度招生日期未當作現在開課時間。 |
| [2 INCOSE](https://www.incose.org/about-systems-engineering/) | 系統工程採跨領域、整合觀點，關注組件關係及從構想到運作、退場的生命週期。 | 支持整體系統思考；不把一門入門課等同完整專業訓練。 |
| [3 Claude Code最佳實務](https://code.claude.com/docs/en/best-practices) | 提供可執行檢查、先探索／規劃再實作，並用CLAUDE.md保存專案脈絡與工作規則。 | 支持協作流程與文件機制，不保證學生理解或模型必然遵守。 |
| [4 Codex AGENTS.md](https://developers.openai.com/codex/guides/agents-md/) → [現行頁](https://learn.chatgpt.com/docs/agent-configuration/agents-md) | 專案可用AGENTS.md設定協作規則，具有不同位置的指示層次。 | 此來源只證明Codex機制；Claude的CLAUDE.md由第3項分別支持。 |
| [5 Codex核准與安全](https://learn.chatgpt.com/docs/agent-approvals-security) | 文件區分沙箱限制與動作核准，包含檔案／網路邊界。 | 指示文字不取代工具權限；本次未修改本機設定。 |
| [6 Claude資料使用](https://code.claude.com/docs/en/data-usage) | 官方說明本機執行仍透過網路與模型互動，包含提示與輸出。 | 不把本機安裝推成資料全程離線；不同帳戶／供應商政策另核，不在本草案概括承諾。 |
| [7 NIST CFTT](https://www.nist.gov/itl/csd/secure-systems-and-applications/computer-forensics-tool-testing-program-cftt) | 以工具規格、程序、標準、測試集與測試硬體發展鑑識工具測試方法。 | 支持工具能力需具體驗證的觀點，不代表教學作品通過NIST認證或可直接處理正式證據。 |
| [補充：Claude權限](https://code.claude.com/docs/en/permissions) | Claude有獨立的權限設定機制；最佳實務另連接沙箱及檔案／網路隔離。 | 不以Codex文件代替Claude規範；教學前依實際版本、環境與帳號核對。 |

## 原文主張、建議與尚缺證據

- Jason的「大多數沒有學過科技及資工知識」記為現場觀察，尚無問卷、名冊或能力診斷統計。
- 「我希望專班開課」是本人的倡議；3學分、18週、每週3節、三分之二實作、課後15–20分鐘與四次試教是所附草案建議，不是課方決定或本人接課承諾。
- 40／20／30／10評量合計100%；是否採用、及格與重測門檻由授課團隊確認。
- 100筆中95筆符合格式、5筆錯誤是教學資料設計例子，尚未建立資料集或觀察學生通過。
- 四次試教是下一個可討論的方案，目前未邀請學生、排日期、安排師資或執行。
- 本筆記保留課程倡議與完整設計，未把案例收件或官方文件閱讀計為學員讀碼、實作或Blog完成。


<a id="course-primm-variant-2026-09-22"></a>

## B候選新增來源與差異

[完整B方案](2026-09-22-programming-course-primm-variant.md)記錄新副標、PRIMM、Python／JavaScript擇一與20／20／40／20評量。2026-09-22查核：

- [PRIMM／Raspberry Pi Foundation](https://www.raspberrypi.org/blog/primm-talk-in-programming-lessons-research-seminar/)：2020-11-13文章介紹Predict、Run、Investigate、Modify、Make與從讀碼開始的設計；是此教法的來源，不是本專班成效證明。
- [Python Tutorial](https://docs.python.org/3/tutorial/index.html)：官方列腳本與快速開發用途，明示教程預期已有一般程式理解；零基礎仍需教師設計教材。頁面版本標籤是本次讀取快照，不作長期固定版本承諾。
- [Codex最佳實務](https://developers.openai.com/codex/learn/best-practices)導向[現行頁](https://learn.chatgpt.com/guides/best-practices)，支持目標、背景、限制、完成條件，以及測試／diff檢查。Claude可執行驗證由前表第3項獨立支持。
- 原文其他引用：[INCOSE](https://www.incose.org/about-systems-engineering/)、[AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md)、[核准與安全](https://learn.chatgpt.com/docs/agent-approvals-security)、[Claude資料使用](https://code.claude.com/docs/en/data-usage)、[NIST SSDF](https://csrc.nist.gov/projects/ssdf)。同日先前已查核，不把來源支持延伸成課程採用或稽核通過。

B每週3小時／課後1–2小時不同於A的3節／15–20分鐘；個人無AI即時代答與有AI小修改也需分開定義。兩套評量各100%，尚未選案；此為所附素材差異，不是要求Jason新增工時。


<a id="foundations-before-models"></a>

## 基礎銜接與模型課程的先備

[完整心得、診斷與來源](2026-09-22-foundations-before-model-courses.md)補充「小工具→資料分析／統計→按需求進入模型」路徑；新增查核Stanford CS229與Harvard CS50P。AI素養可提早教；課前實作診斷與分流、正式學分課或基礎實作時段均為待議方案，A／B條件保留。

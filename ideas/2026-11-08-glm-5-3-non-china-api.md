# GLM-5.3 修改版 API：非中國供應與資料流驗證

日期：2026-11-08（Asia/Taipei）。[canonical YAML](raw/idea_000051_glm_5_3_non_china_api_and_data_residency_verification.yaml)，ID `idea_000051`，raw，0/100（未評分）。

Jason 提供完整問答並要求詳實保存與跨文件連結；本紀錄保留原提問、供應比較、技術範例、建議與待決條件，另列本次公開頁面查核。用途是未來 API 選型與研究評估，尚未採購、接入 OpenCode、發送供應商詢問或執行付費測試。稀缺資源為可信證據、資料治理與評估時間；詳細思考由 brainstorming 持有，Planning 保存下一關與容量。

## 原始問題與供稿內容

> GLM-5.3 uncensored 版本，是否可以在非中國的地區找到 api 呢？

供稿回答將「uncursor」理解為 Uncensored，主張已有中國以外可購買／呼叫的第三方 API，包括美國公司；同時明確區分「可取得服務」與「所有推論及資料處理均不進中國」。後者仍須確認 GPU 所在地與上游轉送政策。原文討論完整 GLM-5.3，並非 Flash。

以下價格完整保留供稿數字，單位為 USD／百萬 tokens；查核欄為本次新增，公開標價不構成實際帳單或呼叫成功證據。

| 供應商與來源 | 版本 | 輸入／輸出 | 2026-11-08 公開頁面核對 |
| --- | --- | --- | --- |
| [Refuseless](https://refuseless.com/) | GLM-5.3 Abliterated | 1.00／2.00 | 頁面模型與價格相符，宣稱相容 API |
| [Arnict](https://arnict.com/models/glm-5.3-abliterated) | GLM-5.3 Abliterated | 1.25／2.25 | 頁面標 Available；API ID 實為 `zai/glm-5.3-uncensored` |
| [Unlid](https://unlid.ai/models/glm-5.3-abliterated) | GLM-5.3 Abliterated | 1.22／2.44 | 價格相符；頁面稱與 uncensored 為不同 checkpoint |
| [Unlid](https://unlid.ai/models/glm-5.3-uncensored) | GLM-5.3 Uncensored | 1.52／2.75 | 價格相符；weights 尚未指定 |
| [Open Uncensored](https://openuncensored.com/models/glm-5.3-uncensored) | GLM-5.3 Uncensored | 1.25／2.25 | 公開上游是 NanoGPT，狀態 degraded；屬路由服務 |

原文另稱 NanoGPT 有完整 Uncensored 的美國／歐洲路由，但獨立頁標 Unavailable，故不優先。此次嘗試讀取 [NanoGPT 模型頁](https://nano-gpt.com/models/glm-5.3-uncensored)未成功，不能把讀取失敗解讀為 API 不可用，也未獨立確認原文路由地區或 Unavailable 狀態。

原建議順序為先 Refuseless、再 Arnict，品質比較可加 Unlid。這是供稿中的候選順序，尚無同任務實測支撐排名。原文稱 Refuseless 為 Wyoming 美國公司；本次未完成公司登記及控制權查核，因此保留為待查主張。Arnict 頁尾刊載 Wilmington, Delaware 地址，僅屬網站自述，不能證明最終控制權或 GPU 地區。

## 本次查核帶來的修正

1. **資料流需涵蓋備援。** [Refuseless 隱私政策](https://refuseless.com/privacy)（頁面更新日 2026-10-24）允許轉送第三方；其自有端宣稱不存提示詞／輸出，但不保證所有上游均零保留。移除帳號資訊也不能消除提示詞內的識別資訊。政策未在本次讀到的內容中提供完整 GPU 地區保證。
2. **模型名稱需對應實際 ID。** Arnict 的 Abliterated 頁面使用 `zai/glm-5.3-uncensored`；不能直接照抄其他供應商 ID。Unlid 的兩個名稱明確對應不同 checkpoint，公開權重連結仍欠缺。後續需記錄版本、量化、revision／hash（若提供）及上游。
3. **供應數量不等於獨立後端數量。** Open Uncensored 頁面顯示 NanoGPT 上游及 fallback 行為，可能與直接使用 NanoGPT 共享故障域。不要把兩者視為已證實獨立冗餘。
4. **基礎模型成績不等於修改版成績。** Refuseless 頁面明說其列示的是 base model 公布分數。修改後的推理、工具呼叫與資安分析品質需另測。

以上為公開供應商陳述的查核，未驗證實際後端、台灣網路可達性、付款資格、合約或服務品質；來源可能更新。

## 名詞與能力邊界

供稿以 Uncensored 泛指降低拒答／內容限制的修改版，可能透過微調或其他權重修改；Abliterated 通常指權重層級削弱拒答傾向。兩個標籤不是可互換的版本識別。原版指原始模型權重與服務商適用政策；修改版不能因名稱相近就視為 Z.ai 官方 uncensored 發行。此次未查核官方發行清單，官方身分仍需來源確認。

拒答減少與正確性、工具參數遵循、任務收斂及資安分析能力分別評估。使用場景限合法授權研究、良性程式任務與防護評估；本紀錄不保存攻擊最佳化提示或繞過操作。

## 接入範例（供稿整理，未執行）

原文 Python 換行黏連，以下僅修復格式。Base URL `https://api.refuseless.com/v1`、model ID `glm-5.3-abliterated` 與公開頁面一致；使用者尚未提供付費金鑰，未安裝 SDK 或發出請求。

```python
import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.refuseless.com/v1",
    api_key=os.environ["REFUSELESS_API_KEY"],
)
response = client.chat.completions.create(
    model="glm-5.3-abliterated",
    messages=[{"role": "user", "content": "請介紹 Linux Kernel"}],
)
print(response.choices[0].message.content)
```

API 相容性範例不是 OpenCode／Coding Agent 已接入證據。正式試用時需另外核對 SDK 版本、streaming、工具 schema、錯誤碼、usage 與模型版本。

## 三層需求與下一個決策

| 條件 | 原文建議／後續驗證 |
| --- | --- |
| 台灣可購買、正常呼叫 | Refuseless 作候選；以實際帳號資格及良性請求回應驗證 |
| GPU 位於中國以外、資料不回中國 | 確認入口、推論、日誌、備份、客服存取、上游與 fallback 地區；供應商須提供可核對證據 |
| 供應商公司及控制權也須非中國 | 另查登記、最終控制權與處理商清單；不能從網址／地址推定 |
| 敏感研究或個資 | 評估可驗證地區的專用部署或自架；另核硬體、權重、維運成本與資料責任 |

三項「非中國」需求可累加，尚未由 Jason 選定，不預設最低條件即可滿足。下次真正啟動選型時，由 Jason 決定必選條件，評估者取得供應商證據；未滿足必要條件即排除，不以低價補償資料地域要求。

最小壓力測試：台灣 coding agent 對公開 toy repo 工作，主路由失效而轉 fallback。先用文件核對是否能鎖定地區；若無法證實，停止該候選。通過且啟動試用後，以同一組五個良性任務比較原版／修改版，記錄任務完成、工具 schema 正確率、首次 token 延遲、重試與每成功任務成本。拒答較少但錯誤或重試增加時，修正品質假設；不要直接升格執行就緒。

## 相關內容與回流路徑

| 連結 | 實質關係與後續回流 |
| --- | --- |
| [AI 工程工作站](2026-05-09-gpu-first-terminal-ai-workbench.md)／`idea_000020` | 外部模型接入會擴大工作站資料出口；沿用 session ledger 與金鑰邊界 |
| [長程代理評估](structured/idea_000027_long_horizon_agent_behavior_evaluation_for_codex_cli_orchestrati.yaml) | 用完成證據、收斂與成本比較模型，避免只看非拒答率 |
| [共享 GPU 模型服務](structured/idea_000043_shared_gpu_model_owner_inference_service.yaml) | 自架／專用部署替代方案；不推定現有單卡能承載完整 GLM-5.3 |
| [跨語言安全盲點](classical-chinese-jailbreak-cross-lingual-safety-blind-spot.md) | 修改版可作受控防護評估的比較條件；區分語言效應與權重改動 |
| [11/8 日誌](../../planning-everything-track/weeks/2026-W45/days/2026-11-08.md#glm-api-2026-11-08) | 保存本次記錄完成與待決條件 |
| [W45](../../planning-everything-track/weeks/2026-W45/weekly-plan.md#glm-api-2026-11-08)／[W46](../../planning-everything-track/weeks/2026-W46/weekly-plan.md#glm-api-2026-11-08) | 本週成果與下週條件式候選，不增加固定工作 |
| [Planning brainstorm bridge](../../planning-everything-track/docs/15-brainstorming-repo-bridge.md#glm-api-2026-11-08) | 長期檢索入口；詳細價格與證據只維護本檔 |

目前沒有部署專案或採購承諾。供稿中的 favicon、追蹤參數、複製按鈕與 citation 聚合標籤屬介面殘留，整理時移除；以上為語義保存及查核增補，不宣稱逐字轉錄。

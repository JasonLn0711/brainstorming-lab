# 七步教學：從一個物件到研究群島

返回[閱讀入口](README.md)。這份教材解釋原理與下一個練習；本輪未替使用者完成練習，也未啟動新的固定學習 lane。範例的預期畫面與實測分開記錄。

## 先認識六個名詞

| 名詞 | 白話說明 | 在這個網站裡 |
| --- | --- | --- |
| Scene | 放置物件的三維世界 | 岩島、建築、燈光都在裡面 |
| Camera | 決定從哪裡、用什麼角度看 | 全景與選島後的鏡頭 |
| Geometry | 物件頂點與表面的形狀 | 方塊、圓錐、岩島 |
| Material | 表面如何回應顏色與光 | 石頭、樹葉、窗戶 |
| Mesh | 形狀加材質，放到世界裡 | 一個可繪製零件 |
| Renderer | 把世界與相機轉成畫面 | WebGL canvas |

資料與畫面之間還有 ID：一棟樓知道自己代表哪個作品，才能在被點擊時顯示正確內容。框架、模型外觀與文章資料是不同層次。

## 步驟一：先讓一個方塊有前後與光影

**目的：**理解相機、物件與燈光的關係。用一個方塊、一種受光材質、一個方向光與相機，不先做城市。

輸入是尺寸、位置與光線；預期看到一個具有明暗面的方塊。把相機從正前方改到斜上方，形狀不變但可見面改變。把方塊縮放，改變的是物體尺寸；把相機拉遠，改變的是觀看距離。

檢查：能指出是哪一行改形狀、哪一行改顏色、哪一行改觀看位置。畫面全黑時先查光源與材質；全空時先查相機方向、near／far 與 canvas 尺寸。原站對照：`app.js` 建立 renderer、camera 與 controls；官方參考：[Fundamentals](https://threejs.org/manual/pages/fundamentals.html)。

## 步驟二：用同一組零件做島與地標

**目的：**理解組合與局部座標。島頂用扁圓柱或自訂輪廓，島底用逐層縮小的岩塊，塔樓用方塊加圓錐；全部放在同一 Group。

輸入是各零件相對位置；輸出是一個可以整體移動的島。先只平移 parent，確認塔樓和名牌錨點一起移動。旋轉與縮放加入後，局部座標不能只用加法轉世界座標，須透過世界矩陣或 Three.js 的座標轉換。

檢查：移動島時，不會只動岩體而留下浮空建築；相同配方可放到第二組位置。原站對照：`kit.part()`、`sceneSpecs`；我們的改造採 per-island Group。常見錯誤是把世界座標寫進 child 後又加 parent 位移，造成位移兩次。

## 步驟三：旋轉和點擊如何共存

**目的：**知道拖曳是操作相機，點擊是選取物件。先加 OrbitControls，再記錄 pointer 起終點，最後才加 Raycaster。

螢幕座標必須以 canvas 自己的矩形為基準。下面是自行撰寫的教學範例，只示範座標換算，並非原站程式複製：

```javascript
function pointerToNdc(clientX, clientY, rect) {
  if (rect.width <= 0 || rect.height <= 0) throw new Error('Canvas has no area');
  return [
    2 * (clientX - rect.left) / rect.width - 1,
    1 - 2 * (clientY - rect.top) / rect.height
  ];
}
const rect = { left: 100, top: 50, width: 400, height: 200 };
if (JSON.stringify(pointerToNdc(300, 150, rect)) !== '[0,0]') throw new Error('center');
if (JSON.stringify(pointerToNdc(100, 50, rect)) !== '[-1,1]') throw new Error('top-left');
if (JSON.stringify(pointerToNdc(500, 250, rect)) !== '[1,-1]') throw new Error('bottom-right');
let rejected = false;
try { pointerToNdc(0, 0, { left: 0, top: 0, width: 0, height: 1 }); }
catch { rejected = true; }
if (!rejected) throw new Error('zero-size must fail');
```

檢查：canvas 不在視窗左上角時仍可正確點選；拖曳結束不打開文章；縮放後點同一地標仍得到同一 ID。原站對照：`app.js` L1435–1474。本例數學檢查的執行情況記在[查核紀錄](07-validation-and-next-gates.md)，不代表 Raycaster 已在自有網站執行。

## 步驟四：三筆內容，同時驅動模型與清單

**目的：**把「好看」連回「看得懂」。先用三筆明確標為示範的內容，或已審核公開作品，不使用私人材料。

每筆有固定 ID、標題、摘要與全文入口；模型只保存對應 ID。清單按鈕和模型點擊都呼叫同一選取函式，卡片透過 Map 讀內容。更改標題時模型不用改名，文章入口也不因排序改變。

檢查：清單和 canvas 選相同 ID 顯示相同內容；未知 ID 有可恢復狀態；無搜尋結果能清除搜尋。原站對照：ID Maps、`selectBuilding()`、`renderTree()`。我們的網站沿用已有文章，不建立第二份成果資料庫。

## 步驟五：用一條航線說明關係

**目的：**讓關係線傳遞可說清楚的意義。先連兩座島的兩個內容項目，寫出「為什麼相連」，再加入曲線。

四個控制點決定三維 cubic Bézier 的形狀。端點取自島上 anchor 的世界位置，中間兩點向上抬高。若每幀浮動，曲線端點也要更新；如果要讓光點等速走，依曲線弧長取樣，而非假設參數 t 等速就是空間等速。

檢查：線不穿過主建築；島移動時端點沒有脫離；停用動態仍看得到關係說明。原站的共享步行 route 是另一種解法；先理解它的語意一致性，再換成適合懸浮空間的幾何。

## 步驟六：手機、文字備援與停止動畫

**目的：**在不同裝置上仍能找資料。先讓文字版完整，再讓場景成為探索方式。

實作一個手機底部面板，清單與詳情互斥。縮窄視窗時相機重新 fit；文字不能只存在 canvas。暫停與 `prefers-reduced-motion` 讓島、光點與鏡頭轉場停止，使用者仍可選取並閱讀。

檢查：390px 寬度能找內容、開全文與回來；鍵盤能完成相同任務；載入 Three.js 失敗時仍有列表。瀏覽器視窗模擬只驗版面，真實手機還要測觸控、GPU、記憶體與 Safari 行為。原站對照：手機 CSS、`setMobPanel()`、`flyTo()` 的 reduced-motion 分支。

## 步驟七：擴到六島前，先理解成本

**目的：**知道瓶頸在哪一層。先記錄三島的可見標籤、draw calls、三角形、資產大小與 frame time，再增加島嶼。

如果很多重複樹木增加繪圖呼叫，可以用 InstancedMesh；如果 GPU 填色太重，先減少透明層與 DPR；如果 CPU 忙在文字邊界量測，就先減少同時出現的名牌。這三種問題需要不同修正。

檢查：離開群島 route 後 RAF、監聽器與 GPU 資源會清理；重進不多出 canvas；十次進出沒有資源數量持續攀升。不能用「畫面出現」代替可靠性驗收。

## 如何保存自己的學習結果

每次只記：這次改了什麼、觀察到什麼、用哪個輸出確認、哪裡還不懂。截圖可證明一個畫面，測試可證明宣告的行為，自己解釋資料流才是概念理解的證據。

本次文件是教學材料，不是已完成學習紀錄。若之後啟動互動教學，依當時採納的 learning lane 與 `professor-learning-prompt` 進行，原題與重測分開記錄；本包不預先填寫分數或完成狀態。

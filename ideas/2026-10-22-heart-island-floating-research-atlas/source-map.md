# 公開程式定位表

返回[閱讀入口](README.md)。行號與雜湊對應本次 [manifest](source-manifest.json)；原站更新後須重新核對。完整副本為本機忽略檔，外部連結仍可開啟現行版本。

## 資源清冊

| 資源 | bytes | 行數 | SHA-256 前 12 碼 |
| --- | ---: | ---: | --- |
| [index.html](https://puma.taipei/heart-island) | 9765 | 37 | `16941eee9628` |
| [app.js](https://puma.taipei/heart-island-assets/app.js?v=20261022-3) | 112050 | 2177 | `0f45160cf0c7` |
| [ui.css](https://puma.taipei/heart-island-assets/ui.css?v=20261022-3) | 56250 | 1539 | `9f230eb2cdf6` |
| [policies.json](https://puma.taipei/heart-island-assets/policies.json?v=20261022-3) | 159069 | 6153 | `de4a6aa30671` |
| [kit.js](https://puma.taipei/heart-island-assets/kit.js?v=20261022-3) | 6362 | 133 | `5b06281db1fa` |
| [scene-models.js](https://puma.taipei/heart-island-assets/scene-models.js?v=20261022-3) | 32158 | 674 | `0d2a6b55397b` |
| [models-extra.js](https://puma.taipei/heart-island-assets/models-extra.js?v=20261022-3) | 38257 | 676 | `34150ebf0ee1` |
| [world.js](https://puma.taipei/heart-island-assets/world.js?v=20261022-3) | 26996 | 704 | `aed714971c1b` |
| [environment.js](https://puma.taipei/heart-island-assets/environment.js?v=20261022-3) | 25383 | 557 | `0917a46c1374` |
| [people.js](https://puma.taipei/heart-island-assets/people.js?v=20261022-3) | 34092 | 749 | `6d9a89368628` |
| [decor.js](https://puma.taipei/heart-island-assets/decor.js?v=20261022-3) | 72982 | 1431 | `0be29f34602b` |
| [decor-items.js](https://puma.taipei/heart-island-assets/decor-items.js?v=20261022-3) | 12351 | 104 | `7e26015c7bcf` |
| [icons.js](https://puma.taipei/heart-island-assets/icons.js?v=20261022-3) | 2092 | 22 | `656609c027a1` |
| [three.module.js](https://puma.taipei/heart-island-assets/vendor/three/build/three.module.js) | 1272972 | 53044 | `76dea8151bc9` |
| [kairos-index.html](https://learn.cs-kairos.com/) | 3100 | 1 | `1f0b4144e487` |
| [kairos-style.css](https://learn.cs-kairos.com/style.css) | 8394 | 6 | `09f6fd0a960e` |

## 函式定位

此表以宣告位置提供閱讀入口；箭頭函式與物件方法不一定列在表中，不能用表的筆數代表所有 runtime 行為。

### app.js

| 行 | 宣告／方法 |
| ---: | --- |
| 99 | `function tree(x, z, size = 0.55, owner = null) {` |
| 110 | `function roof(x, y, z, w, d, owner) {` |
| 115 | `function house(x, z, w, h, owner, color = 0xf4ebdd) {` |
| 126 | `function scaffold() {}` |
| 484 | `function setGhosts(v) {` |
| 511 | `function clipLabels() {` |
| 624 | `function zoomFactor() {` |
| 629 | `function updateWalkers() {` |
| 634 | `function resize() {` |
| 650 | `function overviewPosition() {` |
| 655 | `function overviewTarget() {` |
| 659 | `function flyTo(id = "all") {` |
| 734 | `function sourceLinks(ids) {` |
| 745 | `function cardShow(html) {` |
| 787 | `function updateHud() {` |
| 812 | `function setToggle(k, v) {` |
| 868 | `function pushLog(w, type) {` |
| 881 | `function renderOverview() {` |
| 911 | `function renderLog() {` |
| 921 | `function tickLog() {` |
| 935 | `function flowButtons(ids, from = null) {` |
| 947 | `function heartPills(list) {` |
| 954 | `function statTiles(facts) {` |
| 966 | `function highlight() {` |
| 1013 | `function showFlows(ids) {` |
| 1034 | `function showPins(islandId) {` |
| 1070 | `function syncSigns() {` |
| 1073 | `function hoverItem(id, on) {` |
| 1080 | `function selectIsland(id) {` |
| 1107 | `function stageChip(b) {` |
| 1114 | `function shortPhase(b) {` |
| 1117 | `function selectBuilding(id) {` |
| 1144 | `function portrait(w) {` |
| 1166 | `function thumbnail(id) {` |
| 1194 | `function stageSegs(b) {` |
| 1199 | `function timelineBar(b) {` |
| 1213 | `function tierLabel(t) {` |
| 1216 | `function nameOf(id) {` |
| 1219 | `function quoteHTML(q) {` |
| 1222 | `function selectFlow(id) {` |
| 1241 | `function renderTree() {` |
| 1298 | `function updateDay() {` |
| 1336 | `function setPanel(next) {` |
| 1353 | `function setTerm(index) {` |
| 1407 | `function clearWalker() {` |
| 1412 | `function home() {` |
| 1532 | `function showIntro() {` |
| 1542 | `function closeIntro() {` |
| 1561 | `function startTour() {` |
| 1581 | `function stopTour() {` |
| 1590 | `function toggleTour() {` |
| 1595 | `function updateTour(force = false) {` |
| 1638 | `function walkerScreenStats() {` |
| 1667 | `function selectWalker(index) {` |
| 1728 | `function pumaCard(w) {` |
| 1746 | `function walkerCard(w, f) {` |
| 1755 | `function roleGlyph(role) {` |
| 1936 | `function animate(now) {` |

### kit.js

| 行 | 宣告／方法 |
| ---: | --- |
| 4 | `export function createKit(THREE, top) {` |
| 48 | `function part(kind, pos, scale, color, owner = null, rotation = null) {` |
| 90 | `function countAll() {` |
| 95 | `k.build = function build(scene, mats) {` |

### scene-models.js

| 行 | 宣告／方法 |
| ---: | --- |
| 106 | `export function createPolicyModel({ part, top, colors, tree, house, scaffold }) {` |
| 107 | `return function build(id, x, z, scale = 0.78, opts = {}) {` |

### models-extra.js

| 行 | 宣告／方法 |
| ---: | --- |
| 3 | `export function extraModel(kind, h) {` |

### world.js

| 行 | 宣告／方法 |
| ---: | --- |
| 108 | `export function axialToWorld(THREE, q, r) {` |
| 112 | `export function dirOf(dq, dr) {` |
| 119 | `export function hexVertex(cx, cz, r, k) {` |
| 124 | `export function insideHex(x, z, ri) {` |
| 130 | `function makeTexture(THREE, type) {` |
| 244 | `function cliffGeometry(THREE, cx, cz, r, yTop, yBot, grassTone, seed, id) {` |
| 304 | `function hexRingGeometry(THREE, rOut, rIn) {` |
| 339 | `function bandTexture(THREE, id) {` |
| 426 | `export function buildIslands(THREE, scene, D, kit, colors) {` |
| 565 | `export function buildGraph(THREE, D, centers, neighbors) {` |
| 610 | `function shortest(a, b) {` |
| 636 | `function nodeNear(id, p) {` |
| 653 | `export function slotLayout(n, heroSize) {` |
| 686 | `export function resolveIslandPlacements(buildings, composition, heroId) {` |

### environment.js

| 行 | 宣告／方法 |
| ---: | --- |
| 23 | `export function createEnvironment(THREE, scene, { reduced, quality, cityCenter }) {` |
| 444 | `function lerpKey(min) {` |
| 463 | `env.setTime = (minutes) => {` |
| 498 | `env.cullClouds = (cam) => {` |
| 502 | `env.update = (dt, motion) => {` |
| 521 | `function smooth(a, b, x) {` |
| 525 | `function fbm(n, x, z, o) {` |
| 536 | `export function mulberry(a) {` |
| 544 | `function makeMistTexture(THREE) {` |

### people.js

| 行 | 宣告／方法 |
| ---: | --- |
| 46 | `export function createPeople(THREE, scene, opts) {` |
| 68 | `function plan(role, kind, opts2) {` |
| 280 | `function routeFor(from, to, salt) {` |
| 306 | `function nearestIsland(p) {` |
| 318 | `function sample(route, s) {` |
| 420 | `function badge(kind) {` |
| 471 | `function update(dt, time, motion, zoom = 1) {` |
| 627 | `function drawGlyph(g, kind) {` |

### decor.js

| 行 | 宣告／方法 |
| ---: | --- |
| 8 | `export function buildDecor(T, kit, D, centers, neighbors, footprints, colors, opts = {}) {` |
| 872 | `function canalFeature(kit, kind, x, z, yaw, rnd) {` |
| 923 | `export function seaCurve(P, k) {` |
| 933 | `export function bez(c, t) {` |
| 937 | `function boat(kit, x, z, yaw, W, rnd, sail = true) {` |
| 946 | `function reeds(kit, x, z, W, rnd) {` |
| 950 | `function egret(kit, x, z, W) {` |
| 956 | `function lily(kit, x, z, W, rnd) {` |
| 960 | `function buoy(kit, x, z, W) {` |

### decor-items.js

| 行 | 宣告／方法 |
| ---: | --- |

### icons.js

| 行 | 宣告／方法 |
| ---: | --- |
| 20 | `export function icon(id, cls = "") {` |


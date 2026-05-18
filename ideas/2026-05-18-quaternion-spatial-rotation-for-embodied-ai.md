# Quaternion spatial rotation for embodied AI

Canonical YAML: `ideas/structured/idea_000030_quaternion_spatial_rotation_representation_for_embodied_ai_syste.yaml`

## 核心想法

這張圖在講四元數，英文是 Quaternion。

它最重要的工程用途不是「很酷的 4D 數學」，而是：

> 用一種穩定的方式表示 3D 空間中的旋轉。

資工學生要抓住這件事：

```text
AI 只看文字或表格時，不一定需要 quaternion。
AI 一旦進入相機、機器人、無人機、AR/VR、3D world model，就會碰到姿態與旋轉。
```

所以四元數是 real-world AI systems 的數學地基之一。

## 它到底是什麼

四元數可以寫成：

```text
q = w + xi + yj + zk
```

它有四個 component：

- `w`：scalar part
- `x, y, z`：三個 imaginary direction 的係數
- `i, j, k`：三個虛數基底

核心關係是：

```text
i^2 = j^2 = k^2 = ijk = -1
```

這不是一般複數的 `i` 而已，而是多了 `j` 和 `k` 兩個方向。

工程上最常用的是 unit quaternion：

```text
||q|| = 1
```

因為 unit quaternion 可以穩定表示 3D rotation。

## 重要修正

四元數有四個數字，不代表物體真的跑到「第四個物理空間」。

更精準地說：

> 四元數用四個 component 來表示 3D 空間裡的旋轉狀態。

這跟 RGB 用三個數字表示顏色有點像。

你不會說顏色世界一定是三個物理世界；你會說 RGB 是一種 representation。

四元數也是 representation。

## 為什麼不用 Euler angle 就好

Euler angle 很直覺：

```text
roll
pitch
yaw
```

也就是飛機常講的：

- roll：左右翻滾
- pitch：抬頭低頭
- yaw：左右轉向

但 Euler angle 有幾個問題：

- rotation order 會影響結果
- 有些角度會讓軸重疊
- interpolation 不平滑
- optimization 時可能不連續

最有名的問題是：

```text
Gimbal Lock
```

中文常翻成萬向節鎖。

直觀來說，就是原本應該有三個獨立旋轉方向，但在某些姿態下，兩個軸重疊，系統等於少了一個自由度。

對遊戲角色可能是動作怪怪的。

對 drone 或 spacecraft，這可能是控制問題。

## 四元數怎麼表示旋轉

如果你想繞某個 unit axis：

```text
u = (ux, uy, uz)
```

旋轉角度是：

```text
theta
```

那 unit quaternion 可以寫成：

```text
q = cos(theta/2) + (ux i + uy j + uz k) sin(theta/2)
```

如果要旋轉一個 3D vector：

```text
v = (vx, vy, vz)
```

先把它放進 pure quaternion：

```text
v = 0 + vx i + vy j + vz k
```

再做：

```text
v_rotated = q v q^-1
```

這就是四元數在 3D rotation 裡很核心的操作。

## Real-world instances

### 1. Game engines

Unity、Unreal 這類 3D game engine 常常對使用者顯示 Euler angle，但內部會大量使用 quaternion。

原因是角色轉頭、攝影機旋轉、物件動畫都需要平滑且穩定。

### 2. Drone attitude control

Drone 需要知道自己現在姿態：

- roll
- pitch
- yaw
- body frame
- world frame

IMU 會提供 gyro / accelerometer 等訊號。

飛控系統要把這些訊號融合成穩定 orientation。

這時 quaternion 很常出現。

### 3. Spacecraft / satellite

太空船和衛星要控制姿態：

- antenna 指向哪裡
- solar panel 朝哪裡
- camera / sensor 看哪裡
- thrust direction 怎麼對準

這些都是 orientation problem。

### 4. Robotics

Robot arm 的 end-effector 不只要到某個位置，也要有正確方向。

例如夾爪要拿杯子，不只是 `(x, y, z)` 到了就好。

它還需要：

```text
position + orientation
```

orientation 就常用 quaternion 或 rotation matrix 表示。

### 5. AR / VR

VR 頭盔需要即時知道你的頭朝哪裡。

如果 orientation tracking 不平滑，人會很快感覺不舒服。

所以 AR/VR 對 rotation representation 很敏感。

### 6. SLAM / computer vision

SLAM 要估計：

- camera pose
- robot pose
- world map

camera pose 通常包含：

```text
rotation + translation
```

rotation 就可能用 quaternion 表示。

### 7. AI world model

如果未來 AI agent 要理解 3D 世界，它不只需要知道：

```text
這裡有一張椅子
```

還要知道：

```text
椅子在哪裡？
朝哪個方向？
相機從什麼角度看到它？
agent 自己的身體姿態是什麼？
下一步動作會怎麼改變世界狀態？
```

這些都會碰到 pose、frame、transform、orientation。

四元數就在這裡變成基礎工具。

## 資工系學生應該怎麼學

不要一開始就死背抽象代數。

比較好的順序：

1. 先理解 2D complex number rotation
2. 再理解 3D Euler angles
3. 親眼看一次 gimbal lock
4. 再學 unit quaternion
5. 實作一次 `q v q^-1`
6. 比較 Euler interpolation 和 quaternion SLERP
7. 接到一個實際系統：drone、robot arm、AR/VR、SLAM、game camera

## 最小測試

做一個不用 notebook 的 CLI fixture：

```text
input:
  - vector v = (1, 0, 0)
  - axis u = (0, 0, 1)
  - angle theta = 90 degrees

output:
  - Euler rotation result
  - quaternion rotation result
  - vector length before / after
  - coordinate frame convention
```

再加一個 near-gimbal-lock case：

```text
pitch ~= 90 degrees
```

看 Euler angle 會怎麼變得不穩定。

這會比只看影片更有用，因為你會真正看到：

```text
representation choice changes system behavior
```

## 一句話

四元數是 3D 世界裡表示旋轉的工程語言；AI 一旦進入 robot、drone、AR/VR、SLAM、simulation、world model，就不能只會 model，還要懂空間狀態怎麼被表示。

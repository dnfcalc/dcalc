# DNF计算器

## 介绍
为 DNF 装备搭配及伤害计算提供便利的免费工具

## 运行

### clone

git clone --recurse-submodules --single-branch --branch master https://gitee.com/dnftools/dcalc.git

### frontend

前置条件：node 18+

npm i -g pnpm

cd frontend

pnpm i

### backend

前置条件：python 3.10+

pip install uv

cd backend

uv sync

### scripts

pnpm run dev:image
pnpm run dev:frontend
pnpm run dev:backend

### process

- 装备选择
  - [x] 武器选择
  - [x] 套装选择
  - [x] 贴膜选择
  - [x] 通宝选择
  - [x] 称号宠物选择
  - [x] 秘宝选择

- 技能设置
  - [x] 技能等级设置
  - [x] 觉醒绑定选择
  - [x] 技能次数设置
  - [ ] 技能次数自动计算
  - [ ] buff数值设置

- 打造设置
  - [x] 增幅/强化/锻造
  - [x] 徽章/附魔/调适
  - [x] 时装/皮肤/光环
  - [x] 宠物装备
  - [x] 辟邪玉
  - [x] 勋章/杂项

- 结果计算
  - [x] 技能伤害计算
  - [x] 技能等级计算
  - [x] 技能CD计算
  - [x] 装备特效计算
  - [x] 装备效果/点数计算
  - [x] 角色基础展示

# 赞助

本项目 CDN 加速及安全防护由 Tencent EdgeOne 赞助

![主界面截图](https://edgeone.ai/media/34fe3a45-492d-4ea4-ae5d-ea1087ca7b4b.png)

[亚洲最佳CDN、边缘和安全解决方案 - Tencent EdgeOne](https://edgeone.ai/zh?from=github)
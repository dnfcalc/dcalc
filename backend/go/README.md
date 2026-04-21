# dcalc Go 重构骨架

这个目录是对现有 Python 后端的并行 Go 重构，不直接替换原服务。

当前已迁移：

- 通用响应结构与 HTTP 入口
- CORS、压缩、中间件基础设施
- 冒险团职业列表与 token 生成
- openapi 静态数据读取接口
- 基于 alter_token 的技能详情接口
- colg 金价查询接口
- /api/character 静态职业与装备目录信息
- /api/skillTree/ 编码解码逻辑（Go 实现）
- Python 适配层（职业工厂依赖收口）

兼容性说明：

- jobInfo 接口保持与 Python 一致，返回目录名风格的 jobId 和 jobGrowId
- skills 和 skillDetail 路由同时兼容目录名参数与 Neople UUID 参数

当前未迁移：

- 角色构建与伤害计算公式本体
- DNFHelper 集成
- MCP 服务

当前架构：

- skillTree 的 base64/zlib/binary 解码已经迁移到 Go
- createCharacter 依赖通过 go/python_bridge.py 适配层收口
- calc 域已拆出 CharacterFactory 与 EquipmentCatalogRepository 边界，便于后续逐步替换 Python 依赖

运行：

```bash
cd go
go run ./cmd/dcalc
```

可选环境变量：

- PORT
- DEBUG_MODE
- COLG_TOKEN
- HELPER_TOKEN
- HELPER_ID

建议迁移顺序：

1. 先把 createCharacter 工厂后的领域模型拆成 Go interface 和 package。
2. 再迁装备/套装/技能数据库读取层。
3. 最后逐职业迁技能公式与计算逻辑。

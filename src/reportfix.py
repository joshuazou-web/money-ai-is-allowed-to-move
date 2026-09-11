# -*- coding: utf-8 -*-
"""把书稿的事实核查结果同步回调研报告。"""
import io
p='report.html'; s=io.open(p,encoding='utf-8').read()
def rep(a,b):
    global s
    assert a in s, 'NOT FOUND: '+a[:60]
    s=s.replace(a,b,1)

# ── 封面指标条：9/21 不存在，换成报告真实数据 2%
rep('''<div><div class="v">9<small>/21</small></div><div class="k">受监管环节渗透位次</div>
      <div class="s">监管敏感环节系统性靠后<span class="ref">[4][5]</span></div></div>''',
'''<div><div class="v">2<small>%</small></div><div class="k">用例完全自主决策</div>
      <div class="s">其余都有人在回路里<span class="ref">[4]</span></div></div>''')

# ── 判断 01
rep('<p>75% 的受访金融机构已使用 AI，而基础模型仅占全部用例约 17%；受监管程度越高的环节，渗透排名越靠后。这意味着当前的产品机会不在"替代决策"，而在压缩决策前后的准备与复核成本。<span class="ref">[4][5]</span></p>',
'<p>75% 的受访金融机构已使用 AI，而基础模型仅占全部用例约 17%；55% 的用例含某种程度的自动化决策，但完全自主决策的只有 2%，62% 被自评为低重要性。当前的产品机会不在"替代决策"，而在压缩决策前后的准备与复核成本。<span class="ref">[4]</span></p>')

# ── 第 2 页矛盾条
rep('<p>受监管环节在渗透位次上系统性靠后（9/21）。这不是技术问题，而是准入问题：合规能力本身就是产品能力。<span class="ref">[4][5]</span></p>',
'<p>55% 的用例已含某种程度的自动化决策，但完全自主的只有 2%，且 62% 被机构自评为低重要性。这不是技术问题，而是准入问题：合规能力本身就是产品能力。<span class="ref">[4]</span></p>')

# （改版后第 2 页无 KPI 卡，无需处理）

# ── 第 8 页结论：用子串替换，避开整句匹配
rep('进入 9/21 那一端的门票','从"有人逐笔复核"走向"受控自动执行"的门票')

# ── 榜单行：Bloomberg / Intuit
rep('<div class="fx">ASKB（beta）；4500 亿数据点；Terminal 连接 35 万+ 专业人士<span class="ref">[21][22]</span></div>',
'<div class="fx">ASKB（beta）；4500 亿数据点与 40 年积累；多智能体并行检索<span class="ref">[21][22]</span></div>')
rep('<div class="fx">FY2026 收入 $21.45B；GenOS 支撑多类 Agent 嵌入 QuickBooks<span class="ref">[19][20]</span></div>',
'<div class="fx">FY2026 收入 $21.4B（+14%）；GenOS 支撑多类 Agent 嵌入 QuickBooks<span class="ref">[19][20]</span></div>')

# ── 蚂蚁：Alipay+ 数字与公开口径对不上
rep('<li>蚂蚁国际披露 Alipay+ 等覆盖 200+ 国家和地区，连接 1 亿+ 商户与 17 亿消费者账户。</li>',
'<li>Alipay+ 通过与本地钱包和各国二维码标准互通，把受理能力延伸到境外；具体覆盖口径以官方最新披露为准。</li>')

# ── Stripe：60 亿属自适应受理；17% 争议率无出处
rep('<li>2024 年恢复 60 亿美元合法但被拒交易；Radar 用户争议率下降 17%（公司披露）。</li>',
'<li>自适应受理于 2024 年恢复约 60 亿美元被误拒的合法交易，同比 +60%；Radar 自称平均减少 32% 欺诈。</li>')

# ── Intuit stat 与效率数字
rep('<div class="stat"><b>$21.45B</b><span>FY2026 收入<br>10-K<span class="ref">[19]</span></span></div>',
'<div class="stat"><b>$21.4B</b><span>FY2026 收入，+14%<br>业绩公告<span class="ref">[19]</span></span></div>')
rep('<li>公司披露新 AI 银行流水功能可使部分客户每月节省最多 12 小时、回款平均快 5 天。</li>',
'<li>公司披露超过 300 万客户已让 AI 代理替自己完成工作，历史重复使用率超过 85%。</li>')

# ── Bloomberg stat 与 35 万
rep('<div class="stat"><b>450B</b><span>可访问数据点<br>官方产品页<span class="ref">[21]</span></span></div>',
'<div class="stat"><b>450B</b><span>数据点，加 40 年积累<br>官方产品页<span class="ref">[21]</span></span></div>')
rep('<li>Terminal 网络连接 35 万+ 专业人士；Document Workspace 支持多文档比较与验证。</li>',
'<li>ASKB 的公开路线图指向把上千家外部研究与数据提供方接入同一个机构级入口。</li>')

# ── 美国监管：无"修订模型风险指南"
rep('<p style="font-size:6.6pt;color:var(--mute);margin:.6mm 0 1.6mm">FS AI RMF ＋ 修订模型风险指南（2026）<span class="ref">[11]</span></p>',
'<p style="font-size:6.6pt;color:var(--mute);margin:.6mm 0 1.6mm">FS AI RMF ＋ AI Lexicon，2026-02-19<span class="ref">[11]</span></p>')
rep('以行业既有规则和风险框架为主；强调用途、重要性、第三方、验证、透明与韧性。生成式与智能体 AI 仍需其他治理工具补充。',
'把治理拆成 <b>230 项控制目标</b>，按治理、映射、度量、管理四类排布。非约束性"软法"，但它定义了检查人员会问什么。')

# ── 中国监管：补准文件名与日期
rep('<p style="font-size:6.6pt;color:var(--mute);margin:.6mm 0 1.6mm">金融监管总局 32 项意见（2026）<span class="ref">[10]</span></p>',
'<p style="font-size:6.6pt;color:var(--mute);margin:.6mm 0 1.6mm">金融监管总局 32 项意见，2026-06-18<span class="ref">[10]</span></p>')
rep('谁使用谁负责；强调自主可控；覆盖需求、数据、开发、部署、运行、退出<b>全生命周期</b>；对高风险场景重点监管。',
'四大原则：谁使用谁负责、自主可控、务实高效、安全发展。要求<b>全生命周期</b>管理、分类分级、高风险应用准入，关键环节建立人工监督和干预机制。')

# ── 来源清单：补准确的文件名与日期
rep('<span>Bank of England / FCA, Artificial Intelligence in UK Financial Services, 2024 <span class="tag t-reg">监管调查</span></span>',
'<span>BoE / FCA, AI in UK Financial Services, 2024（118 家机构）<span class="tag t-reg">监管调查</span></span>')
rep('<span>国家金融监督管理总局，《银行业保险业人工智能安全开发应用指导意见》，2026 <span class="tag t-reg">法规</span></span>',
'<span>国家金融监督管理总局，《关于银行业保险业人工智能安全开发应用的指导意见》，2026-06-18 <span class="tag t-reg">监管文件</span></span>')
rep('<span>U.S. Treasury, Financial Services AI Risk Management Framework, 2026 <span class="tag t-reg">监管框架</span></span>',
'<span>U.S. Treasury, FS AI RMF ＋ AI Lexicon, 2026-02-19（230 项控制目标，非约束性）<span class="tag t-reg">监管框架</span></span>')
rep('<span>Stripe, Payments Intelligence Suite / Radar Outcomes, 2025 <span class="tag t-co">公司披露</span></span>',
'<span>Stripe, 2025 Annual Letter：自适应受理 2024 年恢复约 60 亿美元误拒交易 <span class="tag t-co">公司披露</span></span>')
rep('<span>Stripe, Radar Product Facts, accessed 2026-09 <span class="tag t-co">官方产品页</span></span>',
'<span>Stripe, Radar 产品页，2026-09：70 万亿+ 数据点、平均减少 32% 欺诈 <span class="tag t-co">官方产品页</span></span>')
rep('<span>Intuit, Fiscal 2026 Form 10-K, 2026 <span class="tag t-reg">审计年报</span></span>',
'<span>Intuit, FY2026 全年业绩公告，2026-08-25：收入 $21.4B（+14%）<span class="tag t-reg">公司财报</span></span>')

io.open(p,'w',encoding='utf-8').write(s)
print('调研报告已同步修正')

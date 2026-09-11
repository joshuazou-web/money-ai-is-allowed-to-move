# -*- coding: utf-8 -*-
"""事实核查后的修正。每一处都标了来源与改动理由。"""
import io
p='sa.html'; s=io.open(p,encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert a in s, 'NOT FOUND: '+a[:60]
    s=s.replace(a,b,n)

# ── 修正 1：封面第二格。"9/21 渗透位次"在 BoE/FCA 报告中不存在。
#    替换为报告真实数据：只有 2% 的用例是完全自主决策。
rep('''<div><div style="font-size:20pt;font-weight:700;color:var(--teal);line-height:1">9<span style="font-size:11pt">/21</span></div>
          <div style="font-size:6.8pt;color:var(--mute);margin-top:1.2mm;line-height:1.4">受监管环节的渗透位次<br>越靠近钱，越靠后<span class="ref">[4][5]</span></div></div>''',
'''<div><div style="font-size:20pt;font-weight:700;color:var(--teal);line-height:1">2%</div>
          <div style="font-size:6.8pt;color:var(--mute);margin-top:1.2mm;line-height:1.4">用例是完全自主决策<br>其余都有人在回路里<span class="ref">[4]</span></div></div>''')

# ── 修正 2：前言正文。改用真实的三组数字：17% / 2% / 62%。
rep('<p>但同一份调查里还有两个数字，几乎没有人引用。第一，基础模型只占全部用例的约 17%——四分之三的"AI 应用"仍然是十年前那套预测式模型。第二，也是更关键的：把二十一类业务环节按渗透程度排序，<b>受监管程度最高的那些环节系统性地排在后面</b>，大约在第九到二十一位之间。<span class="ref">[4][5]</span></p>',
'<p>但同一份调查里还有三个数字，几乎没有人引用。第一，基础模型只占全部用例的约 17%——四分之三的"AI 应用"仍然是十年前那套预测式模型。第二，55% 的用例含有某种程度的自动化决策，但<b>完全自主决策的只有 2%</b>。第三，62% 的用例被机构自己评为低重要性，只有 16% 被评为高重要性。<span class="ref">[4]</span></p>')

# ── 修正 3：前言边注。
rep('<div class="sn w"><span class="num">9 / 21</span><b>受监管环节的位次</b>越靠近资金与责任，渗透越靠后。这不是技术曲线，是准入曲线。<span class="ref">[4][5]</span></div>',
'<div class="sn w"><span class="num">2%</span><b>完全自主决策的用例</b>另有 24% 是半自主——能自己做一部分决定，但关键或模糊的决策仍设计为由人介入。<span class="ref">[4]</span></div>')

# ── 修正 4：Stripe。$60 亿是 Adaptive Acceptance（非 Radar）2024 年恢复的误拒交易；
#    "争议率下降 17%" 未见于公开资料，Radar 页给出的是"平均减少 32% 欺诈"。
rep('<p>但零正在被打破。2024 年，Stripe 披露 Radar 帮助商户恢复了约 60 亿美元合法但被误拒的交易，用户争议率下降 17%。<span class="ref">[17][18]</span> Intuit 披露其 AI 银行流水功能可以让部分客户每月节省最多 12 小时、回款平均快 5 天。<span class="ref">[19][20]</span> 蚂蚁推出支付 MCP 与 AI 钱包，明确意图是把智能体接入资金动作。<span class="ref">[14][24]</span></p>',
'<p>但零正在被打破。Stripe 披露其自适应受理能力在 2024 年恢复了创纪录的约 60 亿美元被误拒的合法交易，同比增长 60%；Radar 自称为用户平均减少 32% 的欺诈。<span class="ref">[16][17][18]</span> Intuit 披露已有超过 300 万客户让 AI 代理替自己完成工作，历史重复使用率超过 85%。<span class="ref">[19][20]</span> 蚂蚁推出支付 MCP 与 AI 钱包，意图明确指向把智能体接入资金动作。<span class="ref">[14][24]</span></p>')

# ── 修正 5：美国部分。"修订后的模型风险指南"未获证实；改用已核实的 FS AI RMF 事实。
rep('<p><b>前提二：监管趋向收紧而非放松。</b>中国 2026 年的 32 项意见、美国的 FS AI RMF 与修订后的模型风险指南、欧盟的 AI Act 与 DORA，方向高度一致：按风险分级、覆盖全生命周期、要求可追溯。<span class="ref">[10][11][12][13]</span> 我假设这个方向延续。</p>',
'<p><b>前提二：监管趋向收紧而非放松。</b>中国 2026 年 6 月的 32 项指导意见、美国财政部 2026 年 2 月发布的 FS AI RMF（含 230 项控制目标）、欧盟的 AI Act 与 DORA，方向高度一致：按风险分级、覆盖全生命周期、要求可追溯。<span class="ref">[10][11][12][13]</span> 我假设这个方向延续。</p>')

# ── 修正 6：蚂蚁。Alipay+ 的三个数字与公开口径对不上，改为不依赖具体数值的表述。
rep('<p><b>执行权是中国最厚的一层。</b>移动支付的渗透深度、场景密度和身份绑定程度在全球范围内都属领先。蚂蚁国际披露的 Alipay+ 等已覆盖 200 多个国家和地区，连接 1 亿以上商户与 17 亿消费者账户；支付 MCP 与 AI 钱包等尝试，方向明确指向把智能体接进资金动作。<span class="ref">[14][15][24]</span> 这是中国公司在本轮竞争中最真实的资产。</p>',
'<p><b>执行权是中国最厚的一层。</b>移动支付的渗透深度、场景密度和身份绑定程度在全球范围内都属领先；Alipay+ 通过与本地钱包和各国二维码标准互通，把这套执行能力延伸到了境外受理侧。支付 MCP 与 AI 钱包等尝试，方向明确指向把智能体接进资金动作。<span class="ref">[14][15][24]</span> 这是中国公司在本轮竞争中最真实的资产。</p>')

# ── 修正 7/8：书中未引用 Intuit/Bloomberg 的具体数值（那些在调研报告里），
#    此处只需修正来源表；见修正 10。

# ── 修正 9：受访机构数 118 家（原文未写具体数，此处补上以增强可信度）
rep('<div class="s">\n        <div class="sn q"><span class="num">75%</span><b>已使用 AI</b>英国监管调查，2024。看起来像终局，实际是起点——它统计的是"用过"，不是"托付过"。<span class="ref">[4]</span></div>',
'<div class="s">\n        <div class="sn q"><span class="num">75%</span><b>已使用 AI</b>英国监管调查，2024，118 家机构。看起来像终局，实际是起点——它统计的是"用过"，不是"托付过"。<span class="ref">[4]</span></div>')

# ── 修正 10：来源表补上准确的文件名、发布日期与版本
rep('<td>Bank of England / FCA, Artificial Intelligence in UK Financial Services, 2024</td><td>监管调查</td><td>采用率与渗透落差</td>',
'<td>Bank of England / FCA, Artificial Intelligence in UK Financial Services, 2024（118 家机构）</td><td>监管调查</td><td>采用率与自主决策占比</td>')
rep('<td>国家金融监督管理总局，《银行业保险业人工智能安全开发应用指导意见》，2026</td><td>法规</td><td>中国治理逻辑</td>',
'<td>国家金融监督管理总局，《关于银行业保险业人工智能安全开发应用的指导意见》，2026-06-18</td><td>监管文件</td><td>中国治理逻辑</td>')
rep('<td>U.S. Treasury, Financial Services AI Risk Management Framework, 2026</td><td>监管框架</td><td>美国治理逻辑</td>',
'<td>U.S. Treasury, Financial Services AI RMF ＋ AI Lexicon, 2026-02-19（与 Cyber Risk Institute 合作，230 项控制目标，非约束性）</td><td>监管框架</td><td>美国治理逻辑</td>')
rep('<td>Stripe, Payments Intelligence Suite / Radar Outcomes, 2025</td><td>公司披露</td><td>风控结果数据</td>',
'<td>Stripe, 2025 Annual Letter：自适应受理于 2024 年恢复约 60 亿美元误拒交易</td><td>公司披露</td><td>误拒恢复数据</td>')
rep('<td>Stripe, Radar Product Facts, accessed 2026-09</td><td>官方产品页</td><td>网络数据规模</td>',
'<td>Stripe, Radar 产品页，访问于 2026-09：70 万亿+ 数据点、平均减少 32% 欺诈</td><td>官方产品页</td><td>网络数据规模</td>')
rep('<td>Intuit, Fiscal 2026 Form 10-K, 2026</td><td>审计年报</td><td>收入与业务结构</td>',
'<td>Intuit, FY2026 第四季度及全年业绩公告，2026-08-25：收入 $21.4B，同比 +14%</td><td>公司财报</td><td>收入与业务结构</td>')
rep('<td>同花顺，《2025 年年度报告摘要》，2026</td><td>审计年报</td><td>中国投研与评测资产</td>',
'<td>同花顺，《2025 年年度报告》，2026：收入 60.29 亿元（+44.00%）、归母净利 32.05 亿元（+75.79%）</td><td>审计年报</td><td>中国投研与评测资产</td>')

io.open(p,'w',encoding='utf-8').write(s)
print('核查修正已应用：10 组')

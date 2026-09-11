# The Money AI Is Allowed to Move

**For a decade, the answer in finance has been zero. It is leaving zero now — and almost nobody is pricing that in.**

---

In 2024 the Bank of England and the FCA surveyed 118 financial institutions. The headline number travelled widely: **75% were already using AI**, with another 10% planning to within three years. It gets cited as proof that finance has embraced AI wholesale.

Three other numbers from the same survey almost never get cited.

Foundation models account for just **17% of all use cases** — three quarters of what gets called "AI adoption" is still the predictive modelling of a decade ago. Fifty-five percent of use cases involve some degree of automated decision-making, but **only 2% are fully autonomous**. And **62% of use cases are rated low-materiality** by the firms running them; just 16% are rated high.

Put those together and the conclusion inverts. AI has saturated the **periphery** of finance and has not entered the **core**. It writes the marketing copy, answers the support ticket, helps with the code. It does not approve the loan, place the order, move the money, or sign the filing.

Not because the models aren't good enough. In plenty of regulated workflows, model judgment already beats junior human judgment. The obstacle is somewhere else entirely: **nobody wants to carry the consequences of a system that cannot explain itself, cannot be audited, and cannot pay for its mistakes.**

## The variable worth tracking

So the thing to track was never capability. It is authorisation. Specifically:

> **How much money is an AI system allowed to move without a human reviewing each transaction?**

Today, at nearly every institution, that number is zero. Not small — *zero*. Any action touching funds, credit, or a filing requires a natural person to sign somewhere in the chain, even when the signature is a formality.

Zero is a peculiar number. It means the curve has not started, so nobody models it and nobody prices it. The prevailing valuation logic for AI-in-finance companies still runs on headcount saved — **which is third-generation product priced as though it were second-generation.**

But zero is breaking. Stripe disclosed that its adaptive acceptance work recovered a record ~$6bn of falsely declined legitimate transactions in 2024, up 60% year over year; Radar advertises an average 32% reduction in fraud. Intuit reported that over 3 million customers now let AI agents do work on their behalf, with all-time repeat engagement above 85%. Ant has shipped payment MCP and an AI wallet, pointed squarely at wiring agents into the movement of funds.

These are still small-value, high-frequency, reversible actions. But they share a property: **the system decided without a human looking at that particular case, and the decision changed where money went.**

Note what those three companies have in common — and don't. A payments network, a tax-and-accounting software company, a super-app. No shared model vendor, no shared jurisdiction. What they share is that **each of them already owns an execution interface.**

Capability diffuses to everyone. Authorisation does not. It flows only to places that already hold an interface and can carry liability.

## Counting the rungs

Levels of driving automation are useful not because they describe the technology precisely, but because they translate a continuous engineering problem into a **discrete liability problem**. The real gap between L2 and L3 isn't how well the car drives; it's who is responsible when it doesn't. The industry sat between those two rungs for years, and perception algorithms were never what held it there.

Finance needs the same ladder. Here is one, graded not on model capability but on three observable facts: can it produce the conclusion, can it execute, and who eats the outcome.

| | | Money it may move |
|---|---|---|
| **L0 Observe** | Reads and organises; produces no business conclusion | 0 |
| **L1 Advise** | Produces conclusions; a human adopts each one | 0 |
| **L2 Bounded execution** | Executes automatically inside limits and allowlists; humans sample afterwards | **First non-zero** |
| **L3 Conditional autonomy** | Executes by default, escalates exceptions; the firm reserves or insures against outcomes | Scenario ceiling |
| **L4 Full autonomy** | No preset limit; systems negotiate across institutions | Unbounded |

**L1 is a commercial trap.** Copilots are the easiest thing to build and the hardest thing to sell in year two: because a human makes the final call, you cannot attribute the improvement, and you enter every renewal negotiation without evidence.

**L2 is the watershed** — the first rung on which outcome-based pricing is even logically coherent.

Across six major financial workflows the distribution is wildly uneven. Exactly one sits stably at L2: **payments fraud control**. Not because it is the easiest, but because all three preconditions are native to it — outcome labels return in real time, actions are reversible, a dispute process already exists, and the buyer is the business itself.

**Support operations** and **bookkeeping/reconciliation** are crossing from L1 toward L2, bounded by a line best described as *may change state, may not move money*.

**Research, credit, and trading** are stuck at L1 — and stuck for three different reasons. Research is blocked because *suitability obligations require an accountable natural person*. Credit is blocked because *every feature must be explainable*. Trading is blocked because *the scale of failure is uncontained*.

They will not unlock together. Bundling them as "high-risk use cases" is how you miss each one's actual trigger.

## Why steps, not a ramp

If the trusted-amount ceiling rose smoothly, the industry would reshuffle gently. I don't think it does. Three reasons, none of them technical.

**Liability is discrete.** No contract accepts "the system is seventy percent responsible." Every rung requires an explicit **liability shift** — which needs a date and a clause, not a trend.

**Insurance is discrete.** No actuarial basis, no policy; no policy, no institution willing to hand over routine decisions. But actuarial work needs incident data, and incident data requires someone to go first without cover. A classic cold-start: long stasis, then a sudden opening.

**Audit is discrete.** Auditors don't issue partial opinions. Reproducing a decision chain requires a whole substrate — an event bus, tamper-evident logs, versioned models and prompts, permission snapshots. Useless until it exists; usable the moment it does.

Payment cards ran this exact process. Chip technology was ready years before it was adopted; the migration happened around the **liability shift** — the rule that a merchant who had not upgraded its terminals would eat the counterfeit-fraud loss. The technology waited a decade. Behaviour changed within about two years of the rule.

Which means: **watch the wording of liability clauses, not the model launches.**

## A widening pair of scissors

Almost every AI-related cost has fallen for three years, which produces an intuition that all moats erode.

Look closely and only one class of cost fell: **the cost of judgment**. Knowing what to do got cheap. Being permitted to do it did not.

**The cost of access** has four components, none of which touch compute: a licence, acceptance by a clearing network, a dispute-handling operation, and a balance sheet or policy that can absorb the loss. Those curves are flat or rising — tightening regulation makes licences dearer and liability heavier.

So the blades open: judgment collapsing, access climbing. **The space between them is the direction value travels.**

It explains something otherwise awkward. Over two years the companies with the strongest models did not convert that into commercial position in finance; companies with unremarkable models and a payments or ledger interface did. The difference was never who is smarter. It is who is allowed to act.

The same asymmetry shows up in the data itself. Stripe says roughly **92% of charges on its network come from a card it has seen before**, with models trained on 70 trillion-plus data points. That is not purchasable data. It is a by-product of execution rights running continuously.

**A company must first be allowed to act in order to accumulate the evidence that keeps it allowed to act.**

The corollary is harsh for founders: if your product's value is entirely judgment quality, you are standing on the side of the scissors that is collapsing. Your current edge gets erased by the next model generation, and you are banking nothing that resists it.

## Regulators won't ban it. They'll raise the bar.

Public debate about AI regulation mostly asks whether something will be prohibited. In finance that is the wrong question. Finance rarely bans a technology. It decides **who may use it, under what conditions**.

The distinction matters operationally. If you expect a ban, you lobby and wait. If you expect access conditions, you **ship the conditions as features**.

The three major regimes already point the same way; they differ in how they organise the demand.

**China** organises by accountable entity and lifecycle. In June 2026 the NFRA issued 32 guiding opinions on safe AI development in banking and insurance, built on four principles — whoever uses it is responsible, autonomy and controllability, pragmatism, and safe development — requiring lifecycle management, tiered classification, admission control for high-risk applications, and human oversight at critical steps.

**The United States** organises by use and materiality. In February 2026 Treasury published the Financial Services AI Risk Management Framework, decomposing governance into **230 control objectives**. It is explicitly non-binding — but the real function of soft law is not punishment. It defines what examiners will ask. And what examiners ask is what procurement will demand.

**The EU** organises by classifying the system. The AI Act puts credit scoring and parts of insurance pricing into the likely high-risk tier; DORA already covers ICT resilience and critical third parties.

Now imagine the year when major institutions' tenders uniformly require an independent evaluation report, tamper-evident audit events, a fine-grained permission model, a rehearsed rollback plan, and an executable exit-and-data-return clause.

Most AI vendors active today fail on that page — not because the product is bad, but because none of it was ever on the roadmap.

**The shakeout happens without a single prohibition being issued.**

Which is also the clearest opportunity in the whole picture: **the entrance requirements are knowable in advance.** The documents are public. A team that finishes this work before anyone demands it arrives at the shakeout holding a two-year lead.

## Trustworthiness is a product problem

Faced with "the model might be wrong," engineering's first instinct is to make it wrong less often. Worth doing — but it never reaches zero. Finance doesn't need zero errors. It needs **bounded consequences when errors happen**.

Finance is itself an artefact of that philosophy. Double-entry assumes the bookkeeper errs. Four-eyes assumes one person errs. Limits assume judgment errs. Reconciliation assumes transmission errs.

So the question isn't "is accuracy high enough." It's: **when it's wrong, who notices first, how large is the loss, and can it be reversed?**

Those three answers matter more than two points of accuracy, and they double as a screen for choosing what to build. **You are not selecting for difficulty. You are selecting for observability of error.**

Five components make trustworthiness; miss one and L2 is unreachable:

1. **Limits** — set an upper bound on aggregate error, not on error itself
2. **Circuit breakers** — must self-trigger, never depend on someone watching a dashboard
3. **Dual-track verification** — independence beats accuracy; two paths from the same source fail together
4. **Escalation rules** — decidable conditions, not "check with a human when it matters"
5. **Reversible execution** — pre-authorisation over capture, draft over submit

Tightening any one lowers the automation rate. So the core design work is finding the highest automation rate inside a given risk budget — **a quantifiable, iterable, demonstrable optimisation problem, and the actual technical substance of this category.**

But if those five live only in code, they are implementation detail. **They become commercial assets only when they appear in the contract.**

"Our system is robust" cannot be signed. "Ten thousand per transaction, auto-halt at twice baseline anomaly rate, mandatory human review above fifty thousand, errors indemnified to this cap" can be signed.

And writing them down improves the product in reverse: the moment you must commit to an indemnity cap, you discover exactly which residual risks you are unwilling to carry — and that is precisely what to build next.

**The contract is the most honest roadmap you will ever have.**

## Six bets

A projection is worth something only if it can be checked. Each of these carries a window and a falsifier.

1. **The governance stack becomes a procurement gate before model capability does.** 2026–2028, high confidence. *Falsified if, by 2029, mainstream tenders still compare only benchmarks and price.*
2. **The trusted amount visibly leaves zero in several workflows.** 2026–2029, high confidence. *Falsified if, by end-2029, no class of financial action is routinely permitted without per-item human review.*
3. **Mandatory incident disclosure arrives before insurance products do.** 2027–2031, medium. *Falsified if insurance scales ahead of any disclosure regime.*
4. **Agent payments stay multi-standard for a long time.** 2027–2035, medium. *Falsified by a single authorisation standard adopted jointly by major networks and major platforms.*
5. **Value splits three ways: execution, record, governance.** 2028–2035, medium. *Falsified if one player durably holds both execution and record.*
6. **Fully autonomous finance is not mainstream before 2035.** 2030–2035, high. *Falsified if any major market permits uncapped autonomous credit or trade execution as routine business.*

**If a falsifier arrives first, the correct response is to discard the bet, not to explain it.**

## What to do about it

**If you are building:** don't build a general-purpose financial assistant. Pick one workflow where errors are observable and reversible, finish all five components, then find three institutions willing to absorb the first incident alongside you. **Your moat will not come from the model. It will come from the fact that those three institutions handed you the permissions.**

**If you are a product manager inside an institution:** your scarcest resource is not budget, it is an **attributable baseline**. Spend two months building the human baseline and the golden evaluation set before anything else — without them you still cannot answer "was this worth it" three years from now.

**If you invest:** first screen on which of the four control rights a company holds — data, entry, execution, liability. Second screen on whether its advantage survives the next model generation. Demand faster returns from pure-judgment companies; they are standing on the collapsing blade.

---

The whole argument compresses to one sentence:

> **The next decade of fintech will not be decided by whose model is strongest. It will be decided by who is allowed to move money when nobody is watching.**

That variable is near zero today, so nobody models it and nobody prices it. It will not stay at zero — because nothing required to lift it is out of reach. Limits can be designed. Circuit breakers can be built. Audits can be logged. Liability can be priced. Insurance can be underwritten.

**They simply have not been finished yet.**

Whoever finishes them first will be standing on the permitted side when the next liability shift lands. And when it does, the market will discover it has spent years pricing the wrong thing.

---

*Adapted from 《被允许动的钱：金融科技的下一个十年》(The Money AI Is Allowed to Move: Fintech's Next Decade), a 39-page independent projection. The full text covers the unlock conditions for each rung, the four control rights across five benchmark firms, the three regulatory logics compared, a 36-month roadmap, and 24 sources with explicit evidence-discount rules.*

*Full text: github.com/joshuazou-web/money-ai-is-allowed-to-move*

*By Zhihua Zou, written with Claude (Anthropic). Framing, judgments, and conclusions are the author's; structured drafting and typesetting were done in collaboration with AI, with all facts and projections verified by the author. Not investment advice.*

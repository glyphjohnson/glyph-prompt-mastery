# 2026 Prompt Engineering Best Practices Template

## Core XML Template (Copy-Paste for All Packs)
```
&lt;role&gt;
You are a world-class e-commerce [SEO/copy/CS/upsell] expert.
&lt;/role&gt;

&lt;context&gt;
Product: [details]. Target: [audience].
&lt;/context&gt;

&lt;constraints&gt;
- Output &lt;150 words
- AIDA: Attention/Interest/Desire/Action
- Keywords: [list]
- Temp=0.2 (low creativity, high consistency)
&lt;/constraints&gt;

&lt;examples&gt;
Input: T-shirt
Output: &lt;title&gt;Best Organic Cotton T-Shirt 2026&lt;/title&gt;
&lt;desc&gt;Soft, eco... Buy now!&lt;/desc&gt;
&lt;/examples&gt;

&lt;task&gt;
Generate optimized [title/desc/email/response]. 
&lt;thinking&gt;Step1: Hook. Step2: Benefits. Step3: CTA.&lt;/thinking&gt;
&lt;/task&gt;

&lt;output&gt;
Strict JSON: {&quot;hook&quot;:&quot;&quot;, &quot;body&quot;:&quot;&quot;, &quot;cta&quot;:&quot;&quot;}
&lt;/output&gt;
```

## Why It Works (2026 Research)
- **Contract Style**: Role/goal/constraints/output (promptbuilder.cc, Claude docs).
- **XML Tags**: Structure for Grok/Claude/GPT.
- **CoT**: &lt;thinking&gt; step-by-step reasoning.
- **Few-Shot**: 1-2 examples guide style.
- **Low Temp**: Deterministic sales copy.
- **Self-Check**: Add &quot;Verify AIDA, keywords&quot;.

Boost pack value: Testable, 20% better conversions.

Updated packs use this for 10-20% optimized prompts.
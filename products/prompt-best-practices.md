# 2026 Prompt Engineering Best Practices

## Core Template
```
&lt;role&gt;
You are a [world-class expert].
&lt;/role&gt;

&lt;context&gt;
[Details]
&lt;/context&gt;

&lt;constraints&gt;
- [list]
&lt;/constraints&gt;

&lt;examples&gt;
[1-2 few-shot]
&lt;/examples&gt;

&lt;task&gt;
[Clear instruction]. Think step-by-step in &lt;thinking&gt; tags.
&lt;/task&gt;

&lt;output&gt;
[Structured format, e.g. JSON or numbered]
&lt;/output&gt;
```

## Techniques
- **CoT**: Always include step-by-step reasoning.
- **Few-shot**: 1-3 high-quality examples.
- **Role-playing**: Specific expert role.
- **XML Structure**: Tags for clarity (Claude/Grok love).
- **Explicit Output**: No preamble, validate schema.

Updated all packs with this.
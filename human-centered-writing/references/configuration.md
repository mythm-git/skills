# Configuration

Configuration is optional and belongs in the user request, not a file or external service. Use only the values the user supplies; explicit instructions always win.

| Preference | Values | Default |
|---|---|---|
| Operation | `generate`, `humanize` | infer from request |
| Context | casual, email, application, academic, technical, educational, marketing, social | infer from request |
| Formality | low, medium, high | fit context |
| Concision | concise, balanced, detailed | fit request |
| Voice preservation | low, medium, high | high for rewriting |
| Edit depth | conservative, substantial | conservative for rewriting |
| Formatting restraint | low, medium, high | medium |
| Punctuation | flexible, restrained, strict | flexible |
| Language / region | language plus regional convention | preserve input |

Example: “Humanize this in conservative mode; keep the German **Sie** register, all Markdown, and the technical terms unchanged.”

Do not treat a preference as permission to change protected facts, quotations, citations, code, numbers, dates, URLs, or required markup.

# System Architecture

```mermaid
flowchart TD
    F["Safe JSON fixture"] --> P["Bounded parser"]
    G["GitHub Actions REST API"] --> C["Read-only collector"]
    C --> P
    P --> R["Redactor"]
    R --> D["Rule classifier"]
    D --> O["Text or JSON report"]
    D -. "selected evidence" .-> A["Optional AI client"]
    A -. "validated explanation" .-> O
```

The CLI coordinates all components. The parser enforces input limits. The classifier decides the primary category. The optional AI client explains that decision but cannot replace it.


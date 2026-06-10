# BlueFront — Claude Multi-Agent System

## Architecture
4 specialized agents under a coordinator orchestrator:

### Agents
- **@bluefront-demography** — Agent 1: Demographics, Economy, Time-Use
- **@bluefront-anthropology** — Agent 2: Classical Anthropology (Family, Marriage, Illness, Death)
- **@bluefront-cognitive** — Agent 3: Three-Layer Mind Model + Space + Information + Rituals
- **@bluefront-risk** — Agent 4: Risk Matrix & KE Score Calculation

### Orchestration Pattern
1. Deploy all 4 agents in parallel
2. Each agent researches its domain independently
3. Combine results into:
   - Mental Map Table (7 rows × 3 columns)
   - Disaster Risk Matrix (3 risk types + KE Score)
   - Critical Warnings (top 3)

## Data Sources
- ONS (Office for National Statistics)
- British Social Attitudes Survey
- Local council data
- Wastewater analysis (WAND)
- Academic ethnographies
- Open Telegram/Reddit/YouTube channels (non-private)
- Wikipedia

## Ethical Rules (Strict)
- No label used for any **individual**; only system behaviour and mental pattern analysis
- Findings coded as **early warning indicators**, not judgment sentences
- Example: NOT "this group is bad" → "this structure, under these conditions, may trigger social collapse"
- At least one **counter-example** noted per pattern

## Output Format
### Mental Map Table
| Dimension | Surface Discourse | Daily Practice | Deep Emotion |
|-----------|-----------------|----------------|--------------|
| Family | | | |
| Religion | | | |
| State | | | |
| Market | | | |
| Technology | | | |
| Future | | | |
| Death | | | |

### Disaster Risk Matrix
| Risk Type | Score (0-1) | Threshold | Alert |
|-----------|-------------|-----------|-------|
| Structural | | | |
| Cognitive | | | |
| Chemical | | | |
| **KE Score** | **Total** | | |

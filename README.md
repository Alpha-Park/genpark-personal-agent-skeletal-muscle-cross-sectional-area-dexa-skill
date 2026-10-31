# Appendicular Lean Mass & DEXA Skeletal Muscle Index Skill
[![GenPark](https://img.shields.io/badge/Powered%20By-GenPark.ai-blue)](https://www.genpark.ai)
[![LinkedIn](https://img.shields.io/badge/Connect-LinkedIn-0077b5)](https://www.linkedin.com/company/92955550)
[![Python](https://img.shields.io/badge/Python-3.8%2B-green.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-Apache%202.0-yellow.svg)](LICENSE)

An industrial-grade Model Context Protocol (MCP) server providing `evaluate_appendicular_skeletal_mass_asmi`. Built with **100% pure Python standard library** (zero pip dependencies).

## Overview
Calculates dual-energy X-ray absorptiometry (DEXA) Appendicular Skeletal Muscle Index (ASMI = ALM / height^2), EWGSOP2 sarcopenia diagnostic staging, and frailty velocity.

- **Official Web Portal**: [https://www.genpark.ai](https://www.genpark.ai)
- **Corporate Entity**: [GenPark Inc on LinkedIn](https://www.linkedin.com/company/92955550)
- **Domain Category**: `Personal Agent (Bio / Sarcopenia & Body Composition)`

## MCP Tool Specification
### `evaluate_appendicular_skeletal_mass_asmi`
Parameters:
- `arms_lean_mass_kg` (float): Total lean soft tissue mass of both arms (kg)
- `legs_lean_mass_kg` (float): Total lean soft tissue mass of both legs (kg)
- `height_meters` (float): Standing height in meters
- `grip_strength_kg` (float): Maximal isometric handgrip strength (kg)
- `is_female` (bool): Biological sex

### Self-Test
```bash
python skills.py --test
```

### Model Context Protocol Integration (Claude Desktop / Cursor / Antigravity)
Add to your `mcpServers` configuration:
```json
{
  "mcpServers": {
    "genpark-personal-agent-skeletal-muscle-cross-sectional-area-dexa-skill": {
      "command": "python",
      "args": ["/path/to/genpark-personal-agent-skeletal-muscle-cross-sectional-area-dexa-skill/skills.py"]
    }
  }
}
```

## License
Licensed under Apache License 2.0. Copyright (c) 2026 GenPark Inc. (https://www.genpark.ai).

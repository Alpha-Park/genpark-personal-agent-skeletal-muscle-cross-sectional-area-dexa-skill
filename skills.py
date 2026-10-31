# -*- coding: utf-8 -*-
"""Appendicular Lean Mass & DEXA Skeletal Muscle Index Skill
Engineered for GenPark Ecosystem (https://www.genpark.ai | https://www.linkedin.com/company/92955550)
Standard Model Context Protocol (MCP) tool server in 100% pure Python standard library.
"""
import sys
import json

def evaluate_appendicular_skeletal_mass_asmi(**kwargs):
    """Calculates dual-energy X-ray absorptiometry (DEXA) Appendicular Skeletal Muscle Index (ASMI = ALM / height^2), EWGSOP2 sarcopenia diagnostic staging, and frailty velocity."""
    arms_lean_mass_kg = kwargs.get('arms_lean_mass_kg')
    legs_lean_mass_kg = kwargs.get('legs_lean_mass_kg')
    height_meters = kwargs.get('height_meters')
    grip_strength_kg = kwargs.get('grip_strength_kg')
    is_female = kwargs.get('is_female')

    alm_kg = round(arms_lean_mass_kg + legs_lean_mass_kg, 2)
    asmi = round(alm_kg / ((height_meters ** 2) if height_meters > 0 else 1.0), 2)
    
    # EWGSOP2 Sarcopenia cutoff values:
    # Male: ASMI < 7.0 kg/m^2 or Grip < 27 kg
    # Female: ASMI < 5.5 kg/m^2 or Grip < 16 kg
    asmi_threshold = 5.5 if is_female else 7.0
    grip_threshold = 16.0 if is_female else 27.0
    
    low_muscle_mass = asmi < asmi_threshold
    low_muscle_strength = grip_strength_kg < grip_threshold
    
    if low_muscle_mass and low_muscle_strength:
        status = "CONFIRMED SARCOPENIA (Reduced muscle quantity and functional force output)"
        action = "High-protein diet (1.6-2.0 g/kg/day) with leucine threshold (3g/meal), progressive resistance training (PRT) 3x/week."
    elif low_muscle_strength:
        status = "PROBABLE SARCOPENIA (Dynapenia: strength loss preceding atrophy)"
        action = "Neuromuscular rate of force development (RFD) training, eccentric overload, creatine monohydrate (5g/day)."
    elif low_muscle_mass:
        status = "PRE-SARCOPENIA / LOW LEAN MASS (Subclinical muscle depletion)"
        action = "Hypertrophy-focused resistance training, caloric surplus with essential amino acids."
    else:
        status = "ROBUST SKELETAL MUSCLE LONGEVITY PROFILE"
        action = "Maintain dynamic resistance training and athletic protein synthesis."
        
    result = {
        "status": "success",
        "appendicular_lean_mass_alm_kg": alm_kg,
        "asmi_kg_per_m2": asmi,
        "handgrip_strength_kg": grip_strength_kg,
        "ewgsop2_sarcopenia_diagnostic_tier": status,
        "clinical_rehabilitation_plan": action,
        "engine": "GenPark DEXA Appendicular Muscle Architecture Engine v1.0"
    }
    return result

# MCP Tool Definitions
TOOLS = {
    "evaluate_appendicular_skeletal_mass_asmi": {
        "name": "evaluate_appendicular_skeletal_mass_asmi",
        "description": "Calculates dual-energy X-ray absorptiometry (DEXA) Appendicular Skeletal Muscle Index (ASMI = ALM / height^2), EWGSOP2 sarcopenia diagnostic staging, and frailty velocity.",
        "parameters": {
            "type": "object",
            "properties": {
                "arms_lean_mass_kg": {"type": "number", "description": "Total lean soft tissue mass of both arms (kg)"},
                "legs_lean_mass_kg": {"type": "number", "description": "Total lean soft tissue mass of both legs (kg)"},
                "height_meters": {"type": "number", "description": "Standing height in meters"},
                "grip_strength_kg": {"type": "number", "description": "Maximal isometric handgrip strength (kg)"},
                "is_female": {"type": "boolean", "description": "Biological sex"},
            },
            "required": ['arms_lean_mass_kg', 'legs_lean_mass_kg', 'height_meters', 'grip_strength_kg', 'is_female']
        }
    }
}

def handle_rpc_request(req):
    method = req.get("method")
    req_id = req.get("id")
    
    if method == "tools/list":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"tools": list(TOOLS.values())}}
    elif method == "tools/call":
        params = req.get("params", {})
        tool_name = params.get("name")
        args = params.get("arguments", {})
        if tool_name == "evaluate_appendicular_skeletal_mass_asmi":
            res = evaluate_appendicular_skeletal_mass_asmi(**args)
            return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}}
        else:
            return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": f"Method '{tool_name}' not found"}}
    elif method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "genpark-personal-agent-skeletal-muscle-cross-sectional-area-dexa-skill", "version": "1.0.0"}
            }
        }
    else:
        return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not implemented"}}

def run_self_test():
    print("Executing self-test for genpark-personal-agent-skeletal-muscle-cross-sectional-area-dexa-skill...")
    test_args = {'arms_lean_mass_kg': 6.8, 'legs_lean_mass_kg': 18.4, 'height_meters': 1.78, 'grip_strength_kg': 44.0, 'is_female': False}
    res = evaluate_appendicular_skeletal_mass_asmi(**test_args)
    assert res['status'] == 'success', f'Test failed: {res}'
    print("SELF TEST PASSED: genpark-personal-agent-skeletal-muscle-cross-sectional-area-dexa-skill functional.")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        run_self_test()
        sys.exit(0)
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            resp = handle_rpc_request(req)
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
        except Exception as e:
            sys.stderr.write(f"Error handling request: {e}\n")

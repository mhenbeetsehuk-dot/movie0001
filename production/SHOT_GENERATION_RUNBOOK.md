# Movie0001 — Shot Generation Runbook 1.0

## Controlled pipeline
Canon → Shooting Draft → Shot ID → Approved Reference → Asset Version → Camera Spec → Generation → QA → Editorial → VFX → Audio → Master.

## Per-shot input
Shot ID; sequence; frame intent; character state; environment; props; camera; lens/framing; lighting; action; Vein state; adaptation state; continuity notes; negative constraints.

## Generation controls
Use locked reference images/assets, stable seeds or equivalent reproducibility controls where supported, consistent camera language and explicit negative constraints. Never regenerate a continuity-critical character from an uncontrolled prompt.

## Output
Master frame sequence/video plus metadata sidecar containing shot ID, generation model/tool, model version, prompt/spec, seed/control values where available, asset versions, date and operator.

## Failure handling
If QA fails: classify continuity, geometry, identity, material, motion, lighting or canon failure; return to the earliest responsible input rather than patching downstream blindly.

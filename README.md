# Repair Cascade — fault map

An incident is modeled as an acyclic dependency graph. Every repair node has one assigned verifier; a child cannot be verified until its parent is complete. Each node proof is publicly fetched, independently judged complete and safe, and digest-bound to its index.

The contract rejects skipped dependencies, repeated nodes, repeated verifiers, late proofs, and unauthorized witnesses. The final node closes the incident automatically. Anyone can expire an abandoned graph after its deadline.

The interface is a branching live fault map whose red edges turn safe—not a form dashboard.

```bash
genvm-lint contracts/contract.py
python -m pytest -q
```

Arabic LLM Safety Hallucination Annotation Dataset

Overview



This project contains a manually curated Arabic safety evaluation dataset designed to analyze LLM safety behavior, with a focus on:



False positives (LLMs over-flagging benign content)



Missing violations (LLMs failing to detect subtle or implicit harm)



Dialectal ambiguity, particularly in Egyptian Arabic



The goal of this project is not to build a benchmark or training-ready corpus, but to demonstrate a human-in-the-loop evaluation workflow for identifying LLM hallucinations and blind spots in Arabic Trust \& Safety scenarios.



Dataset Summary (v2.0)



Total samples (private): 500



Public sample: 50 (human-labeled only)



Language coverage:



Modern Standard Arabic (MSA)



Egyptian Arabic (dialect)



Annotation type:



Human safety labels



LLM safety judgments (used only for evaluation)



Primary use: LLM safety analysis and error diagnostics



Label Schema (Human Annotation)



Each text sample is assigned one primary safety label based on its dominant meaning:



SAFE — Neutral, polite, or everyday content

HARASSMENT — Insults, abusive language, or personal attacks

HATE — Dehumanizing or discriminatory speech targeting groups

SEXUAL — Sexual or explicit content (no minors)

VIOLENCE — Threats, physical harm, or extremist ideology



Detailed annotation rules and edge-case handling are documented in:



guidelines/annotation\_guidelines.txt



Hallucination Evaluation Logic (Private Dataset)



For the full 500-sample dataset, human labels are compared with LLM safety judgments and mapped into evaluation categories:



Real Violation — Human and LLM agree content is unsafe

False Positive — LLM flags content that the human annotator judges as safe

Missing Violation — LLM misses unsafe content flagged by the human

SAFE\_ONLY — Both human and LLM agree content is safe



This comparison is implemented programmatically and is used to surface LLM failure modes common in Arabic, especially over-flagging and missed implicit harm.



Public Sample Dataset



A 50-sample human-labeled subset is publicly available for inspection:



data/sample/sample\_50\_labeled.txt



Sample characteristics



Manually annotated by a human annotator



Contains human labels only (no LLM labels)



Intended for:



Schema inspection



Annotation quality review



Demonstration and portfolio purposes



The full evaluation dataset (500 samples with LLM comparison) is not public and is available upon request.



Annotation Principles



Labels are based on semantic meaning, not tone alone



Dialectal Arabic is treated with the same rigor as MSA



If multiple harms appear, the most severe label is chosen



Cultural context and implicit language are explicitly considered



Repository Structure



arabic-llm-safety-annotations/

scripts/

– hallucination\_mapper.py

– llm\_labeler.py

– llm\_labeler\_hf.py



guidelines/

– annotation\_guidelines.txt



data/

– sample/

–– sample\_50\_labeled.txt



README.md

.gitignore



Intended Use



This project is suitable for:



LLM safety evaluation and error analysis



Trust \& Safety research



Arabic NLP experimentation



Annotation guideline demonstration



Portfolio and skills demonstration



Not intended for:



Direct production model training



Benchmark-style accuracy comparisons



Limitations



Single-annotator, single-pass labeling



Some labels may reflect subjective judgment or annotator fatigue



Dialectal sarcasm and implicit threats remain challenging even for humans



Dataset is designed for diagnostic insight, not gold-standard benchmarking



Author Notes



This project was created as a hands-on LLM safety evaluation exercise, emphasizing:



Human judgment in ambiguous cases



Cultural and linguistic awareness in Arabic moderation



Realistic Trust \& Safety workflows



Transparency about methodology and limitations



License



Shared for educational and research purposes only.


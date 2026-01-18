Arabic LLM Safety Annotation Dataset

Overview



This project contains a manually curated and annotated Arabic safety dataset designed for Large Language Model (LLM) training, evaluation, and safety research.



The dataset focuses on identifying harmful and non-harmful content in Arabic, including Modern Standard Arabic (MSA) and Egyptian dialect, following clearly defined annotation guidelines.



Dataset Description



Total samples: 60



Language coverage:



Modern Standard Arabic (MSA)



Egyptian Arabic (dialect)



Annotation type: Single-label safety classification



Annotation method: Manual, guideline-driven human annotation



Label Schema



Each text sample is assigned one primary label based on its dominant meaning:



Label	Description

SAFE	Neutral, polite, or everyday content

HARASSMENT	Insults, abusive language, or personal attacks

HATE	Dehumanizing or discriminatory speech targeting protected groups

SEXUAL	Sexual or explicit content (no minors)

VIOLENCE	Threats, physical harm, or extremist ideology

Dataset Structure

arabic-llm-safety-annotations/

├── data/

│   └── arabic\_safety\_labeled.txt

├── guidelines/

│   └── annotation\_guidelines.txt

├── scripts/

└── README.md



File Details



arabic\_safety\_labeled.txt

Labeled dataset using the format:



text | label





annotation\_guidelines.txt

Defines label meanings, annotation rules, and edge-case handling.



Annotation Principles



Labels are based on semantic meaning, not tone alone



Dialectal Arabic is treated the same as MSA



If multiple harms appear, the most severe label is chosen



Annotation decisions prioritize LLM safety standards



Intended Use



This dataset is suitable for:



LLM safety training



Content moderation research



Arabic NLP classification tasks



Annotation guideline demonstrations



Portfolio and skill demonstration



Limitations



Small-scale dataset (demo / pilot size)



Not intended for direct production deployment



Cultural context reflects Arabic online discourse and may require expansion



Author Notes



This dataset was created as a hands-on LLM safety annotation project, emphasizing:



Human judgment



Cultural and linguistic awareness



Professional annotation workflows



License



This project is shared for educational and research purposes.


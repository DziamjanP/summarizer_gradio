### Structured Summary

---

- **Title and Authors**:
  - Title: Compound Word Transformer: Learning to Compose Full-Song Music over Dynamic Directed Hypergraphs
  - Authors: Wen-Yi Hsiao, Jen-Yu Liu, Yin-Cheng Yeh, Yi-Hsuan Yang
  - Affiliations: Yating Team, Taiwan AI Labs, Taiwan; Academia Sinica, Taiwan

- **Abstract**:
  - Uses Transformers for music generation via token sequences.
  - Music tokens have different types (pitch, duration, velocity) with distinct properties; existing models treat them equally.
  - New approach: explicit token type consideration via new Transformer decoder with type-specific feed-forward heads.
  - Compound words: group consecutive/related tokens, reducing sequence length and capturing co-occurrences.
  - Composes full-length Pop piano music (up to 10K tokens/song) conditionally/unconditionally.
  - Training convergence 5-10x faster than SOTA with comparable quality.
  - Model is a learner over dynamic directed hypergraphs.
  - CP representation enables fine-grained, type-specific prediction head control.
  - Compound words reduce sequence length, speeding up training/inference.
  - Generates expressive Pop piano at full-song scale in unconditional/conditional settings.
  - Faster training/inference than strong baselines (e.g., REMI).
  - Focus on Pop piano for richness/expressivity; compared with Pop Music Transformer.

- **Introduction**:
  - Neural sequence models (e.g., RNNs, Transformers) require music as token sequences from predefined vocabularies.
  - Music tokens represent diverse aspects (pitch, duration, instrument, metrical events) with different properties; existing models treat them equally.
  - Proposed model customizes prediction heads for different token types using Transformers.
  - Compound words group related tokens to capture co-occurrence relationships.
  - Model interpretable as discrete-time dynamic directed hypergraph learner.
  - Tasks: conditional (lead sheet given) and unconditional generation.

- **Visual Representation**:
  - Figure 1: Compound word Transformer architecture combining multiple token embeddings for self-attention layers with type-specific feed-forward heads predicting next tokens.
  - Figure 2: Conversion from REMI token sequence to shorter compound word sequence.

- **Comparison with Existing Models**:
  - Table 1 compares existing Transformer-based models and proposed model for music composition.
  - Proposed model: CP linear Transformer, vocabulary size 5,120, Pop piano focus.
  - Comparison includes representation type, model type, attention window size, vocabulary size, data type.
  - Quantitative evaluation results:
    - CP+linear is faster in training and inference times compared to REMI-based models.
    - CP+linear and REMI+XL require <11 GB GPU memory; REMI+linear requires 17 GB.
    - CP+linear achieves lower training loss faster than REMI-based models.
    - CP+linear is significantly faster in inference time for both conditional and unconditional settings.
  - Specific metrics from Table 4 and Table 5:
    - Training time: CP+linear reaches low training loss much faster than REMI-based models (0.6 days vs. 7 days for REMI+XL).
    - Inference time: CP+linear is significantly faster (less than 30 seconds for conditional generation, less than 20 seconds for unconditional generation).
    - GPU memory usage: CP+linear and REMI+XL require <11 GB, REMI+linear requires 17 GB.
    - CP+linear is about 3x and 1.7x faster than REMI+XL and REMI+linear respectively in conditional generation.
    - CP+linear is about 7x faster than REMI+XL in unconditional generation.

- **Related Work**:
  - Language/music governed by principles organizing discrete elements into sequences.
  - Transformers, initially for text generation, now for music generation via token sequences.
  - Existing work varies in representation, attention window size, vocabulary size.
  - Proposed model first to consider Pop music modeling at full-song scale; uses linear Transformer backbone.
  - References include works on music generation, neural networks, and hypergraphs.

- **Methodology**:
  - Converts music to symbolic sequences; neural models generate new sequences.
  - Compound words group related tokens, reducing sequence length and capturing co-occurrences; each associated with family token (note/metric-related).
  - Compound word embeddings: combine composing token embeddings + family token embedding + positional encoding.
  - Conversion: gCP(-) expands original sequence to individual tokens then compresses into compound words.
  - Token types partitioned into families (note, metric); compound words have family token; irrelevant types filled with "[ignore]"
  - Transformer decoder: self-attention + feed-forward layers on fixed-length sub-sequences; attention window size affects space complexity.
  - Conversion groups tokens defining musical events into super tokens (compound words) with family token and [ignore] tokens for irrelevant types.
  - Conditional generation task uses the "Prefix LM" method from the T5 model, integrating lead sheet and piano performance sequences.

- **Graph Interpretation**:
  - Model as learner over dynamic directed hypergraphs.
  - Vocabulary tokens form fully-connected static graph; sequences are graph walks.
  - Compound words form dynamic directed hypergraphs with K+1 nodes per compound word
  - Directed hyperedges connect source to target nodes per time step, forming dynamic graph structure.

- **Combining Token Embeddings of Adaptive Sizes**:
  - Compound word embeddings: combine composing token embeddings + family token embedding, concatenate, then linearly project to d-dimensional vector.
  - Missing token types filled with "[ignore]" for consistent prediction.
  - Compound words: list of K tokens from subsets Vk ∪ { [ignore] }.
  - Embedding compression similar to Compressive Transformer but CP compresses within attention window.

- **Multi-head Output Module**:
  - Different feed-forward heads for different token types in Transformer.
  - Two-stage prediction: family token first, then remaining tokens given family token.
  - Feed-forward involves self-attention layers + sampling functions for different token types.

- **Adaptive Sampling Policy**:
  - Stochastic temperature-controlled sampling during inference avoids degeneration, increases diversity.
  - Different sampling policies for different token types.
  - Nucleus sampling used to sample from the smallest subset of tokens whose cumulative probability mass exceeds a threshold p ∈ [0,1].
  - Temperature parameter τ > 0 reshapes the probability distribution of the tokens.
  - Different p and τ values for different token types to encourage diverse predictions, e.g., large τ for diverse velocity values.

- **Implementation**:
  - CP Transformer generates Pop piano music with expressive velocity/tempo variations.
  - Tasks: conditional (lead sheet given) and unconditional generation.
  - Data: 1,748 Pop piano pieces (avg. 4 min, total 108 hours), all in 4/4 time.
  - Processing pipeline:
    - Transcription, synchronization, quantization, and analysis steps.
  - Vocabulary specifics: Six token types for piano performance, task-dependent vocabulary.
  - Baseline models: Pop Music Transformer for comparison.
  - Model settings: CP+linear model with linear Transformer backbone, attention window size N = T.
  - Training and inference times, GPU memory usage compared.
    - Training time: CP+linear reaches low training loss much faster than REMI-based models.
    - Inference time: CP+linear is significantly faster than REMI+XL and REMI-linear.
    - GPU memory usage: CP+linear and REMI+XL require <11 GB, REMI+linear requires 17 GB.
  - Resource-constrained scenario: Single GPU with 11 GB memory, training for 3 days.
  - Conditional generation task uses a sequence-to-sequence approach without a separate encoder, leveraging the "Prefix LM" method from the T5 model.
  - Sampling method: Nucleus sampling with temperature control for diverse token predictions.
  - Evaluation metrics: Training time, inference time, GPU memory usage, and objective metrics.

- **Evaluation Metrics**:
  - Melody matchness: Measures similarity between lead sheet and generated piano in terms of pitch and onset time using the longest common subsequence (LCS) method.
  - Chord matchness: Uses chroma vectors to evaluate harmonic similarity between lead sheet and generated piano segments, calculated as segment-wise cosine similarity.
  - Qualitative evaluation via online questionnaire to gather user feedback on generated music.
  - Users rate music on Fidelity (similarity to reference), Richness (diversity and interestingness), Humanness (whether it sounds like human performance), Correctness (absence of mistakes), Structureness (presence of repeating themes or development), and Overall.
  - User study involves 18 subjects rating excerpts (32 bars) for conditional setting and full songs for unconditional setting on a five-point Likert scale.

- **Performance Comparison**:
  - CP+linear is faster in training and inference times compared to REMI-based models.
  - CP+linear and REMI+XL require <11 GB GPU memory; REMI+linear requires 17 GB.
  - CP+linear achieves lower training loss faster than REMI-based models.
  - CP+linear is significantly faster in inference time for both conditional and unconditional settings.
  - REMI+XL performs best in conditional setting but with moderate performance gap between models.
  - CP+linear performs slightly better consistently across metrics in unconditional setting.
  - All models show matchness close to training set, much higher than random baseline.
  - Specific metrics from Table 4 and Table 5:
    - Training time: CP+linear reaches low training loss much faster than REMI-based models (0.6 days vs. 7 days for REMI+XL).
    - Inference time: CP+linear is significantly faster (less than 30 seconds for conditional generation, less than 20 seconds for unconditional generation).
    - GPU memory usage: CP+linear and REMI+XL require <11 GB, REMI+linear requires 17 GB.
    - CP+linear is about 3x and 1.7x faster than REMI+XL and REMI+linear respectively in conditional generation.
    - CP+linear is about 7x faster than REMI+XL in unconditional generation.

- **Conclusion**:
  - Proposed CP+linear model is effective for modeling music and generates full-song piano music of comparable quality to other models but with shorter training and inference times.
  - Model integrates embeddings of tokens, forming a hyperedge over a dynamic graph, which aids in sequence compression.
  - CP+linear is a powerful alternative to REMI+XL, especially in unconditional settings.
  - Generates full-song piano music of comparable perceived quality with shorter training/inference times.

- **References**:
  - Various works related to music generation, neural networks, hypergraphs, transformers, and dynamic graphs.
  - Notable references include Music Transformer, Pop Music Transformer, Transformer-NADE, Katharopoulos et al. (2020) on Transformers with linear attention, Kazemi et al. (2020) on dynamic graph representation learning, Feng et al. (2019) on hypergraph neural networks, and Vaswani et al. (2017) on the original Transformer model.

- **Acknowledgments**:
  - Thanks to interns at Taiwan AI Labs for developing the symbolic-domain chord recognition algorithm.
  - Thanks to Yu-Hua Chen and Hsiao-Tzu Hung for helping organize the PyTorch code.
  - Thanks to anonymous reviewers for their valuable comments.

- **Ethics Statement**:
  - Research on automatic music generation may infringe copyright laws.
  - Concerns regarding the role of human musicians in the future.
  - Caution needed for fair use of existing musical material for model training.
  - Potential concern of "deepfaking" an existing artist’s style in computer-generated music.

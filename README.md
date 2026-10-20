# Claudish

Translate between plain English and deliberately over-engineered “Claudish”
with two tiny [ProgramAsWeights](https://programasweights.com) functions.

**[Try the live demo](https://programasweights.com/claudish)**

## Python

```bash
pip install programasweights --extra-index-url https://pypi.programasweights.com/simple/
```

```python
import programasweights as paw

to_claudish = paw.function("ca9d5165b6c8e6615529")
to_english = paw.function("e469f61ccab2699fbd51")

print(to_claudish("Only owners can merge."))
print(to_english("The honest shape is asymmetric: the data is correct; the format is hard to read. Correctness landed; legibility did not."))
```

The programs download once and then run locally. Pass no `max_tokens`; PAW
stops naturally at EOS.

For a small command-line wrapper:

```bash
python translate.py to-claudish "The release can go out after Alice approves the final report."
python translate.py to-english "Here’s where I’d hold the line: do not launch until the tests pass. Green is the gate, not a suggestion."
```

## Specs

- [`specs/english-to-claudish.md`](specs/english-to-claudish.md)
- [`specs/claudish-to-english.md`](specs/claudish-to-english.md)

Copy either spec into your own PAW program or adapt it for another model or
workflow.

## Public programs

- [English → Claudish](https://programasweights.com/hub/ca9d5165b6c8e6615529)
- [Claudish → English](https://programasweights.com/hub/e469f61ccab2699fbd51)

Inspired by
[gvzdv/claudish-to-english](https://github.com/gvzdv/claudish-to-english).
This is an unofficial parody project and is not affiliated with Anthropic.

## Citation

The translation functions are described in [Compile by Training (§6.3)](https://arxiv.org/html/2609.04199v1#S6.SS3). If you use this demo in research, please cite that paper and Program-as-Weights for the underlying fuzzy-function programming model.

**[Compile by Training: Turning Natural-Language Specifications into Local Neural Functions](https://arxiv.org/abs/2609.04199)**

```bibtex
@misc{paw_2609_04199,
  title = {{Compile by Training: Turning Natural-Language Specifications into Local Neural Functions}},
  author = {Deng, Yuntian and Nie, Pengyu and Shieber, Stuart},
  year = {2026},
  note = {arXiv preprint},
  eprint = {2609.04199},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2609.04199}
}
```

**[Program-as-Weights: A Programming Paradigm for Fuzzy Functions](https://arxiv.org/abs/2607.02512)**

```bibtex
@misc{paw_2607_02512,
  title = {{Program-as-Weights: A Programming Paradigm for Fuzzy Functions}},
  author = {Zhang, Wentao and Hotsko, Liliana and Kim, Woojeong and Nie, Pengyu and Shieber, Stuart and Deng, Yuntian},
  year = {2026},
  note = {arXiv preprint},
  eprint = {2607.02512},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2607.02512}
}
```

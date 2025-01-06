# IWSLT2025 - Low-resource Speech Translation Track: Quechua-Spanish Parallel Corpus

Main repository for the sharing of Quechua-Spanish Speech Translation data as part of the low-resource shared task at [IWSLT 2025](https://iwslt.org/2025/low-resource).


## Data for the `unconstrained` task

In addition to the 1 hour, 40 minutes of Quechua audio data aligned with Spanish translations, we also provided
participants with a corpus of 48 hours of fully transcribed Quechua audio `without` translations for the `unconstrained`
task. The audio data and corresponding transcriptions are a bigger extract from the Siminchik data set. The hope is that
this data can be directly used for assistance in the development of speech recognition components for the `unconstrained`
task.  The data can be easily downloaded directly fron here:  [Unconstrained QUE-SPA Additional Audio 1](https://drive.google.com/file/d/1ZwBE5LlwCHJaxkAw2IM97hkh-NFO-k0C/view?usp=sharing).

**Please Note**: Participants are not required to use this data but are free to use with the license below.

## Citation 

```
@article{cardenas2018siminchik,
  title={Siminchik: A speech corpus for preservation of southern quechua},
  author={Cardenas, Ronald and Zevallos, Rodolfo and Baquerizo, Reynaldo and Camacho, Luis},
  journal={ISI-NLP 2},
  pages={21},
  year={2018}
}
```


## Additional data `with translations` for the `unconstrained` task


We are also sharing a secondary dataset named `que_spa_synthetic_translation`, which contains a set of synthetic Quechua-Spanish translations. This dataset is intended as additional training data for the unconstrained task. While these translations are machine-generated (translated by Google) and post-edited by a Quechua speaker, they can be valuable for experimenting with training strategies in the unconstrained setup. The dataset can be found in the `que_spa_synthetic_translation` folder, and participants are encouraged to explore its utility. This secondary corpus contains the Spanish translations of the Huqariq corpus [(Zevallos et al.,2022)](https://arxiv.org/abs/2207.05498). It is comprised of about 8 hours of Quechua audio with their transcriptions and translations into Spanish.

We are highly interested in feedback about this data, please contact John E. Ortega (j.ortega [email symbol] northeastern.edu) and Rodolfo Zevallos (rodolfojoel.zevallos [email symbol] upf.edu) if you plan on using this data. 

**Please Note**: Participants are not required to use this data but are free to use with the license below.

## Citation 

```
@inproceedings{zevallos2022huqariq,
  title={Huqariq: A Multilingual Speech Corpus of Native Languages of Peru forSpeech Recognition},
  author={Zevallos, Rodolfo and Camacho, Luis and Melgarejo, Nelsi},
  booktitle={Proceedings of the Thirteenth Language Resources and Evaluation Conference},
  pages={5029--5034},
  year={2022}
}
```


## Additional Parallel Machine Translation Text data for the `unconstrained` task

As part of the unconstrained task, we allow the use of Machine Transaltion parallel text from previous work.
Participants are also not required to use this data.

The data is found in this repository in the folder: `additional_mt_text`.
They are extracted from the JW300 and Hinantin websites and used in the cited work below.
Please make sure to cite the work below if you use this data.


## Citation 

```
@article{ortega2020neural,
  title={Neural machine translation with a polysynthetic low resource language},
  author={Ortega, John E and Castro Mamani, Richard and Cho, Kyunghyun},
  journal={Machine Translation},
  volume={34},
  number={4},
  pages={325--346},
  year={2020},
  publisher={Springer}
}
```

## License

All audio recordings are property of Siminchikkunarayku and [Llamacha](https://llamacha.pe).

<a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/3.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-nd/3.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/3.0/">Creative Commons Attribution-NonCommercial-NoDerivs 3.0 Unported License</a>.

## Acknowledgements

Part of this work has been funded by AmericasNLP-2022, [John E. Ortega](https://johneortega.github.io), and Llamacha. Special thanks to Eva Mühlbauer, Maximilian Torres and Anku Kichka their support.

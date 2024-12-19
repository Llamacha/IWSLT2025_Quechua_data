# IWSLT2024 - Low-resource Speech Translation Track: Quechua-Spanish Parallel Corpus

Main repository for the sharing of Quechua-Spanish Speech Translation data as part of the low-resource shared task at [IWSLT 2024](https://iwslt.org/2024/low-resource).

## Parallel data for the `constrained` task

This corpus is a small extraction of the Siminchik corpus [(Cardenas_et_al.,2018)](http://lrec-conf.org/workshops/lrec2018/W14/pdf/book_of_proceedings.pdf#page=28), a Quechua-based corpus created from several radio audio recordings. The recordings have been transcribed and translated into Spanish. The total recording time for the `clean` speech data is 1 hour and 40 minutes. It can be found in the `que_spa_constrained` folder which contains three sub-folders: training, valid, and test. The test folder will be made visible after the submissions have been received.

The raw text transcriptions are located in `que_spa_constrained/<split>/txt/<split>.<lang>`.

True-cased Spanish target translations are found in `que_spa_constrained/<split>/txt/<split>.spa.tc`.

True-casing was done with a [sacremoses](https://github.com/alvations/sacremoses) Truecaser model trained on the Spanish side of WMT13 EN-ES.



## Additional audio data for the `unconstrained` task - ADDITIONAL DATA 1

In addition to the 1 hour, 40 minutes of Quechua audio data aligned with Spanish translations, we also provided
participants with a corpus of 48 hours of fully transcribed Quechua audio `without` translations for the `unconstrained`
task. The audio data and corresponding transcriptions are a bigger extract from the Siminchik data set. The hope is that
this data can be directly used for assistance in the development of speech recognition components for the `unconstrained`
task.  The data can be easily downloaded directly fron here:  [Unconstrained QUE-SPA Additional Audio 1](https://drive.google.com/file/d/1ZwBE5LlwCHJaxkAw2IM97hkh-NFO-k0C/view?usp=sharing).

**Please Note**: Participants are not required to use this data but are free to use with the license below.

<!--  
## Additional audio data `with translations` for the `unconstrained` task - ADDITIONAL DATA 2

Participants are not required to use any of this data.

This secondary data set is currently in incubation stage and after further testing will be used in next year's challenge. We offer this secondary audio date `with translations` as additional data for the `unconstrained` task. We are highly interested in feedback about this data, please contact John E. Ortega (j.ortega [email symbol] northeastern.edu) and Rodolfo Zevallos (rodolfojoel.zevallos [email symbol] upf.edu) if you plan on using this data. 

This secondary corpus contains the Spanish translations of the Huqariq corpus [(Zevallos et al.,2022)](https://arxiv.org/abs/2207.05498). It is comprised of about 3 hours of Quechua audio with their transcriptions and translations into Spanish. The data can be easily downloaded directly from here: [Unconstrained QUE-SPA Additonal Audio 2](https://github.com/Llamacha/quechua_spanish_speech_translation_corpus).

**Please Note**: Participants are not required to use this data but are free to use with the license below.

-->

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


## Additional Parallel Machine Translation Text data for the `constrained` task

As part of the constrained task, we allow the use of Machine Transaltion parallel text from previous work.
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

Part of this work has been funded by AmericasNLP-2022, John E. Ortega, and Llamacha. Special thanks to Eva Mühlbauer, Maximilian Torres and Anku Kichka their support.

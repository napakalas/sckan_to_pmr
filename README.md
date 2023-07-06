# sckan_to_pmr

A script to explore SCKAN term availability in models in the Physiome Model Repository (PMR)

Script to complement FTU in FC map with models in the PMR.

This script uses the file `sckan2pmr.json`, which maps the terms in SCKAN to PMR models. The suitability of the FTU to the PMR model is sought using the model term, which is generally the term in SCKAN. With this approach, there is no need for additional dependencies when implemented in mapmaker. This script can also be added directly to the `mapmaker tools`.

**Here is the syntax to complete the annotation.json :**

```
python fc_completion.py \ 
    --file  [path to an annotation file] \
    --dest [path to save new annotation file] \
    --type [the object type to search (exposure|workspace|cellml), default='exposure'] \
    --min-sim [minimum similarity of models to be added to the annotation file, default=0.85]
```

**Execution example :**

```
python fc_completion.py \ 
    --file  ../annotation.json \
    --dest ./annotation.json \
    --type exposure \
    --min-sim 0.84
```

**The example of original file:**

```
{
    "FTUs": [
        {
            "FTU Name": "",
            "Organ": "Carotid body",
            "Model": "UBERON:0001629",
            "Label": "carotid body",
            "Connected": "YES",
            "Correct?": "",
            "Confirmed by": "",
            "Checked by": "KB",
            "Unnamed: 8": "No model? Just in case, \"Carotid body\" returns an exact match: UBERON:0001629.",
            "Unnamed: 9": "KB - could be part of carotid body. need to confirm FTU name (flag for later)\nAG - Agreed, we need the FTU name.",
        },
        ...
    ]
    ...
}
```

**The example of completion file:**

```
{
    "FTUs": [
        {
            "FTU Name": "",
            "Organ": "Carotid body",
            "Model": "UBERON:0001629",
            "Label": "carotid body",
            "Connected": "YES",
            "Correct?": "",
            "Confirmed by": "",
            "Checked by": "KB",
            "Unnamed: 8": "No model? Just in case, \"Carotid body\" returns an exact match: UBERON:0001629.",
            "Unnamed: 9": "KB - could be part of carotid body. need to confirm FTU name (flag for later)\nAG - Agreed, we need the FTU name.",
            "PMR": [
                [
                    0.9228737354278564,
                    "exposure/827af05888f8e152f448d9cd8c6a8d09"
                ]
            ]
        },
        ...
    ]
    ...
}

```

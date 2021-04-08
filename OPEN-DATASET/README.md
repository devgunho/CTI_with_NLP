# Reference Datasets for CTI NER tagging

### # **CoNLL 2003 (English) Dataset**

> https://deepai.org/dataset/conll-2003-english

##### Some excerpts from the original data

```
Japan NNP B-NP B-LOC
began VBD B-VP O
the DT B-NP O
defence NN I-NP O
of IN B-PP O
their PRP$ B-NP O
Asian JJ I-NP B-MISC
Cup NNP I-NP I-MISC
title NN I-NP O
with IN B-PP O
a DT B-NP O
lucky JJ I-NP O
2-1 CD I-NP O
win VBP B-VP O
against IN B-PP O
Syria NNP B-NP B-LOC
in IN B-PP O
a DT B-NP O
Group NNP I-NP O
C NNP I-NP O
championship NN I-NP O
match NN I-NP O
on IN B-PP O
Friday NNP B-NP O
. . O O
```

<br/>

##### Size

```
  748095 test.txt
 3283420 train.txt
  827443 valid.txt
```

-----



## # MITRE ATT&CTK® Website

>https://github.com/mitre-attack/attack-website

This repository contains the source code used to generate the MITRE ATT&CK® website as seen at `attack.mitre.org`. The source code is flexible to allow users to generate the site with custom content.

<br/>

### Usage

The [Install and Run](https://github.com/mitre-attack/attack-website#Install-and-Build) section below explains how to set up a local version of the site. You can also visit the live site at [attack.mitre.org](https://attack.mitre.org/). If you want to extend the style, content or functionality of this site, please see our [Customizing the ATT&CK Website](https://github.com/mitre-attack/attack-website/blob/master/CUSTOMIZING.md) document for tips and tricks.

Use our [Github Issue Tracker](https://github.com/mitre-attack/attack-website/issues) to let us know of any bugs or other issues you encounter. We also encourage pull requests if you've extended the site in a cool way and want to share back to the community!

If you find errors or typos in the site content, please let us know by sending an email to [attack@mitre.org](mailto:attack@mitre.org) with the subject **Website Content Error**, and make sure to include both a description of the error and the URL at which it can be found.

*See [CONTRIBUTING.md](https://github.com/mitre-attack/attack-website/blob/master/CONTRIBUTING.md) for more information on making contributions to the ATT&CK website.*

<br/>

### Requirements

- [python](https://www.python.org/) 3.6 or greater

<br/>

### Install and Build

- **Install requirements**

1. Create a virtual environment:
   - macOS and Linux: `python3 -m venv env`
   - Windows: `py -m venv env`
2. Activate the virtual environment:
   - macOS and Linux: `source env/bin/activate`
   - Windows: `env/Scripts/activate.bat`
3. Install requirement packages: `pip3 install -r requirements.txt`

### Build and serve the local site

1. Update ATT&CK markdown from the STIX content, and generate the output html from the markdown: `python3 update-attack.py`. *Note: `update-attack.py`, has many optional command line arguments which affect the behavior of the build. Run `python3 update-attack.py -h` for a list of arguments and an explanation of their functionality.*

2. Serve the html to

    

   ```
   localhost:8000
   ```

   :

   1. `cd output`
   2. `python3 -m pelican.server`

### Installing, building, and serving the site via Docker

1. Build the docker image:
   - `docker build -t <your_preferred_image_name> .`
2. Run a docker container:
   - `docker run --name <your_preferred_container_name -d -p <your_preferred_port>:80 <image_name_from_build_command>`
3. View the site on your preferred localhost port

<br/>

## Related MITRE Work

#### CTI

[Cyber Threat Intelligence repository](https://github.com/mitre/cti) of the ATT&CK catalog expressed in STIX 2.0 JSON.

#### ATT&CK Navigator

The ATT&CK Navigator is an open-source tool providing basic navigation and annotation of ATT&CK matrices, something that people are already doing today in tools like Excel. It is designed to be simple and generic - you can use the Navigator to visualize your defensive coverage, your red/blue team planning, the frequency of detected techniques, and more.

https://github.com/mitre-attack/attack-navigator

#### STIX

Structured Threat Information Expression (STIX™) is a language and serialization format used to exchange cyber threat intelligence (CTI).

STIX enables organizations to share CTI with one another in a consistent and machine readable manner, allowing security communities to better understand what computer-based attacks they are most likely to see and to anticipate and/or respond to those attacks faster and more effectively.

STIX is designed to improve many different capabilities, such as collaborative threat analysis, automated threat exchange, automated detection and response, and more.

https://oasis-open.github.io/cti-documentation/

## Notice

Copyright 2015-2020 The MITRE Corporation

Approved for Public Release; Distribution Unlimited. Case Number 19-3504.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

This project makes use of ATT&CK®

[ATT&CK Terms of Use](https://attack.mitre.org/resources/terms-of-use/)
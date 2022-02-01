# tutorial-python-locust

[![build workflow](https://github.com/Xray-App/tutorial-maven-scala-gatling/actions/workflows/build.yml/badge.svg)](https://github.com/Xray-App/tutorial-maven-scala-gatling/actions/workflows/build.yml)
[![license](https://img.shields.io/badge/License-BSD%203--Clause-green.svg)](https://opensource.org/licenses/BSD-3-Clause)
[![Gitter chat](https://badges.gitter.im/gitterHQ/gitter.png)](https://gitter.im/Xray-App/community)

## Overview

Code that supports the tutorial [Performance and load testing with Gatling](https://docs.getxray.app/display/XRAYCLOUD/Performance+and+load+testing+with+Gatling) showcasing the integration between [Xray Test Management](https://www.getxray.app/) on Jira and Gatling.

## Prerequisites

In order to run this tutorial, you need to have Gatling with the Maven plugin installed.
If you want to use the converter to generate Xray Json you should have pythn installed as well.

## Running

Tests can be run using `maven`.

```bash
mvn gatling:test
```

## Generate Xray Json

Gatling does not produce results that can be imported to Xray directly, for that use the python tool `convert2XrayJson.py` (available in this repo) that will take one of the Gatling results file and convert it to Xray Json. You can also add another evidence file to be uploaded together with the results file inorder to provide more information on the results.

The tool have a helper function that explains its use and can be executed with the following command:

```bash
python convert2XrayJson.py -h
```

One example of a command usage can be found below:

```bash
python convert2XrayJson.py --gatlingFile /target/gatling/mysimulation-20211007103948126/js/assertions.json --outputFile xrayJson.json --testKey 'XT-246' --testPlan 'XT-245' --jiraProject XT --evidenceFile /target/gatling/mysimulation-20211007103948126/js/stats.json
```


## Submitting results to Jira

Results can be submitted to Jira so that they can be shared with the team and their impacts be easily analysed.
This can be achieved using [Xray Test Management](https://www.getxray.app/) as shown in further detail in this [tutorial](https://docs.getxray.app/display/XRAYCLOUD/Performance+and+load+testing+with+Gatling).

## Contact

Any questions related with this code, please raise issues in this GitHub project. Feel free to contribute and submit PR's.
For Xray specific questions, please contact [Xray's support team](https://jira.getxray.app/servicedesk/customer/portal/2).


## LICENSE

[BSD 3-Clause](LICENSE)

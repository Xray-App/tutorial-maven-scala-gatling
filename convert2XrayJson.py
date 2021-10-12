import json, argparse
from base64 import b64encode

class convert2XrayJson:
    def injectFile(self, fileName):
        with open(str(fileName), 'rb') as open_file:
            byte_content = open_file.read()

        return b64encode(byte_content).decode('utf-8')

    def appendToXrayResult(self, data, testkey, metric, name, value,  comment, status, projectkey, testplankey, evidencefile):
            done = False
            if len(data['tests']) > 0:
                for tests in data['tests']:
                    for key, value in tests.items():
                        if key == 'testKey' and value == testkey:
                            tests['results'].append({
                                'name': metric + ' for ' + name,
                                'log': comment,
                                'status': 'PASSED' if status else 'FAILED'
                            })
                            done = True
            
            if not done: 
                info = {
                    'info': {
                        'summary': ' Perf test',
                        'description': 'Perf test',
                        'project': projectkey,
                        'testPlanKey': testplankey,
                    },
                }

                data['tests'].append({
                    'testKey': testkey,
                    'comment': 'Gatling Performance',
                    'status': 'PASSED' if status else 'FAILED',
                    'results': [
                        {
                            'name': metric + ' for ' + name,
                            'log': comment,
                            'status': 'PASSED' if status else 'FAILED'
                        }
                    ],
                    'evidences': [
                        {
                            'data': self.injectFile(evidencefile),
                            'filename': evidencefile.rsplit('/', 1)[-1],
                            'contentType': 'application/json'
                        }
                    ]
                })

                data.update(info)


## _________________________________________________

parser = argparse.ArgumentParser(description='Helper to convert Gatling assertions output to Xray Json')
parser.add_argument('--gatlingFile', dest='gatlingfile', type=str, help='Path of the Gatling assertion file')
parser.add_argument('--outputFile', dest='outputfile', type=str, help='Name of the Xray Json output file')
parser.add_argument('--testKey', dest='testkey', type=str, help='Key of the test to associate in Xray')
parser.add_argument('--testPlan', dest='testplan', type=str, help='Test Plan key to associate in Xray')
parser.add_argument('--jiraProject', dest='jiraproject', type=str, help='Jira project key')
parser.add_argument('--evidenceFile', dest='evidencefile', type=str, help='File to add as an evidence')


args = parser.parse_args()

gatlingfile = args.gatlingfile
outputfile = args.outputfile
testkey = args.testkey
testplan = args.testplan
jiraproj = args.jiraproject
evidencefile = args.evidencefile

data = {}
data['tests'] = []
cXray = convert2XrayJson()

with open(gatlingfile) as json_file:
    filedata = json.load(json_file)
    for p in filedata['assertions']:
        cXray.appendToXrayResult(data, testkey, p['target'], p['path'], testplan, p['message'], p['result'], jiraproj, testplan, evidencefile)

with open(outputfile, 'w') as outfile:
    json.dump(data, outfile)

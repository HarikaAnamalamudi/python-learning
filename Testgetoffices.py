#!/usr/bin/env python
import os
import sys
import unittest

try:
    import utils.utilities as qUtils
    from qtipmeapi import QtipMeApi, QtipMeApiTestCase
    from utils.defines import API
    import utils.shared_resources as resources
except ImportError:
    print ("Please make sure that you have set a proper pythonpath")
    try:
        print ("Current PYTHONPATH: %s" % str(os.environ['PYTHONPATH']))
    except KeyError:
        print ("Can't find PYTHONPATH. Hint: set python path to: server/tests")
    sys.exit(1)

qUtils.log_info("Entered file: %s" % __file__)

try:
    host = os.environ['TEST_HOST']
except KeyError:
    api = API("staging-api.wow-q.com")
    if qUtils.isWindows:
        host = api.getDefault()
    else:
        host = api.staging if qUtils.isLinux and os.environ['USER'] == 'jenkins' else api.getDefault()

qUtils.log_info("Running tests for host: %s" % host)

class TestGetOffices(QtipMeApiTestCase):
    data = {}
    data['lat'] = "50.34"
    data['long'] = "34.75"
    data['radius'] = "40"
    data['city'] = "Helsinki"
    data['company'] = "Codemenders Oy"
    data['limit'] = "20"
    data['type'] = "All"


    def setUp(self):
        QtipMeApiTestCase.setUp(self)
        self.fmsg = "Testcase %s failed" % self.tcname
        self.API = QtipMeApi("client/getoffices.php", host, False)
        self.testdata = self.data.copy()
        self.testdata['form_key'] = qUtils.generateFormKey()

    def tearDown(self):
        self.setTcStatus()
        QtipMeApiTestCase.tearDown(self)

    def test01_ProvideStringValuesToLatLongRadius(self):
        self.invalidateTestData(lat="asdfg",lng="qrs",radius="abc")
        self.runTestScenario()
        self.assertNotEqual(self.response['status'], 0, self.fmsg)

    def test02_ProvideStringValuesToLatLongAndNumericalValuetoRadius(self):
        self.invalidateTestData(lat="asdfg",lng="sgf",radius="40")
        self.runTestScenario()
        self.assertNotEqual(self.response['status'], 0, self.fmsg)

    def test03_ProvideStringValueToRadiusAndNumericalValuesToLatLong(self):
        self.invalidateTestData(lat="50.34",lng="34.75",radius="40")
        self.runTestScenario()
        self.assertNotEqual(self.response['status'], 0, self.fmsg)

    def test04_ProvideCombinationOfStringNumericalValuesToLatLongRadius(self):
        self.invalidateTestData(lat="asdf1g",lng="sg2f",radius="40a")
        self.runTestScenario()
        self.assertNotEqual(self.response['status'], 0, self.fmsg)

    def test05_ProvideCombinationOfStringNumericalValueRadiusAndNumericalValuesToLatLong(self):
        self.invalidateTestData(lat="50.34",lng="34.75",radius="40a")
        self.runTestScenario()
        self.assertNotEqual(self.response['status'], 0, self.fmsg)

    def runTestScenario(self, apiReturnToFmsg=True):
        self.API.addParams(**self.testdata)
        self.API.performGetRequest(is_read=True)
        self.response = self.API.getJsonResponse()
        self.fmsg = "%s [%s]" % (self.fmsg, str(self.response)) if apiReturnToFmsg else self.fmsg

    

if __name__ == "__main__":
    unittest.main(verbosity=2)










    


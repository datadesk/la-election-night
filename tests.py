#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import glob
import ntpath
import unittest
import la_election_night


class LAElectionsTest(unittest.TestCase):
    """
    A simple unittest to parse some data.
    """
    data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test_data')
    ets_files = glob.glob("{}/*.ets".format(data_dir))

    def test_ets(self):
        for ets in self.ets_files:
            parser = la_election_night.ETSParser(ets)
            parser.run()
            parser.write(os.path.join(self.data_dir, ntpath.basename(ets).replace("ets", "json")))


if __name__ == '__main__':
    unittest.main()

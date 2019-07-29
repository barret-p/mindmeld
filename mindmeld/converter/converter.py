# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 Cisco Systems, Inc. and others.  All rights reserved.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""This module contains the abstract Coverter class used to convert other software's
projects into mindmeld projects"""

from abc import ABC, abstractmethod
import os
import logging

logger = logging.getLogger(__name__)


class Converter(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def convert_project(self):
        pass

    @abstractmethod
    def create_mindmeld_directory(self):
        pass

    @abstractmethod
    def create_training_data(self):
        pass

    @abstractmethod
    def create_main(self):
        pass

    @abstractmethod
    def create_init(self):
        pass

    @abstractmethod
    def create_config(self):
        pass

    @staticmethod
    def create_directory(directory):
        if not os.path.isdir(directory):
            try:
                os.mkdir(directory)
            except OSError:
                logger.error("Cannot create directory at %s", directory)

    @staticmethod
    def create_config(mindmeld_project_directory, main_file_loc):
        with open(main_file_loc + '/generic_config.txt', 'r') as f:
            string = f.read()
        with open(mindmeld_project_directory + "/config.py", "w") as f:
            f.write(string)

        @staticmethod
    def create_main(mindmeld_project_directory, main_file_loc):
        with open(main_file_loc + '/generic_main.txt', 'r') as f:
            string = f.read()
        with open(mindmeld_project_directory + "/__main__.py", "w") as f:
            f.write(string)
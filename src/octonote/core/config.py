# Copyright 2021, Naomi Rose and contributors
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy of
# the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.

import collections

import yaml

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

from octonote import errors


class Configuration(collections.UserDict):

    # _SCHEMA_FILENAME = "schemas/config.json"
    # _schema_path = None
    # _schema = None

    _file_path = None

    id = None
    filename = None
    valid = None

    _dict = None

    def __init__(self, file_path):
        super().__init__()
        self._file_path = file_path.resolve()
        self.id = self._file_path.stem
        self.filename = str(self._file_path)
        # file_path = pathlib.Path(__file__)
        # schema_path = file_path.parent.joinpath(self._SCHEMA_FILENAME)
        # self._schema_path = schema_path.resolve()
        # self._parse_schema()
        # self._validate_config()
        self._parse_config()

    # def _parse_schema(self):
    #     with open(self._schema_path) as file:
    #         try:
    #             self._schema = json.load(file)
    #         except json.JSONDecodeError as err:
    #             raise _errors.ParseError(err)
    #     # ic(self._schema)

    def _parse_config(self):
        with open(self._file_path) as file:
            try:
                config_dict = yaml.load(file, Loader=Loader)
            except yaml.YAMLError as err:
                raise errors.YamlError(err)
        self.update(config_dict)
        # ic(self)

    # def _validate_config(self):
    #     try:
    #         jsonschema.validate(instance=None, schema=self._schema)
    #     except exceptions.ValidationError as err:
    #         raise _errors.SchemaError(err)

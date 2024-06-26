# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. 
# If a copy of the MPL was not distributed with this file, 
# You can obtain one at https://mozilla.org/MPL/2.0/.
# This file is part of NF Compose
# [2019] - [2024] © NeuroForge GmbH & Co. KG

from dataclasses import dataclass, field
from typing import Optional, Dict, Any, List

from dataclasses_json import dataclass_json, Undefined

from compose_client.library.models.diff.mixin import EmptyMixin
from compose_client.library.models.operation.general import ExternalIdOperation, Operation, NameOperation


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class EngineDefinitionDiff(EmptyMixin):
    """
    A complete Engine Definition that we can
    instantiate on any given NF Compose instance
    """
    external_id: str
    engine: Optional[ExternalIdOperation]
    secret: Optional[Operation]
    group_permissions: List[NameOperation] = field(default_factory=list)

    @staticmethod
    def from_dict(dict: Dict[str, Any]) -> 'EngineDefinitionDiff': ...

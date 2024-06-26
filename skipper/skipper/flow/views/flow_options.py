# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. 
# If a copy of the MPL was not distributed with this file, 
# You can obtain one at https://mozilla.org/MPL/2.0/.
# This file is part of NF Compose
# [2019] - [2024] © NeuroForge GmbH & Co. KG


from typing import Optional

from django.http import HttpRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import AllowAny
from .content_negotiation import no_content_negotiation_api_view


@csrf_exempt
@no_content_negotiation_api_view(['OPTIONS'])  # type: ignore
@permission_classes([AllowAny])
def flow_options_view(request: HttpRequest, path: Optional[str] = None) -> HttpResponse:
    # noop view, we redirect to this for OPTIONS calls
    return HttpResponse(status=status.HTTP_200_OK)

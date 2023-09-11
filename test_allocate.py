"""Copyright © 2023 CrowdANALYTIX, Inc. - All Rights Reserved

Unauthorized copying of this file, via any medium is strictly prohibited.
CrowdANALYTIX owns the intellectual property in this source code unless
otherwise stated expressly.

Proprietary and confidential.

Authors:
  - Diva D <diva.d@crowdanalytix.com>, date: 11 September 2023
Project: code
"""
import pytest

from model import Batch, allocate, OrderLine, OutOfStock
from test_model import today


def test_raises_out_of_stock_exception_if_cannot_allocate():
    batch = Batch("batch1", "SMALL-FORK", 10, eta=today)
    allocate(OrderLine("order1", "SMALL-FORK", 10), [batch])

    with pytest.raises(OutOfStock, match="SMALL-FORK"):
        allocate(OrderLine("order2", "SMALL-FORK", 1), [batch])
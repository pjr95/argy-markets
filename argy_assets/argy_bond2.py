import numpy as np
import os
from datetime import date
from bonds import BondCashFlow, SovereignBond

dates_al29 = ["2020-09-04", "2021-07-09", "2022-01-09", "2022-07-09","2023-01-09", "2023-07-09", "2024-01-09",
             "2024-07-09","2025-01-09", "2025-07-09", "2026-01-09", "2026-07-09","2027-01-09", "2027-07-09",
             "2028-01-09", "2028-07-09","2029-01-09", "2029-07-09"]

dates_al29 = [date.fromisoformat(item) for item in dates_al29]

rent_al29 = [None, 0.84722] + [0.5] * 7 + [0.45, 0.40, 0.35, 0.3, 0.25, 0.20, 0.15, 0.1, 0.05]

amortisation_al29 = [None] * 8 + [10] * 10

netflow_al29 = [-100, 0.847] + [0.5] * 6 + [10.5, 10.45, 10.4, 10.35, 10.3, 10.25, 10.2, 10.15, 10.1, 10.05]

couponrate_al29 = [None] + [0.01] * 17

residualvalue_al29 = [-100] * 8 + [-90, -80, -70, -60, -50, -40, -30, -20, -10, 0]

cf_al29 = BondCashFlow(dates_al29, rent_al29, amortisation_al29,netflow_al29,
 couponrate_al29,residualvalue_al29)

al29 = SovereignBond('AL29D',cf_al29, date.fromisoformat('2029-07-09'), 'Bonar')
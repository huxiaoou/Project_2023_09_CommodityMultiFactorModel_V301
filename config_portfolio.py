selected_raw_factors = (
    "BASISA120",
    "CTP120",
    "RSBR240",
    "SKEW010",
    "SKEW120",
    "CVP180LD020",
    "TSA180",
    "MTMS240",
    "BETA020",
    "VOL020",
    "RSI010",
    "IBETA240LD020",
    "NETDOIBD020",
    "SIZEBR010",
    "RVOL010LD020",
    "HRA060",
    "LIQUIDA180",
    "LIQUIDBD010",
)

selected_neu_factors = (
    "CTP120",
    "SKEW010",
    "MTM",
    "BASISA120",
    "LIQUIDBD010",
    "CSP060",
    "NETDOIWLD240",
    "CVP180LD060",
    "RSBR010",
    "RSLR240",
    "TSA180",
    "NETDOIA240",
    "SIZEA180",
    "SRLD060",
)

selected_raw_factors_and_uni_prop = (
    ("BASISA060", 0.3),
    ("BASISBD120", 0.2),
    ("CSP060", 0.3),
    ("CSP180LD020", 0.4),
    ("CTP120", 0.4),
    ("CTP180LD020", 0.4),
    ("CVP120", 0.3),
    ("CVP180LD020", 0.4),
    ("RSBR180", 0.4),
    ("RSLR240", 0.3),
    ("SKEW010", 0.4),
    ("SKEW010LD060", 0.4),
    ("HRA060", 0.4),
    ("SRLD060", 0.3),
    ("TSA060", 0.4),
    ("TSBD010", 0.4),
    ("LIQUIDBD010", 0.2),
    ("NETDOI", 0.2),
    ("NETDOIBD120", 0.2),
)

selected_neu_factors_and_uni_prop = (
    ("BASISA060", 0.4),
    ("BASISBD010", 0.4),
    ("CSP180", 0.4),
    ("CSP120LD020", 0.4),
    ("CTP120", 0.4),
    ("CTP180LD060", 0.4),
    ("CVP120", 0.2),
    ("CVP180LD060", 0.4),
    ("LIQUIDBD010", 0.3),
    ("NETDOIWA020", 0.3),
    ("RSLR240", 0.3),
    ("SKEW010LD060", 0.4),
)

selected_raw_factors_and_uni_prop_ma = (
    ("BASISA060", 0.3, 10),
    ("CSP060", 0.3, 5),
    ("CSP180LD020", 0.4, 5),
    ("CTP120", 0.3, 5),
    ("CTP180LD020", 0.4, 5),
    ("CVP120", 0.2, 5),
    ("CVP180LD020", 0.4, 15),
    ("RSBR240", 0.4, 5),
    ("RSLR240", 0.3, 5),
    ("SKEW010", 0.2, 5),
    ("SKEW010LD060", 0.4, 5),
    ("HRA060", 0.4, 5),
    ("TSA060", 0.4, 5),
    ("NETDOIBD020", 0.2, 5),
)

selected_neu_factors_and_uni_prop_ma = (
    ("BASISA060", 0.4, 15),
    ("CSP120", 0.4, 5),
    ("CSP180LD020", 0.4, 15),
    ("CTP120", 0.4, 5),
    ("CTP180LD060", 0.4, 5),
    ("CVP120", 0.2, 15),
    ("CVP180LD060", 0.4, 15),
    ("NETDOIWA020", 0.3, 5),
    ("NETDOIWBD180", 0.2, 15),
    ("RSBR240", 0.4, 5),
    ("RSLR240", 0.4, 5),
    ("SKEW010", 0.2, 5),
    ("SKEW010LD060", 0.4, 5),
    ("SKEW180LD020", 0.2, 5),

    # ("BASISA060", 0.2, 5),
    # ("CSP120", 0.2, 5),
    # ("CSP180LD020", 0.2, 5),
    # ("CTP120", 0.2, 5),
    # ("CTP180LD060", 0.2, 5),
    # ("CVP120", 0.2, 5),
    # ("CVP180LD060", 0.2, 5),
    # ("NETDOIWA020", 0.2, 5),
    # ("NETDOIWBD180", 0.2, 5),
    # ("RSBR240", 0.2, 5),
    # ("RSLR240", 0.2, 5),
    # ("SKEW010", 0.2, 5),
    # ("SKEW010LD060", 0.2, 5),
    # ("SKEW180LD020", 0.2, 5),
)

src_signal_ids_raw = [f"{fac}_UHP{int(uhp * 10):02d}" for fac, uhp in selected_raw_factors_and_uni_prop]
src_signal_ids_neu = [f"{fac}_WS_UHP{int(uhp * 10):02d}" for fac, uhp in selected_neu_factors_and_uni_prop]
src_signal_ids_raw_ma = [f"{fac}_UHP{int(uhp * 10):02d}_MA{maw:02d}" for fac, uhp, maw in selected_raw_factors_and_uni_prop_ma]
src_signal_ids_neu_ma = [f"{fac}_WS_UHP{int(uhp * 10):02d}_MA{maw:02d}" for fac, uhp, maw in selected_neu_factors_and_uni_prop_ma]
size_raw, size_raw_ma = len(src_signal_ids_raw), len(src_signal_ids_raw_ma)
size_neu, size_neu_ma = len(src_signal_ids_neu), len(src_signal_ids_neu_ma)

trn_win, lbd = 3, 20  # optimized
# trn_win, lbd = 1, 20  # test
min_model_days = int(trn_win * 20 * 0.9)
test_portfolio_ids = [
    "raw_fix",
    "neu_fix",
    "raw_min_uty_con",
    "neu_min_uty_con",
    "raw_fix_ma",
    "neu_fix_ma",
    "raw_min_uty_con_ma",
    "neu_min_uty_con_ma",
]

# unilateral hold proportion
uni_props = (0.2, 0.3, 0.4)
mov_ave_wins = (5, 10, 15)

# secondary parameters
cost_rate_hedge_test = 0e-4
cost_rate_portfolios = 5e-4
risk_free_rate = 0
performance_indicators = [
    "hold_period_return",
    "annual_return",
    "annual_volatility",
    "sharpe_ratio",
    "calmar_ratio",
    "max_drawdown_scale",
    "max_drawdown_scale_idx",
]

if __name__ == "__main__":
    from config_factor import factors_raw
    print("\n".join(factors_raw))
    print("Total number of factors = {}".format(len(factors_raw)))  # 410

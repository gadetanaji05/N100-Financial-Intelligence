import pandas as pd

def net_profit_margin(net_profit, sales):
    """
    Calculate Net Profit Margin
    Formula:
    (Net Profit / Sales) * 100
    """
    if sales == 0:
        return None

    return (net_profit / sales) * 100

def operating_profit_margin(operating_profit, sales):
    """
    Calculate Operating Profit Margin (OPM)
    Formula:
    (Operating Profit / Sales) * 100
    """
    if sales == 0:
        return None

    return (operating_profit / sales) * 100


def return_on_equity(net_profit, shareholder_equity):
    """
    Calculate Return on Equity (ROE)
    Formula:
    (Net Profit / Shareholder Equity) * 100
    """
    if shareholder_equity == 0:
        return None

    return (net_profit / shareholder_equity) * 100

def return_on_capital_employed(ebit, capital_employed):
    """
    Calculate Return on Capital Employed (ROCE)
    Formula:
    (EBIT / Capital Employed) * 100
    """
    if capital_employed == 0:
        return None

    return (ebit / capital_employed) * 100

def return_on_assets(net_profit, total_assets):
    """
    Calculate Return on Assets (ROA)
    Formula:
    (Net Profit / Total Assets) * 100
    """
    if total_assets == 0:
        return None

    return (net_profit / total_assets) * 100

def debt_to_equity(total_debt, shareholder_equity):
    """
    Calculate Debt to Equity Ratio
    Formula:
    Total Debt / Shareholder Equity
    """
    if shareholder_equity == 0:
        return None

    return total_debt / shareholder_equity

def interest_coverage_ratio(ebit, interest_expense):
    """
    Calculate Interest Coverage Ratio (ICR)
    Formula:
    EBIT / Interest Expense
    """
    if interest_expense == 0:
        return None

    return ebit / interest_expense

def net_debt(total_debt, cash_and_cash_equivalents):
    """
    Calculate Net Debt
    Formula:
    Total Debt - Cash and Cash Equivalents
    """
    return total_debt - cash_and_cash_equivalents

def asset_turnover(net_sales, total_assets):
    """
    Calculate Asset Turnover Ratio
    Formula:
    Net Sales / Total Assets
    """
    if total_assets == 0:
        return None

    return net_sales / total_assets

def revenue_cagr(beginning_revenue, ending_revenue, years):
    """
    Calculate Revenue CAGR
    Formula:
    ((Ending Revenue / Beginning Revenue) ** (1 / Years) - 1) * 100
    """
    if beginning_revenue <= 0 or ending_revenue <= 0 or years <= 0:
        return None

    return ((ending_revenue / beginning_revenue) ** (1 / years) - 1) * 100

def profit_cagr(beginning_profit, ending_profit, years):
    """
    Calculate Profit CAGR
    Formula:
    ((Ending Profit / Beginning Profit) ** (1 / Years) - 1) * 100
    """
    if beginning_profit <= 0 or ending_profit <= 0 or years <= 0:
        return None

    return ((ending_profit / beginning_profit) ** (1 / years) - 1) * 100

def eps_cagr(beginning_eps, ending_eps, years):
    """
    Calculate EPS CAGR
    Formula:
    ((Ending EPS / Beginning EPS) ** (1 / Years) - 1) * 100
    """
    if beginning_eps <= 0 or ending_eps <= 0 or years <= 0:
        return None

    return ((ending_eps / beginning_eps) ** (1 / years) - 1) * 100

def free_cash_flow(operating_cash_flow, capital_expenditure):
    """
    Calculate Free Cash Flow (FCF)
    Formula:
    Operating Cash Flow - Capital Expenditure
    """
    return operating_cash_flow - capital_expenditure

def cfo_quality_score(cash_flow_from_operations, net_profit):
    """
    Calculate CFO Quality Score
    Formula:
    Cash Flow from Operations / Net Profit
    """
    if net_profit == 0:
        return None

    return cash_flow_from_operations / net_profit

def capex_intensity(capital_expenditure, operating_cash_flow):
    """
    Calculate CapEx Intensity
    Formula:
    Capital Expenditure / Operating Cash Flow
    """
    if operating_cash_flow == 0:
        return None

    return capital_expenditure / operating_cash_flow

def fcf_conversion(free_cash_flow, net_profit):
    """
    Calculate FCF Conversion
    Formula:
    Free Cash Flow / Net Profit
    """
    if net_profit == 0:
        return None

    return free_cash_flow / net_profit

def capital_allocation_ratio(dividends_paid, share_buyback, free_cash_flow):
    """
    Calculate Capital Allocation Ratio
    Formula:
    (Dividends Paid + Share Buyback) / Free Cash Flow
    """
    if free_cash_flow == 0:
        return None

    return (dividends_paid + share_buyback) / free_cash_flow



if __name__ == "__main__":
    print("Net Profit Margin:", net_profit_margin(500, 2000))
    print("Operating Profit Margin:", operating_profit_margin(600, 2000))
    print("ROE:", return_on_equity(500, 2500))
    print("ROCE:", return_on_capital_employed(800, 4000))
    print("ROA:", return_on_assets(500, 10000))
    print("Debt to Equity:", debt_to_equity(1000, 2000))
    print("Interest Coverage Ratio:", interest_coverage_ratio(1000, 200))
    print("Net Debt:", net_debt(1000, 300))
    print("Asset Turnover:", asset_turnover(5000, 2500))
    print("Revenue CAGR:", revenue_cagr(100, 200, 5))
    print("Profit CAGR:", profit_cagr(100, 180, 5))
    print("EPS CAGR:", eps_cagr(10, 20, 5))
    print("Free Cash Flow:", free_cash_flow(5000, 1500))
    print("CFO Quality Score:", cfo_quality_score(1200, 1000))
    print("CapEx Intensity:", capex_intensity(500, 2500))
    print("FCF Conversion:", fcf_conversion(800, 1000))
    print("Capital Allocation Ratio:", capital_allocation_ratio(200, 100, 1000))
Hours = 45
Rate = 10
if Hours > 40:
    Regular_Pay = (40 * Rate)
    Overtime_Pay = int[(Hours - 40) * (Rate * 1.5)]
    Total_Pay = Regular_Pay + Overtime_Pay
    print Total_Pay


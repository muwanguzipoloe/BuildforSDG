
def estimator():
    region = {
      'name': "Africa",
      'avgAge': 19.7,
      'avgDailyIncomeInUSD': 5,
      'avgDailyIncomePopulation': 0.71
    }
    updates = {
      'periodType': "days",
      'timeToElapse': 58,
      'reportedCases': 674,
      'population': 66622705,
      'totalHospitalBeds': 1380614
    }

#  marging region and updates into one dictionary region and saving region as data to reurned.
    region.update(updates)
    data=region           
# your best case estimation are saved as a dictionary with a number of calculations from the data.
    x=region['reportedCases']*10

# infectionsByRequestedTime = currentlyInfected * 2 ** a  (where a = z / 3) where z = requestedTime.
    
    g=int(input('Please enter number of days to estimate infection by days from today\n'))

# 35% of total hospital beds 

    l=(region['totalHospitalBeds'])*0.35


# Number of days g divided by 3 saved into z .

    z=int(g/3)
    
# infectionsByRequestedTime for impact
    e=x*2**z

# 15% of infections by requested Time.
    h=int(0.15*e)
# number of hospital beds by requested time.
    j=int(l-h)
# 5% of of infections by requested date.
    m=int(0.05*e)
# 2% of infections by requested time
    o=int(0.02*e)
# dollars in flight , estimate of how much money econemy is likely to lose
    q=int(e*0.71*5/g)
    impact={
        'currentlyInfected':x,
        'infectionsByRequestedTime':e,
        'severeCasesByRequestedTime':h,
        'hospitalBedsByRequestedTime':j, 
        'casesForICUByRequestedTime':m,
        'casesForVentilatorsByRequestedTime':o,
        'dollarsInFlight':q}
#   severe case estimation 
    y=region['reportedCases']*50
# infectionsByRequestedTime for severeImpact
    f=y*2**z
# 15% of infections by requested Time.
    i=int (0.15*f)
# number of hospital beds by requested time.
    k=int(l-i)
# 5% of of infections by requested date.
    n=int(0.05*f)
# 2% of infections by requested time
    p=int(0.02*f)
# dollars in flight , estimate of how much money econemy is likely to lose
    r=int(f*0.71*5/g)
    severeImpact={
          'currentlyInfected':y,
          'infectionsByRequestedTime':f,
          'severeCasesByRequestedTime':i,
          'hospitalBedsByRequestedTime':k,
          'casesForICUByRequestedTime':n,
          'casesForVentilatorsByRequestedTime':p,
          'dollarsInFlight':r}         
    print('Data:\n',data,'\nImpact:\n',impact,'\nSevere Impact:\n',severeImpact)
estimator()





 

'''
Classes from the 'SleepHealth' framework.
'''

try:
    from rubicon.objc import ObjCClass
except ValueError:
    def ObjCClass(name):
        return None


def _Class(name):
    try:
        return ObjCClass(name)
    except NameError:
        return None

    
HKSHSleepDaySummary = _Class('HKSHSleepDaySummary')
HKSleepHealthStore = _Class('HKSleepHealthStore')
HKSHSleepPeriod = _Class('HKSHSleepPeriod')
HKSHSleepPeriodSegment = _Class('HKSHSleepPeriodSegment')
HKSHGoalProgressEngine = _Class('HKSHGoalProgressEngine')
HKSHGoalProgress = _Class('HKSHGoalProgress')
HKSHSleepDaySummaryQuery = _Class('HKSHSleepDaySummaryQuery')
HKSHSleepDaySummaryQueryConfiguration = _Class('HKSHSleepDaySummaryQueryConfiguration')

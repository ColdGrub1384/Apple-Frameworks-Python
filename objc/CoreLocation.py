'''
Classes from the 'CoreLocation' framework.
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

    
CLFloor = _Class('CLFloor')
CLLocationInternal = _Class('CLLocationInternal')
CLHarvester = _Class('CLHarvester')
CLReductiveFilterOptions = _Class('CLReductiveFilterOptions')
CLPlacemarkInternal = _Class('CLPlacemarkInternal')
CLLocationInternalClient = _Class('CLLocationInternalClient')
CLGeocoder = _Class('CLGeocoder')
CLGeocoderInternal = _Class('CLGeocoderInternal')
CLVisit = _Class('CLVisit')
CLVehicleSpeed = _Class('CLVehicleSpeed')
CLVehicleSpeedInternal = _Class('CLVehicleSpeedInternal')
CLVehicleHeading = _Class('CLVehicleHeading')
CLVehicleHeadingInternal = _Class('CLVehicleHeadingInternal')
CLBeaconIdentityConstraint = _Class('CLBeaconIdentityConstraint')
CLSimulationManager = _Class('CLSimulationManager')
CLBeacon = _Class('CLBeacon')
CLBeaconInternal = _Class('CLBeaconInternal')
CLRegion = _Class('CLRegion')
CLBeaconRegion = _Class('CLBeaconRegion')
CLCircularRegion = _Class('CLCircularRegion')
CLRegionInternal = _Class('CLRegionInternal')
CLHeading = _Class('CLHeading')
CLHeadingInternal = _Class('CLHeadingInternal')
CLLocationMatchInfo = _Class('CLLocationMatchInfo')
CLLocationMatchInfoInternal = _Class('CLLocationMatchInfoInternal')
CLLocationSmoother = _Class('CLLocationSmoother')
CLAssertion = _Class('CLAssertion')
CLLocationIndependenceAssertion = _Class('CLLocationIndependenceAssertion')
CLInUseAssertion = _Class('CLInUseAssertion')
CLEmergencyEnablementAssertion = _Class('CLEmergencyEnablementAssertion')
CLLocationManagerRoutine = _Class('CLLocationManagerRoutine')
CLPlacemark = _Class('CLPlacemark')
CLLocation = _Class('CLLocation')
CLStateTracker = _Class('CLStateTracker')
CLLocationManagerStateTracker = _Class('CLLocationManagerStateTracker')
CLLocationManagerInternal = _Class('CLLocationManagerInternal')
CLLocationManager = _Class('CLLocationManager')

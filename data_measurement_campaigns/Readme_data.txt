 #################################################################################################
 ## Description of measurement Campaigns Carried out in Lebanon                                 ##
 #################################################################################################

 This ditectory contains the set of data measurements carried out in 
 different environments: Rural, Urban, Indoor, Campus

 #################################################################################################
                              Rural measurements in Bekaa valley 
 #################################################################################################
 Rural_Bekaa contains 3 CSV files:
 csv_rural_1_5m : measurements with end-device antenna heights of 1.5 m
 csv_rural_3m: measurements with end-device antenna heights of 3 m
 csv_rural_20cm: measurements with end-device antenna heights of 20 cm

 Each CSV files contains the following information:
 -------------------------------------------------------------------------------------------------
 DevName | Freq | RSSI | SNR | SF | BW | CR | Time | Seq | Payload | Lat | Long | Dist | Prx| PL
 -------------------------------------------------------------------------------------------------
 DeVName =  The end-device name
 Frequnecy = Frequency used for transmission
 RSSI = Received signal strength Indicator
 SNR = Signal to noise ratio
 SF = Spreading Factor (12)
 BW = Bandwith of transmision (125 khz)
 CR = Coding Rate (4/5)
 Time = time of transmisison of the uplink packet 
 Seq = sequence of the packet
 Payload = the payload send contains GPS coordinates
 Lat = latitude extracted from Payload
 Long = longitude extracted from Payload
 Dist = distance between the gateway and the end-device
 Prx = Power received at the Gateway 
 PL = the computed Path-loss between the tranmitter and the receiver
 (Note Prx = Ptx + Gtx + Grx -PL , with Ptx = 14dBm, Gtx = Grx = 3 dBi).
 
 #################################################################################################
                             Urban measurements in the city of Beirut
 #################################################################################################
 Urban_Beirut contains 4 CSV files:
 csv_urban_1_5m : measurements with end-device antenna heights of 1.5 m
 csv_urban_1m : measurements with end-device antenna heights of 1m
 csv_urban_3m: measurements with end-device antenna heights of 3 m
 csv_urban_20cm: measurements with end-device antenna heights of 20 cm

 Each CSV files contains the following information (same description as rural above):
 -------------------------------------------------------------------------------------------------
  DevName | Freq | RSSI | SNR | SF | BW | CR | Time | Seq | Payload | Lat | Long | Dist | Prx| PL 
 -------------------------------------------------------------------------------------------------

 #################################################################################################
                     Outdoor measurements around USJ-ESIB Campus 
 #################################################################################################
 csv_Outdoor_Campus = mesauremets in the outdoor around the USJ campus using 3 antennas heights.
 CSV file contains the following information:
 --------------------------------------------------------------------------------------------------------
  DevName | Freq | RSSI | SNR | SF | BW | CR | Time | Seq | Payload | Lat | Long | Dist | Prx| PL |height
 --------------------------------------------------------------------------------------------------------
 height is the hight of end-device antenna in meter.

 #################################################################################################
                     Indoor measurements in multi-floor building in USJ-ESIB Campus
 #################################################################################################
 csv_Indoor_building = mesauremets in indoor contains the following information
 -----------------------------------------------------------------------------
 RSSI | SNR | Freq | Prx | PL | location | lat | long | NB_floor| wall | Dist
 -----------------------------------------------------------------------------
 location = the location inside the building 
 Nb_floor = Number of floors between gateway and end-device
 wall	= Number of walls between gateway and end-device

 #################################################################################################
                    Drive measurements in Beirut and Bekaa
 #################################################################################################
 During drive tests, the end-device is mounted on the roof-top of a car. Car speed 30-40km/h
 csv_Rural_drive: data for drive tests in Bekaa
 csv_Urban_drive: data for drive tests in Beirut


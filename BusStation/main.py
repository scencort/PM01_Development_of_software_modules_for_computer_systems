from BusStation.departure import Avtovokzal

avtovokzal = Avtovokzal()

avtovokzal.load_stations("station.txt")
avtovokzal.load_buses("buses.txt")
avtovokzal.load_trips("trips.txt")

a = avtovokzal.trips_station()
for station_id, count in a.items():
    name_station = avtovokzal.stations[station_id].name
    print(f"{name_station}: {count}")
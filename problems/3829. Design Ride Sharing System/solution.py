class RideSharingSystem:
    def __init__(self):
        self.riders = []
        self.drivers = []
        self.timestamp = 0
    
    def addRider(self, riderId: int) -> None:
        self.riders.append((riderId, self.timestamp))
        self.timestamp += 1
    
    def addDriver(self, driverId: int) -> None:
        self.drivers.append((driverId, self.timestamp))
        self.timestamp += 1
    
    def matchDriverWithRider(self) -> list[int]:
        if self.drivers and self.riders:
            driver_id, _ = self.drivers.pop(0)
            rider_id, _ = self.riders.pop(0)
            return [driver_id, rider_id]
        else:
            return [-1, -1]
    
    def cancelRider(self, riderId: int) -> None:
        self.riders = [(r_id, ts) for r_id, ts in self.riders if r_id != riderId]

# Your RideSharingSystem object will be instantiated and called as such:
# obj = RideSharingSystem()
# obj.addRider(riderId)
# obj.addDriver(driverId)
# param_3 = obj.matchDriverWithRider()
# obj.cancelRider(riderId)
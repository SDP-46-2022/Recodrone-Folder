import rospy
from clover import srv
from recodroneapplication.models import Telemetry

class Drone_Info():
    def get_telemetry(drone):
        rospy.init_node('flight')
        get_telemetry = rospy.ServiceProxy('get_telemetry', srv.GetTelemetry)
        t = get_telemetry()
        telemetry = Telemetry(frame_id=t.frame_id, connected=t.connected, armed=t.armed, mode=t.mode,
        x=t.x, y=t.y, z=t.z, lat=t.lat, lon=t.lon, alt=t.alt, vx=t.vx, vy=t.vy, vz=t.vz, pitch=t.pitch,
        roll=t.roll, yaw=t.yaw, pitch_rate=t.pitch_rate, roll_rate=t.roll_rate, yaw_rate=t.yaw_rate,
        voltage=t.voltage, cell_voltage=t.cell_voltage, drone=drone)
        return telemetry
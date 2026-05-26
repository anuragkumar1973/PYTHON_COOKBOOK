"""
rec4_6_observer.py
Example of the Observer pattern by importing Vehicle from rec4_2.py
Wraps a Vehicle instance to observe state changes (speed).
"""

from rec4_2 import Vehicle  # expected to be in the same package/directory


class ObservableVehicle:
    """A wrapper that makes an existing Vehicle observable without modifying it."""
    def __init__(self, vehicle):
        object.__setattr__(self, "_vehicle", vehicle)
        object.__setattr__(self, "_observers", [])
        object.__setattr__(self, "_last_state", self._get_state())

    def _get_state(self):
        # currently observe only 'speed' attribute (common in vehicle examples)
        return getattr(self._vehicle, "speed", None)

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self):
        state = self._get_state()
        if state != self._last_state:
            for obs in list(self._observers):
                # observer protocol: observer.update(subject, state)
                try:
                    obs.update(self, state)
                except Exception:
                    pass
            object.__setattr__(self, "_last_state", state)

    def __getattr__(self, name):
        attr = getattr(self._vehicle, name)
        if callable(attr):
            def _wrapped(*args, **kwargs):
                result = attr(*args, **kwargs)
                self.notify()
                return result
            return _wrapped
        return attr

    def __setattr__(self, name, value):
        # route writes to the wrapped vehicle (unless internal)
        if name.startswith("_"):
            object.__setattr__(self, name, value)
        else:
            setattr(self._vehicle, name, value)
            self.notify()

    def __repr__(self):
        base = getattr(self._vehicle, "__repr__", lambda: object.__repr__(self._vehicle))()
        return f"<ObservableVehicle wrapping {base}>"


# Observer examples
class SpeedLogger:
    def update(self, subject, speed):
        print(f"[SpeedLogger] {subject}: speed -> {speed}")


class SpeedAlarm:
    def __init__(self, limit):
        self.limit = limit

    def update(self, subject, speed):
        if speed is not None and speed > self.limit:
            print(f"[SpeedAlarm] ALERT: {subject} speed {speed} > limit {self.limit}")


# Demo / usage
if __name__ == "__main__":
    # try to instantiate Vehicle with flexible fallback to avoid TypeError if signature differs
    try:
        v = Vehicle()
    except TypeError:
        try:
            v = Vehicle("DemoVehicle")
        except TypeError:
            try:
                v = Vehicle("Demo", "Vehicle")
            except Exception:
                # last-resort simple mock if importing Vehicle succeeded but could not be constructed
                class _SimpleVehicle:
                    def __init__(self):
                        self.speed = 0

                    def accelerate(self, amt=1):
                        self.speed += amt

                    def decelerate(self, amt=1):
                        self.speed -= amt

                    def __repr__(self):
                        return "<SimpleVehicle>"

                v = _SimpleVehicle()

    ov = ObservableVehicle(v)
    logger = SpeedLogger()
    alarm = SpeedAlarm(limit=50)

    ov.add_observer(logger)
    ov.add_observer(alarm)

    print("Initial:", ov)
    # common vehicle APIs often include accelerate/decelerate or direct speed attribute changes
    if hasattr(ov, "accelerate"):
        ov.accelerate(30)   # notify after call
        ov.accelerate(30)   # should trigger alarm if > 50
    else:
        # direct attribute manipulation fallback
        try:
            ov.speed = (getattr(ov, "speed", 0) + 30)
            ov.speed = (getattr(ov, "speed", 0) + 30)
        except Exception:
            pass

    if hasattr(ov, "decelerate"):
        ov.decelerate(20)
    else:
        try:
            ov.speed = (getattr(ov, "speed", 0) - 20)
        except Exception:
            pass
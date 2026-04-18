class HitObject:
    def __init__(self, start_time: int, lane: int, end_time: int | None = None) -> None:
        self.start_time = start_time
        self.lane = lane
        self.end_time = end_time
    
    def __str__(self) -> str:
        if self.end_time:
            return f"- StartTime: {self.start_time}\n  Lane: {self.lane}\n  EndTime: {self.end_time}\n  KeySounds: []\n"
        else:
            return f"- StartTime: {self.start_time}\n  Lane: {self.lane}\n  KeySounds: []\n"
    
    def __repr__(self) -> str:
        if self.end_time:
            return f"- StartTime: {self.start_time}\n  Lane: {self.lane}\n  EndTime: {self.end_time}\n  KeySounds: []\n"
        else:
            return f"- StartTime: {self.start_time}\n  Lane: {self.lane}\n  KeySounds: []\n"
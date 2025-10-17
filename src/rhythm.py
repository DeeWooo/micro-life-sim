#!/usr/bin/env python3
"""
第A纪：节律生命体
拥有24小时生物钟的数字生命
"""

import json
import math
import os
import signal
import sys
import time
from pathlib import Path


class RhythmLife:
    def __init__(self, state_file="rhythm.json"):
        self.state_file = Path(state_file)
        self.running = True
        self.period = 24 * 3600  # 24小时周期
        
    def load_state(self):
        if not self.state_file.exists():
            return {"start_time": time.time(), "phase": 0.0}
        try:
            with open(self.state_file) as f:
                return json.load(f)
        except:
            return {"start_time": time.time(), "phase": 0.0}
    
    def save_state(self, state):
        tmp = self.state_file.with_suffix('.tmp')
        with open(tmp, 'w') as f:
            json.dump(state, f, separators=(',', ':'))
        os.replace(tmp, self.state_file)
    
    def circadian(self, elapsed):
        return (math.sin(2 * math.pi * elapsed / self.period) + 1) / 2
    
    def symbol(self, val):
        return "🌞" if val >= 0.5 else "🌙"
    
    def run(self):
        state = self.load_state()
        start = state["start_time"]
        
        def stop(sig, frame):
            self.running = False
            self.save_state(state)
            print("\n💤 休眠...")
            sys.exit(0)
        
        signal.signal(signal.SIGINT, stop)
        
        tick = 0
        while self.running:
            elapsed = time.time() - start
            val = self.circadian(elapsed)
            sym = self.symbol(val)
            status = "活跃" if 6 <= val*24 < 22 else "休息"
            
            state.update({"last": val, "tick": tick})
            self.save_state(state)
            
            print(f"[节律] {val:.2f} {sym} {status}")
            tick += 1
            time.sleep(1)

if __name__ == "__main__":
    print("🌱 第A纪启动...")
    RhythmLife().run()

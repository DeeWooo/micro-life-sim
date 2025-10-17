import json, os, sys, time

STEP = 0.01; INTERVAL = 1.0

def load_state(path):
    try:
        with open(path) as f:
            d = json.load(f); return int(d.get('tick', round((1.0 - d.get('dot', 1.0))/STEP)))
    except FileNotFoundError:
        return 0
    except json.JSONDecodeError:
        print('invalid dot.json, please remove it'); sys.exit(1)

def save_state(path, tick):
    data = {"dot": round(max(0.0, 1.0 - STEP * tick), 2), "tick": tick}
    tmp = path + '.tmp'
    with open(tmp, 'w') as f: json.dump(data, f, separators=(',', ':'))
    os.replace(tmp, path)

def main():
    path = os.path.join(os.path.dirname(__file__), 'dot.json')
    tick = load_state(path)
    dot = max(0.0, 1.0 - STEP * tick)
    if dot <= 0:
        print('💀 dot has evaporated'); return
    try:
        while dot > 0:
            print(f"[tick {tick}] dot = {dot:.2f}", flush=True)
            save_state(path, tick)
            time.sleep(INTERVAL)
            tick += 1; dot = max(0.0, 1.0 - STEP * tick)
    except KeyboardInterrupt:
        save_state(path, tick); sys.exit(0)
    print('💀 dot has evaporated')

if __name__ == '__main__':
    main()



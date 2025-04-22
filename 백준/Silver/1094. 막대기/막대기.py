x = int(input())
lines = [64]
while True:
    total = sum(lines)
    if total > x:
        min_line = min(lines)
        lines.remove(min_line)
        half = min_line / 2
        if total - half >= x:
            lines.append(half)
        else:
            lines.extend([half, half])
    else:
        break

print(len(lines))
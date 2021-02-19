

def all_clean(room_map):
    clear_rows = []
    for row in room_map:
        not_cleared = [i for i in row if i == 1]

        if not any(not_cleared):
            clear_rows.append(1)

    if len(clear_rows) == len(room_map):
        return True

    return False

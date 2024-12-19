
data = []

with open('input.txt') as f:
    data = list(f.readline().rstrip('\n'))

file_blocks = []

def convert_data_to_file_blocks():
    global file_blocks
    curr_file_index = 0
    is_file_size = True
    for char in data:
        digit = int(char)
        if is_file_size:
            file_blocks += [curr_file_index for _ in range(digit)]
            is_file_size = False
            curr_file_index += 1
        else:
            file_blocks += ['.' for _ in range(digit)]
            is_file_size = True

def calculate_checksum():
    result = 0
    for i, num in enumerate(file_blocks):
        if num == '.':
            continue
        result += i * num
    return result

def solve_part_one():
    convert_data_to_file_blocks()
    file_block_to_move_index = len(file_blocks) - 1
    free_space_index = file_blocks.index('.')
    while file_block_to_move_index > free_space_index:
        file_blocks[free_space_index] = file_blocks[file_block_to_move_index]
        file_blocks[file_block_to_move_index] = '.'
        free_space_index = file_blocks.index('.', free_space_index)
        while file_blocks[file_block_to_move_index] == '.':
            file_block_to_move_index -= 1
    print(calculate_checksum())

solve_part_one()

def solve_part_two():
    file_blocks.clear()
    convert_data_to_file_blocks()
    curr_file_id_index = len(file_blocks) - 1
    while curr_file_id_index > 0:
        # Find the current file id to move
        while file_blocks[curr_file_id_index] == '.':
            curr_file_id_index -= 1
        curr_file_id = file_blocks[curr_file_id_index]
        # count amount of blocks to move
        amount_to_move = 0
        while file_blocks[curr_file_id_index] == curr_file_id:
            curr_file_id_index -= 1
            amount_to_move += 1
        curr_file_id_index += amount_to_move
        # Find the empty space to move the file to
        empty_space_index = 0
        size_of_empty_space = 0
        while empty_space_index < curr_file_id_index:
            size_of_empty_space = 0
            # find the closest empty space
            empty_space_index_start = file_blocks.index('.', empty_space_index)
            # count the size of the empty space
            empty_space_index = empty_space_index_start
            while file_blocks[empty_space_index] == '.' and empty_space_index < curr_file_id_index:
                size_of_empty_space += 1
                empty_space_index += 1
            if size_of_empty_space >= amount_to_move:
                empty_space_index = empty_space_index_start
                break
        # move the file if space is available
        if size_of_empty_space >= amount_to_move:
            while amount_to_move:
                file_blocks[curr_file_id_index] = '.'
                file_blocks[empty_space_index] = curr_file_id
                amount_to_move -= 1
                empty_space_index += 1
                curr_file_id_index -= 1
        curr_file_id_index -= amount_to_move
    print(calculate_checksum())

solve_part_two()
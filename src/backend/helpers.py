'''
utilities
'''

import GPUtil
import constants as c

def check_gpu_availability():
    '''
    check if gpu is available
    '''
    gpu_lists = GPUtil.getGPUs()

    assert(len(gpu_lists) != 0)
    del(gpu_lists)  


def get_start_and_end_indexes_per_segment(wave_file_length, process_index, byte_rate):
    '''
    creates a tuple containing indexes of start and end of a wave file segment
    '''
    chunk_length_in_bytes = (c.STEP)*byte_rate
    start_index = int(process_index * chunk_length_in_bytes)
    end_index = int(min(start_index + chunk_length_in_bytes, wave_file_length))
    return (start_index, end_index)


def get_timestamp(text_register: list, input: str):
    # Check if the input substring can be found in the text_register strings
    timestamps_list = []
    # Go through each line of the text_register
    for i in range(len(text_register)):
        if text_register[i][1].find(input) != -1:
            # Add the index in text_register converted in seconds
            timestamps_list.append((i + 1) * c.STEP)
        else:
            print("No matchs for the input string")
    return timestamps_list

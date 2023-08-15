# Specify the file path where the text replacements will be performed
file_path = 'on_robot_script.txt'

# Define a dictionary containing the text replacements to be made in the file
replacement_dict = {
    'or_vgp.set_grip(0, or_vgp.ALL_CH)': 'set_digital_output(7, ON)',
    'or_vgp.grip(0, <grip_value>, True)': '',  # Placeholder for grip_value
    'or_vgp.release(0, True, or_vgp.ALL_CH)': 'set_digital_output(7, OFF)'
}

# Function to replace text in a file based on the provided replacement dictionary
def replace_with_dict_values(file_path, replacement_dict):
    try:
        # Open the file for reading
        with open(file_path, 'r') as file:
            file_contents = file.read()

        # Perform text replacements
        for search_text, replacement_text in replacement_dict.items():
            file_contents = file_contents.replace(search_text, replacement_text)

        # Open the file for writing and save the modified contents
        with open(file_path, 'w') as file:
            file.write(file_contents)

        print('Text replacements completed and saved successfully.')
    except FileNotFoundError:
        print('File not found.')
    except Exception as e:
        print(f'An error occurred: {e}')

# Function to extract the actual grip value from the file contents
def get_actual_grip_value(file_contents):
    start_index = file_contents.find('or_vgp.grip(0, ') + len('or_vgp.grip(0, ')
    end_index = file_contents.find(',', start_index)
    actual_grip_value = file_contents[start_index:end_index]
    return actual_grip_value

try:
    # Open the file for reading
    with open(file_path, 'r') as file:
        file_contents = file.read()

    # Extract the actual grip value from the file
    actual_grip_value = get_actual_grip_value(file_contents)

    # Update the replacement_dict with the actual grip value
    replacement_dict[f'or_vgp.grip(0, {actual_grip_value}, True)'] = ''

    # Perform text replacements using the replacement_dict
    replace_with_dict_values(file_path, replacement_dict)
except FileNotFoundError:
    print('File not found.')
except Exception as e:
    print(f'An error occurred: {e}')

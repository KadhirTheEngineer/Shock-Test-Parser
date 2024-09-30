import csv
import re

def extract_data(line):
    # Use regular expressions to find Distance and AvgWeight values
    distance_match = re.search(r'Distance:\s*([0-9.]+)', line)
    avg_weight_match = re.search(r'AvgWeight:\s*([0-9.]+)', line)

    # Check if matches were found
    if distance_match and avg_weight_match:
        distance = distance_match.group(1)
        avg_weight = avg_weight_match.group(1)
        return distance, avg_weight
    else:
        return None, None

def process_log(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        csv_writer = csv.writer(outfile)
        csv_writer.writerow(['Distance', 'AvgWeight'])

        for line in infile:
            if "Reading:" in line:
                distance, avg_weight = extract_data(line)
                if distance is not None and avg_weight is not None:
                    csv_writer.writerow([distance, avg_weight])
                else:
                    print(f"Warning: Unable to extract data from line: {line.strip()}")

if __name__ == "__main__":
    input_file_path = 'shock test 6 middle setting 150 psi.log' #change this to desired log file.
    output_file_path = '0_middle_150.csv' #Change this to output file

    process_log(input_file_path, output_file_path)
    print("CSV file created successfully.")

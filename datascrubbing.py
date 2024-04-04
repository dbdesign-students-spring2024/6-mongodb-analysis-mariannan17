import csv

def clean_data(raw_data):
    cleaned_data = []
    for row in raw_data:
        # Parse the row using csv.reader
        cleaned_row = [value for idx, value in enumerate(row) if idx not in [3, 4, 29, 49, 55]]  
        cleaned_data.append(cleaned_row)
    return cleaned_data

def main():
    with open("data/listings.csv", "r", encoding="utf-8") as file:
        # Use csv.reader directly on the file object
        raw_data = csv.reader(file)
        cleaned_data = clean_data(raw_data)

    print("Number of rows after cleaning:", len(cleaned_data))  # Print number of rows
    with open("data/listings_clean.csv", "w", encoding="utf-8", newline='') as file:
        writer = csv.writer(file)
        writer.writerows(cleaned_data)

    print("Data cleaning completed. Output written to listings_clean.csv")

if __name__ == "__main__":
    main()

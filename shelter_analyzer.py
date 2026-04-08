"""
Hawaii Hurricane Shelter Data Analyzer

Author: Andrew Zeidler
This script reads hurricane shelter data from a CSV file, summarizes key shelter
features, and allows the user to search shelters by zip code.
"""

import csv


# Reads CSV file and converts each row into a cleaned dictionary
def read_data(filename):
    shelters = []

    with open(filename, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            shelter = {
                "name": row["Hurricane Shelter"].strip(),
                "special_needs": row["Special Needs"].strip(),
                "pet_friendly": row["Pet Friendly"].strip(),
                "island": row["Island"].strip(),
                "zip_code": row["Zip Code"].strip(),
                "location": row["Location 1"].strip()
            }
            shelters.append(shelter)

    return shelters


 # Returns total number of shelters
def count_total_shelters(shelters):
    return len(shelters)


# Counts number of shelters on each island
def count_by_island(shelters):
    island_counts = {} 

    for shelter in shelters:
        island = shelter["island"]

        if island in island_counts:
            island_counts[island] += 1
        else:
            island_counts[island] = 1

    return island_counts


# Counts total shelters that support special needs
def count_special_needs_shelters(shelters):
    count = 0

    for shelter in shelters:
        if shelter["special_needs"].upper() == "S":
            count += 1

    return count


# Counts shelters that allow pets
def count_pet_friendly_shelters(shelters):
    count = 0

    for shelter in shelters:
        if shelter["pet_friendly"].upper() == "P":
            count += 1

    return count


# Finds shelters matching a given zip code and returns their names and locations
def find_shelters_by_zip(shelters, zip_code):
    matches = []

    for shelter in shelters:
        if shelter["zip_code"] == zip_code:
            matches.append({
                "name": shelter["name"],
                "location": shelter["location"]
            })

    return matches


# Main function to orchestrate data loading, analysis, and user interaction
def main():
    # Load shelter data from CSV file
    filename = "hawaii_shelters.csv"
    shelters = read_data(filename)

    # Generate summary statistics
    total = count_total_shelters(shelters)
    island_counts = count_by_island(shelters)
    special_needs_count = count_special_needs_shelters(shelters)
    pet_friendly_count = count_pet_friendly_shelters(shelters)

    # Display summary results
    print("\n--- Hawaii Hurricane Shelter Data Summary ---")
    print(f"Total shelters: {total}")
    print(f"Special-needs shelters: {special_needs_count}")
    print(f"Pet-friendly shelters: {pet_friendly_count}")

    print("\nShelters by island:")
    for island, count in sorted(island_counts.items()):
        print(f"- {island}: {count}")
    

    # Allow user to search for shelters by zip code
    user_zip = input("\nEnter a zip code to find shelters: ")
    results = find_shelters_by_zip(shelters, user_zip)

    # Display search results
    print(f"\n---Shelters in {user_zip} Zip Code---")

    if results:
        for shelter in results:
            print(f"\n{shelter['name']}")
            print(f"Location: {shelter['location']}")
    else:
        print("No shelters found for that zip code.")   


if __name__ == "__main__":
    main()
#!/bin/bash

# Initialize page number
page=1

# Fetch data using curl until response status code is not 200
while true
do
    url="https://api.rawg.io/api/games?dates=2023-01-01,2023-06-30&key=682f1fd867e1480fbf1b9cf461f4a1ee&page_size=40&page=$page"
    response=$(curl -s -o "rawg_data_page_$page.json" -w "%{http_code}" "$url")  # Save data to a JSON file and append the HTTP status code to the response

    # Extract the response code
    response_code=$(tail -n 1 <<< "$response")

    # Remove the response code from the data
    data=${response%"$response_code"}

    # Check if the response code is not 200
    if [ "$response_code" -ne 200 ]; then
        echo "Error: Failed to fetch data from page $page (HTTP Status Code: $response_code)"
        break
    fi

    # Increment page number
    ((page++))
done

# Move all .json files to ~/temp_data directory
mkdir -p ~/temp_data  # Create the temp_data directory if it doesn't exist
mv *.json ~/temp_data/
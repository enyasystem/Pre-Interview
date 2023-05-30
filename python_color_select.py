import re
from statistics import mode, median
from collections import Counter
import psycopg2
from psycopg2 import Error
import random

# Function to extract colors from the HTML table
def extract_colors(html_code):
    color_pattern = r'([A-Z]+)'
        colors = re.findall(color_pattern, html_code.upper())
            return colors

            # Function to calculate the mean color
            def calculate_mean_color(colors):
                color_counts = Counter(colors)
                    mean_color = color_counts.most_common(1)[0][0]
                        return mean_color

                        # Function to calculate the mode color
                        def calculate_mode_color(colors):
                            mode_color = mode(colors)
                                return mode_color

                                # Function to calculate the median color
                                def calculate_median_color(colors):
                                    median_color = median(colors)
                                        return median_color

                                        # Function to calculate the variance of colors
                                        def calculate_color_variance(colors):
                                            color_counts = Counter(colors)
                                                color_frequencies = list(color_counts.values())
                                                    mean_frequency = sum(color_frequencies) / len(color_frequencies)
                                                        variance = sum((count - mean_frequency) ** 2 for count in color_frequencies) / len(color_frequencies)
                                                            return variance

                                                            # Function to save colors and their frequencies in PostgreSQL database
                                                            def save_colors_to_database(colors):
                                                                try:
                                                                        # Connect to the PostgreSQL database
                                                                                connection = psycopg2.connect(
                                                                                            host="localhost",
                                                                                                        database="your_database",
                                                                                                                    user="root",
                                                                                                                                password="225Enya"
                                                                                                                                        )

                                                                                                                                                # Create a cursor object
                                                                                                                                                        cursor = connection.cursor()

                                                                                                                                                                # Create the colors table if it doesn't exist
                                                                                                                                                                        create_table_query = "CREATE TABLE IF NOT EXISTS colors (color TEXT, frequency INT)"
                                                                                                                                                                                cursor.execute(create_table_query)

                                                                                                                                                                                        # Clear existing data from the table
                                                                                                                                                                                                clear_table_query = "DELETE FROM colors"
                                                                                                                                                                                                        cursor.execute(clear_table_query)

                                                                                                                                                                                                                # Insert color frequencies into the table
                                                                                                                                                                                                                        insert_query = "INSERT INTO colors (color, frequency) VALUES (%s, %s)"
                                                                                                                                                                                                                                color_counts = Counter(colors)
                                                                                                                                                                                                                                        data = [(color, count) for color, count in color_counts.items()]
                                                                                                                                                                                                                                                cursor.executemany(insert_query, data)

                                                                                                                                                                                                                                                        # Commit the changes
                                                                                                                                                                                                                                                                connection.commit()
                                                                                                                                                                                                                                                                        print("Colors and frequencies saved to the database successfully!")

                                                                                                                                                                                                                                                                            except (Exception, Error) as error:
                                                                                                                                                                                                                                                                                    print("Error while connecting to PostgreSQL or saving data:", error)

                                                                                                                                                                                                                                                                                        finally:
                                                                                                                                                                                                                                                                                                # Close the database connection
                                                                                                                                                                                                                                                                                                        if connection:
                                                                                                                                                                                                                                                                                                                    cursor.close()
                                                                                                                                                                                                                                                                                                                                connection.close()

                                                                                                                                                                                                                                                                                                                                # Function to generate a random 4-digit number of 0s and 1s and convert it to base 10
                                                                                                                                                                                                                                                                                                                                def generate_random_number():
                                                                                                                                                                                                                                                                                                                                    binary_number = ''.join(random.choice(['0', '1']) for _ in range(4))
                                                                                                                                                                                                                                                                                                                                        decimal_number = int(binary_number, 2)
                                                                                                                                                                                                                                                                                                                                            return decimal_number

                                                                                                                                                                                                                                                                                                                                            # Function to recursively search for a number in a list
                                                                                                                                                                                                                                                                                                                                            def recursive_search(numbers, target, start, end):
                                                                                                                                                                                                                                                                                                                                                if start > end:
                                                                                                                                                                                                                                                                                                                                                        return -1

                                                                                                                                                                                                                                                                                                                                                            mid = (start + end) // 2

                                                                                                                                                                                                                                                                                                                                                                if numbers[mid] == target:
                                                                                                                                                                                                                                                                                                                                                                        return mid
                                                                                                                                                                                                                                                                                                                                                                            elif numbers[mid] < target:
                                                                                                                                                                                                                                                                                                                                                                                    return recursive_search(numbers, target, mid + 1, end)
                                                                                                                                                                                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                                                                                                                                                                                                return recursive_search(numbers, target, start, mid - 1)

                                                                                                                                                                                                                                                                                                                                                                                                # Function to calculate the sum of the first 50 Fibonacci sequence numbers
                                                                                                                                                                                                                                                                                                                                                                                                def sum_fibonacci_sequence():
                                                                                                                                                                                                                                                                                                                                                                                                    fibonacci = [0, 1]
                                                                                                                                                                                                                                                                                                                                                                                                        for i in range(2, 51):
                                                                                                                                                                                                                                                                                                                                                                                                                fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
                                                                                                                                                                                                                                                                                                                                                                                                                    return sum(fibonacci[:50])


                                                                                                                                                                                                                                                                                                                                                                                                                    #Color extraction from the html code given
                                                                                                                                                                                                                                                                                                                                                                                                                    colors = extract_colors(html_code)

                                                                                                                                                                                                                                                                                                                                                                                                                    # Performing analysis
                                                                                                                                                                                                                                                                                                                                                                                                                    mean_color = calculate_mean_color(colors)
                                                                                                                                                                                                                                                                                                                                                                                                                    mode_color = calculate_mode_color(colors)
                                                                                                                                                                                                                                                                                                                                                                                                                    median_color = calculate_median_color(colors)
                                                                                                                                                                                                                                                                                                                                                                                                                    variance = calculate_color_variance(colors)

                                                                                                                                                                                                                                                                                                                                                                                                                    # Printing the results
                                                                                                                                                                                                                                                                                                                                                                                                                    print("Mean color:", mean_color)
                                                                                                                                                                                                                                                                                                                                                                                                                    print("Mode color:", mode_color)
                                                                                                                                                                                                                                                                                                                                                                                                                    print("Median color:", median_color)
                                                                                                                                                                                                                                                                                                                                                                                                                    print("Variance of colors:", variance)


                                                                                                                                                                                                                                                                                                                                                                                                                    # Calculate the probability of choosing the color red at random
                                                                                                                                                                                                                                                                                                                                                                                                                    red_count = colors.count("RED")
                                                                                                                                                                                                                                                                                                                                                                                                                    total_count = len(colors)
                                                                                                                                                                                                                                                                                                                                                                                                                    probability_red = red_count / total_count

                                                                                                                                                                                                                                                                                                                                                                                                                    print("Probability of choosing the color red:", probability_red)

                                                                                                                                                                                                                                                                                                                                                                                                                    # Save colors and frequencies to PostgreSQL database
                                                                                                                                                                                                                                                                                                                                                                                                                    save_colors_to_database(colors)

                                                                                                                                                                                                                                                                                                                                                                                                                    # Recursive searching algorithm
                                                                                                                                                                                                                                                                                                                                                                                                                    def recursive_search(numbers, target, start, end):
                                                                                                                                                                                                                                                                                                                                                                                                                        if start > end:
                                                                                                                                                                                                                                                                                                                                                                                                                                return -1

                                                                                                                                                                                                                                                                                                                                                                                                                                    mid = (start + end) // 2

                                                                                                                                                                                                                                                                                                                                                                                                                                        if numbers[mid] == target:
                                                                                                                                                                                                                                                                                                                                                                                                                                                return mid
                                                                                                                                                                                                                                                                                                                                                                                                                                                    elif numbers[mid] < target:
                                                                                                                                                                                                                                                                                                                                                                                                                                                            return recursive_search(numbers, target, mid + 1, end)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                else:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                        return recursive_search(numbers, target, start, mid - 1)

                                                                                                                                                                                                                                                                                                                                                                                                                                                                        # Example usage of recursive_search function
                                                                                                                                                                                                                                                                                                                                                                                                                                                                        numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
                                                                                                                                                                                                                                                                                                                                                                                                                                                                        target = 11
                                                                                                                                                                                                                                                                                                                                                                                                                                                                        result = recursive_search(numbers, target, 0, len(numbers) - 1)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                        if result != -1:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                            print("Number", target, "found at index", result)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                            else:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                print("Number", target, "not found")

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                # Generate random 4-digit number of 0s and 1s and convert it to base 10
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                random_number = generate_random_number()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                print("Random number:", random_number)

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                # Calculate the sum of the first 50 Fibonacci sequence numbers
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                fibonacci_sum = sum_fibonacci_sequence()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                print("Sum of the first 50 Fibonacci sequence numbers:", fibonacci_sum)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                

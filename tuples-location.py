def main():
    #Can not be changed and it is immutable. If data has to stay the same then use tuples
    #It takes less memory as well
    coordinates = (42.376,-71.115)
    latitude, longitude = coordinates
    print(f"Latitude: {coordinates[0]}")
    print(f"Latitude: {coordinates[1]}")

    print(f"Latitude: {latitude}")
    print(f"Latitude: {longitude}")

main()
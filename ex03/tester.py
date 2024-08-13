from zoom import zoom


def main():
    try:
        zoom()
    except Exception as e:
        print(f"An Error: {e}")

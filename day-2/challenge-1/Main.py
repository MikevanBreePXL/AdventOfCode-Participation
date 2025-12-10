from Analyzer import Analyzer

def main():
    analyzer = Analyzer()
    result = analyzer.solve()
    print(f"Total sum of numbers made up of identical sequences: {result}")

if __name__ == "__main__":
    main()
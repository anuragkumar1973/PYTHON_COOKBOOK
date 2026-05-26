import os
import sys
# Recipe 2.10 - This code reads from text file 'welcome.txt' line by line based on user input and prints the output
#!/usr/bin/env python3

def main():
    base = os.path.dirname(__file__)
    path = os.path.join(base, "welcome.txt")

    if not os.path.exists(path):
        print(f"File not found: {path}")
        return

    try:
        with open(path, "r", encoding="utf-8") as f:
            lines = iter(f)
            while True:
                try:
                    cmd = input("Enter 1 to print next line, 0 to exit: ").strip()
                except EOFError:
                    print()  # newline if input stream closed
                    break
                if cmd == "0":
                    break
                if cmd == "1":
                    try:
                        line = next(lines)
                    except StopIteration:
                        print("End of file reached.")
                        break
                    # print the line without adding extra blank lines
                    print(line.rstrip("\n"))
                    continue
                print("Please enter 1 or 0.")
    except KeyboardInterrupt:
        print("\nInterrupted.")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()


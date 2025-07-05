import time
import matplotlib.pyplot as plt

class SemiconductorChip:
    def __init__(self):
        self.state = {
            'Oxidation': False,
            'Photolithography': False,
            'Etching': False,
            'Doping': False,
            'Metallization': False,
            'Packaging': False
        }

    def oxidize(self):
        if not self.state['Oxidation']:
            print("\n[Oxidation] Growing silicon dioxide layer on wafer...")
            time.sleep(1)
            self.state['Oxidation'] = True
            print("Completed oxidation.")
        else:
            print("Already oxidized.")

    def photolithography(self):
        if self.state['Oxidation'] and not self.state['Photolithography']:
            print("\n[Photolithography] Transferring circuit pattern onto wafer...")
            time.sleep(1)
            self.state['Photolithography'] = True
            print("Pattern transferred.")
        elif not self.state['Oxidation']:
            print("You must oxidize the wafer before photolithography.")
        else:
            print("Pattern already transferred.")

    def etch(self):
        if self.state['Photolithography'] and not self.state['Etching']:
            print("\n[Etching] Removing exposed areas...")
            time.sleep(1)
            self.state['Etching'] = True
            print("Etching complete.")
        elif not self.state['Photolithography']:
            print("You must complete photolithography before etching.")
        else:
            print("Already etched.")

    def dope(self):
        if self.state['Etching'] and not self.state['Doping']:
            print("\n[Doping] Adding impurities to change electrical properties...")
            time.sleep(1)
            self.state['Doping'] = True
            print("Doping complete.")
        elif not self.state['Etching']:
            print("You must etch before doping.")
        else:
            print("Already doped.")

    def metallize(self):
        if self.state['Doping'] and not self.state['Metallization']:
            print("\n[Metallization] Adding metal contacts...")
            time.sleep(1)
            self.state['Metallization'] = True
            print("Metallization complete.")
        elif not self.state['Doping']:
            print("You must dope before metallization.")
        else:
            print("Already metallized.")

    def package(self):
        if self.state['Metallization'] and not self.state['Packaging']:
            print("\n[Packaging] Sealing and protecting the chip...")
            time.sleep(1)
            self.state['Packaging'] = True
            print("Packaging complete.")
        elif not self.state['Metallization']:
            print("You must metallize before packaging.")
        else:
            print("Already packaged.")

    def status(self):
        print("\n--- Chip Manufacturing Status ---")
        for step, done in self.state.items():
            print(f"{step}: {'✅ ' if done else '❌'}")
        print("----------------------------------")

    def visualize(self):
        steps = list(self.state.keys())
        completed = [int(v) for v in self.state.values()]

        colors = ['green' if done else 'red' for done in completed]
        plt.figure(figsize=(8, 4))
        plt.barh(steps, completed, color=colors)
        plt.xlabel('Status (0 = Incomplete, 1 = Complete)')
        plt.title('Semiconductor Chip Manufacturing Process')
        plt.grid(axis='x')
        plt.tight_layout()
        plt.show()


def main():
    chip = SemiconductorChip()

    steps = {
        '1': chip.oxidize,
        '2': chip.photolithography,
        '3': chip.etch,
        '4': chip.dope,
        '5': chip.metallize,
        '6': chip.package,
        '7': chip.status,
        '8': chip.visualize
    }

    while True:
        print("\nSelect a process step:")
        print("1. Oxidation")
        print("2. Photolithography")
        print("3. Etching")
        print("4. Doping")
        print("5. Metallization")
        print("6. Packaging")
        print("7. View Status")
        print("8. Visualize Progress")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '0':
            print("\nExiting simulation. Goodbye!")
            break
        elif choice in steps:
            steps[choice]()
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()


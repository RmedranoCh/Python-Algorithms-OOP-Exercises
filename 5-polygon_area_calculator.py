
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        line = "*" * self.width + "\n"
        return line * self.height

    def get_amount_inside(self, shape):
        return (self.width // shape.width) * (self.height // shape.height)


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __str__(self):
        return f"Square(side={self.width})"

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, width):
        self.set_side(width)

    def set_height(self, height):
        self.set_side(height)

def shape_manager():
    print("--- SHAPE CALCULATOR ---")
    
    try:
        w = int(input("Rectangle width: "))
        h = int(input("Rectangle height: "))
        rect = Rectangle(w, h)
        
        s = int(input("Square side: "))
        sq = Square(s)

        while True:
            print("\n" + "="*20)
            print(f"CURRENT STATE:\n1. {rect}\n2. {sq}")
            print("="*20)
            print("1. Show pictures (*)")
            print("2. Calculate Areas and Perimeters")
            print("3. Check how many times the square fits in the rectangle")
            print("4. Change dimensions")
            print("5. Exit")
            
            option = input("Select an option: ")

            if option == "1":
                print("\nRectangle Picture:")
                print(rect.get_picture())
                print("Square Picture:")
                print(sq.get_picture())

            elif option == "2":
                print(f"\nRectangle -> Area: {rect.get_area()} | Perimeter: {rect.get_perimeter()}")
                print(f"Square    -> Area: {sq.get_area()} | Diagonal: {sq.get_diagonal():.2f}")

            elif option == "3":
                amount = rect.get_amount_inside(sq)
                print(f"\nThe {sq} fits {amount} times inside the {rect}")

            elif option == "4":
                rect.set_width(int(input("New rectangle width: ")))
                rect.set_height(int(input("New rectangle height: ")))
                sq.set_side(int(input("New square side: ")))

            elif option == "5":
                print("Goodbye!")
                break

    except ValueError:
        print("Error: Please enter valid integers.")

if __name__ == "__main__":
    shape_manager()
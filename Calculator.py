from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


# Main application class for the calculator
class MainApp(App):
    def build(self):
        # Set the application icon
        self.icon = "eagle.png"
        
        # Define supported operators for the calculator
        self.operators = ["/", "*", "+", "-"]
        self.last_was_operator = None  # Track if the last button pressed was an operator
        self.last_button = None        # Track the last button pressed

        # Set up the main layout for the calculator
        main_layout = BoxLayout(orientation="vertical")
        
        # Text input field for displaying the solution/output
        self.solution = TextInput(
            background_color="black",
            foreground_color="white",
            multiline=False,
            halign="right",
            font_size=55,
            readonly=True  # Makes the field read-only
        )
        main_layout.add_widget(self.solution)  # Add solution display to the main layout
        
        # Define the button layout for digits and operators
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "+"],
            [".", "0", "C", "-"]
        ]

        # Loop through the buttons array to create and add buttons
        for row in buttons:
            h_layout = BoxLayout()  # Create a horizontal layout for each row
            for label in row:
                # Create a button for each label
                button = Button(
                    text=label,
                    font_size=30,
                    background_color="grey",
                    pos_hint={"center_x": 0.5, "center_y": 0.5}
                )
                button.bind(on_press=self.on_button_press)  # Bind button to action handler
                h_layout.add_widget(button)  # Add button to the row layout
            main_layout.add_widget(h_layout)  # Add row to the main layout

        # Create and add the "=" button for calculating the result
        equal_button = Button(
            text="=",
            font_size=30,
            background_color="grey",
            pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        equal_button.bind(on_press=self.on_solution)  # Bind "=" button to calculation handler
        main_layout.add_widget(equal_button)  # Add "=" button to main layout

        return main_layout

    # Function to handle button press events
    def on_button_press(self, instance):
        current = self.solution.text  # Get current text in the solution field
        button_text = instance.text   # Get the text of the pressed button

        # Clear the solution field if "C" is pressed
        if button_text == "C":
            self.solution.text = ""
        else:
            # Prevent consecutive operators or starting with an operator
            if current and (self.last_was_operator and button_text in self.operators):
                return
            elif current == "" and button_text in self.operators:
                return
            else:
                # Append button text to current solution
                new_text = current + button_text
                self.solution.text = new_text
        
        # Update tracking variables
        self.last_button = button_text
        self.last_was_operator = self.last_button in self.operators

    # Function to calculate and display the result when "=" is pressed
    def on_solution(self, instance):
        text = self.solution.text  # Get the current expression
        if text:
            # Evaluate the expression and display the result
            solution = str(eval(self.solution.text))
            self.solution.text = solution


# Run the calculator app if this file is executed directly
if __name__ == "__main__":
    app = MainApp()
    app.run()

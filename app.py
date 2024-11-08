import customtkinter as ctk
from tkinter import messagebox


# Function to calculate the monthly premium
def calculate_premium():
    try:
        vehicle_price = float(entry_vehicle_price.get())
        loan_term_months = int(entry_loan_term.get())
        interest_rate_annual = float(entry_interest_rate.get()) / 100
        balloon_percentage = float(entry_balloon_percentage.get()) / 100
        trade_in_offer = float(entry_trade_in_offer.get())

        if var_settlement.get():
            settlement_amount = float(entry_settlement_amount.get())
            shortfall = settlement_amount - trade_in_offer
        else:
            shortfall = 0

        total_loan_amount = vehicle_price + shortfall
        balloon_payment = total_loan_amount * balloon_percentage
        loan_amount_excluding_balloon = total_loan_amount - balloon_payment
        monthly_interest_rate = interest_rate_annual / 12

        monthly_premium = (loan_amount_excluding_balloon * monthly_interest_rate) / (
                    1 - (1 + monthly_interest_rate) ** -loan_term_months)
        label_result.configure(text=f"Monthly Premium: R{monthly_premium:.2f}\nShortfall: R{shortfall:.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")


# Function to toggle settlement amount entry
def toggle_settlement():
    if var_settlement.get():
        entry_settlement_amount.grid(row=5, column=1, padx=10, pady=5, sticky="ew")
    else:
        entry_settlement_amount.grid_remove()


# Create the main window with dark theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.title("Vehicle Finance Calculator")
app.geometry("800x600")

# Create and place the input fields and labels
font_style = ("Helvetica", 12)

frame_inputs = ctk.CTkFrame(app)
frame_inputs.pack(pady=20, padx=20, fill="both", expand=True)

frame_inputs.grid_columnconfigure(0, weight=1)
frame_inputs.grid_columnconfigure(1, weight=1)

ctk.CTkLabel(frame_inputs, text="Vehicle Price:", font=font_style).grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_vehicle_price = ctk.CTkEntry(frame_inputs, font=font_style)
entry_vehicle_price.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

ctk.CTkLabel(frame_inputs, text="Loan Term (Months):", font=font_style).grid(row=1, column=0, padx=10, pady=5,
                                                                             sticky="e")
entry_loan_term = ctk.CTkEntry(frame_inputs, font=font_style)
entry_loan_term.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

ctk.CTkLabel(frame_inputs, text="Interest Rate (Annual %):", font=font_style).grid(row=2, column=0, padx=10, pady=5,
                                                                                   sticky="e")
entry_interest_rate = ctk.CTkEntry(frame_inputs, font=font_style)
entry_interest_rate.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

ctk.CTkLabel(frame_inputs, text="Balloon Payment (%):", font=font_style).grid(row=3, column=0, padx=10, pady=5,
                                                                              sticky="e")
entry_balloon_percentage = ctk.CTkEntry(frame_inputs, font=font_style)
entry_balloon_percentage.grid(row=3, column=1, padx=10, pady=5, sticky="ew")

ctk.CTkLabel(frame_inputs, text="Trade-in Offer:", font=font_style).grid(row=4, column=0, padx=10, pady=5, sticky="e")
entry_trade_in_offer = ctk.CTkEntry(frame_inputs, font=font_style)
entry_trade_in_offer.grid(row=4, column=1, padx=10, pady=5, sticky="ew")

var_settlement = ctk.BooleanVar()
check_settlement = ctk.CTkCheckBox(frame_inputs,
                                   text="Settlement Amount",
                                   variable=var_settlement,
                                   command=toggle_settlement)
check_settlement.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

entry_settlement_amount = ctk.CTkEntry(frame_inputs, font=("Helvetica", 12))

# Create and place the button to calculate the premium
button_calculate = ctk.CTkButton(app, text="Calculate Premium", command=calculate_premium)
button_calculate.pack(pady=(20))

# Create and place the result label in a nice block with bigger green font
label_result_frame = ctk.CTkFrame(app)
label_result_frame.pack(pady=(20), padx=(20), fill="both", expand=True)

label_result = ctk.CTkLabel(label_result_frame,
                            text="Monthly Premium: R0.00\nShortfall: R0.00",
                            font=("Helvetica", 24),
                            text_color="green")
label_result.pack(pady=(20))

# Run the application .
app.mainloop()

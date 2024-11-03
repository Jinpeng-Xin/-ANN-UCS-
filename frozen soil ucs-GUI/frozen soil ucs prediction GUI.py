import numpy as np
import pandas as pd
import tensorflow as tf
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from tkinter import ttk

# trained ANN qu model
model = tf.keras.models.load_model('冻土ucs.h5')

# Create a Tkinter window
window = tk.Tk()
window.title("基于ANN的冻土UCS预测模型")

# Set background color and font
window.configure(bg='#f0f0f0')
# Define a larger font
larger_font = ('Helvetica', 16)

# Load the watermark image and resize it
watermark_image = Image.open('北京交通大学校徽.png')
resized_image = watermark_image.resize((221, 75), Image.LANCZOS)
watermark_photo = ImageTk.PhotoImage(resized_image)
watermark_label = tk.Label(window, image=watermark_photo, bg='#f0f0f0')
watermark_label.image = watermark_photo
watermark_label.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Add program name label below the watermark with larger font
program_name_label = tk.Label(window, text="Prediction Model for Unconfined Compressive Strength of Frozen Soil Based on Machine Learning\n基于机器学习的冻土UCS预测", bg='#f0f0f0', font=larger_font)
program_name_label.grid(row=1, column=0, columnspan=4, padx=10, pady=5)

# Create a style for rounded entry widgets
style = ttk.Style()
style.configure('TEntry', borderwidth=2, relief='solid', fieldbackground='#ffffff')
style.map('TEntry', relief=[('active', 'solid'), ('pressed', 'solid')], bordercolor=[('active', '#4CAF50'), ('pressed', '#4CAF50')], lightcolor=[('active', '#4CAF50'), ('pressed', '#4CAF50')], darkcolor=[('active', '#4CAF50'), ('pressed', '#4CAF50')])

def predict():
    try:
        # Load user input
        feature1 = float(entry_feature1.get())
        feature2 = float(entry_feature2.get())
        feature3 = float(entry_feature3.get())
        feature4 = float(entry_feature4.get())
        category = category_var.get()

        # Create a DataFrame from user input
        input_data = pd.DataFrame([[feature1, feature2, feature3, feature4, category]],
                                  columns=['temperature', 'water_content', 'dry_density', 'strain_rate', 'category'])

        # Make prediction
        prediction = model.predict(input_data)[0, 0]

        # Display the prediction
        result_label.config(text=f"Predicted UCS: {prediction:.2f}", fg='green', bg='#f0f0f0', font=larger_font)
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numeric values.")

def load_data():
    file_path = filedialog.askopenfilename(title="Select Data File")
    if file_path:
        try:
            data = pd.read_excel(file_path)
            # Without normalization
            prediction = model.predict(data)
            messagebox.showinfo("Prediction", f"The predicted qu is: {prediction}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Labels and entry widgets for user input
label_feature1 = tk.Label(window, text="温度 tempture (℃) :", bg='#f0f0f0', font=larger_font)
label_feature1.grid(row=2, column=0, padx=10, pady=10)
entry_feature1 = ttk.Entry(window, style='TEntry', font=larger_font)
entry_feature1.grid(row=2, column=1)

label_feature2 = tk.Label(window, text="质量含水量 mass water content (%) :", bg='#f0f0f0', font=larger_font)
label_feature2.grid(row=3, column=0, padx=10, pady=10)
entry_feature2 = ttk.Entry(window, style='TEntry', font=larger_font)
entry_feature2.grid(row=3, column=1)

label_feature3 = tk.Label(window, text="干密度 dry density (g/cm³):", bg='#f0f0f0', font=larger_font)
label_feature3.grid(row=4, column=0, padx=10, pady=10)
entry_feature3 = ttk.Entry(window, style='TEntry', font=larger_font)
entry_feature3.grid(row=4, column=1)

label_feature4 = tk.Label(window, text="应变速率 strain rate (s⁻¹) :", bg='#f0f0f0', font=larger_font)
label_feature4.grid(row=5, column=0, padx=10, pady=10)
entry_feature4 = ttk.Entry(window, style='TEntry', font=larger_font)
entry_feature4.grid(row=5, column=1)

# Create a variable to hold the category selection
category_var = tk.StringVar()
category_var.set("1")  # Default to clay (1)

# Create a radio button group for category selection
category_label = tk.Label(window, text="类别:", bg='#f0f0f0', font=larger_font)
category_label.grid(row=6, column=0, padx=10, pady=10)
clay_radio = tk.Radiobutton(window, text="黏土", variable=category_var, value="0", bg='#f0f0f0', font=larger_font)
clay_radio.grid(row=6, column=1, padx=10)
silt_radio = tk.Radiobutton(window, text="粉土", variable=category_var, value="1", bg='#f0f0f0', font=larger_font)
silt_radio.grid(row=6, column=2, padx=10)
sand_radio = tk.Radiobutton(window, text="砂土", variable=category_var, value="2", bg='#f0f0f0', font=larger_font)
sand_radio.grid(row=6, column=3, padx=10)

# Button to trigger prediction
predict_button = tk.Button(window, text="Predict", command=predict, bg='#4CAF50', fg='white', font=larger_font)
predict_button.grid(row=7, column=0, columnspan=2, pady=10)

# Label to display the prediction result
result_label = tk.Label(window, text="", bg='#f0f0f0', font=larger_font)
result_label.grid(row=8, column=0, columnspan=2, pady=10)

# Button to load data from a file for prediction
load_data_button = tk.Button(window, text="Load Data", command=load_data, bg='#2196F3', fg='white', font=larger_font)
load_data_button.grid(row=9, column=0, columnspan=2, pady=10)

# Function to clear input fields and prediction result
def clear_fields():
    entry_feature1.delete(0, tk.END)
    entry_feature2.delete(0, tk.END)
    entry_feature3.delete(0, tk.END)
    entry_feature4.delete(0, tk.END)
    category_var.set("1")
    result_label.config(text="")

clear_button = tk.Button(window, text="Clear", command=clear_fields, bg='#FF9800', fg='white', font=larger_font)
clear_button.grid(row=7, column=1, columnspan=2, pady=10)

# Run the Tkinter event loop
window.mainloop()
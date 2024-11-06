import tkinter as tk 
import moving
import threading
import time
import os
import capturing
import recognition
import counting
import gui

class FileMovingApp: 
    def __init__(self, root): 
        self.root = root 
        self.root.title("File Moving App") 

        # Dictionary to store result counts 
        self.result_counts = {'塑膠': 0, '紙包飲品': 0, '金屬製品': 0, '其他': 0} 
        self.running = True

        # Label to display file name and result 
        self.label = tk.Label(root, text="File: None, 分類結果: None", font=("Arial", 14)) 
        self.label.pack(pady=20) 

        # Start button 
        self.start_button = tk.Button(root, text="Recognize", command=self.start_process, font=("Arial", 12)) 
        self.start_button.pack(pady=10) 

        #End button
        self.end_button = tk.Button(root, text='End', command=self.end_process, font=("Arial", 12))
        self.end_button.pack(pady=10)

        # Result boxes 
        self.result_labels = {} 
        for key in self.result_counts.keys(): 
            self.result_labels[key] = tk.Label(root, text=f"{key.upper()}: 0", font=("Arial", 14), width=10, borderwidth=2, relief="groove") 
            self.result_labels[key].pack(side=tk.LEFT, padx=10, pady=20) 
    
    def process_files_once(self):
            file_name = capturing.capture()
            result = recognition.recognize(file_name)
            moving.file_moving(file_name, result)
            self.label.config(text=f"File: {file_name}, 分類結果: {result}")

            self.result_counts[result] += 1
            self.result_labels[result].config(text=f"{result.upper()}: {self.result_counts[result]}")
            

    def start_process(self): 
        if self.running:
            self.thread = threading.Thread(target=self.process_files_once)
            self.thread.start()

    def end_process(self):
        self.running = False
        self.root.quit()

if __name__ == "__main__": 
    root = tk.Tk() 
    app = FileMovingApp(root) 
    root.mainloop()
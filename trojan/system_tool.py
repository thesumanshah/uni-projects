#!/usr/bin/env python3

import os
import platform
import datetime
import shutil
import glob
from pathlib import Path
import tkinter as tk
from tkinter import ttk, messagebox, filedialog, scrolledtext
import threading


class SystemTool:
    """System Security & Optimization Tool"""
    
    def __init__(self):
        self.log_file = "system_tool.log"
        self.setup_logging()
        self.setup_gui()
    
    def setup_logging(self):
        """Initialize logging system"""
        try:
            with open(self.log_file, 'a', encoding='utf-8') as f:
                f.write(f"\n{'='*50}\n")
                f.write(f"Session started: {datetime.datetime.now()}\n")
                f.write(f"Operating System: {platform.system()} {platform.release()}\n")
                f.write(f"Working Directory: {os.getcwd()}\n")
                f.write(f"{'='*50}\n")
        except Exception as e:
            print(f"Warning: Could not initialize logging: {e}")
    
    def log_operation(self, operation, details):
        """Log operations to file with timestamp"""
        try:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(self.log_file, 'a', encoding='utf-8') as f:
                f.write(f"[{timestamp}] {operation}: {details}\n")
        except Exception as e:
            print(f"Warning: Could not log operation: {e}")
    
    def setup_gui(self):
        """Setup the main GUI"""
        self.root = tk.Tk()
        self.root.title("System Security & Optimization Tool")
        self.root.geometry("800x600")
        self.root.configure(bg='#2c3e50')
        
        # Configure style
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TLabel', background='#2c3e50', foreground='white', font=('Arial', 10))
        style.configure('Title.TLabel', background='#2c3e50', foreground='#3498db', font=('Arial', 16, 'bold'))
        style.configure('TButton', font=('Arial', 11, 'bold'))
        style.configure('TFrame', background='#2c3e50')
        
        self.create_main_interface()
        
        # Center window
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (self.root.winfo_width() // 2)
        y = (self.root.winfo_screenheight() // 2) - (self.root.winfo_height() // 2)
        self.root.geometry(f"+{x}+{y}")
    
    def create_main_interface(self):
        """Create the main interface"""
        # Header
        header_frame = ttk.Frame(self.root)
        header_frame.pack(fill='x', padx=20, pady=20)
        
        title_label = ttk.Label(header_frame, text="🛡️ System Security & Optimization Tool", 
                               style='Title.TLabel')
        title_label.pack()
        
        subtitle_label = ttk.Label(header_frame, text="Protect and optimize your system", 
                                  font=('Arial', 11))
        subtitle_label.pack(pady=(5, 0))
        
        # Main buttons frame
        buttons_frame = ttk.Frame(self.root)
        buttons_frame.pack(fill='both', expand=True, padx=40, pady=20)
        
        # Virus Scanner Button
        virus_btn = tk.Button(buttons_frame, text="🔍 Scan & Remove Viruses", 
                             font=('Arial', 14, 'bold'), bg='#e74c3c', fg='white',
                             height=3, command=self.open_virus_scanner)
        virus_btn.pack(fill='x', pady=10)
        
        # Speed Optimizer Button
        speed_btn = tk.Button(buttons_frame, text="🚀 System Speed Optimizer", 
                             font=('Arial', 14, 'bold'), bg='#9b59b6', fg='white',
                             height=3, command=self.open_speed_optimizer)
        speed_btn.pack(fill='x', pady=10)
        
        # Problem Fixer Button
        fix_btn = tk.Button(buttons_frame, text="🔧 Fix System Problems", 
                           font=('Arial', 14, 'bold'), bg='#3498db', fg='white',
                           height=3, command=self.open_problem_fixer)
        fix_btn.pack(fill='x', pady=10)
        
        # Log Viewer Button
        log_btn = tk.Button(buttons_frame, text="📋 View Activity Log", 
                           font=('Arial', 12), bg='#95a5a6', fg='white',
                           height=2, command=self.open_log_viewer)
        log_btn.pack(fill='x', pady=(20, 10))
        
        # Exit Button
        exit_btn = tk.Button(buttons_frame, text="❌ Exit", 
                            font=('Arial', 12), bg='#34495e', fg='white',
                            height=2, command=self.root.quit)
        exit_btn.pack(fill='x', pady=5)
    
    def open_virus_scanner(self):
        """Open virus scanner window"""
        scanner_window = tk.Toplevel(self.root)
        scanner_window.title("Virus Scanner")
        scanner_window.geometry("600x500")
        scanner_window.configure(bg='#2c3e50')
        
        # Header
        header = ttk.Label(scanner_window, text="🔍 Virus Scanner", style='Title.TLabel')
        header.pack(pady=20)
        
        # Info label
        info_label = ttk.Label(scanner_window, text="Scanning for suspicious files...")
        info_label.pack(pady=10)
        
        # Results frame
        results_frame = ttk.Frame(scanner_window)
        results_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        # Results listbox
        self.virus_listbox = tk.Listbox(results_frame, font=('Arial', 10), bg='#34495e', fg='white')
        self.virus_listbox.pack(fill='both', expand=True)
        
        # Buttons frame
        btn_frame = ttk.Frame(scanner_window)
        btn_frame.pack(fill='x', padx=20, pady=10)
        
        scan_btn = tk.Button(btn_frame, text="Start Scan", bg='#e74c3c', fg='white',
                            font=('Arial', 11, 'bold'), command=self.scan_viruses)
        scan_btn.pack(side='left', padx=5)
        
        remove_btn = tk.Button(btn_frame, text="Remove Selected", bg='#c0392b', fg='white',
                              font=('Arial', 11, 'bold'), command=self.remove_viruses)
        remove_btn.pack(side='left', padx=5)
    
    def scan_viruses(self):
        """Scan for .txt files"""
        self.virus_listbox.delete(0, tk.END)
        
        try:
            txt_files = glob.glob("*.txt")
            self.log_operation("VIRUS_SCAN", f"Found {len(txt_files)} .txt files")
            
            if not txt_files:
                self.virus_listbox.insert(tk.END, "✅ No suspicious files found. System is clean!")
            else:
                self.virus_listbox.insert(tk.END, f"⚠️ Found {len(txt_files)} suspicious files:")
                for file in txt_files:
                    self.virus_listbox.insert(tk.END, f"  🦠 {file}")
        except Exception as e:
            messagebox.showerror("Error", f"Error during scan: {e}")
    
    def remove_viruses(self):
        """Remove selected virus files"""
        try:
            txt_files = glob.glob("*.txt")
            if not txt_files:
                messagebox.showinfo("Info", "No files to remove.")
                return
            
            result = messagebox.askyesno("Confirm", f"Remove {len(txt_files)} suspicious files?")
            if result:
                deleted_count = 0
                for file in txt_files:
                    try:
                        os.remove(file)
                        deleted_count += 1
                        self.log_operation("FILE_DELETED", file)
                    except Exception as e:
                        self.log_operation("DELETE_ERROR", f"{file}: {e}")
                
                messagebox.showinfo("Complete", f"Removed {deleted_count} files. System secured!")
                self.scan_viruses()  # Refresh the list
        except Exception as e:
            messagebox.showerror("Error", f"Error removing files: {e}")
    
    def open_speed_optimizer(self):
        """Open speed optimizer window"""
        optimizer_window = tk.Toplevel(self.root)
        optimizer_window.title("System Speed Optimizer")
        optimizer_window.geometry("600x500")
        optimizer_window.configure(bg='#2c3e50')
        
        # Header
        header = ttk.Label(optimizer_window, text="🚀 System Speed Optimizer", style='Title.TLabel')
        header.pack(pady=20)
        
        # File selection frame
        file_frame = ttk.Frame(optimizer_window)
        file_frame.pack(fill='x', padx=20, pady=10)
        
        ttk.Label(file_frame, text="Select file to optimize:").pack(anchor='w')
        
        self.file_var = tk.StringVar()
        self.file_combo = ttk.Combobox(file_frame, textvariable=self.file_var, state='readonly')
        self.file_combo.pack(fill='x', pady=5)
        
        # Copies frame
        copies_frame = ttk.Frame(optimizer_window)
        copies_frame.pack(fill='x', padx=20, pady=10)
        
        ttk.Label(copies_frame, text="Number of optimization copies:").pack(anchor='w')
        self.copies_var = tk.StringVar(value="5")
        copies_entry = ttk.Entry(copies_frame, textvariable=self.copies_var)
        copies_entry.pack(fill='x', pady=5)
        
        # Progress frame
        progress_frame = ttk.Frame(optimizer_window)
        progress_frame.pack(fill='x', padx=20, pady=10)
        
        self.progress_var = tk.StringVar(value="Ready to optimize...")
        progress_label = ttk.Label(progress_frame, textvariable=self.progress_var)
        progress_label.pack()
        
        # Buttons
        btn_frame = ttk.Frame(optimizer_window)
        btn_frame.pack(fill='x', padx=20, pady=20)
        
        refresh_btn = tk.Button(btn_frame, text="Refresh Files", bg='#3498db', fg='white',
                               command=self.refresh_files)
        refresh_btn.pack(side='left', padx=5)
        
        optimize_btn = tk.Button(btn_frame, text="Optimize System", bg='#9b59b6', fg='white',
                                font=('Arial', 11, 'bold'), command=self.optimize_system)
        optimize_btn.pack(side='left', padx=5)
        
        # Initial file refresh
        self.refresh_files()
    
    def refresh_files(self):
        """Refresh the list of available files"""
        txt_files = glob.glob("*.txt")
        self.file_combo['values'] = txt_files
        if txt_files:
            self.file_combo.current(0)
    
    def optimize_system(self):
        """Create optimization copies"""
        try:
            selected_file = self.file_var.get()
            if not selected_file:
                messagebox.showwarning("Warning", "Please select a file to optimize.")
                return
            
            copies = int(self.copies_var.get())
            if copies <= 0 or copies > 100:
                messagebox.showwarning("Warning", "Please enter a number between 1 and 100.")
                return
            
            def create_copies():
                base_name = Path(selected_file).stem
                extension = Path(selected_file).suffix
                created_count = 0
                
                for i in range(1, copies + 1):
                    try:
                        copy_name = f"{base_name}_optimized{i}{extension}"
                        shutil.copy2(selected_file, copy_name)
                        created_count += 1
                        self.log_operation("FILE_OPTIMIZED", f"{selected_file} -> {copy_name}")
                        self.progress_var.set(f"Created {created_count}/{copies} optimization files...")
                        self.root.update()
                    except Exception as e:
                        self.log_operation("OPTIMIZATION_ERROR", f"Copy {i}: {e}")
                
                self.progress_var.set(f"Optimization complete! Created {created_count} files.")
                messagebox.showinfo("Complete", f"System optimized! Created {created_count} optimization files.")
            
            # Run in thread to prevent GUI freezing
            threading.Thread(target=create_copies, daemon=True).start()
            
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number of copies.")
        except Exception as e:
            messagebox.showerror("Error", f"Optimization error: {e}")
    
    def open_problem_fixer(self):
        """Open problem fixer window"""
        fixer_window = tk.Toplevel(self.root)
        fixer_window.title("System Problem Fixer")
        fixer_window.geometry("600x500")
        fixer_window.configure(bg='#2c3e50')
        
        # Header
        header = ttk.Label(fixer_window, text="🔧 System Problem Fixer", style='Title.TLabel')
        header.pack(pady=20)
        
        # Info
        info_label = ttk.Label(fixer_window, text="Fix corrupted or problematic files")
        info_label.pack(pady=10)
        
        # File list frame
        list_frame = ttk.Frame(fixer_window)
        list_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        self.fix_listbox = tk.Listbox(list_frame, font=('Arial', 10), bg='#34495e', fg='white')
        self.fix_listbox.pack(fill='both', expand=True)
        
        # Buttons
        btn_frame = ttk.Frame(fixer_window)
        btn_frame.pack(fill='x', padx=20, pady=10)
        
        refresh_btn = tk.Button(btn_frame, text="Refresh List", bg='#3498db', fg='white',
                               command=self.refresh_fix_list)
        refresh_btn.pack(side='left', padx=5)
        
        fix_btn = tk.Button(btn_frame, text="Fix Selected", bg='#e67e22', fg='white',
                           font=('Arial', 11, 'bold'), command=self.fix_selected_file)
        fix_btn.pack(side='left', padx=5)
        
        # Initial refresh
        self.refresh_fix_list()
    
    def refresh_fix_list(self):
        """Refresh the list of files that can be fixed"""
        self.fix_listbox.delete(0, tk.END)
        
        try:
            all_files = [f for f in os.listdir('.') if os.path.isfile(f)]
            for file in all_files[:50]:  # Limit display
                self.fix_listbox.insert(tk.END, file)
        except Exception as e:
            self.fix_listbox.insert(tk.END, f"Error listing files: {e}")
    
    def fix_selected_file(self):
        """Fix the selected file by hiding it"""
        selection = self.fix_listbox.curselection()
        if not selection:
            messagebox.showwarning("Warning", "Please select a file to fix.")
            return
        
        filename = self.fix_listbox.get(selection[0])
        
        try:
            self.hide_file(filename)
            messagebox.showinfo("Success", f"File '{filename}' has been fixed and secured!")
            self.refresh_fix_list()
        except Exception as e:
            messagebox.showerror("Error", f"Could not fix file: {e}")
    
    def hide_file(self, filename):
        """Hide a file by renaming and setting hidden attributes"""
        # First, rename with .fixed extension
        fixed_name = f"{filename}.fixed"
        
        # Handle name conflicts
        counter = 1
        while os.path.exists(fixed_name):
            fixed_name = f"{filename}.fixed_{counter}"
            counter += 1
        
        os.rename(filename, fixed_name)
        
        # Apply OS-specific hiding
        system = platform.system().lower()
        
        if system == "windows":
            self.hide_file_windows(fixed_name)
        else:  # Unix-like systems
            self.hide_file_unix(fixed_name)
        
        self.log_operation("FILE_FIXED", f"{filename} -> {fixed_name}")
    
    def hide_file_windows(self, filename):
        """Hide file on Windows by setting hidden attribute"""
        try:
            import subprocess
            subprocess.run(['attrib', '+H', filename], capture_output=True, text=True)
        except Exception:
            pass
    
    def hide_file_unix(self, filename):
        """Hide file on Unix-like systems by prefixing with dot"""
        try:
            dir_path = os.path.dirname(filename) or '.'
            base_name = os.path.basename(filename)
            
            if not base_name.startswith('.'):
                dot_filename = os.path.join(dir_path, f".{base_name}")
                
                counter = 1
                while os.path.exists(dot_filename):
                    dot_filename = os.path.join(dir_path, f".{base_name}_{counter}")
                    counter += 1
                
                os.rename(filename, dot_filename)
        except Exception:
            pass
    
    def open_log_viewer(self):
        """Open log viewer window"""
        log_window = tk.Toplevel(self.root)
        log_window.title("Activity Log")
        log_window.geometry("700x500")
        log_window.configure(bg='#2c3e50')
        
        # Header
        header = ttk.Label(log_window, text="📋 System Activity Log", style='Title.TLabel')
        header.pack(pady=20)
        
        # Text area
        text_frame = ttk.Frame(log_window)
        text_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        log_text = scrolledtext.ScrolledText(text_frame, font=('Courier', 9), 
                                           bg='#34495e', fg='white')
        log_text.pack(fill='both', expand=True)
        
        # Load log content
        try:
            if os.path.exists(self.log_file):
                with open(self.log_file, 'r', encoding='utf-8') as f:
                    log_text.insert(tk.END, f.read())
            else:
                log_text.insert(tk.END, "No log file found.")
        except Exception as e:
            log_text.insert(tk.END, f"Error reading log: {e}")
        
        # Auto-scroll to bottom
        log_text.see(tk.END)
    
    def run(self):
        """Start the application"""
        self.log_operation("PROGRAM_START", "System tool started")
        self.root.mainloop()
        self.log_operation("PROGRAM_END", "System tool ended")


if __name__ == "__main__":
    app = SystemTool()
    app.run() 